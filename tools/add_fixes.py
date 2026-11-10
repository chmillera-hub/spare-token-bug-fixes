"""Apply one batch of fixes: save one patch per fix, check it, add the shelf entry."""
import ast, json, subprocess, sys, unicodedata, os
SHELF = "/home/claude/spare-token-bug-fixes"
REPOS = "/home/claude/work/repos"
SC_NOTE = ("The bug report lists the untested lines from a coverage run on an older commit. The chatbot did not run "
           "the tests or a coverage tool so nobody has confirmed that the new tests reach the named lines.")
def sh(args, cwd, check=True, inp=None):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True, input=inp)
    if check and r.returncode: raise SystemExit(f"FAIL {args}: {r.stderr[:400]}")
    return r
def width(s): return sum(2 if unicodedata.east_asian_width(c) in "WFA" else 1 for c in s)
def main(batch):
    data_path = f"{SHELF}/tools/shelf-data.json"
    data = json.load(open(data_path, encoding="utf-8"))
    titles = {}
    try:
        for k, v in json.load(open("/home/claude/work/search/sc_all.json", encoding="utf-8")).items():
            titles[("Sh1n1230/security-checker", int(k))] = v["title"]
        import glob
        for name in sorted(glob.glob("/home/claude/work/search/cands*.json")):
            for v in json.load(open(name, encoding="utf-8")):
                titles[(v["repo"], v["number"])] = v["title"]
    except FileNotFoundError: pass
    have = {(f["project"], f["issue"]) for f in data["fixes"]}
    for it in json.load(open(batch, encoding="utf-8")):
        repo = f"{REPOS}/{it['repo']}"; key = (it["project"], it["issue"])
        if key in have: print("SKIP dup", key); continue
        assert not sh(["git", "status", "--porcelain"], repo).stdout.strip(), "clone not clean"
        ok = True; why = ""
        try:
            for path, content in it.get("files", {}).items():
                full = f"{repo}/{path}"
                assert not os.path.exists(full), f"exists {path}"
                os.makedirs(os.path.dirname(full), exist_ok=True)
                open(full, "w", encoding="utf-8").write(content if content.endswith("\n") else content + "\n")
            for e in it.get("edits", []):
                full = f"{repo}/{e['path']}"; s = open(full, encoding="utf-8", newline="").read()
                crlf = "\r\n" in s
                if crlf: s = s.replace("\r\n", "\n")
                assert s.count(e["old"]) == e.get("count", 1), f"old text found {s.count(e['old'])} times in {e['path']}"
                s = s.replace(e["old"], e["new"])
                if crlf: s = s.replace("\n", "\r\n")
                open(full, "w", encoding="utf-8", newline="").write(s)
            for argv in it.get("cmds", []):
                sh(argv, repo, check=False)
            changed = list(it.get("files", {})) + [e["path"] for e in it.get("edits", [])]
            for path in changed:
                s = open(f"{repo}/{path}", encoding="utf-8").read()
                if path.endswith(".py"):
                    ast.parse(s)
                    lim = it.get("width", 100 if it["repo"] == "sc" else 0)
                    if lim and path in it.get("files", {}):
                        for i, line in enumerate(s.split("\n"), 1):
                            assert width(line) <= lim, f"{path}:{i} is {width(line)} wide"
                    assert "\t" not in s or it.get("tabs_ok"), "tab"
                if path.endswith((".js", ".mjs", ".cjs")):
                    r = sh(["node", "--check", full if False else f"{repo}/{path}"], repo, check=False)
                    assert r.returncode == 0, r.stderr[:300]
                if path.endswith(".json"): json.loads(s)
                if path.endswith(".sh"):
                    assert sh(["bash", "-n", f"{repo}/{path}"], repo, check=False).returncode == 0
            sh(["git", "add", "-A", "-N", "."], repo)
            diff = subprocess.run(["git", "diff"], cwd=repo, capture_output=True).stdout.decode("utf-8")
            assert diff.strip(), "empty diff"
        except (AssertionError, SyntaxError) as ex:
            ok = False; why = str(ex)
        sh(["git", "reset", "-q"], repo); sh(["git", "checkout", "-q", "--", "."], repo); sh(["git", "clean", "-fdq"], repo)
        if not ok: print("BAD", it["issue"], why); continue
        n = max(f["n"] for f in data["fixes"]) + 1
        name = f"{n}-{it['short']}-{it['issue']}.patch"
        open(f"{SHELF}/fixes/{name}", "w", encoding="utf-8", newline="").write(diff)
        r = sh(["git", "apply", "--check", f"{SHELF}/fixes/{name}"], repo, check=False)
        if r.returncode: os.remove(f"{SHELF}/fixes/{name}"); print("BAD apply", it["issue"], r.stderr[:200]); continue
        entry = {"n": n, "patch": name, "project": it["project"], "issue": it["issue"], "lic": it["lic"], "lang": it["lang"],
                 "test": it.get("test", True), "title": it["title"], "symptom": it["symptom"], "change": it["change"],
                 "note": it.get("note") or SC_NOTE, "words": it["words"],
                 "report_title": it.get("report_title") or titles.get(key, ""), "logic_checked": it.get("logic_checked", False),
                 "full_report_read": it.get("full_report_read", True), "written_on": "2026-11-10"}
        for k in ("title", "symptom", "change", "note"): assert "," not in entry[k], f"comma in {k} of {it['issue']}"
        assert entry["report_title"], f"no report title for {key}"
        data["fixes"].append(entry); have.add(key)
        json.dump(data, open(data_path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        print("OK", n, name, len(diff.splitlines()), "lines")
    print("total", len(data["fixes"]))
main(sys.argv[1])

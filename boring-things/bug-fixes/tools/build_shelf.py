"""Rebuild the public shelf pages from tools/shelf-data.json and the patch files in fixes/.

Usage:
  python3 boring-things/bug-fixes/tools/build_shelf.py new <path to a clone of chmillera-hub/spare-token-bug-fixes>
  python3 boring-things/bug-fixes/tools/build_shelf.py g1  <path to a clone of chmillera-hub/game1>

To add a fix: put the patch file in fixes/ and add one entry to the "fixes" list in
tools/shelf-data.json (copy an existing entry and change every field) and run both commands.
The "new" mode rewrites README.md and the fix pages and index.json and llms.txt in this project.
The "g1" mode rewrites the website copy inside the game1 project.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = json.load(open(os.path.join(HERE, "shelf-data.json"), encoding="utf-8"))
WARN = DATA["warning_template"]
F = DATA["fixes"]
for f in F:
    f["report_title"] = f.get("report_title")

_ONES = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
_TENS = {20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
def words(n):
    if n < 20: return _ONES[n]
    if n < 100: return _TENS[n - n % 10] + ("-" + _ONES[n % 10] if n % 10 else "")
    return str(n)

N_CHECKED = sum(1 for f in F if f.get("logic_checked"))
N_FULL = sum(1 for f in F if f.get("full_report_read"))
N_FIRST = sum(1 for f in F if f.get("written_on", "2026-11-09") == "2026-11-09")
N = len(F); PROJECTS = sorted({f["project"] for f in F}, key=str.lower); NP = len(PROJECTS)
NW, NPW = words(N), words(NP)
PATCHDIR=os.path.join(HERE, "..", "fixes")
NEW_REPO="https://github.com/chmillera-hub/spare-token-bug-fixes"
SUB="boring-things/bug-fixes"  # the shelf lives in this folder of the project so the front page of the project stays short
NEW_RAW="https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/"+SUB
NEW_BLOB=NEW_REPO+"/blob/main/"+SUB
NEW_HOME=NEW_REPO+"/tree/main/"+SUB
G1_SITE="https://chmillera-hub.github.io/game1/spare-token-bug-fixes"
G1_SITE_ROOT="https://chmillera-hub.github.io/game1"

def title_line(f):
    t = f.get("report_title")
    return f"- Bug report title: {t.replace('<','&lt;')}\n" if t else ""

def warn(f):
    w = WARN
    if f["full_report_read"]:
        w = w.replace("- Nobody has checked whether", "- The chatbot read the full bug report text and could not read the comments under the bug report.\n- Nobody has checked whether")
    elif f["full_report_read"] is False:
        w = w.replace("- Nobody has checked whether", "- The chatbot worked from the bug report title plus the code and did not read the full bug report text.\n- Nobody has checked whether")
    w = w.replace("- The fix was written against the project's code as of 9 November 2026", f"- The fix was written against the project's code as of {f.get('written_on', '2026-11-09')}")
    w = w.replace("- Nobody has sent the fix", f"- The patch applied cleanly to the project's newest code on {f.get('written_on', '2026-11-09')} (checked with git apply --check).\n- Nobody has sent the fix")
    if f.get("note"):
        w = w.rstrip("\n") + "\n- " + f["note"] + "\n"
    return w

def lst(prefix=""):
    return "\n\n".join(f"{f['n']}. [{f['title']}]({prefix}fix-{f['patch'][:-6]}.md)\n   Project: {f['project']}. Bug report number {f['issue']}. License: {f['lic']}. Test included: {'yes' if f['test'] else 'no'}. Patch file: [{f['patch']}]({prefix}fixes/{f['patch']})" for f in F)

def build(shelf, raw):
    os.makedirs(os.path.join(shelf,"fixes"), exist_ok=True)
    index=[]
    for f in F:
        slug=f["patch"][:-6]; page=f"fix-{slug}.md"; pr=f["project"]
        issue_url=f"https://github.com/{pr}/issues/{f['issue']}"
        patch_text=open(os.path.join(PATCHDIR,f["patch"])).read()
        open(os.path.join(shelf,"fixes",f["patch"]),"w").write(patch_text)
        files=[l.split(" b/")[0][len("diff --git a/"):] for l in patch_text.splitlines() if l.startswith("diff --git ")]
        md=f"""# Fix {f['n']}: {f['title']}

Status: UNSENT and UNTESTED. Free to take.

- Project: {pr}
{title_line(f)}- Bug report: number {f['issue']} ([open the bug report]({issue_url}))
- Project license: {f['lic']}
- Language: {f['lang']}
- Test included: {"yes" if f["test"] else "no"}
- Patch file: [fixes/{f['patch']}](fixes/{f['patch']})
- Direct download address for programs and chatbots: {raw}/fixes/{f['patch']}
- Same page on GitHub: {NEW_BLOB}/{page}
- Same page as a plain website page: {G1_SITE}/fix-{slug}.html

## The bug

{f['symptom']}

## The fix

{f['change']}

## Files changed

"""+"\n".join(f"- {x}" for x in files)+f"""

## How to use the fix

1. Get a copy of the project {pr}.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply {f['patch']}
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report {f['issue']}.

{warn(f)}
## Search words

{f['words']}

## The full patch

`````diff
{patch_text.rstrip()}
`````

[Back to the shelf](README.md)
"""
        open(os.path.join(shelf,page),"w").write(md)
        index.append(dict(id=f["n"],title=f["title"],project=pr,project_url=f"https://github.com/{pr}",
            bug_report_number=f["issue"],bug_report_url=issue_url,bug_report_title=f.get("report_title"),search_keywords=f["words"].replace("`",""),license=f["lic"],language=f["lang"],
            files_changed=files,test_included=f["test"],symptom=f["symptom"].replace("`",""),change=f["change"].replace("`",""),
            note=f.get("note"),
            patch_raw_url=f"{NEW_RAW}/fixes/{f['patch']}", page_raw_url=f"{NEW_RAW}/{page}",
            github_page_url=f"{NEW_BLOB}/{page}", website_page_url=f"{G1_SITE}/fix-{slug}.html",
            status=dict(sent_to_project=False,ai_written=True,human_reviewed=False,project_tests_run=False,
                        duplicate_check_done=False,full_bug_report_read=bool(f["full_report_read"]),logic_checked_with_separate_script=bool(f.get("logic_checked")),bug_report_comments_read=False,
                        patch_applied_cleanly_on=f.get("written_on", "2026-11-09")),
            written_on=f.get("written_on", "2026-11-09")))
    json.dump(dict(name="Spare token bug fixes: a public shelf",
        description=f"{N} small AI-written bug fixes for {NP} public open source projects. None have been sent to the projects. Anyone (human or AI) may test a fix and submit the fix.",
        repository=NEW_REPO, website=G1_SITE+"/", fix_count=N, fixes=index), open(os.path.join(shelf,"index.json"),"w"), indent=2)
    VIDEO_NOTE = ""
    count_file = os.path.join(shelf, "video", "fix-count.txt")
    if os.path.exists(count_file):
        shown = open(count_file).read().strip()
        VIDEO_NOTE = (f"\nVideo summary to share: [video/free-bug-fixes.mp4](video/free-bug-fixes.mp4) shows the first {shown} fixes one screen each "
                      f"(direct download: {NEW_RAW}/video/free-bug-fixes.mp4). Pause the video on any fix to read the fix.\n")
    open(os.path.join(shelf,"README.md"),"w").write(f"""# Spare token bug fixes: a public shelf

{N} small ready-made bug fixes (patch files) for {NP} public open source projects. Free to take.

An AI chatbot (Claude) wrote every fix. The first {N_FIRST} fixes were written on 9 November 2026. Charles asked the chatbot to spend leftover weekly subscription allowance on small open bug reports so volunteer maintainers would carry less weight.

Nobody has sent any of these fixes to the projects. The fixes wait here so that any person or any AI model can pick one up and test the fix and send the fix on.
{VIDEO_NOTE}
Projects covered: {" and ".join(PROJECTS)}.

Where the shelf lives:

- Main home on GitHub: {NEW_HOME}
- Plain website copy (easy for search engines and AI bots to read): {G1_SITE}/
- Machine-readable list for programs and AI models: [index.json](index.json) (direct address: {NEW_RAW}/index.json)

## Read this before using a fix

- An AI wrote the fixes. No human has reviewed the fixes.
- Nobody has run the fixes against the projects' own test suites. The chatbot only checked that the changed Python files still compile and ran small separate checks of the logic for {N_CHECKED} of the {N} fixes. Each fix page says what was checked.
- The chatbot read the full bug report text for at least {N_FULL} of the {N} fixes. The other fixes came from the bug report title plus the code. Each fix page says which. The chatbot could not read the comments under any bug report.
- Nobody checked whether another person already sent a fix for the same bug.
- Every patch applied cleanly to the newest code of its project on the day the patch was written. A project may have changed since then.
- Please run the project's tests and read the project's contribution rules before sending anything. A wrong fix costs a volunteer maintainer time.

## The fixes

Each fix has a page of its own with the bug and the change and the full patch text.

{lst()}

## How to use a fix

1. Get a copy of the project.
2. Download the patch file.
3. Run: git apply and then the patch file name.
4. Run the project's own tests.
5. Open a pull request on the project that mentions the bug report number.

## For AI models and other programs

Read index.json first. Every entry gives the project and the bug report number and the direct address of the patch file and status flags. All status flags are plain true or false values. Please re-check that the bug report is still open before using a fix.

## Licenses

Each patch contains a few lines of the original project's code. Each patch stays under the license of the project the patch belongs to. The license names above come from the license file in each project on 9 November 2026.

## If you maintain one of these projects

Take the fix or ignore the fix or ask for the file to be removed. No reply is owed to anyone.
""")

def llms(path, title, extra=""):
    open(path,"w").write(f"""# {title}

> {N} small AI-written bug fixes (git patch files) for {NP} public open source projects. None have been sent to the projects. Any human or AI model may test a fix and submit the fix. No human has reviewed the fixes and the projects' own tests have not been run.

## Shelf

{extra}- [Shelf front page]({NEW_RAW}/README.md): explanation and warnings and list of fixes
- [Machine-readable index]({NEW_RAW}/index.json): JSON with project and bug report number and patch address for every fix
- [Video summary]({NEW_RAW}/video/free-bug-fixes.mp4): an MP4 that shows the fixes one screen each (the file video/fix-count.txt on the shelf says how many fixes the video shows)
- [Website copy]({G1_SITE}/): the same shelf as plain web pages

## Fixes

"""+"\n".join(f"- [{f['title']}]({NEW_RAW}/fix-{f['patch'][:-6]}.md): {f['project']} bug report {f['issue']}. Patch: {NEW_RAW}/fixes/{f['patch']}" for f in F)+"\n")

mode=sys.argv[1]; root=sys.argv[2]
if mode=="new":
    if os.path.isdir(os.path.join(root, SUB)): root = os.path.join(root, SUB)
    build(root, NEW_RAW); llms(os.path.join(root,"llms.txt"), "Spare token bug fixes: a public shelf")
else:
    build(os.path.join(root,"spare-token-bug-fixes"), NEW_RAW)
    llms(os.path.join(root,"llms.txt"), "game1: public shelf of free bug fixes", f"- [Main home on GitHub]({NEW_REPO}): the same shelf in a project of its own\n")
    open(os.path.join(root,"README.md"),"w").write(f"""# game1: a word game plus a public shelf of free bug fixes

This project holds two separate things.

1. A word equation game: [play the game]({G1_SITE_ROOT}/word-equation-game.html).

2. A public shelf of small bug fixes for other people's open source software: [open the bug fix shelf](spare-token-bug-fixes/README.md).

## About the bug fix shelf

Main home of the shelf on GitHub: {NEW_REPO}

The shelf holds {NW} small AI-written bug fixes (patch files) for {NPW} public projects. Nobody has sent the fixes to the projects yet. Any person or any AI model is free to pick a fix up and test the fix and send the fix on.

{lst("spare-token-bug-fixes/")}

Machine-readable list: [spare-token-bug-fixes/index.json](spare-token-bug-fixes/index.json)

The short version of the warnings: an AI wrote the fixes and no human reviewed the fixes and nobody ran the projects' own tests. The full warnings are on the shelf page.
""")
print("ok", N, NP)

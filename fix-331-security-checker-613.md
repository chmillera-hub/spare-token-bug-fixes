# Fix 331: security-checker: the warning about files written by a reviewer stops at 20 and hides how many more there are

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: feat(providers): process transport の書き込み検知で、20 件を超えた分の件数も報告する
- Bug report: number 613 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/613))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/331-security-checker-613.patch](fixes/331-security-checker-613.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/331-security-checker-613.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-331-security-checker-613.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-331-security-checker-613.html

## The bug

created_paths in src/security_checker/providers/process/sandbox.py stops listing after 20 entries and does not say whether more exist. A reviewer that wrote hundreds of files gives the same warning as one that wrote 20.

## The fix

created_paths now counts every entry and adds one last entry such as ほか 5 件 when more than 20 exist. The first 20 entries are unchanged. A new file tests/unit/test_created_paths_reports_the_rest.py covers 25 files and exactly 20 files.

## Files changed

- src/security_checker/providers/process/sandbox.py
- tests/unit/test_created_paths_reports_the_rest.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 331-security-checker-613.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 613.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The last entry is a count and not a path. The two callers the chatbot found join the entries into a warning text and store the list in the trace.

## Search words

security-checker providers process sandbox created_paths CREATED_PATHS_LIMIT 20 remaining count warning reviewer wrote files

## The full patch

`````diff
diff --git a/src/security_checker/providers/process/sandbox.py b/src/security_checker/providers/process/sandbox.py
index c5c8d73..fc85ae2 100644
--- a/src/security_checker/providers/process/sandbox.py
+++ b/src/security_checker/providers/process/sandbox.py
@@ -171,11 +171,15 @@ def created_paths(cwd: Path) -> tuple[str, ...]:
     (§25.2 の契約テスト 9 番)。絶対パスでこの外に書かれた場合は検知できない。
     """
     found: list[str] = []
+    total = 0
     for path in sorted(cwd.rglob("*")):
-        suffix = "/" if path.is_dir() else ""
-        found.append(path.relative_to(cwd).as_posix() + suffix)
-        if len(found) >= CREATED_PATHS_LIMIT:
-            break
+        total += 1
+        if len(found) < CREATED_PATHS_LIMIT:
+            suffix = "/" if path.is_dir() else ""
+            found.append(path.relative_to(cwd).as_posix() + suffix)
+    if total > CREATED_PATHS_LIMIT:
+        # 上限を超えた分は件数だけを知らせる (#613)
+        found.append(f"ほか {total - CREATED_PATHS_LIMIT} 件")
     return tuple(found)
 
 
diff --git a/tests/unit/test_created_paths_reports_the_rest.py b/tests/unit/test_created_paths_reports_the_rest.py
new file mode 100644
index 0000000..a86102c
--- /dev/null
+++ b/tests/unit/test_created_paths_reports_the_rest.py
@@ -0,0 +1,32 @@
+"""created_paths: 上限を超えた分の件数も最後の 1 件として返すこと (#613)."""
+
+from __future__ import annotations
+
+from pathlib import Path
+
+from security_checker.providers.process.sandbox import CREATED_PATHS_LIMIT, created_paths
+
+
+def _fill(cwd: Path, count: int) -> None:
+    for index in range(count):
+        (cwd / f"file{index:03d}.txt").write_text("x", encoding="utf-8")
+
+
+def test_more_files_than_the_limit_end_with_the_remaining_count(tmp_path: Path) -> None:
+    _fill(tmp_path, CREATED_PATHS_LIMIT + 5)
+
+    found = created_paths(tmp_path)
+
+    assert len(found) == CREATED_PATHS_LIMIT + 1
+    assert found[0] == "file000.txt"
+    assert found[-1] == "ほか 5 件"
+
+
+def test_exactly_the_limit_has_no_extra_entry(tmp_path: Path) -> None:
+    """対になるケース."""
+    _fill(tmp_path, CREATED_PATHS_LIMIT)
+
+    found = created_paths(tmp_path)
+
+    assert len(found) == CREATED_PATHS_LIMIT
+    assert all(name.startswith("file") for name in found)
`````

[Back to the shelf](README.md)

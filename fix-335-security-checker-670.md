# Fix 335: security-checker: a changed binary file is missing from the changed files of a diff

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(github): バイナリファイルの変更が changed_files に入らず、依存の jar などの変更が diff 外になる
- Bug report: number 670 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/670))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/335-security-checker-670.patch](fixes/335-security-checker-670.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/335-security-checker-670.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-335-security-checker-670.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-335-security-checker-670.html

## The bug

parse_unified_diff in src/security_checker/github/pr.py learns the path of a file from the --- and +++ lines. A binary change has neither line (only Binary files ... differ) so the file never reaches changed_files.

## The fix

The parser now remembers the path from the diff --git line and adds that path to the changed files when the header holds a Binary files ... differ line. A new file tests/unit/test_diff_binary_files_are_changed_files.py covers a changed binary file and a new binary file with a space in the name and a text file that follows a binary file.

## Files changed

- src/security_checker/github/pr.py
- tests/unit/test_diff_binary_files_are_changed_files.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 335-security-checker-670.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 670.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot ran a separate scratch copy of the new helper that splits the diff --git line against six made-up lines and all six gave the expected result. The chatbot did not run the project's tests. A binary file that was renamed in the same change (two different paths on the diff --git line) is still not counted.

## Search words

security-checker github pr parse_unified_diff Binary files differ changed_files diff --git binary change missing

## The full patch

`````diff
diff --git a/src/security_checker/github/pr.py b/src/security_checker/github/pr.py
index d412df7..3261495 100644
--- a/src/security_checker/github/pr.py
+++ b/src/security_checker/github/pr.py
@@ -84,12 +84,19 @@ def parse_unified_diff(text: str) -> tuple[dict[str, tuple[tuple[int, int], ...]
     changed: set[str] = set()
     current: str | None = None
     old_path: str | None = None
+    git_path: str | None = None
     # `diff --git` 行の無い素の unified diff も受け付けるよう、先頭はヘッダとして扱う
     in_header = True
     for line in text.splitlines():
         if line.startswith("diff --git "):
             in_header = True
             current = old_path = None
+            git_path = _same_path(line[len("diff --git ") :])
+            continue
+        if in_header and line.startswith("Binary files ") and line.endswith(" differ"):
+            # バイナリの変更には --- / +++ もハンクも無い. diff --git 行のパスで数える (#670)
+            if git_path is not None:
+                changed.add(git_path)
             continue
         if in_header and line.startswith("--- "):
             old_path = _strip_prefix(line[4:])
@@ -113,6 +120,17 @@ def parse_unified_diff(text: str) -> tuple[dict[str, tuple[tuple[int, int], ...]
     return {path: tuple(ranges) for path, ranges in added.items()}, changed
 
 
+def _same_path(rest: str) -> str | None:
+    """`a/x b/x` から x を取り出す. 前後でパスが違う (名前の変更) ときは None."""
+    half, odd = divmod(len(rest) - 1, 2)
+    if odd or half < 0 or rest[half] != " ":
+        return None
+    before, after = rest[:half], rest[half + 1 :]
+    if before.startswith("a/") and after.startswith("b/") and before[2:] == after[2:]:
+        return before[2:]
+    return None
+
+
 def _strip_prefix(raw: str) -> str | None:
     path = raw.split("\t", 1)[0]
     if path == "/dev/null":
diff --git a/tests/unit/test_diff_binary_files_are_changed_files.py b/tests/unit/test_diff_binary_files_are_changed_files.py
new file mode 100644
index 0000000..be6d0a3
--- /dev/null
+++ b/tests/unit/test_diff_binary_files_are_changed_files.py
@@ -0,0 +1,46 @@
+"""parse_unified_diff: バイナリファイルの変更も changed_files に入れること (#670)."""
+
+from __future__ import annotations
+
+from security_checker.github.pr import parse_unified_diff
+
+BINARY = (
+    "diff --git a/img/logo.png b/img/logo.png\n"
+    "index 1111111..2222222 100644\n"
+    "Binary files a/img/logo.png and b/img/logo.png differ\n"
+)
+NEW_BINARY = (
+    "diff --git a/data/a b.bin b/data/a b.bin\n"
+    "new file mode 100644\n"
+    "index 0000000..3333333\n"
+    "Binary files /dev/null and b/data/a b.bin differ\n"
+)
+TEXT = (
+    "diff --git a/app.py b/app.py\n"
+    "index 4444444..5555555 100644\n"
+    "--- a/app.py\n"
+    "+++ b/app.py\n"
+    "@@ -1,0 +2,1 @@\n"
+    "+x = 1\n"
+)
+
+
+def test_changed_binary_file_is_counted() -> None:
+    added, changed = parse_unified_diff(BINARY)
+
+    assert added == {}
+    assert changed == {"img/logo.png"}
+
+
+def test_new_binary_file_with_a_space_in_its_name_is_counted() -> None:
+    added, changed = parse_unified_diff(NEW_BINARY)
+
+    assert added == {}
+    assert changed == {"data/a b.bin"}
+
+
+def test_text_file_after_a_binary_file_is_still_parsed() -> None:
+    added, changed = parse_unified_diff(BINARY + TEXT)
+
+    assert added == {"app.py": ((2, 2),)}
+    assert changed == {"img/logo.png", "app.py"}
`````

[Back to the shelf](README.md)

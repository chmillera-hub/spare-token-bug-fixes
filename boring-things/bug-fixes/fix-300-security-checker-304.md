# Fix 300: security-checker: repository facts are empty when the checked folder sits under a folder named build or vendor

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(context): collect_repo_facts が除外ディレクトリを絶対パスで判定し、build/ や vendor/ の下にあるリポジトリでは事実が空になる
- Bug report: number 304 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/304))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/300-security-checker-304.patch](fixes/300-security-checker-304.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/300-security-checker-304.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-300-security-checker-304.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-300-security-checker-304.html

## The bug

collect_repo_facts in src/security_checker/context/facts.py tests every part of the absolute path against SKIP_DIRS. A repository at a place such as /home/u/build/repo has every file skipped and all facts come out unknown.

## The fix

The check now uses path.relative_to(root).parts so only folders inside the checked folder count. A new file tests/unit/test_repo_facts_under_a_directory_named_build.py covers a repository under a folder named build and a build folder inside the repository.

## Files changed

- src/security_checker/context/facts.py
- tests/unit/test_repo_facts_under_a_directory_named_build.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 300-security-checker-304.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 304.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes.

## Search words

security-checker context facts collect_repo_facts SKIP_DIRS build vendor absolute path parts relative_to unknown facts

## The full patch

`````diff
diff --git a/src/security_checker/context/facts.py b/src/security_checker/context/facts.py
index 1f22479..3da3f10 100644
--- a/src/security_checker/context/facts.py
+++ b/src/security_checker/context/facts.py
@@ -79,7 +79,7 @@ def collect_repo_facts(root: Path) -> RepoFacts:
     for path in root.rglob("*"):
         if seen >= MAX_FILES:
             break
-        if any(part in SKIP_DIRS for part in path.parts):
+        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
             continue
         if not path.is_file():
             continue
diff --git a/tests/unit/test_repo_facts_under_a_directory_named_build.py b/tests/unit/test_repo_facts_under_a_directory_named_build.py
new file mode 100644
index 0000000..7941620
--- /dev/null
+++ b/tests/unit/test_repo_facts_under_a_directory_named_build.py
@@ -0,0 +1,24 @@
+"""collect_repo_facts: 検査対象の上にあるディレクトリ名で除外しないこと (#304)."""
+
+from __future__ import annotations
+
+from pathlib import Path
+
+from security_checker.context.facts import collect_repo_facts
+
+
+def test_repository_placed_under_a_directory_named_build_is_still_scanned(tmp_path: Path) -> None:
+    root = tmp_path / "build" / "repo"
+    root.mkdir(parents=True)
+    (root / "app.py").write_text("print(1)\n", encoding="utf-8")
+
+    assert collect_repo_facts(root).languages == ["Python"]
+
+
+def test_build_directory_inside_the_repository_is_still_skipped(tmp_path: Path) -> None:
+    """対になるケース."""
+    inner = tmp_path / "build"
+    inner.mkdir()
+    (inner / "generated.py").write_text("print(1)\n", encoding="utf-8")
+
+    assert collect_repo_facts(tmp_path).languages == []
`````

[Back to the shelf](README.md)

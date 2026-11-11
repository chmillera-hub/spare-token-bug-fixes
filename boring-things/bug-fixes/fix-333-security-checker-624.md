# Fix 333: security-checker: an evaluation case can write outside the temporary workspace through ../ in its id or path

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(eval): 評価ケースの path と id に ../ を書くと、一時ワークスペースの外にファイルを書き出す
- Bug report: number 624 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/624))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/333-security-checker-624.patch](fixes/333-security-checker-624.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/333-security-checker-624.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-333-security-checker-624.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-333-security-checker-624.html

## The bug

_prepare in src/security_checker/eval/runner.py writes the code of a case to workspace / id / path with no check. An id or a path with ../ writes a file outside the temporary workspace.

## The fix

EvalCase.id now accepts only letters and digits and . and _ and - (the pattern from the bug report). _prepare also resolves the folder and the file of each case and raises ConfigError when the folder is not directly inside the workspace or the file is not inside the folder. A new file tests/unit/test_eval_case_id_stays_inside_workspace.py covers five bad ids and one good id.

## Files changed

- src/security_checker/eval/dataset.py
- src/security_checker/eval/runner.py
- tests/unit/test_eval_case_id_stays_inside_workspace.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 333-security-checker-624.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 624.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The new tests cover the id pattern only. The resolve check in _prepare (which also catches ../ in the path and an id of two dots) has no test because the chatbot did not read how to build the objects that _prepare needs. All 100 bundled case ids fit the pattern (the chatbot checked the id lines of the bundled files).

## Search words

security-checker eval dataset EvalCase id path traversal ../ workspace resolve ConfigError _prepare

## The full patch

`````diff
diff --git a/src/security_checker/eval/dataset.py b/src/security_checker/eval/dataset.py
index afc618b..ba3579f 100644
--- a/src/security_checker/eval/dataset.py
+++ b/src/security_checker/eval/dataset.py
@@ -52,7 +52,7 @@ class EvalCase(BaseModel):
 
     model_config = ConfigDict(frozen=True, extra="forbid")
 
-    id: str
+    id: str = Field(pattern=r"^[A-Za-z0-9._-]+$")
     source: str = "handmade"
     language: str = "python"
     candidate: CaseCandidate
diff --git a/src/security_checker/eval/runner.py b/src/security_checker/eval/runner.py
index bd36a9c..9623f3a 100644
--- a/src/security_checker/eval/runner.py
+++ b/src/security_checker/eval/runner.py
@@ -64,6 +64,14 @@ def _prepare(dataset: Dataset, config: Config, workspace: Path, setup: ReviewerS
     for case in dataset.cases:
         root = workspace / case.id
         target = root / case.candidate.path
+        # id や path の ../ で一時ワークスペースの外に書かない (#624)
+        inside = root.resolve().parent == workspace.resolve() and target.resolve().is_relative_to(
+            root.resolve()
+        )
+        if not inside:
+            raise ConfigError(
+                f"評価ケース {case.id!r} の id / path がワークスペースの外を指しています"
+            )
         target.parent.mkdir(parents=True, exist_ok=True)
         target.write_text(case.code, encoding="utf-8")
 
diff --git a/tests/unit/test_eval_case_id_stays_inside_workspace.py b/tests/unit/test_eval_case_id_stays_inside_workspace.py
new file mode 100644
index 0000000..9885a16
--- /dev/null
+++ b/tests/unit/test_eval_case_id_stays_inside_workspace.py
@@ -0,0 +1,44 @@
+"""評価ケースの id: ../ などで一時ワークスペースの外を指せないこと (#624)."""
+
+from __future__ import annotations
+
+from pathlib import Path
+
+import pytest
+
+from security_checker.errors import ConfigError
+from security_checker.eval.dataset import load_dataset
+
+CASE = """\
+candidate:
+  scanner: semgrep
+  rule_id: python.lang.security.dangerous-subprocess-use
+  path: app/upload.py
+  start_line: 12
+code: |
+  import subprocess
+ground_truth:
+  vulnerable: true
+  severity: high
+  rationale: 引数が利用者の入力から来る
+"""
+
+
+def _dataset(tmp_path: Path, case_id: str) -> Path:
+    cases = tmp_path / "cases"
+    cases.mkdir()
+    (cases / "x.yaml").write_text(f'id: "{case_id}"\n' + CASE, encoding="utf-8")
+    return tmp_path
+
+
+@pytest.mark.parametrize("case_id", ["../evil", "a/b", "a\\\\b", "", "名前"])
+def test_id_with_other_characters_is_a_config_error(tmp_path: Path, case_id: str) -> None:
+    with pytest.raises(ConfigError):
+        load_dataset(_dataset(tmp_path, case_id))
+
+
+def test_plain_id_still_loads(tmp_path: Path) -> None:
+    """対になるケース."""
+    dataset = load_dataset(_dataset(tmp_path, "0001-upload.v2_a"))
+
+    assert dataset.cases[0].id == "0001-upload.v2_a"
`````

[Back to the shelf](README.md)

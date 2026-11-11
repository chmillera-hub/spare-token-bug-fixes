# Fix 315: security-checker: an evaluation case with no rationale loads silently although the docs call rationale required

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(eval): ground_truth.rationale は「必須」と書かれているのに、省略しても黙って読み込める
- Bug report: number 235 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/235))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/315-security-checker-235.patch](fixes/315-security-checker-235.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/315-security-checker-235.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-315-security-checker-235.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-315-security-checker-235.html

## The bug

GroundTruth.rationale in src/security_checker/eval/dataset.py defaults to an empty string. docs/evaluation.md says rationale is required and that broken cases are errors yet a case with no rationale loads with no warning.

## The fix

rationale is now a required field with a minimum length of 1 so a missing or empty rationale ends in the existing ConfigError for a broken case. A new file tests/unit/test_eval_dataset_rationale_required.py uses the case from the bug report.

## Files changed

- src/security_checker/eval/dataset.py
- tests/unit/test_eval_dataset_rationale_required.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 315-security-checker-235.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 235.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. A rationale made only of spaces still loads. The bug report says all 100 bundled cases hold a rationale and the chatbot did not check the 100 files.

## Search words

security-checker eval dataset GroundTruth rationale required Field min_length ConfigError load_dataset missing

## The full patch

`````diff
diff --git a/src/security_checker/eval/dataset.py b/src/security_checker/eval/dataset.py
index afc618b..b47877e 100644
--- a/src/security_checker/eval/dataset.py
+++ b/src/security_checker/eval/dataset.py
@@ -28,7 +28,7 @@ class GroundTruth(BaseModel):
     cwe: list[str] = Field(default_factory=list)
     severity: Severity = Severity.NONE
     #: なぜその正解なのか. 評価レポートに載せて、ラベルの妥当性を後から検証できるようにする
-    rationale: str = ""
+    rationale: str = Field(min_length=1)
 
 
 class CaseCandidate(BaseModel):
diff --git a/tests/unit/test_eval_dataset_rationale_required.py b/tests/unit/test_eval_dataset_rationale_required.py
new file mode 100644
index 0000000..0fee241
--- /dev/null
+++ b/tests/unit/test_eval_dataset_rationale_required.py
@@ -0,0 +1,43 @@
+"""評価データセット: ground_truth.rationale の省略と空文字をエラーにすること (#235)."""
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
+"""
+
+
+def _dataset(tmp_path: Path, extra: str) -> Path:
+    cases = tmp_path / "cases"
+    cases.mkdir()
+    (cases / "x.yaml").write_text(CASE + extra, encoding="utf-8")
+    return tmp_path
+
+
+@pytest.mark.parametrize("extra", ["", '  rationale: ""\n'])
+def test_missing_or_empty_rationale_is_a_config_error(tmp_path: Path, extra: str) -> None:
+    with pytest.raises(ConfigError):
+        load_dataset(_dataset(tmp_path, extra))
+
+
+def test_case_with_a_rationale_still_loads(tmp_path: Path) -> None:
+    """対になるケース."""
+    dataset = load_dataset(_dataset(tmp_path, "  rationale: 引数が利用者の入力から来る\n"))
+
+    assert dataset.cases[0].ground_truth.rationale == "引数が利用者の入力から来る"
`````

[Back to the shelf](README.md)

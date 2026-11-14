# Fix 295: security-checker: no test covers the warning section of the evaluation table

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(eval): runner.py の to_markdown で未テストの分岐をテストする（3 行）
- Bug report: number 502 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/502))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/295-security-checker-502.patch](fixes/295-security-checker-502.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/295-security-checker-502.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-295-security-checker-502.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-295-security-checker-502.html

## The bug

to_markdown in src/security_checker/eval/runner.py adds a section that lists every warning of the evaluation run. No test ran those three lines.

## The fix

Tests only. A new file tests/unit/test_eval_markdown_warnings_section.py builds a result with two warnings and expects the heading and one line per warning and builds a result with no warning and expects no heading.

## Files changed

- tests/unit/test_eval_markdown_warnings_section.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 295-security-checker-502.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 502.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The tests build an EvalResult with the default empty metrics and assume that to_markdown can render empty metrics. The chatbot did not read every helper that to_markdown calls. The chatbot did not run the tests or a coverage tool so nobody has confirmed that the new tests reach the named lines.

## Search words

security-checker eval runner to_markdown warnings section EvalResult markdown table untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_eval_markdown_warnings_section.py b/tests/unit/test_eval_markdown_warnings_section.py
new file mode 100644
index 0000000..664a2af
--- /dev/null
+++ b/tests/unit/test_eval_markdown_warnings_section.py
@@ -0,0 +1,19 @@
+"""eval の比較表 (Markdown): 警告があれば「警告」の節に 1 行ずつ並べること."""
+
+from __future__ import annotations
+
+from security_checker.eval.runner import EvalResult, to_markdown
+
+
+def test_warnings_are_listed_in_their_own_section() -> None:
+    result = EvalResult(dataset="d", cases=0, warnings=["予算の上限に達しました", "w2"])
+
+    lines = to_markdown(result).split("\n")
+
+    start = lines.index("## 警告")
+    assert lines[start : start + 5] == ["## 警告", "", "- 予算の上限に達しました", "- w2", ""]
+
+
+def test_no_warning_section_without_warnings() -> None:
+    """対になるケース."""
+    assert "## 警告" not in to_markdown(EvalResult(dataset="d", cases=0))
`````

[Back to the shelf](README.md)

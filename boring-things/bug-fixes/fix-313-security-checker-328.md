# Fix 313: security-checker: the evaluation table embeds model text and names with no cleaning

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(eval): 比較表 (Markdown) が LLM の summary をそのまま埋め込み、report.md・PR コメントと同じ無害化を通していない
- Bug report: number 328 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/328))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/313-security-checker-328.patch](fixes/313-security-checker-328.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/313-security-checker-328.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-313-security-checker-328.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-313-security-checker-328.html

## The bug

to_markdown in src/security_checker/eval/runner.py puts the summary written by the model and the warnings and the dataset name and the reviewer names into the Markdown table as they are. report.md and the PR comment clean the same kinds of text.

## The fix

to_markdown now passes the summary and every warning through md.text and wraps the dataset name and every reviewer name with md.code_span. A new file tests/unit/test_eval_markdown_sanitized.py covers a dataset name and a reviewer name with a backtick and a warning with an HTML tag.

## Files changed

- src/security_checker/eval/runner.py
- tests/unit/test_eval_markdown_sanitized.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 313-security-checker-328.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 328.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The heading and the reviewer line now show the names inside backticks so an existing test that compares those two lines may need an update. The new test does not cover the summary line. The test assumes that md.text neutralises an HTML tag.

## Search words

security-checker eval runner to_markdown sanitize md.text code_span summary warnings dataset reviewer markdown injection

## The full patch

`````diff
diff --git a/src/security_checker/eval/runner.py b/src/security_checker/eval/runner.py
index bd36a9c..262b3b1 100644
--- a/src/security_checker/eval/runner.py
+++ b/src/security_checker/eval/runner.py
@@ -27,6 +27,7 @@ from security_checker.models.candidate import Candidate
 from security_checker.models.finding import Finding
 from security_checker.models.task import ReviewTask
 from security_checker.observability.cost import PriceTable
+from security_checker.report import sanitize as md
 from security_checker.run import (
     ReviewerSetup,
     build_reviewers,
@@ -160,9 +161,9 @@ def to_markdown(result: EvalResult) -> str:
     """人間が読む比較表 (§27.3). 数字を隠さない."""
     metrics = result.metrics
     lines = [
-        f"# 評価結果: {result.dataset}",
+        f"# 評価結果: {md.code_span(result.dataset)}",
         "",
-        f"- Reviewer: {', '.join(result.reviewers) or '(なし)'}",
+        f"- Reviewer: {', '.join(md.code_span(name) for name in result.reviewers) or '(なし)'}",
         f"- 集約戦略: {result.aggregation}",
         f"- ケース数: {metrics.cases} "
         f"(採点外: エラー {metrics.errors} / 未レビュー {metrics.not_reviewed})",
@@ -204,12 +205,13 @@ def to_markdown(result: EvalResult) -> str:
         by_id = {outcome.case_id: outcome for outcome in result.outcomes}
         for case_id in metrics.missed_case_ids:
             outcome = by_id[case_id]
-            lines.append(f"- `{case_id}` — {outcome.summary or '(要約なし)'}")
+            summary = md.text(outcome.summary) if outcome.summary else "(要約なし)"
+            lines.append(f"- `{case_id}` — {summary}")
         lines.append("")
 
     if result.warnings:
         lines += ["## 警告", ""]
-        lines += [f"- {message}" for message in result.warnings]
+        lines += [f"- {md.text(message)}" for message in result.warnings]
         lines.append("")
 
     return "\n".join(lines)
diff --git a/tests/unit/test_eval_markdown_sanitized.py b/tests/unit/test_eval_markdown_sanitized.py
new file mode 100644
index 0000000..d4b2627
--- /dev/null
+++ b/tests/unit/test_eval_markdown_sanitized.py
@@ -0,0 +1,20 @@
+"""eval の比較表 (Markdown): 名前と警告を無害化して埋め込むこと (#328)."""
+
+from __future__ import annotations
+
+from security_checker.eval.runner import EvalResult, to_markdown
+
+
+def test_names_and_warnings_cannot_inject_markup() -> None:
+    result = EvalResult(
+        dataset="data`set",
+        cases=0,
+        reviewers=["re`viewer"],
+        warnings=["<img src=x onerror=alert(1)>"],
+    )
+
+    text = to_markdown(result)
+
+    assert "# 評価結果: `data'set`" in text
+    assert "- Reviewer: `re'viewer`" in text
+    assert "<img src=x" not in text
`````

[Back to the shelf](README.md)

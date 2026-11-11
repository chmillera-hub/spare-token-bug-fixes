# Fix 281: security-checker: no test covers the suppression row or the false positive count of the report summary

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(report): markdown.py の _summary で未テストの分岐をテストする（2 行）
- Bug report: number 559 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/559))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/281-security-checker-559.patch](fixes/281-security-checker-559.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/281-security-checker-559.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-281-security-checker-559.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-281-security-checker-559.html

## The bug

_summary in src/security_checker/report/markdown.py adds a row for suppressed candidates and adds the false positive count to the verdict row. No test ran those two lines.

## The fix

Tests only. A new file tests/unit/test_markdown_summary_suppressed_and_false_positive.py expects the row with 3 suppressed candidates (baseline 2 and ignore 1) and expects the verdict row to read false positive 1 when the only finding is a false positive.

## Files changed

- tests/unit/test_markdown_summary_suppressed_and_false_positive.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 281-security-checker-559.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 559.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The bug report lists the untested lines from a coverage run on an older commit. The chatbot did not run the tests or a coverage tool so nobody has confirmed that the new tests reach the named lines.

## Search words

security-checker markdown _summary suppression_label suppressed false_positive breakdown report.md untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_markdown_summary_suppressed_and_false_positive.py b/tests/unit/test_markdown_summary_suppressed_and_false_positive.py
new file mode 100644
index 0000000..e52cd6d
--- /dev/null
+++ b/tests/unit/test_markdown_summary_suppressed_and_false_positive.py
@@ -0,0 +1,38 @@
+"""report.md の概要表: 抑制の行と、誤検出だけのときの判定の行."""
+
+from __future__ import annotations
+
+from security_checker.models.enums import FindingStatus
+from security_checker.models.finding import SuppressionReason
+from security_checker.models.report import SuppressedCandidate
+from security_checker.report.markdown import _summary
+from tests.factories import make_candidate, make_finding, make_report
+
+
+def test_suppressed_candidates_get_their_own_row() -> None:
+    suppressed = [
+        SuppressedCandidate(candidate=make_candidate("s1"), reason=SuppressionReason.BASELINE),
+        SuppressedCandidate(candidate=make_candidate("s2"), reason=SuppressionReason.BASELINE),
+        SuppressedCandidate(candidate=make_candidate("s3"), reason=SuppressionReason.IGNORE_FILE),
+    ]
+    report = make_report([], suppressed=suppressed)
+
+    lines = _summary(report)
+
+    assert "| 抑制 | 3 件 (baseline 2 / ignore 1) (レビュー・判定の対象外) |" in lines
+
+
+def test_false_positives_alone_are_named_in_the_verdict_row() -> None:
+    candidate = make_candidate("c1")
+    report = make_report([candidate], [make_finding(candidate, FindingStatus.FALSE_POSITIVE)])
+
+    lines = _summary(report)
+
+    assert "| 判定 | 誤検出 1 |" in lines
+
+
+def test_no_suppression_row_without_suppressed_candidates() -> None:
+    """対になるケース."""
+    lines = _summary(make_report([]))
+
+    assert not any(line.startswith("| 抑制 |") for line in lines)
`````

[Back to the shelf](README.md)

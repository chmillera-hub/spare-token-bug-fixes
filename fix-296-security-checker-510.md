# Fix 296: security-checker: no test covers how the summary comment shows a reviewer verdict that failed

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(github): comment.py の _summary_block で未テストの分岐をテストする（3 行）
- Bug report: number 510 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/510))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/296-security-checker-510.patch](fixes/296-security-checker-510.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/296-security-checker-510.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-296-security-checker-510.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-296-security-checker-510.html

## The bug

_summary_block in src/security_checker/github/comment.py leaves a failed verdict out of the review required list and marks a failed verdict with a warning sign in the reviewer table. No test ran those lines.

## The fix

Tests only. A new file tests/unit/test_github_comment_summary_block_failed_verdicts.py builds a finding with one good verdict and one provider_error verdict and expects only the good reviewer in the review required list and expects the warning row for the failed reviewer in the table of a confirmed finding.

## Files changed

- tests/unit/test_github_comment_summary_block_failed_verdicts.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 296-security-checker-510.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 510.

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

security-checker github comment _summary_block verdict status provider_error reviewer table review required untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_github_comment_summary_block_failed_verdicts.py b/tests/unit/test_github_comment_summary_block_failed_verdicts.py
new file mode 100644
index 0000000..7551d13
--- /dev/null
+++ b/tests/unit/test_github_comment_summary_block_failed_verdicts.py
@@ -0,0 +1,40 @@
+"""sticky サマリの Finding ブロック: 失敗した Reviewer の判定の扱い."""
+
+from __future__ import annotations
+
+from security_checker.github.comment import _summary_block
+from security_checker.models.enums import FindingStatus
+from security_checker.models.verdict import VerdictStatus
+from tests.factories import make_candidate, make_finding, make_verdict
+
+
+def test_review_required_block_lists_only_the_verdicts_that_succeeded() -> None:
+    finding = make_finding(
+        make_candidate(),
+        FindingStatus.REVIEW_REQUIRED,
+        verdicts=[
+            make_verdict("r1"),
+            make_verdict("r2", status=VerdictStatus.PROVIDER_ERROR, vulnerable=False),
+        ],
+    )
+
+    lines = _summary_block(finding)
+
+    assert any(line.startswith("- `r1`: ") for line in lines)
+    assert not any("`r2`" in line for line in lines)
+
+
+def test_confirmed_block_marks_a_failed_verdict_in_the_reviewer_table() -> None:
+    finding = make_finding(
+        make_candidate(),
+        FindingStatus.CONFIRMED,
+        verdicts=[
+            make_verdict("r1"),
+            make_verdict("r2", status=VerdictStatus.PROVIDER_ERROR, vulnerable=False),
+        ],
+    )
+
+    lines = _summary_block(finding)
+
+    assert "| `r2` | ⚠️ provider_error | | | |" in lines
+    assert any(line.startswith("| `r1` | ✅ | ") for line in lines)
`````

[Back to the shelf](README.md)

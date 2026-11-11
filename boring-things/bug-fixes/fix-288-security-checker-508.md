# Fix 288: security-checker: no test covers the summary comment limits for the number of findings and the body length

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(github): comment.py の render_summary で未テストの分岐をテストする（2 行）
- Bug report: number 508 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/508))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/288-security-checker-508.patch](fixes/288-security-checker-508.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/288-security-checker-508.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-288-security-checker-508.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-288-security-checker-508.html

## The bug

render_summary in src/security_checker/github/comment.py shows at most 15 findings and cuts a body longer than 60000 characters with a notice. No test ran those two lines.

## The fix

Tests only. A new file tests/unit/test_github_comment_summary_limits.py builds 17 confirmed findings and expects the line for 2 more findings. A second test lowers MAX_BODY_CHARS to 200 and expects the body to be cut at 200 characters and to end with the notice.

## Files changed

- tests/unit/test_github_comment_summary_limits.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 288-security-checker-508.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 508.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The third test assumes that a summary of three findings is longer than 200 characters and that render_summary reads MAX_BODY_CHARS from the module at call time. The chatbot read the function and both hold in the newest code. The chatbot did not run the tests or a coverage tool so nobody has confirmed that the new tests reach the named lines.

## Search words

security-checker github comment render_summary MAX_SUMMARY_FINDINGS MAX_BODY_CHARS truncate sticky summary untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_github_comment_summary_limits.py b/tests/unit/test_github_comment_summary_limits.py
new file mode 100644
index 0000000..fc1537b
--- /dev/null
+++ b/tests/unit/test_github_comment_summary_limits.py
@@ -0,0 +1,40 @@
+"""sticky サマリ: Finding の件数の上限と、本文の長さの上限."""
+
+from __future__ import annotations
+
+import pytest
+
+from security_checker.github import comment
+from security_checker.models.enums import FindingStatus
+from security_checker.models.report import Report
+from tests.factories import make_candidate, make_finding, make_report
+
+
+def _report(count: int) -> Report:
+    candidates = [make_candidate(f"c{index}", line=index + 1) for index in range(count)]
+    findings = [make_finding(candidate, FindingStatus.CONFIRMED) for candidate in candidates]
+    return make_report(candidates, findings)
+
+
+def test_findings_over_the_limit_are_counted_in_one_line() -> None:
+    body = comment.render_summary(_report(comment.MAX_SUMMARY_FINDINGS + 2))
+
+    assert "_ほか 2 件は full report を参照_" in body
+
+
+def test_findings_at_the_limit_have_no_overflow_line() -> None:
+    """対になるケース."""
+    body = comment.render_summary(_report(comment.MAX_SUMMARY_FINDINGS))
+
+    assert "件は full report を参照_" not in body
+
+
+def test_body_over_the_length_limit_is_cut_with_a_notice(monkeypatch: pytest.MonkeyPatch) -> None:
+    monkeypatch.setattr(comment, "MAX_BODY_CHARS", 200)
+    notice = "\n\n_(長すぎるため省略しました。full report を参照)_\n"
+
+    body = comment.render_summary(_report(3))
+
+    assert body.endswith(notice)
+    assert len(body) == 200 + len(notice)
+    assert body.startswith(comment.SUMMARY_MARKER)
`````

[Back to the shelf](README.md)

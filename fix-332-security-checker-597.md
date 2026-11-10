# Fix 332: security-checker: the PR summary says no problems when every review failed

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(github): レビューが全件失敗 (error / not_reviewed) だと has_problems が偽になり、PR にコメントが付かない
- Bug report: number 597 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/597))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/332-security-checker-597.patch](fixes/332-security-checker-597.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/332-security-checker-597.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-332-security-checker-597.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-332-security-checker-597.html

## The bug

has_problems and render_summary in src/security_checker/github/comment.py look only at confirmed and likely and review required findings. When every candidate ended as error or not reviewed or inconclusive the summary shows the green no problems line and the comment may not be posted at all.

## The fix

has_problems is now true when at least one finding is error or not reviewed or inconclusive. In that case the body shows a warning line that says some candidates could not be reviewed in place of the green line. A new file tests/unit/test_github_comment_all_reviews_failed.py covers the three states and a report with only false positives.

## Files changed

- src/security_checker/github/comment.py
- tests/unit/test_github_comment_all_reviews_failed.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 332-security-checker-597.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 597.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The wording of the warning line follows the bug report.

## Search words

security-checker github comment has_problems render_summary error not_reviewed inconclusive no problems all reviews failed

## The full patch

`````diff
diff --git a/src/security_checker/github/comment.py b/src/security_checker/github/comment.py
index 274992a..6afafef 100644
--- a/src/security_checker/github/comment.py
+++ b/src/security_checker/github/comment.py
@@ -95,10 +95,19 @@ def visible_findings(report: Report) -> list[Finding]:
 def has_problems(report: Report) -> bool:
     """サマリで「問題あり」として扱うか. 判定前の候補 (scan のみ) も含める."""
     if report.findings:
-        return bool(visible_findings(report))
+        return bool(visible_findings(report)) or _has_unreviewed(report)
     return bool(report.candidates)
 
 
+def _has_unreviewed(report: Report) -> bool:
+    """レビューできなかった候補があるか. あれば「問題なし」とは言えない (#597)."""
+    unreviewed = (FindingStatus.ERROR, FindingStatus.NOT_REVIEWED, FindingStatus.INCONCLUSIVE)
+    return any(
+        finding.suppressed is None and finding.status in unreviewed
+        for finding in report.findings
+    )
+
+
 # --- sticky サマリ ---------------------------------------------------------------
 
 
@@ -111,7 +120,9 @@ def render_summary(report: Report, *, report_url: str | None = None) -> str:
 
     if report.findings:
         shown = visible_findings(report)
-        if not shown:
+        if not shown and _has_unreviewed(report):
+            lines += ["⚠️ レビューできなかった候補があります。", ""]
+        elif not shown:
             lines += ["✅ 問題は検出されませんでした。", ""]
         ordered = sorted(shown, key=lambda f: (_SUMMARY_ORDER.index(f.status), -f.severity.order))
         for finding in ordered[:MAX_SUMMARY_FINDINGS]:
diff --git a/tests/unit/test_github_comment_all_reviews_failed.py b/tests/unit/test_github_comment_all_reviews_failed.py
new file mode 100644
index 0000000..13ee257
--- /dev/null
+++ b/tests/unit/test_github_comment_all_reviews_failed.py
@@ -0,0 +1,39 @@
+"""sticky サマリ: レビューできなかった候補だけのときに「問題なし」と言わないこと (#597)."""
+
+from __future__ import annotations
+
+import pytest
+
+from security_checker.github.comment import has_problems, render_summary
+from security_checker.models.enums import FindingStatus
+from tests.factories import make_candidate, make_finding, make_report
+
+CLEAN = "✅ 問題は検出されませんでした。"
+UNREVIEWED = "⚠️ レビューできなかった候補があります。"
+
+
+@pytest.mark.parametrize(
+    "status",
+    [FindingStatus.ERROR, FindingStatus.NOT_REVIEWED, FindingStatus.INCONCLUSIVE],
+)
+def test_unreviewed_findings_count_as_problems(status: FindingStatus) -> None:
+    candidate = make_candidate("c1")
+    report = make_report([candidate], [make_finding(candidate, status)])
+
+    body = render_summary(report)
+
+    assert has_problems(report) is True
+    assert UNREVIEWED in body
+    assert CLEAN not in body
+
+
+def test_only_false_positives_are_still_clean() -> None:
+    """対になるケース."""
+    candidate = make_candidate("c1")
+    report = make_report([candidate], [make_finding(candidate, FindingStatus.FALSE_POSITIVE)])
+
+    body = render_summary(report)
+
+    assert has_problems(report) is False
+    assert CLEAN in body
+    assert UNREVIEWED not in body
`````

[Back to the shelf](README.md)

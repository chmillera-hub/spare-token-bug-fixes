# Fix 325: security-checker: the PR summary calls false positives suppressed which reads like baseline suppression

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(github): サマリの「false positive (suppressed)」の表記が、baseline などの抑制と紛らわしい
- Bug report: number 601 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/601))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/325-security-checker-601.patch](fixes/325-security-checker-601.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/325-security-checker-601.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-325-security-checker-601.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-325-security-checker-601.html

## The bug

_counts_line in src/security_checker/github/comment.py prints N false positive (suppressed). The word suppressed is also the word for candidates removed by the baseline or an ignore rule so a reader cannot tell the two apart and the real suppressed count is not shown.

## The fix

The count line now reads N false positive (PR には非表示) and a separate line shows 抑制 N 件 when candidates were suppressed (the wording the bug report gives). The example in docs/DESIGN.md uses the new wording. A new file tests/unit/test_github_comment_counts_wording.py covers both lines.

## Files changed

- docs/DESIGN.md
- src/security_checker/github/comment.py
- tests/unit/test_github_comment_counts_wording.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 325-security-checker-601.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 601.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The new line for suppressed candidates appears only when the report holds findings. A scan with no review keeps its one-line output.

## Search words

security-checker github comment _counts_line false positive suppressed wording baseline ignore count PR summary

## The full patch

`````diff
diff --git a/docs/DESIGN.md b/docs/DESIGN.md
index 869c899..9fd98bf 100644
--- a/docs/DESIGN.md
+++ b/docs/DESIGN.md
@@ -1878,7 +1878,7 @@ HTML コメントのマーカー `<!-- security-checker:summary:v2 -->` で自
 <!-- security-checker:summary:v2 -->
 ## 🛡 AI Security Review
 
-**1 confirmed** · 0 likely · **1 review required** · 10 false positive (suppressed)
+**1 confirmed** · 0 likely · **1 review required** · 10 false positive (PR には非表示)
 Reviewers: `alpha`, `beta` · Aggregation: consensus (2 of 2)
 ⚠️ trivy が失敗したため、設定ファイルの検査は行われていません。
 
diff --git a/src/security_checker/github/comment.py b/src/security_checker/github/comment.py
index 274992a..41ef521 100644
--- a/src/security_checker/github/comment.py
+++ b/src/security_checker/github/comment.py
@@ -140,7 +140,7 @@ def _counts_line(report: Report) -> list[str]:
         f"**{counts.get('confirmed', 0)} confirmed**",
         f"{counts.get('likely', 0)} likely",
         f"**{counts.get('review_required', 0)} review required**",
-        f"{counts.get('false_positive', 0)} false positive (suppressed)",
+        f"{counts.get('false_positive', 0)} false positive (PR には非表示)",
     ]
     lines = [" · ".join(parts)]
     for status, label in (
@@ -150,6 +150,9 @@ def _counts_line(report: Report) -> list[str]:
     ):
         if counts.get(status.value):
             lines.append(f"⚠️ {label} {counts[status.value]} 件 (「問題なし」ではありません)")
+    if report.suppressed:
+        # 誤検知 (false positive) と、baseline / ignore による抑制を別の言葉で出す (#601)
+        lines.append(f"抑制 {len(report.suppressed)} 件")
     reviewers = ", ".join(f"`{run.name}`" for run in report.reviewers)
     strategy = next(
         (f.aggregation.strategy for f in report.findings if f.aggregation is not None), None
diff --git a/tests/unit/test_github_comment_counts_wording.py b/tests/unit/test_github_comment_counts_wording.py
new file mode 100644
index 0000000..e68a745
--- /dev/null
+++ b/tests/unit/test_github_comment_counts_wording.py
@@ -0,0 +1,38 @@
+"""sticky サマリの件数の行: 誤検知と抑制 (baseline / ignore) を別の言葉で出すこと (#601)."""
+
+from __future__ import annotations
+
+from security_checker.github.comment import _counts_line
+from security_checker.models.enums import FindingStatus
+from security_checker.models.finding import SuppressionReason
+from security_checker.models.report import SuppressedCandidate
+from tests.factories import make_candidate, make_finding, make_report
+
+
+def test_false_positives_and_suppressed_candidates_use_different_words() -> None:
+    candidate = make_candidate("c1")
+    suppressed = [
+        SuppressedCandidate(candidate=make_candidate("s1"), reason=SuppressionReason.BASELINE),
+        SuppressedCandidate(candidate=make_candidate("s2"), reason=SuppressionReason.IGNORE_FILE),
+    ]
+    report = make_report(
+        [candidate],
+        [make_finding(candidate, FindingStatus.FALSE_POSITIVE)],
+        suppressed=suppressed,
+    )
+
+    lines = [line.rstrip() for line in _counts_line(report)]
+
+    assert "1 false positive (PR には非表示)" in lines[0]
+    assert "(suppressed)" not in lines[0]
+    assert "抑制 2 件" in lines
+
+
+def test_no_suppressed_line_without_suppressed_candidates() -> None:
+    """対になるケース."""
+    candidate = make_candidate("c1")
+    report = make_report([candidate], [make_finding(candidate, FindingStatus.FALSE_POSITIVE)])
+
+    lines = [line.rstrip() for line in _counts_line(report)]
+
+    assert not any(line.startswith("抑制") for line in lines)
`````

[Back to the shelf](README.md)

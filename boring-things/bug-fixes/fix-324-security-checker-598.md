# Fix 324: security-checker: the PR summary comment says nothing about scanners that were skipped

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(github): PR コメントのサマリが skipped のスキャナを警告せず、未導入の観点が検査されていないことが分からない
- Bug report: number 598 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/598))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/324-security-checker-598.patch](fixes/324-security-checker-598.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/324-security-checker-598.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-324-security-checker-598.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-324-security-checker-598.html

## The bug

_scanner_warnings in src/security_checker/github/comment.py warns only about failed scanners. A skipped scanner (not installed for example) gives no line so the PR summary hides that one kind of check did not run.

## The fix

_scanner_warnings now adds one line per skipped scanner with the scanner name and the reason when the run holds one. The lines for failed scanners are unchanged and come first. A new file tests/unit/test_github_comment_skipped_scanner.py covers skipped scanners with and without a reason and a failed scanner.

## Files changed

- src/security_checker/github/comment.py
- tests/unit/test_github_comment_skipped_scanner.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 324-security-checker-598.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 598.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The wording of the new line follows the example in the bug report.

## Search words

security-checker github comment _scanner_warnings skipped scanner not installed summary PR comment ScanStatus SKIPPED

## The full patch

`````diff
diff --git a/src/security_checker/github/comment.py b/src/security_checker/github/comment.py
index 274992a..ab0a059 100644
--- a/src/security_checker/github/comment.py
+++ b/src/security_checker/github/comment.py
@@ -167,11 +167,17 @@ def _counts_line(report: Report) -> list[str]:
 
 def _scanner_warnings(report: Report) -> list[str]:
     """壊れた事実を隠さない (§7.2)."""
-    return [
+    lines = [
         f"⚠️ `{run.scanner}` が失敗したため、この観点の検査は行われていません。"
         for run in report.scanners
         if run.status is ScanStatus.FAILED
     ]
+    # skipped (未導入など) も、検査していない観点として 1 行で知らせる (#598)
+    for run in report.scanners:
+        if run.status is ScanStatus.SKIPPED:
+            reason = f"（{md.text(run.reason)}）" if run.reason else ""
+            lines.append(f"⏭️ {md.code_span(run.scanner)} は実行されていません{reason}")
+    return lines
 
 
 def _summary_block(finding: Finding) -> list[str]:
diff --git a/tests/unit/test_github_comment_skipped_scanner.py b/tests/unit/test_github_comment_skipped_scanner.py
new file mode 100644
index 0000000..aa2bfa5
--- /dev/null
+++ b/tests/unit/test_github_comment_skipped_scanner.py
@@ -0,0 +1,43 @@
+"""sticky サマリ: skipped のスキャナを 1 行で知らせること (#598)."""
+
+from __future__ import annotations
+
+from security_checker.github.comment import _scanner_warnings
+from security_checker.models.enums import Category, ScanStatus
+from security_checker.models.report import ScannerRun
+from tests.factories import make_report
+
+
+def _run(name: str, status: ScanStatus, reason: str | None = None) -> ScannerRun:
+    return ScannerRun(scanner=name, category=Category.SAST, status=status, reason=reason)
+
+
+def test_skipped_scanner_is_listed_with_its_reason() -> None:
+    report = make_report(
+        [],
+        scanners=[
+            _run("semgrep", ScanStatus.OK),
+            _run("osv", ScanStatus.SKIPPED, "osv-scanner が見つかりません"),
+            _run("trivy", ScanStatus.SKIPPED),
+        ],
+    )
+
+    lines = _scanner_warnings(report)
+
+    assert lines == [
+        "⏭️ `osv` は実行されていません（osv-scanner が見つかりません）",
+        "⏭️ `trivy` は実行されていません",
+    ]
+
+
+def test_failed_scanner_keeps_its_warning_and_comes_first() -> None:
+    report = make_report(
+        [],
+        scanners=[_run("osv", ScanStatus.SKIPPED), _run("semgrep", ScanStatus.FAILED)],
+    )
+
+    lines = _scanner_warnings(report)
+
+    assert len(lines) == 2
+    assert lines[0].startswith("⚠️ `semgrep` が失敗したため")
+    assert lines[1] == "⏭️ `osv` は実行されていません"
`````

[Back to the shelf](README.md)

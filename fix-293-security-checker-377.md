# Fix 293: security-checker: bare numbers 4.0 and 7.0 and 9.0 in the CVSS score to severity mapping

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: refactor: osv.py の severity_from_score にある比較用の数値 (4.0, 7.0, 9.0) を名前付き定数にする
- Bug report: number 377 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/377))
- Project license: MIT
- Language: Python
- Test included: no
- Patch file: [fixes/293-security-checker-377.patch](fixes/293-security-checker-377.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/293-security-checker-377.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-293-security-checker-377.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-293-security-checker-377.html

## The bug

severity_from_score in src/security_checker/scanners/osv.py compares the score with the bare numbers 9.0 and 7.0 and 4.0. The ruff rule PLR2004 reports the three comparisons.

## The fix

Three named constants (CVSS_CRITICAL_MIN and CVSS_HIGH_MIN and CVSS_MEDIUM_MIN) now sit near the top of osv.py and the three comparisons use the constants. Behaviour is unchanged.

## Files changed

- src/security_checker/scanners/osv.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 293-security-checker-377.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 377.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- No test was added because behaviour is unchanged. The chatbot did not run ruff so nobody has confirmed that PLR2004 now reports nothing for the file. The chatbot did not run the project's tests.

## Search words

security-checker osv severity_from_score CVSS 9.0 7.0 4.0 PLR2004 magic value named constant

## The full patch

`````diff
diff --git a/src/security_checker/scanners/osv.py b/src/security_checker/scanners/osv.py
index e1f2901..a3e6577 100644
--- a/src/security_checker/scanners/osv.py
+++ b/src/security_checker/scanners/osv.py
@@ -33,6 +33,10 @@ from security_checker.scanners.filters import is_excluded
 
 EXIT_NO_PACKAGES = 128
 MAX_REFERENCES = 5
+#: CVSS v3 の定性評価の帯の下限 (基本値がこの値以上ならその重大度)
+CVSS_CRITICAL_MIN = 9.0
+CVSS_HIGH_MIN = 7.0
+CVSS_MEDIUM_MIN = 4.0
 
 #: OSV の database_specific.severity (GHSA の表記) → Severity
 _TEXT_SEVERITY = {
@@ -47,11 +51,11 @@ _CVE_RE = re.compile(r"^CVE-\d{4}-\d+$")
 
 def severity_from_score(score: float) -> Severity:
     """CVSS の基本値 → Severity (CVSS v3 の定性評価の帯)."""
-    if score >= 9.0:
+    if score >= CVSS_CRITICAL_MIN:
         return Severity.CRITICAL
-    if score >= 7.0:
+    if score >= CVSS_HIGH_MIN:
         return Severity.HIGH
-    if score >= 4.0:
+    if score >= CVSS_MEDIUM_MIN:
         return Severity.MEDIUM
     if score > 0.0:
         return Severity.LOW
`````

[Back to the shelf](README.md)

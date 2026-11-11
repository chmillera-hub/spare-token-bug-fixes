# Fix 298: security-checker: the CWE list of a finding includes CWEs from reviewers who judged the code not vulnerable

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(aggregate): Finding の CWE に「脆弱ではない」と判定した Reviewer や失敗した判定の CWE まで混ざる
- Bug report: number 460 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/460))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/298-security-checker-460.patch](fixes/298-security-checker-460.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/298-security-checker-460.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-298-security-checker-460.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-298-security-checker-460.html

## The bug

_merge_cwe in src/security_checker/aggregate/findings.py adds the CWE of every verdict. A CWE named by a reviewer who judged not vulnerable or by a failed verdict lands on the finding and shows in SARIF tags and report.md.

## The fix

_merge_cwe now reads the CWE only from a verdict whose status is OK and whose judgement is vulnerable. A new file tests/unit/test_merge_cwe_only_from_vulnerable_verdicts.py covers one vulnerable verdict and one not vulnerable verdict and one failed verdict.

## Files changed

- src/security_checker/aggregate/findings.py
- tests/unit/test_merge_cwe_only_from_vulnerable_verdicts.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 298-security-checker-460.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 460.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. An existing test may expect the old CWE list.

## Search words

security-checker aggregate findings _merge_cwe verdict cwe not vulnerable status OK finding CWE SARIF tags

## The full patch

`````diff
diff --git a/src/security_checker/aggregate/findings.py b/src/security_checker/aggregate/findings.py
index e32a36e..4b390f5 100644
--- a/src/security_checker/aggregate/findings.py
+++ b/src/security_checker/aggregate/findings.py
@@ -78,6 +78,9 @@ def _not_reviewed(candidate: Candidate) -> Finding:
 def _merge_cwe(candidate: Candidate, verdicts: list[ReviewVerdict]) -> list[str]:
     merged = list(candidate.cwe)
     for verdict in verdicts:
+        # 脆弱だと判定できた Reviewer の CWE だけを足す (#460)
+        if verdict.status is not VerdictStatus.OK or not verdict.vulnerable:
+            continue
         for cwe in verdict.cwe:
             if cwe not in merged:
                 merged.append(cwe)
diff --git a/tests/unit/test_merge_cwe_only_from_vulnerable_verdicts.py b/tests/unit/test_merge_cwe_only_from_vulnerable_verdicts.py
new file mode 100644
index 0000000..1b8894b
--- /dev/null
+++ b/tests/unit/test_merge_cwe_only_from_vulnerable_verdicts.py
@@ -0,0 +1,20 @@
+"""_merge_cwe: 脆弱だと判定できた Reviewer の CWE だけを Finding に足すこと (#460)."""
+
+from __future__ import annotations
+
+from security_checker.aggregate.findings import _merge_cwe
+from security_checker.models.verdict import VerdictStatus
+from tests.factories import make_candidate, make_verdict
+
+
+def test_cwe_of_a_not_vulnerable_or_failed_verdict_is_left_out() -> None:
+    candidate = make_candidate()
+    verdicts = [
+        make_verdict("r1", cwe=["CWE-918"]),
+        make_verdict("r2", vulnerable=False, cwe=["CWE-611"]),
+        make_verdict("r3", status=VerdictStatus.PROVIDER_ERROR, vulnerable=False, cwe=["CWE-502"]),
+    ]
+
+    merged = _merge_cwe(candidate, verdicts)
+
+    assert merged == [*candidate.cwe, "CWE-918"]
`````

[Back to the shelf](README.md)

# Fix 305: security-checker: the CWE named by the judge never reaches the finding

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(aggregate): Judge 自身が挙げた CWE が Finding に反映されない
- Bug report: number 463 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/463))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/305-security-checker-463.patch](fixes/305-security-checker-463.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/305-security-checker-463.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-305-security-checker-463.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-305-security-checker-463.html

## The bug

apply_judgement in src/security_checker/aggregate/judge.py takes the judgement and severity and confidence and reasoning of the judge and ignores judge.cwe. A CWE corrected by the judge does not show in SARIF tags.

## The fix

When the judge says vulnerable the finding now lists the CWEs of the judge first and then the earlier CWEs with repeats removed. A new file tests/unit/test_judge_cwe_reaches_the_finding.py covers a vulnerable judgement and a not vulnerable judgement.

## Files changed

- src/security_checker/aggregate/judge.py
- tests/unit/test_judge_cwe_reaches_the_finding.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 305-security-checker-463.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 463.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The tests assume that PolicyConfig() can be built with no arguments and that the test factory accepts cwe and confidence.

## Search words

security-checker aggregate judge apply_judgement judge.cwe finding cwe SARIF tags order first

## The full patch

`````diff
diff --git a/src/security_checker/aggregate/judge.py b/src/security_checker/aggregate/judge.py
index c544c9a..576daa6 100644
--- a/src/security_checker/aggregate/judge.py
+++ b/src/security_checker/aggregate/judge.py
@@ -109,6 +109,10 @@ def apply_judgement(
             "needs_more_context": list(judge.needs_more_context),
         },
     }
+    cwe = list(finding.cwe)
+    if judge.vulnerable:
+        # Judge の CWE を先頭に置き、一次レビューの CWE は重複を除いて続ける (#463)
+        cwe = list(dict.fromkeys([*judge.cwe, *finding.cwe]))
     summary = judge.reasoning.split("\n", 1)[0][:200] if judge.reasoning else finding.summary
     return finding.model_copy(
         update={
@@ -116,6 +120,7 @@ def apply_judgement(
             "severity": severity,
             "confidence": judge.confidence,
             "summary": summary,
+            "cwe": cwe,
             "aggregation": _aggregation(finding, detail),
         }
     )
diff --git a/tests/unit/test_judge_cwe_reaches_the_finding.py b/tests/unit/test_judge_cwe_reaches_the_finding.py
new file mode 100644
index 0000000..ded4379
--- /dev/null
+++ b/tests/unit/test_judge_cwe_reaches_the_finding.py
@@ -0,0 +1,30 @@
+"""apply_judgement: Judge が脆弱と判定したら、Judge の CWE を Finding の先頭に置くこと (#463)."""
+
+from __future__ import annotations
+
+from security_checker.aggregate.judge import apply_judgement
+from security_checker.config.schema import PolicyConfig
+from security_checker.models.enums import FindingStatus
+from tests.factories import make_candidate, make_finding, make_verdict
+
+
+def _finding() -> object:
+    finding = make_finding(make_candidate(), FindingStatus.REVIEW_REQUIRED)
+    return finding.model_copy(update={"cwe": ["CWE-20", "CWE-78"]})
+
+
+def test_cwe_of_a_vulnerable_judgement_comes_first_without_repeats() -> None:
+    judge = make_verdict("judge", cwe=["CWE-78", "CWE-77"], confidence=0.9)
+
+    result = apply_judgement(_finding(), judge, policy=PolicyConfig())  # type: ignore[arg-type]
+
+    assert result.cwe == ["CWE-78", "CWE-77", "CWE-20"]
+
+
+def test_cwe_is_unchanged_when_the_judge_says_not_vulnerable() -> None:
+    """対になるケース."""
+    judge = make_verdict("judge", vulnerable=False, cwe=["CWE-77"], confidence=0.9)
+
+    result = apply_judgement(_finding(), judge, policy=PolicyConfig())  # type: ignore[arg-type]
+
+    assert result.cwe == ["CWE-20", "CWE-78"]
`````

[Back to the shelf](README.md)

# Fix 312: security-checker: a strict run that ends with exit code 3 drops the policy violations that hold at the same time

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(policy): strict で exit 3 になるとき、同時に成立しているポリシー違反の理由が捨てられる
- Bug report: number 459 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/459))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/312-security-checker-459.patch](fixes/312-security-checker-459.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/312-security-checker-459.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-312-security-checker-459.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-312-security-checker-459.html

## The bug

evaluate in src/security_checker/policy/engine.py returns at once when a scanner failed or the review is incomplete under strict. A critical detection that also breaks the policy never reaches the reasons so the last line of the report says only that a scanner failed.

## The fix

evaluate now collects the execution errors first and still checks the policy. The exit code stays 3 and the reasons list the execution errors first and then every policy violation. A new file tests/unit/test_policy_strict_keeps_violation_reasons.py covers a failed scanner together with a critical detection.

## Files changed

- src/security_checker/policy/engine.py
- tests/unit/test_policy_strict_keeps_violation_reasons.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 312-security-checker-459.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 459.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. One more change comes with the patch: a failed scanner and an incomplete review under strict are now both listed where the old code listed only the failed scanner. An existing test that compares the full reasons list may need an update. The new test uses a scanner-only report and not a confirmed finding.

## Search words

security-checker policy engine evaluate strict EXECUTION_ERROR reasons policy violation dropped exit code 3 fail_on

## The full patch

`````diff
diff --git a/src/security_checker/policy/engine.py b/src/security_checker/policy/engine.py
index 50f0e06..55f372d 100644
--- a/src/security_checker/policy/engine.py
+++ b/src/security_checker/policy/engine.py
@@ -29,19 +29,15 @@ class PolicyDecision:
 def evaluate(report: Report, policy: PolicyConfig) -> PolicyDecision:
     """レポートをポリシーに照らして exit code を決める."""
     reasons: list[str] = []
+    errors: list[str] = []
 
     failed_runs = [run for run in report.scanners if run.status is ScanStatus.FAILED]
     if failed_runs and policy.strict:
         names = ", ".join(run.scanner for run in failed_runs)
-        return PolicyDecision(
-            exit_code=ExitCode.EXECUTION_ERROR,
-            reasons=[f"スキャナが失敗しました (strict): {names}"],
-        )
+        errors.append(f"スキャナが失敗しました (strict): {names}")
 
     if policy.strict:
-        incomplete = _incomplete_review(report)
-        if incomplete:
-            return PolicyDecision(exit_code=ExitCode.EXECUTION_ERROR, reasons=incomplete)
+        errors.extend(_incomplete_review(report))
 
     if report.findings:
         # レビュー済み: 「LLM が脆弱と判断したもの」だけをゲートにする
@@ -77,6 +73,9 @@ def evaluate(report: Report, policy: PolicyConfig) -> PolicyDecision:
     if policy.min_score is not None and report.score.value < policy.min_score:
         reasons.append(f"スコア {report.score.value} が下限 {policy.min_score} を下回りました")
 
+    if errors:
+        # exit code は実行エラーのまま. 同時に成立したポリシー違反の理由も捨てない (#459)
+        return PolicyDecision(exit_code=ExitCode.EXECUTION_ERROR, reasons=[*errors, *reasons])
     if reasons:
         return PolicyDecision(exit_code=ExitCode.POLICY_VIOLATION, reasons=reasons)
     return PolicyDecision(exit_code=ExitCode.OK, reasons=[])
diff --git a/tests/unit/test_policy_strict_keeps_violation_reasons.py b/tests/unit/test_policy_strict_keeps_violation_reasons.py
new file mode 100644
index 0000000..c8efceb
--- /dev/null
+++ b/tests/unit/test_policy_strict_keeps_violation_reasons.py
@@ -0,0 +1,31 @@
+"""evaluate: strict で exit 3 になるときも、同時に成立したポリシー違反の理由を残すこと (#459)."""
+
+from __future__ import annotations
+
+from security_checker.config.schema import PolicyConfig
+from security_checker.errors import ExitCode
+from security_checker.models.candidate import Candidate
+from security_checker.models.enums import Category, ScanStatus, Severity
+from security_checker.models.report import ScannerRun
+from security_checker.policy.engine import evaluate
+from tests.factories import make_report
+
+
+def test_scanner_failure_and_a_blocking_detection_are_both_reported() -> None:
+    candidate = Candidate(
+        id="c1",
+        scanner="gitleaks",
+        category=Category.SAST,
+        rule_id="r",
+        title="t",
+        message="m",
+        severity_reported=Severity.CRITICAL,
+    )
+    failed = ScannerRun(scanner="semgrep", category=Category.SAST, status=ScanStatus.FAILED)
+    report = make_report([candidate], scanners=[failed])
+
+    decision = evaluate(report, PolicyConfig(fail_on=Severity.HIGH, strict=True))
+
+    assert decision.exit_code is ExitCode.EXECUTION_ERROR
+    assert decision.reasons[0].startswith("スキャナが失敗しました")
+    assert any("policy.fail_on" in reason for reason in decision.reasons[1:])
`````

[Back to the shelf](README.md)

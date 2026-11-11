# Fix 290: security-checker: no test covers the budget that is left for the judge step

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(run): run.py の _remaining_budget で未テストの分岐をテストする（4 行）
- Bug report: number 575 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/575))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/290-security-checker-575.patch](fixes/290-security-checker-575.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/290-security-checker-575.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-290-security-checker-575.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-290-security-checker-575.html

## The bug

_remaining_budget in src/security_checker/run.py subtracts the dollars and tokens used by the first review and returns None when nothing is left. No test ran those lines.

## The fix

Tests only. A new file tests/unit/test_run_remaining_budget.py expects 0.6 dollars and 600 tokens left after 0.4 dollars and 400 tokens and expects None when the dollars or the tokens are used up and expects an unchanged dollar limit when the cost is unknown.

## Files changed

- tests/unit/test_run_remaining_budget.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 290-security-checker-575.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 575.

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

security-checker run _remaining_budget BudgetConfig max_usd max_total_tokens Usage estimated_usd judge untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_run_remaining_budget.py b/tests/unit/test_run_remaining_budget.py
new file mode 100644
index 0000000..bcf535f
--- /dev/null
+++ b/tests/unit/test_run_remaining_budget.py
@@ -0,0 +1,45 @@
+"""_remaining_budget: 一次レビューで使った分を引き、残りが無ければ None を返すこと."""
+
+from __future__ import annotations
+
+import pytest
+
+from security_checker.config.schema import BudgetConfig
+from security_checker.models.verdict import Usage
+from security_checker.run import _remaining_budget
+
+
+def test_spent_dollars_and_tokens_are_subtracted() -> None:
+    budget = BudgetConfig(max_usd=1.0, max_total_tokens=1000)
+    used = Usage(input_tokens=300, output_tokens=100, estimated_usd=0.4)
+
+    remaining = _remaining_budget(budget, used)
+
+    assert remaining is not None
+    assert remaining.max_usd == pytest.approx(0.6)
+    assert remaining.max_total_tokens == 600
+
+
+@pytest.mark.parametrize("spent", [1.0, 2.5])
+def test_no_dollars_left_means_no_budget(spent: float) -> None:
+    budget = BudgetConfig(max_usd=1.0, max_total_tokens=None)
+
+    assert _remaining_budget(budget, Usage(estimated_usd=spent)) is None
+
+
+@pytest.mark.parametrize("output_tokens", [700, 5000])
+def test_no_tokens_left_means_no_budget(output_tokens: int) -> None:
+    budget = BudgetConfig(max_usd=None, max_total_tokens=1000)
+    used = Usage(input_tokens=300, output_tokens=output_tokens)
+
+    assert _remaining_budget(budget, used) is None
+
+
+def test_unknown_cost_leaves_the_dollar_limit_unchanged() -> None:
+    budget = BudgetConfig(max_usd=1.0, max_total_tokens=None)
+
+    remaining = _remaining_budget(budget, Usage(input_tokens=10, estimated_usd=None))
+
+    assert remaining is not None
+    assert remaining.max_usd == 1.0
+    assert remaining.max_total_tokens is None
`````

[Back to the shelf](README.md)

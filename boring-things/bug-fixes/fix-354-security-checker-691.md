# Fix 354: security-checker: two contract tests join two conditions in one assert so a failure does not say which one broke

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: refactor(testing): 契約テストの複合 assert を分ける (PT018)
- Bug report: number 691 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/691))
- Project license: MIT
- Language: Python
- Test included: no
- Patch file: [fixes/354-security-checker-691.patch](fixes/354-security-checker-691.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/354-security-checker-691.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-354-security-checker-691.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-354-security-checker-691.html

## The bug

test_identity in src/security_checker/testing/provider_contract.py and in src/security_checker/testing/scanner_contract.py use assert a and b. Plugin authors run these contract tests and a failure does not tell them whether the type or the empty value was the problem. The ruff rule PT018 reports both lines.

## The fix

Each joined assert is now two asserts and each one carries a message that states the expected value and shows the actual one.

## Files changed

- src/security_checker/testing/provider_contract.py
- src/security_checker/testing/scanner_contract.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 354-security-checker-691.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 691.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- After the change the chatbot ran ruff with the rule PT018 and saw no report left under src and ran ruff check and ruff format --check with the settings of the project on the two files and both passed. The chatbot did not run the project's tests. No new test was added because the changed lines are tests themselves.

## Search words

security-checker testing provider_contract scanner_contract PT018 composite assert split message plugin contract test

## The full patch

`````diff
diff --git a/src/security_checker/testing/provider_contract.py b/src/security_checker/testing/provider_contract.py
index 6ccbe96..d854972 100644
--- a/src/security_checker/testing/provider_contract.py
+++ b/src/security_checker/testing/provider_contract.py
@@ -91,7 +91,8 @@ class ProviderContractTests:
     def test_identity_fields(self) -> None:
         provider = self.make_provider()
         assert provider.transport in ("http", "process")
-        assert isinstance(provider.dialect, str) and provider.dialect
+        assert isinstance(provider.dialect, str), f"dialect は str を期待: {provider.dialect!r}"
+        assert provider.dialect, "dialect は空でない文字列を期待"
 
     @pytest.mark.asyncio
     async def test_complete_returns_response(self) -> None:
diff --git a/src/security_checker/testing/scanner_contract.py b/src/security_checker/testing/scanner_contract.py
index 1225faf..c69c0a7 100644
--- a/src/security_checker/testing/scanner_contract.py
+++ b/src/security_checker/testing/scanner_contract.py
@@ -52,7 +52,8 @@ class ScannerContractTests:
 
     def test_identity(self) -> None:
         scanner = self.make_scanner()
-        assert isinstance(scanner.name, str) and scanner.name
+        assert isinstance(scanner.name, str), f"name は str を期待: {scanner.name!r}"
+        assert scanner.name, "name は空でない文字列を期待"
         assert isinstance(scanner.category, Category)
 
     def test_probe_does_not_raise(self) -> None:
`````

[Back to the shelf](README.md)

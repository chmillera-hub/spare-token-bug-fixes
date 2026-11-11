# Fix 280: security-checker: no test covers the hint shown when Gemini rejects the response schema

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(providers): gemini_generate.py の explain_error で未テストの分岐をテストする（1 行）
- Bug report: number 540 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/540))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/280-security-checker-540.patch](fixes/280-security-checker-540.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/280-security-checker-540.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-280-security-checker-540.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-280-security-checker-540.html

## The bug

explain_error in src/security_checker/providers/http/dialects/gemini_generate.py returns a hint to use json_mode when a 400 answer mentions response_schema or responseSchema. No test ran that return line.

## The fix

Tests only. A new file tests/unit/test_gemini_generate_explain_schema_error.py expects a hint that names json_mode for both spellings and expects no hint for status 500.

## Files changed

- tests/unit/test_gemini_generate_explain_schema_error.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 280-security-checker-540.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 540.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The bug report lists one untested return line from a coverage run on an older commit. An existing test already covers the API key hint and the model hint so the chatbot guessed that the schema hint is the line meant. The chatbot did not run the tests or a coverage tool.

## Search words

security-checker gemini_generate explain_error response_schema responseSchema 400 json_mode hint untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_gemini_generate_explain_schema_error.py b/tests/unit/test_gemini_generate_explain_schema_error.py
new file mode 100644
index 0000000..2873475
--- /dev/null
+++ b/tests/unit/test_gemini_generate_explain_schema_error.py
@@ -0,0 +1,26 @@
+"""gemini_generate の explain_error: スキーマ拒否の 400 に回避策を添えること."""
+
+from __future__ import annotations
+
+import pytest
+
+from security_checker.providers.http.dialects.gemini_generate import GeminiGenerateDialect
+
+
+@pytest.mark.parametrize(
+    "body",
+    [
+        "Invalid JSON payload received. Unknown name \"response_schema\"",
+        "generation_config.responseSchema: unsupported keyword",
+    ],
+)
+def test_schema_rejection_suggests_json_mode(body: str) -> None:
+    message = GeminiGenerateDialect().explain_error(400, body)
+
+    assert message is not None
+    assert "json_mode" in message
+
+
+def test_schema_words_with_another_status_get_no_explanation() -> None:
+    """対になるケース. 400 以外では説明を付けない."""
+    assert GeminiGenerateDialect().explain_error(500, "response_schema") is None
`````

[Back to the shelf](README.md)

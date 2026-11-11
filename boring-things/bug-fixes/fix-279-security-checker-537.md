# Fix 279: security-checker: no test covers sending a seed or joining the system text into the user turn for Gemini

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(providers): gemini_generate.py の build_payload で未テストの分岐をテストする（2 行）
- Bug report: number 537 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/537))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/279-security-checker-537.patch](fixes/279-security-checker-537.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/279-security-checker-537.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-279-security-checker-537.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-279-security-checker-537.html

## The bug

build_payload in src/security_checker/providers/http/dialects/gemini_generate.py sends a seed when the endpoint supports one and joins the system text into the user turn when the endpoint has no system role. No test ran those two lines.

## The fix

Tests only. A new file tests/unit/test_gemini_generate_seed_and_no_system_role.py expects seed 7 in generationConfig with supports_seed and no seed without and expects one user turn holding both texts when supports_system_role is false.

## Files changed

- tests/unit/test_gemini_generate_seed_and_no_system_role.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 279-security-checker-537.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 537.

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

security-checker gemini_generate build_payload seed supports_seed supports_system_role systemInstruction contents untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_gemini_generate_seed_and_no_system_role.py b/tests/unit/test_gemini_generate_seed_and_no_system_role.py
new file mode 100644
index 0000000..b5782e1
--- /dev/null
+++ b/tests/unit/test_gemini_generate_seed_and_no_system_role.py
@@ -0,0 +1,41 @@
+"""gemini_generate の build_payload: seed の送信と、system ロールが使えないときの連結."""
+
+from __future__ import annotations
+
+from security_checker.providers.base import Capabilities, CompletionRequest, StructuredMode
+from security_checker.providers.http.dialects.gemini_generate import GeminiGenerateDialect
+
+
+def _payload(capabilities: Capabilities, request: CompletionRequest) -> dict[str, object]:
+    return GeminiGenerateDialect().build_payload(
+        request, model="m", capabilities=capabilities, mode=StructuredMode.PROMPT_ONLY
+    )
+
+
+def test_seed_is_sent_when_the_endpoint_supports_it() -> None:
+    request = CompletionRequest(system="sys", user="usr", seed=7)
+
+    payload = _payload(Capabilities(supports_seed=True), request)
+
+    generation = payload["generationConfig"]
+    assert isinstance(generation, dict)
+    assert generation["seed"] == 7
+
+
+def test_seed_is_not_sent_when_the_endpoint_does_not_support_it() -> None:
+    request = CompletionRequest(system="sys", user="usr", seed=7)
+
+    payload = _payload(Capabilities(supports_seed=False), request)
+
+    generation = payload["generationConfig"]
+    assert isinstance(generation, dict)
+    assert "seed" not in generation
+
+
+def test_system_text_is_joined_into_the_user_turn_without_a_system_role() -> None:
+    request = CompletionRequest(system="sys", user="usr")
+
+    payload = _payload(Capabilities(supports_system_role=False), request)
+
+    assert "systemInstruction" not in payload
+    assert payload["contents"] == [{"role": "user", "parts": [{"text": "sys\n\nusr"}]}]
`````

[Back to the shelf](README.md)

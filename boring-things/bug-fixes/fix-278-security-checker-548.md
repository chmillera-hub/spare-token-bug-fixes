# Fix 278: security-checker: no test covers a 200 answer whose JSON is a list or a bare value

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(providers): transport.py の _post で未テストの分岐をテストする（1 行）
- Bug report: number 548 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/548))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/278-security-checker-548.patch](fixes/278-security-checker-548.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/278-security-checker-548.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-278-security-checker-548.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-278-security-checker-548.html

## The bug

HttpProvider._post in src/security_checker/providers/http/transport.py raises ProviderResponseError when the answer is valid JSON and the top level is not an object. No test ran that line.

## The fix

Tests only. A new file tests/unit/test_http_transport_non_object_json_body.py answers a request with a list and a string and a number and expects ProviderResponseError each time.

## Files changed

- tests/unit/test_http_transport_non_object_json_body.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 278-security-checker-548.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 548.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The bug report lists the untested line from a coverage run on an older commit. In the newest code two lines raise ProviderResponseError in _post (invalid JSON and JSON that is not an object). The chatbot guessed that the second one is the line meant because an existing test already expects ProviderResponseError. The chatbot did not run the tests or a coverage tool.

## Search words

security-checker transport HttpProvider _post response json list top level object ProviderResponseError untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_http_transport_non_object_json_body.py b/tests/unit/test_http_transport_non_object_json_body.py
new file mode 100644
index 0000000..076066f
--- /dev/null
+++ b/tests/unit/test_http_transport_non_object_json_body.py
@@ -0,0 +1,36 @@
+"""HttpProvider: 応答の JSON がオブジェクトでなければ ProviderResponseError になること."""
+
+from __future__ import annotations
+
+import httpx
+import pytest
+import respx
+
+from security_checker.providers.base import Capabilities, CompletionRequest
+from security_checker.providers.errors import ProviderResponseError
+from security_checker.providers.http.dialects.openai_chat import OpenAIChatDialect
+from security_checker.providers.http.transport import HttpProvider
+
+BASE_URL = "http://endpoint.test/v1"
+URL = f"{BASE_URL}/chat/completions"
+
+
+@respx.mock
+@pytest.mark.parametrize("body", [["a", "b"], "text", 3])
+async def test_top_level_json_that_is_not_an_object_is_a_response_error(body: object) -> None:
+    respx.post(URL).mock(return_value=httpx.Response(200, json=body))
+    client = httpx.AsyncClient()
+    provider = HttpProvider(
+        name="r1",
+        dialect=OpenAIChatDialect(),
+        base_url=BASE_URL,
+        model="m",
+        capabilities=Capabilities(),
+        api_key="secret-key",
+        client=client,
+    )
+
+    with pytest.raises(ProviderResponseError, match="オブジェクトではありません"):
+        await provider.complete(CompletionRequest(system="s", user="u", timeout_s=5.0))
+
+    await client.aclose()
`````

[Back to the shelf](README.md)

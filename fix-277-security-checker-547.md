# Fix 277: security-checker: no test covers closing the HTTP client that the provider created

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(providers): transport.py の aclose で未テストの分岐をテストする（1 行）
- Bug report: number 547 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/547))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/277-security-checker-547.patch](fixes/277-security-checker-547.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/277-security-checker-547.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-277-security-checker-547.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-277-security-checker-547.html

## The bug

HttpProvider.aclose in src/security_checker/providers/http/transport.py closes the HTTP client only when the provider created the client. No test ran the closing line.

## The fix

Tests only. A new file tests/unit/test_http_transport_aclose_owned_client.py builds a provider with no client and expects the created client to be closed after aclose. A second test passes a client in and expects that client to stay open.

## Files changed

- tests/unit/test_http_transport_aclose_owned_client.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 277-security-checker-547.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 547.

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

security-checker transport HttpProvider aclose owns_client httpx AsyncClient is_closed untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_http_transport_aclose_owned_client.py b/tests/unit/test_http_transport_aclose_owned_client.py
new file mode 100644
index 0000000..de6fc56
--- /dev/null
+++ b/tests/unit/test_http_transport_aclose_owned_client.py
@@ -0,0 +1,42 @@
+"""HttpProvider.aclose: 自分で作ったクライアントだけを閉じること."""
+
+from __future__ import annotations
+
+import httpx
+
+from security_checker.providers.base import Capabilities
+from security_checker.providers.http.dialects.openai_chat import OpenAIChatDialect
+from security_checker.providers.http.transport import HttpProvider
+
+
+def _provider(client: httpx.AsyncClient | None) -> HttpProvider:
+    return HttpProvider(
+        name="r1",
+        dialect=OpenAIChatDialect(),
+        base_url="http://endpoint.test/v1",
+        model="m",
+        capabilities=Capabilities(),
+        api_key=None,
+        client=client,
+    )
+
+
+async def test_aclose_closes_the_client_the_provider_created() -> None:
+    provider = _provider(None)
+    owned = provider._client
+    assert not owned.is_closed
+
+    await provider.aclose()
+
+    assert owned.is_closed
+
+
+async def test_aclose_leaves_a_client_passed_in_by_the_caller_open() -> None:
+    """対になるケース. 呼び出し側が渡したクライアントは呼び出し側が閉じる."""
+    client = httpx.AsyncClient()
+    provider = _provider(client)
+
+    await provider.aclose()
+
+    assert not client.is_closed
+    await client.aclose()
`````

[Back to the shelf](README.md)

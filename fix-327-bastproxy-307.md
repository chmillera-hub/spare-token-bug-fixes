# Fix 327: bastproxy: the Clients table shows the text Term Type in place of the terminal type of the client

Status: UNSENT and UNTESTED. Free to take.

- Project: endavis/bastproxy
- Bug report title: bug: the Clients table shows the literal text "Term Type" instead of the client's terminal type
- Bug report: number 307 ([open the bug report](https://github.com/endavis/bastproxy/issues/307))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/327-bastproxy-307.patch](fixes/327-bastproxy-307.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/327-bastproxy-307.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-327-bastproxy-307.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-327-bastproxy-307.html

## The bug

_api_client_list_formatted in src/bastproxy/plugins/core/clients/plugin/_clients.py fills the Term Type column with the fixed text Term Type for every client.

## The fix

The column now shows client.writer.get_extra_info("TERM") and shows - when the client reported no terminal type (the behaviour the bug report asks for). The stub client of the existing test file gains a writer and a new file tests/plugins/core/clients/test_clients_term_type.py covers a client that reported xterm and a client that reported nothing.

## Files changed

- src/bastproxy/plugins/core/clients/plugin/_clients.py
- tests/plugins/core/clients/test_clients_formatted.py
- tests/plugins/core/clients/test_clients_term_type.py

## How to use the fix

1. Get a copy of the project endavis/bastproxy.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 327-bastproxy-307.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 307.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's code or tests. The new tests import the stub helper from the existing test file test_clients_formatted.py.

## Search words

bastproxy clients show Term Type column terminal type TTYPE telnetlib3 get_extra_info TERM

## The full patch

`````diff
diff --git a/src/bastproxy/plugins/core/clients/plugin/_clients.py b/src/bastproxy/plugins/core/clients/plugin/_clients.py
index b300601..3d4662e 100644
--- a/src/bastproxy/plugins/core/clients/plugin/_clients.py
+++ b/src/bastproxy/plugins/core/clients/plugin/_clients.py
@@ -297,7 +297,7 @@ class ClientPlugin(BasePlugin):
                 "state": "Active",
                 "address": client.addr,
                 "port": client.port,
-                "term_type": "Term Type",
+                "term_type": client.writer.get_extra_info("TERM") or "-",
                 "connected": client.connected_length,
                 "view_only": str(client.view_only),
             }
diff --git a/tests/plugins/core/clients/test_clients_formatted.py b/tests/plugins/core/clients/test_clients_formatted.py
index 0769296..9338fbb 100644
--- a/tests/plugins/core/clients/test_clients_formatted.py
+++ b/tests/plugins/core/clients/test_clients_formatted.py
@@ -16,7 +16,13 @@ def _stub(banned: dict[str, Any] | None = None, permbanips: list[str] | None = N
     stub = MagicMock()
     stub.plugin_id = PID
     stub.clients = {
-        "uuid1": SimpleNamespace(addr="10.0.0.5", port=4242, connected_length="1m", view_only=False)
+        "uuid1": SimpleNamespace(
+            addr="10.0.0.5",
+            port=4242,
+            connected_length="1m",
+            view_only=False,
+            writer=SimpleNamespace(get_extra_info=lambda _name: None),
+        )
     }
     stub.banned = banned or {}
 
diff --git a/tests/plugins/core/clients/test_clients_term_type.py b/tests/plugins/core/clients/test_clients_term_type.py
new file mode 100644
index 0000000..4ed3ef5
--- /dev/null
+++ b/tests/plugins/core/clients/test_clients_term_type.py
@@ -0,0 +1,38 @@
+"""Tests for the Term Type column of the Clients table (#307)."""
+
+from types import SimpleNamespace
+
+from bastproxy.plugins.core.clients.plugin._clients import ClientPlugin
+from tests.plugins.core.clients.test_clients_formatted import _stub
+
+
+def _client(term: str | None) -> SimpleNamespace:
+    return SimpleNamespace(
+        addr="::1",
+        port=49276,
+        connected_length="18s",
+        view_only=False,
+        writer=SimpleNamespace(get_extra_info=lambda name: term if name == "TERM" else None),
+    )
+
+
+def _client_row(term: str | None) -> str:
+    stub = _stub()
+    stub.clients = {"uuid1": _client(term)}
+    rows = [line for line in ClientPlugin._api_client_list_formatted(stub) if "49276" in line]
+    assert len(rows) == 1
+    return rows[0]
+
+
+def test_reported_terminal_type_is_shown() -> None:
+    row = _client_row("xterm")
+
+    assert "xterm" in row
+    assert "Term Type" not in row
+
+
+def test_missing_terminal_type_is_a_dash() -> None:
+    row = _client_row(None)
+
+    assert "Term Type" not in row
+    assert "-" in row
`````

[Back to the shelf](README.md)

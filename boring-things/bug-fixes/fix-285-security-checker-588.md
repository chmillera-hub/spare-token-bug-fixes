# Fix 285: security-checker: no test covers loading scanner plugins or a scanner plugin that fails to load

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(scanners): registry.py の discover_plugin_scanners で未テストの分岐をテストする（6 行）
- Bug report: number 588 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/588))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/285-security-checker-588.patch](fixes/285-security-checker-588.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/285-security-checker-588.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-285-security-checker-588.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-285-security-checker-588.html

## The bug

discover_plugin_scanners in src/security_checker/scanners/registry.py loads every scanner plugin and turns a failed load into a warning. No test ran those lines.

## The fix

Tests only. A new file tests/unit/test_scanner_registry_plugin_discovery.py replaces entry_points with two made-up entries. One raises RuntimeError and one loads. The test expects the loaded factory in the result and one warning that names the broken plugin and the error text.

## Files changed

- tests/unit/test_scanner_registry_plugin_discovery.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 285-security-checker-588.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 588.

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

security-checker scanners registry discover_plugin_scanners entry_points plugin load failure warning untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_scanner_registry_plugin_discovery.py b/tests/unit/test_scanner_registry_plugin_discovery.py
new file mode 100644
index 0000000..f5b3e04
--- /dev/null
+++ b/tests/unit/test_scanner_registry_plugin_discovery.py
@@ -0,0 +1,44 @@
+"""discover_plugin_scanners: 読み込めたプラグインを返し、失敗は警告にすること."""
+
+from __future__ import annotations
+
+from typing import Any
+
+import pytest
+
+from security_checker.scanners import registry
+
+
+class _Entry:
+    def __init__(self, name: str, value: Any = None, error: Exception | None = None) -> None:
+        self.name = name
+        self._value = value
+        self._error = error
+
+    def load(self) -> Any:
+        if self._error is not None:
+            raise self._error
+        return self._value
+
+
+def test_loaded_plugins_are_returned_and_a_broken_one_becomes_a_warning(
+    monkeypatch: pytest.MonkeyPatch,
+) -> None:
+    def factory(config: Any) -> Any:
+        return config
+
+    groups: list[str] = []
+
+    def fake_entry_points(*, group: str) -> list[_Entry]:
+        groups.append(group)
+        return [_Entry("broken", error=RuntimeError("boom")), _Entry("custom", value=factory)]
+
+    monkeypatch.setattr(registry, "entry_points", fake_entry_points)
+
+    found, warnings = registry.discover_plugin_scanners()
+
+    assert groups == [registry.ENTRY_POINT_GROUP]
+    assert found == {"custom": factory}
+    assert len(warnings) == 1
+    assert "broken" in warnings[0]
+    assert "boom" in warnings[0]
`````

[Back to the shelf](README.md)

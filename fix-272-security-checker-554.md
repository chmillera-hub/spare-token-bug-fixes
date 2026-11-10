# Fix 272: security-checker: no test covers a provider plugin that fails to load

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(providers): registry.py の discover_plugin_providers で未テストの分岐をテストする（4 行）
- Bug report: number 554 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/554))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/272-security-checker-554.patch](fixes/272-security-checker-554.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/272-security-checker-554.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-272-security-checker-554.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-272-security-checker-554.html

## The bug

discover_plugin_providers in src/security_checker/providers/registry.py loads every provider plugin and turns a failed load into a warning. No test ran the loading lines or the warning line.

## The fix

Tests only. A new file tests/unit/test_registry_plugin_discovery_failure.py replaces entry_points with two made-up entries. One loads and one raises ImportError. The test expects the good factory in the result and one warning that names the broken plugin and the error text.

## Files changed

- tests/unit/test_registry_plugin_discovery_failure.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 272-security-checker-554.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 554.

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

security-checker registry discover_plugin_providers entry_points plugin load failure warning untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_registry_plugin_discovery_failure.py b/tests/unit/test_registry_plugin_discovery_failure.py
new file mode 100644
index 0000000..418aa4b
--- /dev/null
+++ b/tests/unit/test_registry_plugin_discovery_failure.py
@@ -0,0 +1,44 @@
+"""discover_plugin_providers: 読み込みに失敗したプラグインは警告にして残りを返すこと."""
+
+from __future__ import annotations
+
+from typing import Any
+
+import pytest
+
+from security_checker.providers import registry
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
+def test_broken_plugin_becomes_a_warning_and_the_rest_is_kept(
+    monkeypatch: pytest.MonkeyPatch,
+) -> None:
+    def factory(reviewer: Any) -> Any:
+        return reviewer
+
+    groups: list[str] = []
+
+    def fake_entry_points(*, group: str) -> list[_Entry]:
+        groups.append(group)
+        return [_Entry("good", value=factory), _Entry("broken", error=ImportError("no module x"))]
+
+    monkeypatch.setattr(registry, "entry_points", fake_entry_points)
+
+    found, warnings = registry.discover_plugin_providers()
+
+    assert groups == [registry.ENTRY_POINT_GROUP]
+    assert found == {"good": factory}
+    assert len(warnings) == 1
+    assert "broken" in warnings[0]
+    assert "no module x" in warnings[0]
`````

[Back to the shelf](README.md)

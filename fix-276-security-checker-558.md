# Fix 276: security-checker: no test covers a reviewer whose transport belongs to a plugin

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(providers): registry.py の build_provider で未テストの分岐をテストする（2 行）
- Bug report: number 558 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/558))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/276-security-checker-558.patch](fixes/276-security-checker-558.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/276-security-checker-558.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-276-security-checker-558.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-276-security-checker-558.html

## The bug

build_provider in src/security_checker/providers/registry.py hands a reviewer with a plugin transport to the plugin factory and returns the result. No test ran those two lines.

## The fix

Tests only. A new file tests/unit/test_registry_build_provider_plugin_transport.py swaps the transport name with model_copy and expects the plugin factory to receive the reviewer and expects its result back. A second test expects a ConfigError that lists the registered plugin names when no plugin matches.

## Files changed

- tests/unit/test_registry_build_provider_plugin_transport.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 276-security-checker-558.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 558.

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

security-checker registry build_provider plugins transport factory entry point ConfigError untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_registry_build_provider_plugin_transport.py b/tests/unit/test_registry_build_provider_plugin_transport.py
new file mode 100644
index 0000000..33d3005
--- /dev/null
+++ b/tests/unit/test_registry_build_provider_plugin_transport.py
@@ -0,0 +1,44 @@
+"""build_provider: http / process 以外の transport はプラグインの factory に渡すこと."""
+
+from __future__ import annotations
+
+from typing import Any
+
+import pytest
+
+from security_checker.config.schema import ReviewerConfig
+from security_checker.errors import ConfigError
+from security_checker.providers.registry import build_provider
+
+
+def _plugin_reviewer() -> ReviewerConfig:
+    base = ReviewerConfig(name="r1", transport="process", command=["tool"])
+    # transport は Literal なので、検証を通さない model_copy でプラグインの名前に差し替える
+    return base.model_copy(update={"transport": "custom"})
+
+
+def test_plugin_factory_receives_the_reviewer_and_its_result_is_returned() -> None:
+    reviewer = _plugin_reviewer()
+    received: list[Any] = []
+    sentinel = object()
+
+    def factory(config: Any) -> Any:
+        received.append(config)
+        return sentinel
+
+    provider = build_provider(reviewer, plugins={"custom": factory})
+
+    assert provider is sentinel
+    assert received == [reviewer]
+
+
+def test_unknown_transport_lists_the_registered_plugins() -> None:
+    """対になるケース. 該当するプラグインが無ければ、登録済みの名前を添えて ConfigError."""
+
+    def factory(config: Any) -> Any:
+        return config
+
+    with pytest.raises(ConfigError, match="custom") as excinfo:
+        build_provider(_plugin_reviewer(), plugins={"other": factory})
+
+    assert "other" in str(excinfo.value)
`````

[Back to the shelf](README.md)

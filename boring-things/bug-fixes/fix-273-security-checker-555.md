# Fix 273: security-checker: no test covers broken preset capabilities or a raised output token limit

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(providers): registry.py の resolve_capabilities で未テストの分岐をテストする（3 行）
- Bug report: number 555 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/555))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/273-security-checker-555.patch](fixes/273-security-checker-555.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/273-security-checker-555.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-273-security-checker-555.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-273-security-checker-555.html

## The bug

resolve_capabilities in src/security_checker/providers/registry.py turns invalid preset capabilities into a ConfigError and raises the output token limit when the reviewer asks for more. No test ran those lines.

## The fix

Tests only. A new file tests/unit/test_registry_capabilities_preset_error_and_output_limit.py expects a ConfigError that names the preset for a non-numeric max_context_tokens and expects 9000 output tokens when the reviewer asks for 9000 and 4096 when the reviewer asks for 100.

## Files changed

- tests/unit/test_registry_capabilities_preset_error_and_output_limit.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 273-security-checker-555.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 555.

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

security-checker registry resolve_capabilities preset capabilities ValidationError ConfigError max_output_tokens untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_registry_capabilities_preset_error_and_output_limit.py b/tests/unit/test_registry_capabilities_preset_error_and_output_limit.py
new file mode 100644
index 0000000..1eeb3e1
--- /dev/null
+++ b/tests/unit/test_registry_capabilities_preset_error_and_output_limit.py
@@ -0,0 +1,48 @@
+"""resolve_capabilities: プリセットの不正な capabilities と max_output_tokens の引き上げ."""
+
+from __future__ import annotations
+
+from typing import Any
+
+import pytest
+
+from security_checker.config.schema import ReviewerConfig
+from security_checker.errors import ConfigError
+from security_checker.providers.presets.loader import HttpPreset
+from security_checker.providers.registry import resolve_capabilities
+
+
+def _reviewer(**overrides: Any) -> ReviewerConfig:
+    payload: dict[str, Any] = {
+        "name": "r1",
+        "transport": "http",
+        "dialect": "openai_chat",
+        "base_url": "https://endpoint.test/v1",
+        "model": "m",
+    }
+    payload.update(overrides)
+    return ReviewerConfig(**payload)
+
+
+def test_invalid_preset_capabilities_are_a_config_error_naming_the_preset() -> None:
+    preset = HttpPreset(
+        name="broken-preset",
+        dialect="openai_chat",
+        capabilities={"max_context_tokens": "not-a-number"},
+    )
+
+    with pytest.raises(ConfigError, match="broken-preset"):
+        resolve_capabilities(_reviewer(), preset)
+
+
+def test_reviewer_max_output_tokens_above_the_capability_raises_the_limit() -> None:
+    capabilities = resolve_capabilities(_reviewer(max_output_tokens=9000), None)
+
+    assert capabilities.max_output_tokens == 9000
+
+
+def test_reviewer_max_output_tokens_below_the_capability_keeps_the_limit() -> None:
+    """対になるケース. 既定の上限 4096 より小さい値では上限を変えない."""
+    capabilities = resolve_capabilities(_reviewer(max_output_tokens=100), None)
+
+    assert capabilities.max_output_tokens == 4096
`````

[Back to the shelf](README.md)

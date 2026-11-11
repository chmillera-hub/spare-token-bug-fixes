# Fix 274: security-checker: no test covers an http reviewer whose base_url cannot be resolved

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(providers): registry.py の build_http_provider で未テストの分岐をテストする（1 行）
- Bug report: number 556 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/556))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/274-security-checker-556.patch](fixes/274-security-checker-556.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/274-security-checker-556.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-274-security-checker-556.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-274-security-checker-556.html

## The bug

build_http_provider in src/security_checker/providers/registry.py raises a ConfigError when dialect or base_url or model stays unresolved after the preset lookup. No test ran that line.

## The fix

Tests only. A new file tests/unit/test_registry_http_provider_unresolved_base_url.py builds a reviewer that names a preset with no base_url and expects a ConfigError that names the reviewer.

## Files changed

- tests/unit/test_registry_http_provider_unresolved_base_url.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 274-security-checker-556.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 556.

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

security-checker registry build_http_provider preset base_url dialect model unresolved ConfigError untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_registry_http_provider_unresolved_base_url.py b/tests/unit/test_registry_http_provider_unresolved_base_url.py
new file mode 100644
index 0000000..452740d
--- /dev/null
+++ b/tests/unit/test_registry_http_provider_unresolved_base_url.py
@@ -0,0 +1,20 @@
+"""build_http_provider: preset からも base_url が決まらないときは ConfigError になること."""
+
+from __future__ import annotations
+
+import pytest
+
+from security_checker.config.schema import ReviewerConfig
+from security_checker.errors import ConfigError
+from security_checker.providers.presets.loader import HttpPreset
+from security_checker.providers.registry import build_http_provider
+
+
+def test_preset_without_base_url_and_reviewer_without_base_url_is_a_config_error() -> None:
+    reviewer = ReviewerConfig(name="r1", transport="http", preset="no-url", model="m")
+    presets = {"no-url": HttpPreset(name="no-url", dialect="openai_chat")}
+
+    with pytest.raises(ConfigError, match="dialect / base_url / model") as excinfo:
+        build_http_provider(reviewer, environ={}, presets=presets)
+
+    assert "r1" in str(excinfo.value)
`````

[Back to the shelf](README.md)

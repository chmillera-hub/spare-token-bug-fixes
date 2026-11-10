# Fix 275: security-checker: no test covers a process reviewer whose command cannot be resolved

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(providers): registry.py の build_process_provider で未テストの分岐をテストする（1 行）
- Bug report: number 557 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/557))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/275-security-checker-557.patch](fixes/275-security-checker-557.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/275-security-checker-557.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-275-security-checker-557.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-275-security-checker-557.html

## The bug

build_process_provider in src/security_checker/providers/registry.py raises a ConfigError when neither the reviewer nor the preset gives a command. No test ran that line.

## The fix

Tests only. A new file tests/unit/test_registry_process_provider_empty_command.py builds a reviewer that names a preset with an empty command list and expects a ConfigError that names the reviewer and expects no warning to be added first.

## Files changed

- tests/unit/test_registry_process_provider_empty_command.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 275-security-checker-557.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 557.

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

security-checker registry build_process_provider preset command empty ConfigError untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_registry_process_provider_empty_command.py b/tests/unit/test_registry_process_provider_empty_command.py
new file mode 100644
index 0000000..886fb63
--- /dev/null
+++ b/tests/unit/test_registry_process_provider_empty_command.py
@@ -0,0 +1,22 @@
+"""build_process_provider: preset の command が空なら ConfigError になること."""
+
+from __future__ import annotations
+
+import pytest
+
+from security_checker.config.schema import ReviewerConfig
+from security_checker.errors import ConfigError
+from security_checker.providers.presets.loader import ProcessPreset
+from security_checker.providers.registry import build_process_provider
+
+
+def test_preset_with_an_empty_command_is_a_config_error() -> None:
+    reviewer = ReviewerConfig(name="r1", transport="process", preset="empty")
+    presets = {"empty": ProcessPreset(name="empty", command=[])}
+    warnings: list[str] = []
+
+    with pytest.raises(ConfigError, match="command を解決できません") as excinfo:
+        build_process_provider(reviewer, environ={}, presets=presets, warnings=warnings)
+
+    assert "r1" in str(excinfo.value)
+    assert warnings == []
`````

[Back to the shelf](README.md)

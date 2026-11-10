# Fix 301: security-checker: baseline update shows a traceback when the suppression rules cannot be loaded

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(cli): baseline update が load_rules の SecurityCheckerError を捕まえず、トレースバックで終わる
- Bug report: number 192 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/192))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/301-security-checker-192.patch](fixes/301-security-checker-192.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/301-security-checker-192.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-301-security-checker-192.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-301-security-checker-192.html

## The bug

baseline_update in src/security_checker/cli.py calls load_rules outside the try block. A syntax error in the ignore file ends with a traceback and an exit code outside the promised 2 and 3.

## The fix

The load_rules call now sits inside the existing try block so a SecurityCheckerError goes through _fail. A new file tests/unit/test_baseline_update_broken_ignore_rules.py makes load_rules raise ConfigError and expects the exit code of ConfigError and a clean SystemExit.

## Files changed

- src/security_checker/cli.py
- tests/unit/test_baseline_update_broken_ignore_rules.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 301-security-checker-192.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 192.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The test replaces load_rules with a made-up function and does not use a real broken ignore file.

## Search words

security-checker cli baseline update load_rules SecurityCheckerError traceback exit code ignore file

## The full patch

`````diff
diff --git a/src/security_checker/cli.py b/src/security_checker/cli.py
index 6f0a497..01605f6 100644
--- a/src/security_checker/cli.py
+++ b/src/security_checker/cli.py
@@ -705,10 +705,10 @@ def baseline_update(
     config = loaded.config.model_copy(
         update={"policy": loaded.config.policy.model_copy(update={"baseline": None})}
     )
-    rules = load_rules(
-        config, root, config_dir=config_dir, untrusted_target=loaded.untrusted_target
-    )
     try:
+        rules = load_rules(
+            config, root, config_dir=config_dir, untrusted_target=loaded.untrusted_target
+        )
         outcome = asyncio.run(run_scan(config, root, suppression=rules, diff=None))
     except SecurityCheckerError as exc:
         _fail(str(exc), exc.exit_code)
diff --git a/tests/unit/test_baseline_update_broken_ignore_rules.py b/tests/unit/test_baseline_update_broken_ignore_rules.py
new file mode 100644
index 0000000..7fc24ad
--- /dev/null
+++ b/tests/unit/test_baseline_update_broken_ignore_rules.py
@@ -0,0 +1,28 @@
+"""baseline update: 抑制ルールの読み込みエラーを整形して終了すること (#192)."""
+
+from __future__ import annotations
+
+from pathlib import Path
+from typing import Any
+
+import pytest
+from typer.testing import CliRunner
+
+from security_checker import cli
+from security_checker.errors import ConfigError
+
+runner = CliRunner()
+
+
+def test_error_from_load_rules_becomes_a_formatted_exit(
+    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
+) -> None:
+    def broken(*args: Any, **kwargs: Any) -> Any:
+        raise ConfigError("ignore ファイルの 3 行目を読めません")
+
+    monkeypatch.setattr(cli, "load_rules", broken)
+
+    result = runner.invoke(cli.app, ["baseline", "update", str(tmp_path)])
+
+    assert result.exit_code == int(ConfigError("x").exit_code)
+    assert isinstance(result.exception, SystemExit)
`````

[Back to the shelf](README.md)

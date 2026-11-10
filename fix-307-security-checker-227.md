# Fix 307: security-checker: config show and providers check accept a folder that does not exist

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(cli): `config show` と `providers check --path` が存在しないディレクトリを指定しても既定の設定で続行する
- Bug report: number 227 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/227))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/307-security-checker-227.patch](fixes/307-security-checker-227.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/307-security-checker-227.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-307-security-checker-227.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-307-security-checker-227.html

## The bug

config_show and providers_check in src/security_checker/cli.py do not check that the folder exists. config show prints the default settings with exit code 0 and providers check reports that no reviewers are set. A typo in the path looks like an empty configuration.

## The fix

Both commands now end with exit code 2 and a not found message when the folder does not exist (the same check that scan and review and init already make). A new file tests/unit/test_cli_missing_directory_config_show_providers_check.py covers both commands.

## Files changed

- src/security_checker/cli.py
- tests/unit/test_cli_missing_directory_config_show_providers_check.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 307-security-checker-227.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 227.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The last lines of the bug report text were cut off in the copy the chatbot read. The chatbot wrote the check that the visible part of the text describes.

## Search words

security-checker cli config show providers check --path missing directory exit code 2 not found default config

## The full patch

`````diff
diff --git a/src/security_checker/cli.py b/src/security_checker/cli.py
index 6f0a497..9dac425 100644
--- a/src/security_checker/cli.py
+++ b/src/security_checker/cli.py
@@ -649,6 +649,8 @@ def config_show(
 ) -> None:
     """解決された最終設定を出力する (秘匿値は保持しない設計のため常に安全)."""
     root = path.expanduser().resolve()
+    if not root.is_dir():
+        _fail(f"検査対象が見つかりません: {path}", ExitCode.CONFIG_ERROR)
     loaded = _load(root, config_path, preset, {})
     console = Console()
 
@@ -847,6 +849,8 @@ def providers_check(
     リポジトリのコードは送らない。
     """
     root = path.expanduser().resolve()
+    if not root.is_dir():
+        _fail(f"ディレクトリが見つかりません: {path}", ExitCode.CONFIG_ERROR)
     loaded = _load(root, config_path, None, {})
     reviewers = [r for r in loaded.config.reviewers if name is None or r.name == name]
     if not reviewers:
diff --git a/tests/unit/test_cli_missing_directory_config_show_providers_check.py b/tests/unit/test_cli_missing_directory_config_show_providers_check.py
new file mode 100644
index 0000000..94450c1
--- /dev/null
+++ b/tests/unit/test_cli_missing_directory_config_show_providers_check.py
@@ -0,0 +1,26 @@
+"""config show / providers check: 存在しないディレクトリは exit 2 にすること (#227)."""
+
+from __future__ import annotations
+
+from pathlib import Path
+
+from typer.testing import CliRunner
+
+from security_checker.cli import app
+from security_checker.errors import ExitCode
+
+runner = CliRunner()
+
+
+def test_config_show_rejects_a_missing_directory(tmp_path: Path) -> None:
+    result = runner.invoke(app, ["config", "show", str(tmp_path / "missing")])
+
+    assert result.exit_code == ExitCode.CONFIG_ERROR
+    assert "見つかりません" in result.stderr
+
+
+def test_providers_check_rejects_a_missing_directory(tmp_path: Path) -> None:
+    result = runner.invoke(app, ["providers", "check", "--path", str(tmp_path / "missing")])
+
+    assert result.exit_code == ExitCode.CONFIG_ERROR
+    assert "見つかりません" in result.stderr
`````

[Back to the shelf](README.md)

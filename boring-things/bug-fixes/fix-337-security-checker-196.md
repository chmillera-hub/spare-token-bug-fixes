# Fix 337: security-checker: the command line has no --version flag

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: feat(cli): --version フラグを追加する
- Bug report: number 196 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/196))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/337-security-checker-196.patch](fixes/337-security-checker-196.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/337-security-checker-196.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-337-security-checker-196.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-337-security-checker-196.html

## The bug

src/security_checker/cli.py offers the version only through the version subcommand. security-checker --version ends with a usage error.

## The fix

A typer callback now adds an eager --version option that prints the same line as the version subcommand and exits with code 0. The subcommand stays. A new file tests/unit/test_cli_version_flag.py covers the flag and the subcommand.

## Files changed

- src/security_checker/cli.py
- tests/unit/test_cli_version_flag.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 337-security-checker-196.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 196.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes.

## Search words

security-checker cli --version flag typer callback is_eager version subcommand

## The full patch

`````diff
diff --git a/src/security_checker/cli.py b/src/security_checker/cli.py
index 6f0a497..82da04f 100644
--- a/src/security_checker/cli.py
+++ b/src/security_checker/cli.py
@@ -66,6 +66,27 @@ app = typer.Typer(
     no_args_is_help=True,
     add_completion=False,
 )
+
+
+def _version_callback(value: bool) -> None:
+    if value:
+        print(f"security-checker {__version__}")
+        raise typer.Exit
+
+
+@app.callback()
+def _root(
+    show_version: Annotated[
+        bool,
+        typer.Option(
+            "--version",
+            callback=_version_callback,
+            is_eager=True,
+            help="バージョンを表示する",
+        ),
+    ] = False,
+) -> None:
+    """拡張可能な AI Security Review プラットフォーム."""
 config_app = typer.Typer(help="設定の確認", no_args_is_help=True)
 app.add_typer(config_app, name="config")
 
diff --git a/tests/unit/test_cli_version_flag.py b/tests/unit/test_cli_version_flag.py
new file mode 100644
index 0000000..7731d5a
--- /dev/null
+++ b/tests/unit/test_cli_version_flag.py
@@ -0,0 +1,25 @@
+"""--version: サブコマンド無しでバージョンを表示すること (#196)."""
+
+from __future__ import annotations
+
+from typer.testing import CliRunner
+
+from security_checker import __version__
+from security_checker.cli import app
+
+runner = CliRunner()
+
+
+def test_version_flag_prints_the_version_and_exits_0() -> None:
+    result = runner.invoke(app, ["--version"])
+
+    assert result.exit_code == 0
+    assert result.stdout == f"security-checker {__version__}\n"
+
+
+def test_version_subcommand_still_works() -> None:
+    """対になるケース. 既存の version サブコマンドは残す."""
+    result = runner.invoke(app, ["version"])
+
+    assert result.exit_code == 0
+    assert result.stdout == f"security-checker {__version__}\n"
`````

[Back to the shelf](README.md)

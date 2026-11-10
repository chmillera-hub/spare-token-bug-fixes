# Fix 304: security-checker: error messages lose text in square brackets or crash with MarkupError

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(cli): エラーメッセージを rich のマークアップとして解釈し、`[` を含むパスで表示が欠けるか MarkupError で落ちる
- Bug report: number 206 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/206))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/304-security-checker-206.patch](fixes/304-security-checker-206.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/304-security-checker-206.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-304-security-checker-206.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-304-security-checker-206.html

## The bug

_fail in src/security_checker/cli.py puts the message into a rich markup string. A path such as nope[bold]y is shown without [bold] and a path such as nope[/x] ends with a rich MarkupError traceback and exit code 1.

## The fix

_fail and the last-resort handler in main now pass the message through rich.markup.escape. A new file tests/unit/test_cli_error_message_square_brackets.py runs scan on two missing paths with square brackets and expects exit code 2 and the path as typed in the error output.

## Files changed

- src/security_checker/cli.py
- tests/unit/test_cli_error_message_square_brackets.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 304-security-checker-206.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 206.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The bug report also names five warning lines that keep markup switched on. This patch does not change those five lines.

## Search words

security-checker cli _fail rich markup escape MarkupError square brackets path error message exit code

## The full patch

`````diff
diff --git a/src/security_checker/cli.py b/src/security_checker/cli.py
index 6f0a497..bcdfe28 100644
--- a/src/security_checker/cli.py
+++ b/src/security_checker/cli.py
@@ -17,6 +17,7 @@ from typing import Annotated, Any, NoReturn
 import typer
 import yaml
 from rich.console import Console
+from rich.markup import escape
 from rich.panel import Panel
 
 from security_checker import __version__
@@ -73,7 +74,7 @@ err_console = Console(stderr=True)
 
 
 def _fail(message: str, code: ExitCode) -> NoReturn:
-    err_console.print(f"[bold red]エラー:[/bold red] {redact_known_patterns(message)}")
+    err_console.print(f"[bold red]エラー:[/bold red] {escape(redact_known_patterns(message))}")
     raise typer.Exit(code=int(code))
 
 
@@ -982,7 +983,8 @@ def main() -> None:
     try:
         app()
     except SecurityCheckerError as exc:  # pragma: no cover - 最後の砦
-        err_console.print(f"[bold red]エラー:[/bold red] {redact_known_patterns(str(exc))}")
+        message = escape(redact_known_patterns(str(exc)))
+        err_console.print(f"[bold red]エラー:[/bold red] {message}")
         sys.exit(int(exc.exit_code))
 
 
diff --git a/tests/unit/test_cli_error_message_square_brackets.py b/tests/unit/test_cli_error_message_square_brackets.py
new file mode 100644
index 0000000..e8fed2f
--- /dev/null
+++ b/tests/unit/test_cli_error_message_square_brackets.py
@@ -0,0 +1,25 @@
+"""_fail: メッセージ中の角括弧を rich のマークアップとして解釈しないこと (#206)."""
+
+from __future__ import annotations
+
+from pathlib import Path
+
+import pytest
+from typer.testing import CliRunner
+
+from security_checker.cli import app
+from security_checker.errors import ExitCode
+
+runner = CliRunner()
+
+
+@pytest.mark.parametrize("name", ["nope[bold]y", "nope[/x]"])
+def test_path_with_square_brackets_is_shown_as_typed(
+    name: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
+) -> None:
+    monkeypatch.chdir(tmp_path)
+
+    result = runner.invoke(app, ["scan", name])
+
+    assert result.exit_code == ExitCode.CONFIG_ERROR
+    assert name in result.stderr
`````

[Back to the shelf](README.md)

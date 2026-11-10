# Fix 294: vericode: the command line has no --version flag

Status: UNSENT and UNTESTED. Free to take.

- Project: LucasXlab/vericode
- Bug report title: Add `vericode --version` flag
- Bug report: number 1 ([open the bug report](https://github.com/LucasXlab/vericode/issues/1))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/294-vericode-1.patch](fixes/294-vericode-1.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/294-vericode-1.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-294-vericode-1.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-294-vericode-1.html

## The bug

vericode --version ends with a click error because the command defines no version option.

## The fix

vericode/cli.py now imports __version__ from the package and adds click.version_option(__version__) to the command. A new file tests/test_cli_version.py runs the command with --version and expects exit code 0 and the version number in the output.

## Files changed

- tests/test_cli_version.py
- vericode/cli.py

## How to use the fix

1. Get a copy of the project LucasXlab/vericode.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 294-vericode-1.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 1.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The bug report is labelled as a good first issue and asks for a small feature. The chatbot did not run the project's code or tests.

## Search words

vericode cli --version click version_option __version__ flag

## The full patch

`````diff
diff --git a/tests/test_cli_version.py b/tests/test_cli_version.py
new file mode 100644
index 0000000..b192dbd
--- /dev/null
+++ b/tests/test_cli_version.py
@@ -0,0 +1,12 @@
+"""The CLI answers --version with the package version."""
+
+from click.testing import CliRunner
+
+from vericode import __version__
+from vericode.cli import main
+
+
+def test_version_flag_prints_the_package_version():
+    out = CliRunner().invoke(main, ["--version"])
+    assert out.exit_code == 0
+    assert __version__ in out.output
diff --git a/vericode/cli.py b/vericode/cli.py
index ee03ccf..a85d2bc 100644
--- a/vericode/cli.py
+++ b/vericode/cli.py
@@ -9,10 +9,12 @@ from pathlib import Path
 import click
 from rich.console import Console
 
+from . import __version__
 from .core import run
 
 
 @click.command()
+@click.version_option(__version__)
 @click.argument("target", default=".", type=click.Path(exists=True, path_type=Path))
 @click.option("--json", "json_output", is_flag=True, help="Output JSON instead of a pretty report.")
 @click.option(
`````

[Back to the shelf](README.md)

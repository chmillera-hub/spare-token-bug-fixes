# Fix 321: security-checker: an unexpected exception ends with exit code 1 which also means a policy violation

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(cli): 想定外の例外が exit 1 になり、「ツールが壊れた」がポリシー違反と区別できない
- Bug report: number 207 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/207))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/321-security-checker-207.patch](fixes/321-security-checker-207.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/321-security-checker-207.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-321-security-checker-207.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-321-security-checker-207.html

## The bug

main in src/security_checker/cli.py catches only SecurityCheckerError. Any other exception ends the program with a traceback and exit code 1 so a broken tool looks the same as a policy violation to a CI job.

## The fix

main now catches every other Exception and prints the traceback to standard error and ends with the execution error code (3). KeyboardInterrupt is not caught. A new file tests/unit/test_main_unexpected_exception_exit_code.py makes the app raise RuntimeError and expects exit code 3 and the error text on standard error.

## Files changed

- src/security_checker/cli.py
- tests/unit/test_main_unexpected_exception_exit_code.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 321-security-checker-207.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 207.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The bug report also asks to save the traceback into the trace folder when the folder is usable. This patch does not do that part. This patch and the patch of fix 304 on this shelf change neighbouring lines of main and do not apply together.

## Search words

security-checker cli main unexpected exception exit code 1 3 EXECUTION_ERROR traceback policy violation

## The full patch

`````diff
diff --git a/src/security_checker/cli.py b/src/security_checker/cli.py
index 6f0a497..6b938fc 100644
--- a/src/security_checker/cli.py
+++ b/src/security_checker/cli.py
@@ -11,6 +11,7 @@ import json
 import os
 import shlex
 import sys
+import traceback
 from pathlib import Path
 from typing import Annotated, Any, NoReturn
 
@@ -984,6 +985,10 @@ def main() -> None:
     except SecurityCheckerError as exc:  # pragma: no cover - 最後の砦
         err_console.print(f"[bold red]エラー:[/bold red] {redact_known_patterns(str(exc))}")
         sys.exit(int(exc.exit_code))
+    except Exception:
+        # 想定外の例外は「ツールが壊れた」(exit 3). ポリシー違反 (exit 1) と区別する (#207)
+        traceback.print_exc()
+        sys.exit(int(ExitCode.EXECUTION_ERROR))
 
 
 if __name__ == "__main__":  # pragma: no cover
diff --git a/tests/unit/test_main_unexpected_exception_exit_code.py b/tests/unit/test_main_unexpected_exception_exit_code.py
new file mode 100644
index 0000000..640c084
--- /dev/null
+++ b/tests/unit/test_main_unexpected_exception_exit_code.py
@@ -0,0 +1,23 @@
+"""main: 想定外の例外は exit 3 で終わり、スタックトレースを標準エラーに出すこと (#207)."""
+
+from __future__ import annotations
+
+import pytest
+
+from security_checker import cli
+from security_checker.errors import ExitCode
+
+
+def test_unexpected_exception_ends_with_the_execution_error_code(
+    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
+) -> None:
+    def broken() -> None:
+        raise RuntimeError("scanner exploded")
+
+    monkeypatch.setattr(cli, "app", broken)
+
+    with pytest.raises(SystemExit) as excinfo:
+        cli.main()
+
+    assert excinfo.value.code == int(ExitCode.EXECUTION_ERROR)
+    assert "scanner exploded" in capsys.readouterr().err
`````

[Back to the shelf](README.md)

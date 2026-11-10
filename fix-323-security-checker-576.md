# Fix 323: security-checker: no test covers a scanner command that runs past its timeout

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(scanners): base.py の run_command で未テストの分岐をテストする（4 行）
- Bug report: number 576 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/576))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/323-security-checker-576.patch](fixes/323-security-checker-576.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/323-security-checker-576.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-323-security-checker-576.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-323-security-checker-576.html

## The bug

run_command in src/security_checker/scanners/base.py kills the child process and returns a timed_out result when the command runs past timeout_s. No test ran those four lines.

## The fix

Tests only. A new file tests/unit/test_run_command_timeout.py starts a Python child that sleeps 60 seconds with a timeout of 1 second and expects timed_out to be true and no exit code and empty output.

## Files changed

- tests/unit/test_run_command_timeout.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 323-security-checker-576.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 576.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The test starts a real Python child process and takes about one second. The bug report asks for fakes in place of external commands and the chatbot treated the Python interpreter that runs the tests as acceptable. The chatbot did not run the tests or a coverage tool.

## Search words

security-checker scanners base run_command timeout TimeoutError kill wait timed_out CommandResult untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_run_command_timeout.py b/tests/unit/test_run_command_timeout.py
new file mode 100644
index 0000000..c5805a0
--- /dev/null
+++ b/tests/unit/test_run_command_timeout.py
@@ -0,0 +1,19 @@
+"""run_command: タイムアウトしたら子プロセスを止め、timed_out の結果を返すこと."""
+
+from __future__ import annotations
+
+import sys
+from pathlib import Path
+
+from security_checker.scanners.base import run_command
+
+
+async def test_command_that_outlives_the_timeout_is_reported_as_timed_out(tmp_path: Path) -> None:
+    argv = [sys.executable, "-c", "import time; time.sleep(60)"]
+
+    result = await run_command(argv, cwd=tmp_path, timeout_s=1)
+
+    assert result.timed_out is True
+    assert result.exit_code is None
+    assert result.stdout == b""
+    assert result.stderr == b""
`````

[Back to the shelf](README.md)

# Fix 308: security-checker: a cancelled scan leaves the scanner process running

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(scanners): run_command がキャンセル (Ctrl-C) 時に子プロセスを止めない
- Bug report: number 332 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/332))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/308-security-checker-332.patch](fixes/308-security-checker-332.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/308-security-checker-332.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-308-security-checker-332.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-308-security-checker-332.html

## The bug

run_command in src/security_checker/scanners/base.py kills the child process only on a timeout. When the task is cancelled (Ctrl-C included) the function leaves while the scanner process keeps running.

## The fix

run_command now also catches every other exception around the wait and kills the child and waits for the child to end and then raises the exception again. A new file tests/unit/test_run_command_cancel_kills_child.py starts a sleeping Python child and cancels the task and expects the child to be gone. The test is skipped on Windows.

## Files changed

- src/security_checker/scanners/base.py
- tests/unit/test_run_command_cancel_kills_child.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 308-security-checker-332.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 332.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot ran a separate scratch copy of the changed logic: a cancelled task raised CancelledError and the child process was gone. The chatbot did not run the project's code or tests.

## Search words

security-checker scanners base run_command CancelledError Ctrl-C child process kill wait orphan scanner

## The full patch

`````diff
diff --git a/src/security_checker/scanners/base.py b/src/security_checker/scanners/base.py
index bb8f154..72027bd 100644
--- a/src/security_checker/scanners/base.py
+++ b/src/security_checker/scanners/base.py
@@ -128,6 +128,12 @@ async def run_command(
             process.kill()
             await process.wait()
             return CommandResult(exit_code=None, stdout=b"", stderr=b"", timed_out=True)
+        except BaseException:
+            # キャンセル (Ctrl-C を含む) でも子プロセスを残さない (#332)
+            if process.returncode is None:
+                process.kill()
+                await process.wait()
+            raise
         return CommandResult(
             exit_code=process.returncode,
             stdout=stdout or b"",
diff --git a/tests/unit/test_run_command_cancel_kills_child.py b/tests/unit/test_run_command_cancel_kills_child.py
new file mode 100644
index 0000000..e413bdc
--- /dev/null
+++ b/tests/unit/test_run_command_cancel_kills_child.py
@@ -0,0 +1,34 @@
+"""run_command: キャンセルされたら子プロセスを止めてから抜けること (#332)."""
+
+from __future__ import annotations
+
+import asyncio
+import os
+import sys
+from pathlib import Path
+
+import pytest
+
+from security_checker.scanners.base import run_command
+
+CHILD = "import os,sys,time; open(sys.argv[1],'w').write(str(os.getpid())); time.sleep(60)"
+
+
+@pytest.mark.skipif(os.name == "nt", reason="os.kill(pid, 0) で生存を確かめられない")
+async def test_cancelling_the_task_leaves_no_child_process(tmp_path: Path) -> None:
+    pid_file = tmp_path / "pid"
+    task = asyncio.create_task(
+        run_command([sys.executable, "-c", CHILD, str(pid_file)], cwd=tmp_path, timeout_s=30)
+    )
+    for _ in range(100):
+        if pid_file.exists() and pid_file.read_text():
+            break
+        await asyncio.sleep(0.1)
+    pid = int(pid_file.read_text())
+
+    task.cancel()
+    with pytest.raises(asyncio.CancelledError):
+        await task
+
+    with pytest.raises(ProcessLookupError):
+        os.kill(pid, 0)
`````

[Back to the shelf](README.md)

# Fix 302: security-checker: trace files are written with permissions that let other users of the machine read them

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(trace): save_prompts のトレースが他のユーザーも読める権限 (0644 / 0755) で書かれる
- Bug report: number 317 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/317))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/302-security-checker-317.patch](fixes/302-security-checker-317.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/302-security-checker-317.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-302-security-checker-317.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-302-security-checker-317.html

## The bug

TraceWriter in src/security_checker/observability/trace.py uses mkdir and write_text with the default umask. With umask 022 the folders get 0755 and the files get 0644 so other users on a shared machine can read the model answers and (with save_prompts) the checked code.

## The fix

TraceWriter now creates the trace folder and the run folder and the calls folder with mode 0700 and writes run.json and every call file with mode 0600. On Windows nothing changes. A new file tests/unit/test_trace_file_permissions.py checks the modes and is skipped on Windows.

## Files changed

- src/security_checker/observability/trace.py
- tests/unit/test_trace_file_permissions.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 302-security-checker-317.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 317.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot ran a separate scratch copy of the two new helper functions and saw modes 0700 and 0600. The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. Any other code that writes into the trace folder keeps its own permissions. The chatbot did not search for such code.

## Search words

security-checker observability trace TraceWriter permissions umask 0644 0755 0600 0700 save_prompts chmod

## The full patch

`````diff
diff --git a/src/security_checker/observability/trace.py b/src/security_checker/observability/trace.py
index 66459d2..e705cb5 100644
--- a/src/security_checker/observability/trace.py
+++ b/src/security_checker/observability/trace.py
@@ -8,6 +8,7 @@ from __future__ import annotations
 
 import hashlib
 import json
+import os
 from pathlib import Path
 from typing import Any
 
@@ -26,25 +27,48 @@ class TraceWriter:
         self.enabled = enabled
         self._index = 0
 
+    def _private_root(self) -> None:
+        _private_dir(self.root.parent)
+        _private_dir(self.root)
+
     def write_run(self, payload: dict[str, Any]) -> Path | None:
         if not self.enabled:
             return None
-        self.root.mkdir(parents=True, exist_ok=True)
+        self._private_root()
         path = self.root / "run.json"
-        path.write_text(_dump(payload), encoding="utf-8")
+        _write_private(path, _dump(payload))
         return path
 
     def write_call(self, payload: dict[str, Any]) -> Path | None:
         if not self.enabled:
             return None
         calls = self.root / "calls"
-        calls.mkdir(parents=True, exist_ok=True)
+        self._private_root()
+        _private_dir(calls)
         path = calls / f"{self._index:04d}.json"
         self._index += 1
-        path.write_text(_dump(payload), encoding="utf-8")
+        _write_private(path, _dump(payload))
         return path
 
 
+def _private_dir(path: Path) -> None:
+    """ディレクトリを作り、所有者だけが読めるようにする (#317). Windows では権限を変えない."""
+    path.mkdir(parents=True, exist_ok=True)
+    if os.name != "nt":
+        path.chmod(0o700)
+
+
+def _write_private(path: Path, text: str) -> None:
+    """所有者だけが読めるファイルとして書く (#317). Windows では通常どおり書く."""
+    if os.name == "nt":
+        path.write_text(text, encoding="utf-8")
+        return
+    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
+    with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
+        handle.write(text)
+    path.chmod(0o600)
+
+
 def _dump(payload: dict[str, Any]) -> str:
     """マスキングフィルタを必ず通す (§19.1)."""
     text = json.dumps(payload, ensure_ascii=False, indent=2, default=str)
diff --git a/tests/unit/test_trace_file_permissions.py b/tests/unit/test_trace_file_permissions.py
new file mode 100644
index 0000000..cbab230
--- /dev/null
+++ b/tests/unit/test_trace_file_permissions.py
@@ -0,0 +1,30 @@
+"""TraceWriter: trace/ 以下を所有者だけが読める権限で書くこと (#317)."""
+
+from __future__ import annotations
+
+import os
+import stat
+from pathlib import Path
+
+import pytest
+
+from security_checker.observability.trace import TraceWriter
+
+
+def _mode(path: Path) -> int:
+    return stat.S_IMODE(path.stat().st_mode)
+
+
+@pytest.mark.skipif(os.name == "nt", reason="Windows では権限を変えない")
+def test_trace_directories_are_0700_and_files_are_0600(tmp_path: Path) -> None:
+    writer = TraceWriter(tmp_path, "RUN1")
+
+    run_path = writer.write_run({"a": 1})
+    call_path = writer.write_call({"b": 2})
+
+    assert run_path is not None
+    assert call_path is not None
+    for directory in (tmp_path / "trace", tmp_path / "trace" / "RUN1", call_path.parent):
+        assert _mode(directory) == 0o700
+    for file in (run_path, call_path):
+        assert _mode(file) == 0o600
`````

[Back to the shelf](README.md)

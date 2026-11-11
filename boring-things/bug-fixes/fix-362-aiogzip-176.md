# Fix 362: aiogzip: writelines() drops earlier lines of a batch when a later line fails to encode

Status: UNSENT and UNTESTED. Free to take.

- Project: geoff-davis/aiogzip
- Bug report title: writelines() drops earlier lines in a batch when a later line fails to encode
- Bug report: number 176 ([open the bug report](https://github.com/geoff-davis/aiogzip/issues/176))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/362-aiogzip-176.patch](fixes/362-aiogzip-176.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/362-aiogzip-176.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-362-aiogzip-176.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-362-aiogzip-176.html

## The bug

writelines in src/aiogzip/_text.py joins lines into batches and encodes each batch once. When one line cannot be encoded the whole batch is rejected so valid lines before the bad line are not written and the error positions refer to the joined batch.

## The fix

A new helper writes a batch and on UnicodeEncodeError falls back to writing the lines of that batch one by one (the fix the bug report suggests). Every line before the bad line is written and the error describes the bad line. The five batch writes in writelines use the helper. The fast path is unchanged. A new file tests/test_writelines_encode_error.py uses the example from the bug report and expects a and b in the file.

## Files changed

- src/aiogzip/_text.py
- tests/test_writelines_encode_error.py

## How to use the fix

1. Get a copy of the project geoff-davis/aiogzip.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 362-aiogzip-176.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 176.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's code or tests. The fix assumes that a batch write raises UnicodeEncodeError before writing any part of the batch (the bug report says the whole batch is rejected). The bug report also says docs/api.md does not describe the behaviour. This patch does not change the docs.

## Search words

aiogzip writelines UnicodeEncodeError batch drops earlier lines surrogate encode chunk_size TextIOWrapper

## The full patch

`````diff
diff --git a/src/aiogzip/_text.py b/src/aiogzip/_text.py
index 0d0d811..1042965 100644
--- a/src/aiogzip/_text.py
+++ b/src/aiogzip/_text.py
@@ -2193,19 +2193,19 @@ class AsyncGzipTextFile:
                     break
                 except BaseException:
                     if pending or pending_empty:
-                        await self._write_batch_reserved("".join(pending))
+                        await self._write_pending_reserved(pending)
                     raise
 
                 if not isinstance(line, str):
                     if pending or pending_empty:
-                        await self._write_batch_reserved("".join(pending))
+                        await self._write_pending_reserved(pending)
                     await self._write_batch_reserved(line)
                     continue
 
                 length = len(line)
                 if length >= self._chunk_size:
                     if pending or pending_empty:
-                        await self._write_batch_reserved("".join(pending))
+                        await self._write_pending_reserved(pending)
                         pending = []
                         pending_chars = 0
                         pending_empty = False
@@ -2216,7 +2216,7 @@ class AsyncGzipTextFile:
                     pending_empty = True
                 else:
                     if pending and pending_chars + length > self._chunk_size:
-                        await self._write_batch_reserved("".join(pending))
+                        await self._write_pending_reserved(pending)
                         pending = []
                         pending_chars = 0
                         pending_empty = False
@@ -2224,7 +2224,21 @@ class AsyncGzipTextFile:
                     pending_chars += length
 
             if pending or pending_empty:
-                await self._write_batch_reserved("".join(pending))
+                await self._write_pending_reserved(pending)
+
+    async def _write_pending_reserved(self, pending: List[str]) -> None:
+        """Write a batch of lines, falling back to line by line on an encode error.
+
+        The fallback writes every line before the offending one and raises the
+        error for that line alone, as io.TextIOWrapper does. It runs only on the
+        error path, so the batched fast path is unchanged.
+        """
+        try:
+            await self._write_batch_reserved("".join(pending))
+        except UnicodeEncodeError:
+            for line in pending:
+                await self._write_batch_reserved(line)
+            raise
 
     async def flush(self) -> None:
         """
diff --git a/tests/test_writelines_encode_error.py b/tests/test_writelines_encode_error.py
new file mode 100644
index 0000000..a08e409
--- /dev/null
+++ b/tests/test_writelines_encode_error.py
@@ -0,0 +1,29 @@
+"""writelines() keeps the lines written before one that cannot be encoded."""
+
+import gzip
+
+import pytest
+
+import aiogzip
+
+
+async def test_lines_before_an_unencodable_line_are_written(tmp_path):
+    path = str(tmp_path / "lines.gz")
+
+    async with aiogzip.open(path, "wt") as stream:
+        with pytest.raises(UnicodeEncodeError) as caught:
+            await stream.writelines(["a\n", "b\n", "\ud800", "c\n"])
+
+    with gzip.open(path) as written:
+        assert written.read() == b"a\nb\n"
+    assert caught.value.object == "\ud800"
+
+
+async def test_a_batch_without_a_bad_line_is_written_whole(tmp_path):
+    path = str(tmp_path / "lines.gz")
+
+    async with aiogzip.open(path, "wt") as stream:
+        await stream.writelines(["a\n", "b\n", "c\n"])
+
+    with gzip.open(path) as written:
+        assert written.read() == b"a\nb\nc\n"
`````

[Back to the shelf](README.md)

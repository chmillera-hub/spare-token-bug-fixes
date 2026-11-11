# Fix 322: security-checker: scanner error output goes into report.json with keys and proxy passwords in clear text

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(report): ScannerRun.stderr_excerpt を伏せずに report.json に書いている
- Bug report: number 701 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/701))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/322-security-checker-701.patch](fixes/322-security-checker-701.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/322-security-checker-701.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-322-security-checker-701.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-322-security-checker-701.html

## The bug

excerpt in src/security_checker/scanners/base.py copies the first 2000 characters of the scanner stderr into stderr_excerpt as they are. The text can hold a token from a file that failed to parse or a proxy URL with a password and lands in report.json and the CI artifact.

## The fix

excerpt now passes the text through redact_known_patterns and masks the password part of scheme://user:password@host before cutting the text. The user name and the host stay. A new file tests/unit/test_scanner_stderr_excerpt_is_redacted.py covers a GitHub token and a proxy URL and a text with no secret.

## Files changed

- src/security_checker/scanners/base.py
- tests/unit/test_scanner_stderr_excerpt_is_redacted.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 322-security-checker-701.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 701.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot ran a separate scratch copy of the URL pattern against six made-up lines and the pattern masked only the two passwords. The chatbot did not run the project's tests. The test assumes that redact_known_patterns hides at least part of a token that starts with ghp_.

## Search words

security-checker scanners base excerpt stderr_excerpt redact_known_patterns proxy url password report.json token leak

## The full patch

`````diff
diff --git a/src/security_checker/scanners/base.py b/src/security_checker/scanners/base.py
index bb8f154..6f39125 100644
--- a/src/security_checker/scanners/base.py
+++ b/src/security_checker/scanners/base.py
@@ -8,6 +8,7 @@
 from __future__ import annotations
 
 import asyncio
+import re
 import shutil
 import subprocess
 import time
@@ -18,6 +19,7 @@ from typing import Any, ClassVar, Protocol
 from pydantic import BaseModel, ConfigDict
 
 from security_checker.config.schema import ScannerConfig
+from security_checker.context.redact import redact_known_patterns
 from security_checker.models.candidate import Candidate
 from security_checker.models.enums import Category, ScanStatus
 from security_checker.scanners.untrusted import UntrustedOverrides
@@ -157,13 +159,18 @@ def probe_command(command: str, version_args: tuple[str, ...] = ("--version",))
     return ToolStatus(available=True, version=version)
 
 
+#: URL に埋め込まれた資格情報 (scheme://user:password@host) の password の部分 (#701)
+_URL_PASSWORD_RE = re.compile(r"(?P<head>[A-Za-z][A-Za-z0-9+.\-]*://[^\s/:@]+:)[^\s/@]+(?=@)")
+
+
 def excerpt(data: bytes, limit: int = STDERR_EXCERPT_LIMIT) -> str | None:
-    """stderr の先頭を安全に抜き出す."""
+    """stderr の先頭を安全に抜き出す. 既知形式のキーと URL のパスワードは伏せる (#701)."""
     if not data:
         return None
     text = data.decode("utf-8", "replace").strip()
     if not text:
         return None
+    text = _URL_PASSWORD_RE.sub(r"\g<head>****", redact_known_patterns(text))
     return text if len(text) <= limit else text[:limit] + " …(truncated)"
 
 
diff --git a/tests/unit/test_scanner_stderr_excerpt_is_redacted.py b/tests/unit/test_scanner_stderr_excerpt_is_redacted.py
new file mode 100644
index 0000000..fc8c583
--- /dev/null
+++ b/tests/unit/test_scanner_stderr_excerpt_is_redacted.py
@@ -0,0 +1,24 @@
+"""excerpt: スキャナの stderr に含まれる既知形式のキーと URL のパスワードを伏せること (#701)."""
+
+from __future__ import annotations
+
+from security_checker.scanners.base import excerpt
+
+
+def test_known_key_and_url_password_are_masked() -> None:
+    key = "ghp_" + "a1B2" * 9
+    stderr = f"parse error near {key}\nproxy https://user:p4ssw0rd@proxy.example:8080 refused"
+
+    text = excerpt(stderr.encode())
+
+    assert text is not None
+    assert key not in text
+    assert "p4ssw0rd" not in text
+    assert "https://user:****@proxy.example:8080 refused" in text
+
+
+def test_text_without_secrets_is_unchanged() -> None:
+    """対になるケース. ポート番号や SSH 形式の URL は伏せない."""
+    stderr = b"  failed: https://example.com:8080/a@b and git@github.com:o/r.git\n"
+
+    assert excerpt(stderr) == "failed: https://example.com:8080/a@b and git@github.com:o/r.git"
`````

[Back to the shelf](README.md)

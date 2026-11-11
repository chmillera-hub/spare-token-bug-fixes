# Fix 355: security-checker: an import inside a function of the process runner has no stated reason

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: refactor: 関数の中で import している箇所を整理する (PLC0415)
- Bug report: number 689 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/689))
- Project license: MIT
- Language: Python
- Test included: no
- Patch file: [fixes/355-security-checker-689.patch](fixes/355-security-checker-689.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/355-security-checker-689.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-355-security-checker-689.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-355-security-checker-689.html

## The bug

health_check in src/security_checker/providers/process/runner.py imports command_version inside the function and gives no reason. The ruff rule PLC0415 reports the line. The other reported place (tiktoken in context/budget.py) is an optional dependency and needs the late import.

## The fix

The import of command_version now sits at the top of runner.py with the other imports. The chatbot found no import cycle: providers/detect.py imports only the preset loader and the preset loader imports only the errors module. The tiktoken import keeps its place and its comment now states the reason for the late import in full. The chatbot did not add a noqa marker there because PLC0415 is not switched on in the settings of the project and ruff reports a marker for a rule that is off as unused.

## Files changed

- src/security_checker/context/budget.py
- src/security_checker/providers/process/runner.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 355-security-checker-689.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 689.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- After the change the chatbot ran ruff with the rule PLC0415 and saw one report left under src (the tiktoken import that carries its reason) and ran ruff check and ruff format --check with the settings of the project on the two files and both passed. The chatbot did not run the project's tests. No test replaces command_version on the detect module as far as a text search of the tests folder shows. No new test was added because behaviour is unchanged.

## Search words

security-checker providers process runner health_check import inside function PLC0415 command_version tiktoken lazy import noqa

## The full patch

`````diff
diff --git a/src/security_checker/context/budget.py b/src/security_checker/context/budget.py
index 9065511..f0d5b1b 100644
--- a/src/security_checker/context/budget.py
+++ b/src/security_checker/context/budget.py
@@ -17,7 +17,7 @@ PROMPT_OVERHEAD_TOKENS = 1500
 @lru_cache(maxsize=1)
 def _encode_fn() -> Callable[[str], list[int]] | None:
     """tiktoken があればその encode を返す. なければ None (概算にフォールバック)."""
-    try:  # tiktoken は任意依存 (extras)
+    try:  # tiktoken は任意依存 (extras) なので、使うときに遅延 import する
         import tiktoken  # type: ignore[import-not-found]
     except ImportError:
         return None
diff --git a/src/security_checker/providers/process/runner.py b/src/security_checker/providers/process/runner.py
index 49e2670..da32e6f 100644
--- a/src/security_checker/providers/process/runner.py
+++ b/src/security_checker/providers/process/runner.py
@@ -28,6 +28,7 @@ from security_checker.providers.base import (
     HealthStatus,
     StructuredMode,
 )
+from security_checker.providers.detect import command_version
 from security_checker.providers.errors import (
     ProviderError,
     ProviderResponseError,
@@ -109,8 +110,6 @@ class ProcessProvider:
 
     async def health_check(self) -> HealthStatus:
         """到達性の確認. 起動対象を実際には走らせず、存在とバージョンだけを見る."""
-        from security_checker.providers.detect import command_version
-
         if not self.command:
             return HealthStatus(ok=False, detail="command が空です")
         found = command_version(self.command[0])
`````

[Back to the shelf](README.md)

# Fix 356: security-checker: the internal function _diff_scope takes a true or false value as a positional argument

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: refactor(cli): 真偽値の位置引数を受け取る関数をキーワード専用にする (FBT001/FBT002)
- Bug report: number 693 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/693))
- Project license: MIT
- Language: Python
- Test included: no
- Patch file: [fixes/356-security-checker-693.patch](fixes/356-security-checker-693.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/356-security-checker-693.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-356-security-checker-693.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-356-security-checker-693.html

## The bug

_diff_scope in src/security_checker/cli.py takes full as its fourth positional argument. A call such as _diff_scope(loaded root None True) does not show what True means. The ruff rules FBT001 and FBT002 report the argument.

## The fix

full is now a keyword-only argument and both callers pass full=full. In the newest code _diff_scope is the only internal function that ruff reports for these two rules. The other 14 reports are typer command functions which the bug report leaves out.

## Files changed

- src/security_checker/cli.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 356-security-checker-693.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 693.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- After the change the chatbot ran ruff with the rules FBT001 and FBT002 and saw reports only for typer command functions and ran ruff check and ruff format --check with the settings of the project on the file and both passed. The chatbot did not run the project's tests. The bug report also asks to leave the typer commands out through per-file-ignores. This patch does not change the ruff settings because the two rules are not switched on there. No new test was added because behaviour is unchanged.

## Search words

security-checker cli _diff_scope boolean positional argument keyword-only FBT001 FBT002 full flag refactor

## The full patch

`````diff
diff --git a/src/security_checker/cli.py b/src/security_checker/cli.py
index 6f0a497..2c5a21b 100644
--- a/src/security_checker/cli.py
+++ b/src/security_checker/cli.py
@@ -186,7 +186,7 @@ def _suppression(loaded: LoadedConfig, root: Path) -> SuppressionRules:
 
 
 def _diff_scope(
-    loaded: LoadedConfig, root: Path, base: str | None, full: bool
+    loaded: LoadedConfig, root: Path, base: str | None, *, full: bool
 ) -> tuple[DiffScope | None, list[str]]:
     """target.mode と --base / --full から検査範囲を決める (§7.4)."""
     mode = "full" if full else loaded.config.target.mode
@@ -262,7 +262,7 @@ def scan(
     overrides.update(_logging_overrides(log_format, log_level))
     loaded = _load(root, config_path, preset, overrides)
     _configure_logging(loaded)
-    diff, diff_warnings = _diff_scope(loaded, root, base, full)
+    diff, diff_warnings = _diff_scope(loaded, root, base, full=full)
 
     try:
         outcome = asyncio.run(
@@ -345,7 +345,7 @@ def review(
     overrides.update(_logging_overrides(log_format, log_level))
     loaded = _load(root, config_path, preset, overrides)
     _configure_logging(loaded)
-    diff, diff_warnings = _diff_scope(loaded, root, base, full)
+    diff, diff_warnings = _diff_scope(loaded, root, base, full=full)
 
     price_table = load_price_table(
         loaded.config_path.parent if loaded.config_path is not None else None
`````

[Back to the shelf](README.md)

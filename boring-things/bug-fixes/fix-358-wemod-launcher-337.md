# Fix 358: wemod-launcher: scanfolderforversions calls os.makedirs with exists_ok and crashes with TypeError

Status: UNSENT and UNTESTED. Free to take.

- Project: DeckCheatz/wemod-launcher
- Bug report title: scanfolderforversions(): os.makedirs(..., exists_ok=True) typo
- Bug report: number 337 ([open the bug report](https://github.com/DeckCheatz/wemod-launcher/issues/337))
- Project license: AGPL-3.0
- Language: Python
- Test included: no
- Patch file: [fixes/358-wemod-launcher-337.patch](fixes/358-wemod-launcher-337.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/358-wemod-launcher-337.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-358-wemod-launcher-337.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-358-wemod-launcher-337.html

## The bug

src/constutils.py calls os.makedirs(prefixesfolder exists_ok=True). The name of the argument is exist_ok so the call raises TypeError as soon as scanfolderforversions finds a GE-Proton 7 prefix with WeMod installed.

## The fix

The argument is now spelled exist_ok.

## Files changed

- src/constutils.py

## How to use the fix

1. Get a copy of the project DeckCheatz/wemod-launcher.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 358-wemod-launcher-337.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 337.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- No test was added for the one-word change. The chatbot did not run the project's code or tests.

## Search words

wemod-launcher scanfolderforversions os.makedirs exists_ok exist_ok TypeError constutils prefix upload

## The full patch

`````diff
diff --git a/src/constutils.py b/src/constutils.py
index ec9b535..7529050 100755
--- a/src/constutils.py
+++ b/src/constutils.py
@@ -261,7 +261,7 @@ def scanfolderforversions(
         from mainutils import copy_folder_with_progress
 
         prefixesfolder = os.path.join(SCAN_FOLDER, "prefix")
-        os.makedirs(prefixesfolder, exists_ok=True)
+        os.makedirs(prefixesfolder, exist_ok=True)
         protonconfminor = load_conf_setting("ProtonMinorSeven")
         prefixesfile = os.path.join(
             prefixesfolder, f"Proton7.{protonconfminor}.zip"
`````

[Back to the shelf](README.md)

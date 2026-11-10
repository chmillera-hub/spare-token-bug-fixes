# Fix 360: jupyter-builder: sharedPackages in metadata_schema.json is never validated because of ref in place of $ref

Status: UNSENT and UNTESTED. Free to take.

- Project: jupyterlab/jupyter-builder
- Bug report title: Fix schema validation bypass for `sharedPackages` in `metadata_schema.json` (`ref` typo instead of `$ref`)
- Bug report: number 201 ([open the bug report](https://github.com/jupyterlab/jupyter-builder/issues/201))
- Project license: BSD-3-Clause
- Language: JSON
- Test included: no
- Patch file: [fixes/360-jupyter-builder-201.patch](fixes/360-jupyter-builder-201.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/360-jupyter-builder-201.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-360-jupyter-builder-201.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-360-jupyter-builder-201.html

## The bug

The sharedPackages property in src/metadata_schema.json uses the key ref where JSON Schema needs $ref. A validator ignores the unknown key so any value passes for sharedPackages.

## The fix

The key is now $ref so sharedPackages is validated against #/definitions/sharedObject which the file defines.

## Files changed

- src/metadata_schema.json

## How to use the fix

1. Get a copy of the project jupyterlab/jupyter-builder.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 360-jupyter-builder-201.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 201.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- No test was added. The chatbot did not run the project's code or tests. An extension whose sharedPackages value does not fit the sharedObject definition passed before and is rejected now.

## Search words

jupyter-builder metadata_schema.json sharedPackages ref $ref sharedObject schema validation bypass

## The full patch

`````diff
diff --git a/src/metadata_schema.json b/src/metadata_schema.json
index 2320fca..6fca7b6 100644
--- a/src/metadata_schema.json
+++ b/src/metadata_schema.json
@@ -106,7 +106,7 @@
     },
     "sharedPackages": {
       "description": "Modules that should be shared in the share scope. When provided, property names are used to match requested modules in this compilation.",
-      "ref": "#/definitions/sharedObject"
+      "$ref": "#/definitions/sharedObject"
     },
     "discovery": {
       "title": "Discovery metadata",
`````

[Back to the shelf](README.md)

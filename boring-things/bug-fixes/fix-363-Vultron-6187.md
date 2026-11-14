# Fix 363: Vultron: markdownlint ignores leave out the mkdocs build output so a bare run lints generated files

Status: UNSENT and UNTESTED. Free to take.

- Project: CERTCC/Vultron
- Bug report title: markdownlint's ignores omit the mkdocs build output, so a bare run lints the built site
- Bug report: number 6187 ([open the bug report](https://github.com/CERTCC/Vultron/issues/6187))
- Project license: MIT (SEI)
- Language: YAML
- Test included: no
- Patch file: [fixes/363-Vultron-6187.patch](fixes/363-Vultron-6187.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/363-Vultron-6187.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-363-Vultron-6187.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-363-Vultron-6187.html

## The bug

The ignores list of .markdownlint-cli2.yaml names every other generated or scratch folder and leaves out site (the mkdocs build output which .gitignore lists). After a docs build a bare markdownlint-cli2 run lints the generated markdown under site. The command in mdlint.sh has the same gap.

## The fix

site/** is now in the ignores list of .markdownlint-cli2.yaml and the command in mdlint.sh carries the matching #site/** negation.

## Files changed

- .markdownlint-cli2.yaml
- mdlint.sh

## How to use the fix

1. Get a copy of the project CERTCC/Vultron.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 363-Vultron-6187.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 6187.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- No test was added because the change is in lint settings. Nobody has run markdownlint with the change. The chatbot read the first part of the bug report and the text was cut off after the evidence section so a requested detail may be missing.

## Search words

Vultron markdownlint-cli2 ignores site mkdocs build output mdlint.sh generated markdown lint

## The full patch

`````diff
diff --git a/.markdownlint-cli2.yaml b/.markdownlint-cli2.yaml
index 49a872e..06928b4 100644
--- a/.markdownlint-cli2.yaml
+++ b/.markdownlint-cli2.yaml
@@ -61,6 +61,8 @@ ignores:
   - "wip_outputs/**"
   # Generated knowledge-graph output; git-ignored, but markdownlint globs it anyway
   - "graphify-out/**"
+  # mkdocs build output; git-ignored, but markdownlint globs it anyway
+  - "site/**"
   # Any node_modules, including ui/node_modules after `npm ci` in ui/
   - "**/node_modules/**"
   - ".github/**"
diff --git a/mdlint.sh b/mdlint.sh
index 869164e..048a0de 100755
--- a/mdlint.sh
+++ b/mdlint.sh
@@ -15,4 +15,4 @@
 # U.S. Patent and Trademark Office by Carnegie Mellon University
 #
 
-markdownlint-cli2 --fix --config .markdownlint-cli2.yaml "**/*.md" "#node_modules/**" "#.venv/**" "#.git/**" "#wip_notes/**" "#graphify-out/**" "#plan/history/**"
+markdownlint-cli2 --fix --config .markdownlint-cli2.yaml "**/*.md" "#node_modules/**" "#.venv/**" "#.git/**" "#wip_notes/**" "#graphify-out/**" "#site/**" "#plan/history/**"
`````

[Back to the shelf](README.md)

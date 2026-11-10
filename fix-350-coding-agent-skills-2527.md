# Fix 350: coding-agent-skills: the malformed-input corpus feeds parse_codex_catalog lines split by splitlines()

Status: UNSENT and UNTESTED. Free to take.

- Project: EJRyan89/coding-agent-skills
- Bug report title: malformed-input corpus: parse_codex_catalog is fed splitlines() lines, not the converse stream's
- Bug report: number 2527 ([open the bug report](https://github.com/EJRyan89/coding-agent-skills/issues/2527))
- Project license: MIT
- Language: Python
- Test included: no
- Patch file: [fixes/350-coding-agent-skills-2527.patch](fixes/350-coding-agent-skills-2527.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/350-coding-agent-skills-2527.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-350-coding-agent-skills-2527.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-350-coding-agent-skills-2527.html

## The bug

_codex_catalog in tests/malformed_input/readers_deployer.py splits the text with str.splitlines() which also breaks on U+0085 and U+2028 and U+2029. The deployer itself splits program output with discovery.output_lines (newline only) so the corpus case reads as several lines a catalog that the deployer reads as one.

## The fix

_codex_catalog now passes discovery.output_lines(text_of(path)) to parse_codex_catalog so the corpus feeds the same lines the deployer would.

## Files changed

- tests/malformed_input/readers_deployer.py

## How to use the fix

1. Get a copy of the project EJRyan89/coding-agent-skills.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 350-coding-agent-skills-2527.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 2527.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- One line of test support code changed and no new test was added. The chatbot did not run the project's tests so nobody has confirmed that every corpus case still gives its recorded result.

## Search words

coding-agent-skills malformed_input readers_deployer parse_codex_catalog splitlines output_lines U+2028

## The full patch

`````diff
diff --git a/tests/malformed_input/readers_deployer.py b/tests/malformed_input/readers_deployer.py
index 8d57be6..6cfdae1 100644
--- a/tests/malformed_input/readers_deployer.py
+++ b/tests/malformed_input/readers_deployer.py
@@ -174,7 +174,7 @@ def _codex_refusals(path: Path) -> object:
 
 def _codex_catalog(path: Path) -> object:
     """The catalog as list_skills reads it, from the lines `codex debug prompt-input` prints."""
-    return discovery.parse_codex_catalog(text_of(path).splitlines())
+    return discovery.parse_codex_catalog(discovery.output_lines(text_of(path)))
 
 
 def _adapter_frontmatter(path: Path) -> object:
`````

[Back to the shelf](README.md)

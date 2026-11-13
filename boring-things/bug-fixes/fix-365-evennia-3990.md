# Fix 365: Evennia: the multidescer contrib shows the misspelled heading Decsription

Status: UNSENT and UNTESTED. Free to take.

- Project: evennia/evennia
- Bug report title: [BUG] Small typo in the multidescer contrib
- Bug report: number 3990 ([open the bug report](https://github.com/evennia/evennia/issues/3990))
- Project license: BSD-3-Clause
- Language: Python
- Test included: no
- Patch file: [fixes/365-evennia-3990.patch](fixes/365-evennia-3990.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/365-evennia-3990.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-365-evennia-3990.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-365-evennia-3990.html

## The bug

The command that shows one stored description in evennia/contrib/game_systems/multidescer/multidescer.py prints the heading Decsription in front of the key.

## The fix

The heading now reads Description.

## Files changed

- evennia/contrib/game_systems/multidescer/multidescer.py

## How to use the fix

1. Get a copy of the project evennia/evennia.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 365-evennia-3990.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 3990.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-12 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-12 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- No test was added because the change is one word in a message. No line was added to CHANGELOG.md because the maintainers write the entries with a link to the pull request.

## Search words

evennia multidescer contrib Decsription Description typo heading message

## The full patch

`````diff
diff --git a/evennia/contrib/game_systems/multidescer/multidescer.py b/evennia/contrib/game_systems/multidescer/multidescer.py
index 55cba97..e542ad7 100644
--- a/evennia/contrib/game_systems/multidescer/multidescer.py
+++ b/evennia/contrib/game_systems/multidescer/multidescer.py
@@ -260,7 +260,7 @@ class CmdMultiDesc(default_cmds.MuxCommand):
                     multidesc = caller.db.multidesc
                     for mkey, desc in multidesc:
                         if key == mkey:
-                            caller.msg("|wDecsription %s:|n\n%s" % (key, desc))
+                            caller.msg("|wDescription %s:|n\n%s" % (key, desc))
                             return
                     caller.msg("Description key '%s' not found." % key)
                 else:
`````

[Back to the shelf](README.md)

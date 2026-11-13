# Fix 364: cam-ai: the eventer keeps the old tag names after the school of the eventer is changed

Status: UNSENT and UNTESTED. Free to take.

- Project: ludgerh/cam-ai
- Bug report title: Eventer does not pick up a school change (typo taglist vs. tag_list)
- Bug report: number 172 ([open the bug report](https://github.com/ludgerh/cam-ai/issues/172))
- Project license: GPL-3.0
- Language: Python
- Test included: no
- Patch file: [fixes/364-cam-ai-172.patch](fixes/364-cam-ai-172.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/364-cam-ai-172.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-364-cam-ai-172.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-364-cam-ai-172.html

## The bug

tags_refresh in eventers/c_eventers.py notices a changed school and stores the new tags in self.taglist. Every reader uses self.tag_list so the eventer keeps showing the old tag names. When the new school has fewer tags the loop over the predictions can raise IndexError and the eventer has to restart.

## The fix

tags_refresh now stores the new tags in self.tag_list which is the name every reader uses.

## Files changed

- eventers/c_eventers.py

## How to use the fix

1. Get a copy of the project ludgerh/cam-ai.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 364-cam-ai-172.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 172.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-12 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-12 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- No test was added because the method runs inside a loop that needs the camera server and Django. Nobody has run the project with the change. The project keeps a file named CLAUDE.md with rules for AI helpers that the chatbot did not read.

## Search words

cam-ai eventer tags_refresh taglist tag_list school change IndexError predictions

## The full patch

`````diff
diff --git a/eventers/c_eventers.py b/eventers/c_eventers.py
index 911b132..16b8160 100644
--- a/eventers/c_eventers.py
+++ b/eventers/c_eventers.py
@@ -638,7 +638,7 @@ class eve_worker(mp_process):
         await(a_break_time(60.0))
         if self.tag_list_active != self.shared_mem.read_1_meta('school'):
           self.tag_list_active = self.shared_mem.read_1_meta('school')
-          self.taglist = await database_sync_to_async(get_taglist)(self.tag_list_active)
+          self.tag_list = await database_sync_to_async(get_taglist)(self.tag_list_active)
     except Exception as fatal:
       self.logger.error('Error in process: ' 
         + self.logname
`````

[Back to the shelf](README.md)

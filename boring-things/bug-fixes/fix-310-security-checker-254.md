# Fix 310: security-checker: the CI run of one commit on main is cancelled when the next commit is merged

<!-- {% raw %} -->

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(ci): concurrency の cancel-in-progress が main への push にも効き、続けてマージすると前のコミットの CI が取り消される
- Bug report: number 254 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/254))
- Project license: MIT
- Language: Python
- Test included: no
- Patch file: [fixes/310-security-checker-254.patch](fixes/310-security-checker-254.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/310-security-checker-254.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-310-security-checker-254.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-310-security-checker-254.html

## The bug

The concurrency block of .github/workflows/ci.yml sets cancel-in-progress to true for every event. On main the group is the same for every push so a second merge cancels the CI run of the first commit and that commit keeps the result cancelled.

## The fix

cancel-in-progress is now true only when the event is pull_request (the expression the bug report gives). A push to main lets the earlier run finish.

## Files changed

- .github/workflows/ci.yml

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 310-security-checker-254.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 254.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- No test was added because the change is one line of workflow settings. Nobody has run the workflow with the change.

## Search words

security-checker ci.yml concurrency cancel-in-progress main push pull_request cancelled workflow github actions

## The full patch

`````diff
diff --git a/.github/workflows/ci.yml b/.github/workflows/ci.yml
index 14b939a..98dbd3d 100644
--- a/.github/workflows/ci.yml
+++ b/.github/workflows/ci.yml
@@ -13,7 +13,7 @@ permissions:
 
 concurrency:
   group: ci-${{ github.ref }}
-  cancel-in-progress: true
+  cancel-in-progress: ${{ github.event_name == 'pull_request' }}
 
 jobs:
   # squash merge 後のコミットメッセージは PR タイトルになる (設計書 §31.1)。
`````

[Back to the shelf](README.md)

<!-- {% endraw %} -->

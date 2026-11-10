# Fix 351: coding-agent-skills: the shepherd script docstring says the tick hands each merge to repo-cleanup

Status: UNSENT and UNTESTED. Free to take.

- Project: EJRyan89/coding-agent-skills
- Bug report title: shepherd_pull_requests: docstring says the tick hands each merge to repo-cleanup
- Bug report: number 2524 ([open the bug report](https://github.com/EJRyan89/coding-agent-skills/issues/2524))
- Project license: MIT
- Language: Python
- Test included: no
- Patch file: [fixes/351-coding-agent-skills-2524.patch](fixes/351-coding-agent-skills-2524.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/351-coding-agent-skills-2524.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-351-coding-agent-skills-2524.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-351-coding-agent-skills-2524.html

## The bug

The module docstring of .claude/skills/shepherd-pull-requests/scripts/shepherd_pull_requests.py says the session hands each merge to repo-cleanup. SKILL.md of the same skill forbids the session to start repo-cleanup and tells the session to name the worktree for the user.

## The fix

The docstring now says the session names each merged worktree for the user to retire with /repo-cleanup (the wording the bug report asks for). Only the docstring changed.

## Files changed

- .claude/skills/shepherd-pull-requests/scripts/shepherd_pull_requests.py

## How to use the fix

1. Get a copy of the project EJRyan89/coding-agent-skills.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 351-coding-agent-skills-2524.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 2524.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- Only a docstring changed so no test was added. The chatbot read the sentence quoted in the bug report and did not read SKILL.md.

## Search words

coding-agent-skills shepherd_pull_requests docstring repo-cleanup merge worktree user retires

## The full patch

`````diff
diff --git a/.claude/skills/shepherd-pull-requests/scripts/shepherd_pull_requests.py b/.claude/skills/shepherd-pull-requests/scripts/shepherd_pull_requests.py
index 139e986..f2e2b9e 100644
--- a/.claude/skills/shepherd-pull-requests/scripts/shepherd_pull_requests.py
+++ b/.claude/skills/shepherd-pull-requests/scripts/shepherd_pull_requests.py
@@ -1,5 +1,6 @@
 """One tick of the merge shepherd over this repository's open pull requests, so the session that runs it only
-messages the sessions that own them, judges what the script cannot, and hands each merge to repo-cleanup.
+messages the sessions that own them, judges what the script cannot, and names each merged worktree for the
+user to retire with /repo-cleanup.
 
 Run it from the hub on main. One tick:
`````

[Back to the shelf](README.md)

# Fix 353: coding-agent-skills: two FAILED lines print outside text without flat_text

Status: UNSENT and UNTESTED. Free to take.

- Project: EJRyan89/coding-agent-skills
- Bug report title: repository skills: FAILED lines print an outside value without flat_text
- Bug report: number 2536 ([open the bug report](https://github.com/EJRyan89/coding-agent-skills/issues/2536))
- Project license: MIT
- Language: Python
- Test included: no
- Patch file: [fixes/353-coding-agent-skills-2536.patch](fixes/353-coding-agent-skills-2536.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/353-coding-agent-skills-2536.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-353-coding-agent-skills-2536.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-353-coding-agent-skills-2536.html

## The bug

main in .claude/skills/audit-repository/scripts/audit_repository.py and main in .claude/skills/implement-change/scripts/pull_request.py print FAILED followed by the error text as it is. The error can carry an error message from git that spans several lines so the FAILED line is not one line.

## The fix

Both lines now pass the error text through flat_text which both scripts already import. Each FAILED line is one line.

## Files changed

- .claude/skills/audit-repository/scripts/audit_repository.py
- .claude/skills/implement-change/scripts/pull_request.py

## How to use the fix

1. Get a copy of the project EJRyan89/coding-agent-skills.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 353-coding-agent-skills-2536.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 2536.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- No test was added because the chatbot did not read how the project tests the main functions of these two scripts. The chatbot did not run the project's code or tests. The bug report text the chatbot read was cut off after the first sentence of the expected behaviour.

## Search words

coding-agent-skills FAILED line flat_text audit_repository pull_request outside value one line git error

## The full patch

`````diff
diff --git a/.claude/skills/audit-repository/scripts/audit_repository.py b/.claude/skills/audit-repository/scripts/audit_repository.py
index bd40a88..0788852 100644
--- a/.claude/skills/audit-repository/scripts/audit_repository.py
+++ b/.claude/skills/audit-repository/scripts/audit_repository.py
@@ -1664,7 +1664,7 @@ def main(
             else:
                 lines = duplicates(gh, options.queries)
     except AuditError as exc:
-        print(f"FAILED {exc}")
+        print(f"FAILED {flat_text(str(exc))}")
         return 1
     print("\n".join(lines))
     return 0
diff --git a/.claude/skills/implement-change/scripts/pull_request.py b/.claude/skills/implement-change/scripts/pull_request.py
index 5bd47c1..a5a21c3 100644
--- a/.claude/skills/implement-change/scripts/pull_request.py
+++ b/.claude/skills/implement-change/scripts/pull_request.py
@@ -398,7 +398,7 @@ def main(
     try:
         return run(options, git or GitClient(), github)
     except PullRequestError as exc:
-        print(f"FAILED {exc}")
+        print(f"FAILED {flat_text(str(exc))}")
         return 1
`````

[Back to the shelf](README.md)

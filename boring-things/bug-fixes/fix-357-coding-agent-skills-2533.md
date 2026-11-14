# Fix 357: coding-agent-skills: the trust-boundary route of review-repository misses the hub guard option suite and its fixture

Status: UNSENT and UNTESTED. Free to take.

- Project: EJRyan89/coding-agent-skills
- Bug report title: review-repository trust-boundary route misses the hub guard option suite and its fixture
- Bug report: number 2533 ([open the bug report](https://github.com/EJRyan89/coding-agent-skills/issues/2533))
- Project license: MIT
- Language: JSON
- Test included: no
- Patch file: [fixes/357-coding-agent-skills-2533.patch](fixes/357-coding-agent-skills-2533.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/357-coding-agent-skills-2533.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-357-coding-agent-skills-2533.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-357-coding-agent-skills-2533.html

## The bug

Two route patterns in .claude/skills/review-repository/references/specialists.json list the hub guard test suites and leave out tests/tools/test_hub_guard_git_options.py. No pattern names tests/fixtures/hub-guard/option-catalogues.json. A change that loosens the option catalogue of the guard goes to no trust-boundary reviewer.

## The fix

Both patterns now include hub_guard_git_options and each is followed by a new pattern for tests/fixtures/hub-guard/option-catalogues.json. The file is still valid JSON.

## Files changed

- .claude/skills/review-repository/references/specialists.json

## How to use the fix

1. Get a copy of the project EJRyan89/coding-agent-skills.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 357-coding-agent-skills-2533.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 2533.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- No test was added because the chatbot did not read how the project tests the routes. The chatbot did not run the project's code or tests. The fixtures folder also holds option-catalogues-uutils.json. The bug report names only option-catalogues.json so the new pattern matches only that file.

## Search words

coding-agent-skills review-repository specialists.json trust-boundary route hub_guard_git_options option-catalogues fixture

## The full patch

`````diff
diff --git a/.claude/skills/review-repository/references/specialists.json b/.claude/skills/review-repository/references/specialists.json
index 6a09736..a7950ed 100644
--- a/.claude/skills/review-repository/references/specialists.json
+++ b/.claude/skills/review-repository/references/specialists.json
@@ -104,7 +104,8 @@
         "(?i)^tools/hub_guard-powershell\\.ps1$",
         "(?i)^\\.claude/settings\\.json$",
         "(?i)^deployer/platform_support\\.py$",
-        "(?i)^tests/tools/test_(?:bash_syntax|checkout_trust|hub_guard|hub_guard_bash|hub_guard_pwsh|plugin_canary|prefix_programs|runtime_canary|skill_evals)\\.py$",
+        "(?i)^tests/tools/test_(?:bash_syntax|checkout_trust|hub_guard|hub_guard_bash|hub_guard_git_options|hub_guard_pwsh|plugin_canary|prefix_programs|runtime_canary|skill_evals)\\.py$",
+        "(?i)^tests/fixtures/hub-guard/option-catalogues\\.json$",
         "(?i)^\\.claude/skills/shepherd-pull-requests/scripts/(?:test_)?shepherd_pull_requests\\.py$",
         "(?i)^skills/ejryan89-code-review-core/scripts/review_(?:analyzers|batches|canary|dispatch|documents|github|guard|hosts|io|operation|pipeline|process|records|reporting|reviewer_setup|reviewers|run|runtime|snapshot|source|specialists|vocabularies)\\.py$",
         "(?i)^skills/ejryan89-code-review-core/scripts/test_(?:adversarial_inputs|review_documents|review_guard)\\.py$",
@@ -174,7 +175,8 @@
         "(?i)^tools/hub_guard-powershell\\.ps1$",
         "(?i)^\\.claude/settings\\.json$",
         "(?i)^deployer/platform_support\\.py$",
-        "(?i)^tests/tools/test_(?:bash_syntax|checkout_trust|hub_guard|hub_guard_bash|hub_guard_pwsh|plugin_canary|prefix_programs|runtime_canary|skill_evals)\\.py$",
+        "(?i)^tests/tools/test_(?:bash_syntax|checkout_trust|hub_guard|hub_guard_bash|hub_guard_git_options|hub_guard_pwsh|plugin_canary|prefix_programs|runtime_canary|skill_evals)\\.py$",
+        "(?i)^tests/fixtures/hub-guard/option-catalogues\\.json$",
         "(?i)^\\.claude/skills/shepherd-pull-requests/scripts/(?:test_)?shepherd_pull_requests\\.py$",
         "(?i)^skills/ejryan89-code-review-core/scripts/review_(?:analyzers|batches|canary|dispatch|documents|github|guard|hosts|io|operation|pipeline|process|records|reporting|reviewer_setup|reviewers|run|runtime|snapshot|source|specialists|vocabularies)\\.py$",
         "(?i)^skills/ejryan89-code-review-core/scripts/test_(?:adversarial_inputs|review_documents|review_guard)\\.py$",
`````

[Back to the shelf](README.md)

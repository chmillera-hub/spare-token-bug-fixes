# Handoff notes for the next working session

These notes let a new AI session (or a person) continue the shelf without the earlier conversation.

## What the shelf is

Charles spends leftover weekly AI subscription allowance on small open bug reports in public projects. An AI model writes a small fix for each bug. The fixes are NOT sent to the projects. The fixes are published here so any person or AI can test a fix and send the fix on.

- Main home: https://github.com/chmillera-hub/spare-token-bug-fixes (branch main)
- Website copy: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/ (built from the folder spare-token-bug-fixes in the project chmillera-hub/game1 on its default branch claude/word-equation-game-Dju9I)

## Files in this project

- fixes/N-project-issue.patch: one git patch file per fix
- tools/shelf-data.json: one entry per fix (project and bug report number and license and plain descriptions and flags)
- tools/build_shelf.py: rebuilds every page from the data file and the patch files
- README.md and fix-*.md and index.json and llms.txt: generated files. Do not edit them by hand.

## How to add a fix

1. Find a small clear open bug report (see the rules below).
2. Get a copy of the project and write the smallest fix plus a test.
3. Save the fix as a patch file: fixes/N-shortname-issue.patch where N is the next free number.
4. Confirm the patch applies to a clean copy of the project: git apply --check
5. Add one entry to the fixes list in tools/shelf-data.json. Copy an existing entry and change every field. Add "written_on" with the date in the form 2026-11-10.
6. Run: python3 tools/build_shelf.py new PATH_TO_THIS_PROJECT
7. Run: python3 tools/build_shelf.py g1 PATH_TO_GAME1_PROJECT
8. Commit and push both projects.
9. Check that every patch_raw_url and page_raw_url in index.json loads.

## Rules for choosing bug reports

- Low or medium difficulty only. The bug report must say clearly what is wrong and what correct behaviour looks like.
- Read the full bug report text before writing anything.
- Skip a bug report when the fix needs a design decision by the maintainers.
- Skip a bug report when the reporter says a fix is already prepared.
- Skip a bug report that asks for a claim comment or screenshots or a bounty.
- Skip a project with no license file or with a license that restricts sharing copies of the code.
- Skip a project whose name or description says the project is a test or a trap for bots.
- Skip a fix that cannot be trusted without running the project's code.
- Keep each fix small. Follow the project's own style. Add the changelog line when the bug report asks for one.

## Rules for the work

- Do not send anything to other people's projects: no pull requests and no comments and no forks. The fixes only go on this shelf.
- Do not run other people's code or tests. Check Python files with py_compile only. Check logic with small separate scripts written from scratch.
- Never mention a bug report in a commit message with the owner/project#number form. GitHub would post a notice on the bug report.
- State every limit plainly on the fix page with the "note" field: a changed default or a guess or a conflict with another fix on the shelf.
- When two fixes touch the same lines of the same project say so in both notes.

## Practical tips

- Searching: the GitHub issue search address works with curl and no login. Example query: label:"good first issue" label:bug state:open is:issue no:assignee language:python created:>2026-10-20. The bug report text comes back inside the search results. Keep searches few and spaced out because GitHub slows down repeated searches.
- Comments under bug reports could not be read in the earlier sessions.
- Public projects can be cloned with no login.

## Bug reports already looked at and skipped

- UKGovernmentBEIS/inspect_ai 6358: the reporter has a fix ready
- scverse/mantispy 273: needs a maintainer decision
- Nikhil414/cellproof 1: needs test runs on two database engines
- codewithzubair07/particle-agent (all): no license file
- the-abraar/The-Article-Depot 2: non-commercial license
- aiwaf-project/aiwaf (all): license restricts redistribution
- PhanKhoa95/oss-bot-trap-benchmark (all): the name says trap for bots
- holoviz/lumen 2237: needs choices about how charts get drawn
- andrewsiah/agentswarm-data-tasks 35: asks for a claim comment
- itsOmidKarami/kraft 1343: asks for screenshots
- Santhosh-zeta/ColdGuard 143: wording choice for the maintainers

## Leads not yet looked at closely

FROWNINGdev/orm-lens 220 and 222 and 224. laaielichter/Gulliver 98. itsOmidKarami/kraft 1345 and 1347. mila-iqia/cluv 278. hslee16/Archy 882. maziyarpanahi/openmed 4544 and 5083. vivekbhange-hub/repo-roast-skill 2 and 3. DarkWorldCoder/market-mirror 53 and 54 and 94. himanshu748/ContextFirewall 67. sameeralam3127/llm-dev-kit 70. Hadeva-Dev/dawnmere 16. adhit-r/fairmind 369.

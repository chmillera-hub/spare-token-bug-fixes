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
- tools/build_video.sh and tools/video_cards.py and tools/video_music.py: build the video of every fix (see the section How to make the video)
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

## How to make the video

Charles posts a video of the shelf on social media so a person or a chatbot who sees the video can find a fix and send the fix on. Rebuild the video whenever fixes were added.

1. Finish the shelf first: every new fix has its entry in tools/shelf-data.json. The video reads that file.
2. Make sure python3 has Pillow and NumPy and that ffmpeg is installed.
3. Run: bash tools/build_video.sh SOME_EMPTY_WORK_FOLDER OUTPUT.mp4 (name the output after the number of fixes: for example 121-free-bug-fixes-fast.mp4).
4. Look at three frames before sending: the first frame and one fix screen and the closing screen. ffmpeg -ss SECONDS -i OUTPUT.mp4 -frames:v 1 frame.png grabs one frame.
5. Send the file to Charles in the chat. The video is not stored in either GitHub project.

What the build script makes and why:

- Portrait 1080 by 1920 at 30 frames per second. Why: Charles posts the video on phones.
- An opening screen for 3 seconds with the shelf address and five steps for using a fix. Then one screen per fix in order for 1.5 seconds each. Then a closing screen for 3 seconds. Why 1.5 seconds: Charles asked for that length because a chatbot reads the frames fast. A person has to pause to read a screen.
- Straight cuts between screens with no scroll. Why: a fast scroll made the file four times larger and gave blurred in-between frames.
- The first frame is the opening screen with no fade from black. Why: social media previews show the first frame.
- Each fix screen shows the fix number and the project and the bug report number and the title and what is wrong and what the fix changes and the patch file name and a three-line warning (written by an AI chatbot and not reviewed and not tested in the project and not sent). The note field with the limits of each fix is not on the screen: the fix pages hold the notes.
- Music: tools/video_music.py makes soft chords and a plucked pattern from scratch. No existing song or recording is used. Why: a video with someone else's music can be taken down.
- Small file: one encode of still screens (libx264 with crf 31 and the stillimage tune) and 48 kbit audio. 121 fixes gave 3 minutes 8 seconds and about 8.4 megabytes. Why: Charles wants the smallest file that keeps the text sharp so uploads are fast.

Limits to tell Charles each time: nobody listened to the music (the script only measures loudness when asked) and the screens leave out the notes of each fix.

Changing the video: the seconds per fix are the two duration lines in tools/build_video.sh. The look of the screens is in tools/video_cards.py (the text shrinks by itself until a fix fits on one screen). An older slow version (5 seconds per fix with a scroll between fixes and about 30 megabytes for 101 fixes) was replaced by this fast version at Charles's request.

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
- FROWNINGdev/orm-lens 222: no longer in the list of open bug reports on 2026-11-10
- laaielichter/Gulliver 98: asks for a claim comment and already has three comments that could not be read
- mila-iqia/cluv 278: the output format needs maintainer choices and the result cannot be trusted without running against remote clusters
- hslee16/Archy 882: the maintainers must choose the shape of the result and every sweep caller changes
- himanshu748/ContextFirewall 67: asks for a claim comment and offers two different approaches for /health
- sameeralam3127/llm-dev-kit 70: needs a new stored field in the database and cannot be trusted without running the app
- DarkWorldCoder/market-mirror 94: needs the lock file rebuilt with the project's tooling and an unknown list of lint errors fixed
- adhit-r/fairmind 369: the address must change in step in the frontend and the backend setting and the Authentik setup script and the docs. Sign-in can only be confirmed by running the app with an Authentik server. The project also asks contributors to sign a contributor agreement.
- mila-iqia/cluv 261: the right behaviour for --test-only is the subject of an open feature request (193)
- itsOmidKarami/kraft 1117: asks for a before and after screenshot
- hslee16/Archy 526: cannot be trusted without running the tree-sitter parser
- salismt/promisebench 1: the fix changes the benchmark and must ship as a new fixture version
- stillproof-labs/stillproof-anchor 5: says comment to be assigned before starting
- flisk-sh/flisk 3536: asks for a claim comment and a rebuilt cli/dist folder and a signed-off commit and re-captured file hashes
- gregoryduckworth/homepage-traefik (all): no license file
- Subhrangsu90/repopilot-demo (all): no license file
- vivekbhange-hub/repo-roast-skill 4: labelled enhancement and needs a choice about what counts as a test file
- Hayuuka/sshhh 8: the maintainer offers two options (build the feature or delete the README section)
- astahmer/dshfiles 196: cannot be trusted without running the jj tool
- hslee16/Archy 879: the text says decide first whether the comment or the section order is wrong
- hslee16/Archy 863: the maintainers must decide whether to re-date the research document and the numbers depend on another project
- andrewsiah/agentswarm-web-tasks 22: asks for a claim and for a run of the project's own checker in Docker
- himanshu748/devswarm 5: the maintainers must decide how zero and invalid values are handled
- maximem-ai/maximem_synap_core 23: the text does not say what the correct answer for an unknown type is (an error or an empty result)
- ShisatoYano/AutonomousVehicleControlBeginnersGuide 164: touches many files that an open pull request (157) moves and the demos must be regenerated by running the code
- wildlifeai/spyfish-aotearoa-toolkit (all): no license file
- himanshu748/devswarm 74: the page still says the numbers are live when a value is missing so the maintainers must choose what to show
- jasonkryst/MyFinances 509: the maintainers must choose the number format of the chart axes (whole numbers or compact form) and how the unit symbol is shown
- Sh1n1230/security-checker 602: needs a new way to carry a warning from the GitHub client to the comment result which is a design choice
- jwalk999/TDH-Weather-Data-Visualizer 1: asks for new tip lists and research and is not a small bug
- KonstantinStarovoytov/kitden 12: asks for a screenshot
- jumilandelapena/demo-inventory-api (all): no license file
- DennisSab/workout-pr-tracker (all): no license file
- justin06lee/ucscmsa.com (all): no license file
- TMHSDigital/godot-correctness-mcp (all): the license (CC BY-NC-ND) forbids changed copies
- eogenyi23-creator/soroban-merkle-airdrop (all seen): every report ends with comment to claim this issue
- laaielichter/Gulliver 111 and 112 and laaielichter/Ai-edit-studio 89 and 90: every report ends with comment here to claim it and you'll be assigned
- jynlee7/portfolio 35 and 36: the code named in the reports is an uncommitted working copy or needs new content fields
- Scrumsdotcom/scrums 10 and nxtg-ai/forge-ui 91: each report offers two ways and leaves the choice open
- ourdao/ourdao-frontend 539: asks for a new guard check whose rule would flag another existing test file
- ourdao/ourdao-frontend 536: the download checks the bytes against the content id so the test needs content ids computed by the project's own code
- rel-kit/relkit 183 and 184: need a re-pinned template digest or a regenerated help snapshot made by the project's tooling
- mfeflow/mfeflow 96: needs template version bumps and may change generated snapshot files

## Leads not yet looked at closely

Read in full and looked doable but not started: hslee16/Archy 749 (two unread comments) and 756 (shallow clone warning: touches three outputs) and 802 (medium: needs the exact exception types of import-linter and grimp). himanshu748/devswarm 42 (count regeneration rounds apart from review attempts in src/orchestrator.js) and 29 (needs a choice of field names). Sh1n1230/security-checker 615 (keep an excerpt of osv-scanner stderr on success) and 644 (test exclude patterns of a bundled rule). awslabs/social-messaging-agent-runtime-toolkit 62 (return 502 when CodeBuild reads fail: also touches the console frontend). ujjwalv01/releaseproof 113 (size limits on registry downloads: medium). rdlugs/sentryward 270 (add provider to a server response and use it in the client: license not checked). Pranayd555/codelens-graph 27 and 28 and 41 (each has a todo test that names the bug: MIT checked: every new codelens fix collides with the changelog lines of the fixes already on the shelf). gabe-santana/arkdraw 45 (MIT checked). mfeflow/mfeflow 99 is done and 96 is skipped.

Titles seen but text unread: hslee16/Archy 800 and the reports labelled good second issue (880 and 893 and 790 and 789 and 785 and 784 and 778 and 776 and 773 and 763 and 759 and 757 and 748 and 747 and 746 and 745 and 744 and 743 and 742 and 741) and the Archy documentation reports 792 and 787 and 848 and the Archy test reports 825 and 808 and 807 and 805. Santhosh-zeta/ColdGuard 61. Muneer320/klicky 126 (Rust). renatoasterio/DynamoOps 8 (two approaches offered). ModAVD/ModAVD 135 and 136 and 139. mloda-ai/mloda 2684. neomjs/neo 20673. laaielichter/Gulliver 93 and 109 (check for the claim sentence first). stillproof-labs/stillproof 13 and 15 (check for a claim rule first). uutils/sed and uutils/grep and uutils/findutils (Rust: no way to compile). maziyarpanahi/openmed 4544 and 5083. DarkWorldCoder/market-mirror 53 and 54. Sh1n1230/security-checker 645 and 598. awslabs/social-messaging-agent-runtime-toolkit 72 and 74 and 76 and 77 and 79 and 85 and 87. K1rL3s/maxo 388. aerostack2/aerostack2 1047. l3montree-dev/devguard 3319 and 3320. Lumos-Programming/lumos-web 394. Open-Glassbeetle/glassbeetle 302 and 268 and 277 and 281 and 282. Soneso/stellar-agent-wallet 630. davotoula/brollyzapper 114. notjj1234/audiotools 71 and 72. ZIZKA-AI-SL/ZizkaDB 380. knnmelprop/YAADO 130. flisk-sh/flisk 3539 and 3540 and 3541 and flisk-sh/flisk-import 84 (check the claim and signing rules first). From the searches of the fourth session (licenses not checked unless said): ourdao/ourdao-frontend 530 (MIT checked). dhanushbs10/vynlore 16 (MIT checked: Rust). capybarist/hive 4. pidrang/pidrang 198 (MIT checked). ujjwalv01/releaseproof (MIT checked: look for more reports). rim-platform/rim-ui 362 and 363 and 366 and 368. jamesalmeida/tesla-infotainment 82 and 83 and 85 and 87 and 96. digitalaidseattle/culturous-exchange 338. uvais724/fair-interviews 1 and 2 and 3. Open-Source-Orchestra/fork-the-first-artist 17 and 18. codewithpom/cses-better 1. Ghostlink-Labs/ghostlink 10. bymorning/bymorning 53. Nano-Collective/nanocoder 1991. cybermax4200/stellar-did-credit 1146. G33ks/foundryvtt-mcp 16. jenissimo/bottleship 97 and 122. roszhan2684/orgworld-public 4. rchrp/Blame 26. bonzo81/comnd 100. Fuasmattn/design-token-authority 65. agmxyz/me-pi 40. goatplatform/goatdb 94. edkahall/vitrail 2. nema1502/tinkazo 32 and 33 and 34 (Spanish text). AIMFllyYS/DayDayOn 62 (Chinese text). patsypppe/auto-applier 5. rashad-isayev/proofskill 1. OpenDataEnsemble/website 17.

## Notes from the session of 2026-11-10

- The GitHub address for one bug report (api.github.com/repos/OWNER/PROJECT/issues/NUMBER) was refused for projects that are not attached to the session. The search address still worked: api.github.com/search/issues?q=repo:OWNER/PROJECT+is:issue+state:open returns the full text of each bug report. Wait about seven seconds between searches.
- Use the date in UTC for written_on. tools/build_shelf.py counts every fix dated 2026-11-09 as part of the first batch.
- hslee16/Archy and FROWNINGdev/orm-lens bug reports name file lines from an older commit. Find the function by name before editing.
- A second search that worked well for projects in other languages: label:"good first issue" label:bug state:open is:issue no:assignee created:>DATE comments:0 -language:python with sort=created.
- Check the end of every bug report for a claim rule. Several projects end the text with "comment to be assigned" (skip) or "comment before you start" (the earlier sessions wrote the fix and put a note on the fix page).
- When two fixes for one project add tests put the second test in a new file. Two patches that add text at the same spot of one file do not apply together.
- Projects with a prettier or ruff format check: write new code in the shape the formatter would produce. Nobody ran any formatter in the session of 2026-11-10.
- Near the end of the session of 2026-11-10 GitHub answered the search address with "You have exceeded a secondary rate limit" after about 25 searches in one hour. Stop searching when that answer appears and work from the search results already saved.
- MuNuChapterHKN/HKrecruitment 107 and Navardow/personal_website 4 were read and left alone: the first reads like coursework for the members of one student group and the second is a personal site with no license check done.

## Notes from the second session of 2026-11-10 (fixes 69 to 81)

- Thirteen fixes were added in one session with two searches. Many reports in the search results belong to projects already on the shelf so read the leads list before searching.
- A helper shape that worked: write the change in a clone and run git add -A -N . and git diff to save the patch and then git reset and git checkout -- . and git clean -fd and then git apply --check against the clean clone.
- Do not let Python write __pycache__ folders into a clone. Check syntax with ast.parse in a one-line script. Check JavaScript with node --check and shell with bash -n.
- hslee16/Archy moves code between files often. The help text of archy conventions had moved from cli.py to cli_conventions.py. Find the text with grep before trusting the file named in a bug report.
- Under-Research-Labs/CONTINUUM asks for a CHANGELOG.md entry under Unreleased. Two fixes for that project that both add an entry at the top of the Fixed list do not apply together (fixes 69 and 81). Say so in both notes.
- Sh1n1230/security-checker builds its changelog with release-please: add no changelog line. Its line-length check counts Japanese characters as two columns.
- jasonkryst/MyFinances ties every changelog entry to a version bump chosen by the maintainer: add no changelog line.
- The older Archy patches on the shelf were not re-checked against the newest Archy code in this session.

## Notes from the third session of 2026-11-10 (fixes 82 to 101)

- Twenty fixes were added with no new search. Every one came from the leads list or from the two saved search results of the second session.
- awslabs/social-messaging-agent-runtime-toolkit wants a CHANGELOG.md line under Unreleased for a behaviour change and none for a tests-only change. Fixes 72 and 96 and 97 and 99 add their line at the same spot and do not apply one after another. For the next fix in that project say so in the note again.
- The search results cut off long bug report texts. Fixes 96 and 97 and 98 were written from texts whose last lines were missing and their entries carry full_report_read false.
- Scratch checks that worked well: a scratch git repository to produce real git output (fix 85) and a small local test server (fix 101) and the TypeScript compiler from npm run on a scratch copy of a new file (fix 95).
- A project with bandit-style lint rules (noqa: S603 in its code) will reject try/except/pass: use contextlib.suppress.
- For a fix inside an inline script of an HTML page a test can take the changed lines out of the page source with a pattern and run them with made-up data (fix 89).

## Notes from the fourth session of 2026-11-10 (fixes 102 to 121)

- Two new searches worked and the third search got the secondary rate limit answer straight away. The two saved results gave about 110 new bug reports.
- Check the license before reading the code. Three projects in this round had no license file and one had a license that forbids changed copies.
- Pranayd555/codelens-graph marks known bugs with tests that carry a todo option. A fix removes the todo option and changes the code and adds one line to changelog.md. Its default branch is dev. Its reports ask for a comment before starting: the fixes were written and the note on each page says to comment first.
- Changelog lines for one project collide when two patches add a line at the same spot. Adding each line after a different existing bullet (at least four bullets apart) let three codelens-graph patches apply together.
- When a project comment says to raise a version number whenever stored results change (PARSER_VERSION in codelens-graph) raise the number in the patch.
- A one-line change suggested in a bug report can still break at start-up: in vynlore the suggested line used a function before the function was defined so the line had to move.
- ourdao-frontend downloads check file bytes against their content id. A test that passes a made-up id cannot simply get another made-up id.

## Notes from the fifth session of 2026-11-10 (fixes 122 to 171)

- The first request for push access in this session was refused by a safety check because Charles had not yet asked for publishing in his own words. After Charles wrote put them on the Shelf the same request went through. Lesson: when push access is refused finish the work locally and hand Charles a zip file and ask Charles to say plainly that the fixes should go on GitHub.
- Fifty fixes were added with one new search. The search gave almost no new projects so the fixes came from five projects already on the shelf: hslee16/Archy (122 to 125) and awslabs/social-messaging-agent-runtime-toolkit (126 to 131) and Sh1n1230/security-checker (132 to 137 and 142 to 171) and Pranayd555/codelens-graph (138 to 140) and himanshu748/devswarm (141).
- A fast source of small clear reports: Sh1n1230/security-checker has about 500 open reports. Reports 537 to 596 each name one function with untested lines (title: 未テストの分岐をテストする). Each one takes a new small test file. Put every test in its own new file so the patches never collide. The line numbers in those reports come from an older commit so read the function first: in report 589 the code had changed from a warning to an exception.
- Still open from that series and not looked at: 537 and 540 and 547 and 548 and 554 to 558 and 559 and 560 and 563 to 569 and 571 to 576 and 582 and 586 to 588 and 591 to 593. Also not looked at: the third to fifth page of the security-checker list.
- security-checker reports read and skipped: 688 (the reported line is an ordinary comment in the newest code) and 681 (the method could not be found at the reported line) and 685 and 680 and 667 and 695 and 699 (each offers two ways and leaves the choice open) and 645 (needs a label created in the project's settings).
- awslabs/social-messaging-agent-runtime-toolkit: fixes 126 and 128 and 129 add changelog text at the same spot as 72 and 96 and 97 and 99. Reports 77 and 85 (confirmation dialogs) and 79 and 76 and 72 (console pages) were read and not started: each needs React changes that cannot be trusted without running the console. Report 67 leaves a choice open. Report 105 depends on report 68.
- hslee16/Archy: reports 785 (same function as fix 122) and 763 and 778 and 800 and 771 and 915 and 921 were read and not started. 771 says to check which test fixtures read files outside tests/ and that needs a run.
- Pranayd555/codelens-graph: the three new patches and the seven older ones were checked against the newest dev branch and all still apply one by one.
- Use one helper script per session that saves the patch and resets the clone and runs git apply --check. A file removed with git rm must be removed again with plain rm before git diff or the deletion is missing from the patch.

## Notes from the sixth session of 2026-11-10 (fixes 172 to 271)

- One hundred fixes were added and published in six batches. All one hundred are for Sh1n1230/security-checker because that project has about 500 open reports and most of them are small and exact. The shelf is now lopsided: 143 of 271 fixes belong to that one project. For the next round look for other projects first.
- Four kinds of report were used. Named constants for bare numbers (364 to 378). Missing docstrings (379 to 432). Untested lines (468 to 536). Small bugs with a clear fix (446 and 452 and 453 and 462).
- Docstring reports: the project writes its docstrings in Japanese. Read the function body before writing the docstring and check every claim against the code. Each fix page says a native reader should check the wording.
- Patches that collide (each pair is named in both notes): 132 with 180 and 132 with 264. 179 with 197. 185 with 225. 177 with 235. 121 with 136. Every other security-checker patch from 132 to 271 applies one after another (131 patches in a row).
- A docstring patch collides with a code patch only when the two changes sit within three lines of each other. Check pairs with git apply --check after applying one of them.
- The line length limit of the project is 100 columns and Japanese characters count as two columns. Check every added line with unicodedata.east_asian_width before saving a patch.
- security-checker reports read and skipped in this session: 467 (the method is used by two tests so removal needs a choice) and 441 (needs a new warning path and a docs change).
- security-checker reports still open and not started. Untested lines: 537 and 540 and 547 and 548 and 554 to 560 and 563 to 569 and 571 to 576 and 582 and 586 to 588 and 591 to 593 and 532 and 527 and 510 and 508 and 500 to 502 and 493 and 474 to 487. Docstrings: 382 (21 items in config/schema.py) and 384 to 392 and 404 and 420. Typing reports 350 to 363 and complexity reports 338 to 349 need more judgment.
- Working method that was fast: one JSON list of edits per batch and one helper that applies each edit and saves one patch per report and resets the clone. Tests go in new files only. Publish after every batch of about twenty so nothing is lost.


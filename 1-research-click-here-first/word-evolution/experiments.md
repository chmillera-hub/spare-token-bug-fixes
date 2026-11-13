# Can copying with small mistakes build sentences when a reader picks what gets copied

One AI model (Claude) ran every test in a single working session on 11 November 2026 and no other person has rerun the tests yet which means every number on this page is a single unconfirmed analysis.
An AI chatbot reran two of the tests in a new session on 12 November 2026 and the page named second-pass.md in this folder reports the new numbers.

A live version of the experiment with sliders runs in a web browser at this address: https://htmlpreview.github.io/?https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/1-research-click-here-first/word-evolution/live-program.html
The live address depends on a free outside service named htmlpreview and nobody has tested the address yet which means the address might fail.
A second live address runs on the free website copy of this repository: https://chmillera-hub.github.io/spare-token-bug-fixes/1-research-click-here-first/word-evolution/live-program.html
An AI chatbot loaded the second live address on 12 November 2026 and the page came back with the title and the settings and the buttons of the program. The tool that the chatbot used does not run page scripts which means nobody has confirmed yet that the sliders move.

A pool of 300 strings starts as single letters and each paste copies one string with a chance of an added letter or a letter swap or a letter change and no deleting.
A "reader" chooses which strings get copied and the reader is a letter-pattern scorer and not a mind.

- With no reader the pool becomes gibberish with about 1 percent real words.
- A reader who copies the most English-looking string freezes the pool on a two-letter word because every added letter looks worse.
- Forcing one letter onto every string at intervals breaks the freeze and a forced letter every 5 minutes of experiment time gave 90 percent real words across 135 letters while a forced letter every second gave about 2 percent real words.
- A reader with a bonus for command patterns (action word then pointing word then thing word) evolved commands only when partial credit existed as stepping stones (about 1 to 2 commands per string with partial credit and 0 without).
- A reader who favors closeness to a list of 10000 sensible commands reached an exact command such as "wash my dogs" within about 15 to 28 minutes of experiment time with no forcing and about 80 percent of the pool became the same single command.
- Forced letters hurt the closeness reader because a fixed target has a fixed length and extra letters only move a string away from the target.
- Known loophole: a letter changed into a space beside another space disappears because the scripts merge double spaces which works as a hidden form of deleting.

## One long string that holds many different commands

The reader score in this experiment is the number of different complete commands from the 10000-command list found inside one string with a cap of 300 letters.

- A first scoring rule failed because both runs stalled at 1 command when only the single best half-formed command earned partial credit and junk letters cost nothing.
- A corrected rule gave partial credit to every half-formed command and a small cost to every junk letter and the corrected rule reached 7 to 13 different commands per string after 1500 minutes of experiment time across four runs.
- A wrong extra letter inside a half-formed command such as "hug myson" becomes a permanent dead end because the no-deleting rule means the extra letter can never be removed.

## Sorting the picked commands into the order of a one-day story

All 10000 commands were arranged into one story of a single day with eleven scenes that run from waking up to closing the house for the night and the picked commands were sorted into story order after each run.

- One run evolved the jumbled sequence "eat the pie / fix my lid / dry the pot / fix my bags / lift my cup / lock the door / help my son / walk the cat / wash my spoon / hug my son / lock my box".
- Story order turned the same eleven commands into "walk the cat / hug my son / help my son / fix my lid / fix my bags / wash my spoon / dry the pot / lift my cup / eat the pie / lock the door / lock my box".
- A "scene change" means a jump from one scene to a different scene between neighboring commands and story order cut the scene changes from 11 to 6 in one run and from 8 to 5 in a second run and from 7 to 2 in a third run.

## A bonus for commands that sit close together in the story

- The closeness bonus pulled the commands into fewer scenes (4 scenes against 7 scenes in one starting point and 2 scenes against 6 scenes in a second starting point).
- The closeness bonus cost commands (9 commands against 13 and 7 commands against 11).
- The tightest run produced near-copies such as "take my cup / take the cup / lift my cup" which suggests closeness in the list rewards repeating one action and does not reward a sequence of different steps.
- Only two starting points were tested for the closeness bonus which means the sizes of the effects are uncertain.

## A bonus for words that are not repeats

The reader in this experiment gives extra credit for every different word inside the complete commands which means a string that uses the word "cup" three times earns less than a string that uses three different thing words.

- Before the bonus about 64 percent of the words inside the commands were not repeats in two starting points (25 different words out of 39 and 21 different words out of 33).
- With the bonus for words that are not repeats the share rose to 92 percent in one starting point (22 different words out of 24) and to 71 percent in the other starting point (34 different words out of 48).
- One string evolved with the bonus read in story order "pet this bird / hug that boy / pick my herb / fix the lid / dry my pot / take our box / eat my fish / hold your bag" which uses seven different pointing words and thing words where earlier strings repeated "my" in almost every command.
- The count of commands moved in opposite directions in the two starting points (13 commands fell to 8 and 11 commands rose to 16) which means the effect of the bonus on the number of commands is unknown from two starting points.
- Turning on the bonus for words that are not repeats together with the bonus for closeness in the story left many repeats (63 percent and 56 percent of words were not repeats) and produced strings such as "fix the lid / fix my lid / fix the gate / fix your bag".
- Here is a guess about the reason: the two bonuses could pull in opposite directions because commands that sit side by side in the story list share most of their words.

The list of 10000 commands was changed on 12 November 2026 after every run on this page because four words about highly vulnerable people ("baby" and "child" and "children" and "kids") were swapped for "farmer" and "baker" and "farmers" and "bakers" under rule 54 of the rules page in the Bible quote builder folder. A fresh run with the same starting point can therefore give different commands from the commands quoted on this page.

The program files behind every number on this page sit in the folder named boring-things at the top of this project inside the folder named research-program-files.

# A second pass on two of the word evolution tests

November 12 2026

## What this page is

The page named experiments.md in this folder reports tests where text is copied with small mistakes over and over while a "reader" picks which copies survive. The reader is a scoring program and not a mind. The page named experiments.md says no other person has rerun the tests. This page reports a second pass by an AI chatbot (Claude) in a new working session on 12 November 2026.

The second pass reran two tests with new starting points. A starting point is the number that sets the string of random choices a program makes which means a new starting point gives a fresh run of the same experiment. The engine programs were not changed.

A second pass by the same kind of AI chatbot is weaker evidence than a rerun by a person because the same kind of chatbot could repeat the same kind of mistake.

## Test 1: the reader who favors closeness to a list of 10000 commands

The earlier page used two starting points and reported that the pool reached an exact command within about 15 to 28 minutes of experiment time and that about 80 percent of the pool became the same single command. Experiment time counts 600 pastes as one minute.

The second pass used ten new starting points (numbers 11 to 20) and ran each one for 300000 pastes.

- All ten runs reached an exact command from the list which agrees with the earlier page. Three of the exact commands were "find that box" and "fix my lid" and "dry the cup".
- The time to the first exact command ranged from about 7 minutes to about 80 minutes of experiment time. The ten times in minutes were about 7 and 9 and 9 and 11 and 12 and 13 and 22 and 23 and 79 and 80.
- The earlier range of 15 to 28 minutes was too narrow because six of the ten new runs were faster than 15 minutes and two of the ten new runs were slower than 28 minutes.
- The share of the pool holding an exact command at the end ranged from 73 percent to 85 percent with an average of 79 percent which agrees with the earlier "about 80 percent".
- Seven of the ten pools ended with one single exact command and three of the ten pools ended with two different exact commands.

## Test 2: one long string that holds many different commands

The earlier page reported that the corrected scoring rule reached 7 to 13 different commands per string after 1500 minutes of experiment time across four runs.

The second pass used four new starting points (numbers 21 to 24) and ran each one for 900000 pastes which is 1500 minutes of experiment time.

- The best strings held 9 and 15 and 14 and 10 different commands which overlaps the earlier range and reaches a little higher. The two passes together give a range of 7 to 15 different commands across eight runs.
- Sorting the picked commands into the order of the one-day story cut the scene changes in all four new runs (8 to 3 and 13 to 8 and 9 to 6 and 8 to 6) which agrees with the earlier page. A scene change means a jump from one scene of the story to a different scene between neighboring commands.
- The share of words inside the commands that were not repeats was 67 percent and 62 percent and 71 percent and 67 percent which agrees with the earlier figure of about 64 percent before any bonus.

## What the second pass did not rerun

- The tests with no reader and with the reader who favors English-looking strings were not rerun because those programs need a copy of a book that the workspace of the chatbot did not hold.
- The tests with forced letters were not rerun.
- The bonus for closeness in the story and the bonus for words that are not repeats were not rerun which means those results still rest on two starting points each.

## What stays unproven

- No person has rerun either pass which means every number on this page is still unconfirmed by a human.
- The second pass used the same engine programs as the first pass so a mistake inside an engine program would affect both passes.

## A change to the command list after the runs

The list of 10000 commands was changed on 12 November 2026 after every run on this page because four words about highly vulnerable people ("baby" and "child" and "children" and "kids") were swapped for "farmer" and "baker" and "farmers" and "bakers" under rule 54 of the rules page in the Bible quote builder folder. A fresh run with the same starting point can therefore give different numbers from the numbers on this page.

## How to check this page

The program files sit in the folder boring-things/research-program-files/word-evolution-scripts in this repository and need the program Node.js.

- The command "node closeness_rerun.js" reruns test 1 and takes about two minutes.
- The command "node many_commands_story_order.js A 21" reruns the first starting point of test 2 and takes about eleven minutes. The numbers 22 and 23 and 24 rerun the other three starting points.

## Who made this page

An AI chatbot (Claude) ran the tests and wrote this page.

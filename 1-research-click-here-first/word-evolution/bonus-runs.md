# Twenty runs that measure the two bonuses in the word evolution experiment

November 12 2026

## What this page is

The page named experiments.md in this folder describes a "reader" which is a scoring program that picks which copied strings survive. The reader on this page scores one long string by the number of different complete commands inside the string. The page named experiments.md tested two extra bonuses and warned that each bonus was tested on only two starting points which means the sizes of the effects were uncertain.

This page reports twenty new runs by an AI chatbot (Claude) on 12 November 2026 that measure both bonuses with five starting points each. A starting point is the number that sets the string of random choices a program makes which means a new starting point gives a fresh run of the same experiment.

## The four settings

- The plain setting uses no bonus.
- The story setting adds a bonus for commands that sit close together in a story of one day. The story sorts all 10000 commands into eleven scenes that run from waking up to closing the house for the night.
- The fresh-words setting adds a bonus for every different word inside the complete commands which means a string that says "cup" three times earns less than a string with three different thing words.
- The both setting turns on the story bonus and the fresh-words bonus together.

Every setting ran on the same five starting points (numbers 31 to 35) for 900000 pastes which is 1500 minutes of experiment time. Using the same five starting points for every setting lets each bonus run be compared with the plain run that began from the same random choices.

## Finding 1: the story bonus pulls commands into fewer scenes and costs commands

- The best string covered 6.2 scenes on average in the plain setting and 2.4 scenes on average with the story bonus.
- The count of scenes fell in all five starting points (by 4 and 5 and 2 and 4 and 4 scenes).
- The best string held 11.6 commands on average in the plain setting and 7.8 commands on average with the story bonus.
- The count of commands fell in all five starting points (by 3 and 7 and 2 and 2 and 5 commands).

A fall in all five starting points would happen by luck about 3 times in 100 if the story bonus did nothing because a coin lands the same way five times in a row about 3 times in 100. Finding 1 agrees with the earlier page which reported fewer scenes and fewer commands from two starting points.

## Finding 2: the fresh-words bonus cuts repeats and leaves the count of commands about the same

- The share of words inside the commands that were not repeats was 64 percent in the plain setting and 73 percent with the fresh-words bonus.
- The share rose in all five starting points (by 13 and 3 and 12 and 6 and 12 percentage points).
- The count of commands moved both ways (down 3 and down 3 and up 3 and up 1 and no change) and the average moved from 11.6 to 11.2.

The earlier page said the effect of the fresh-words bonus on the count of commands was unknown because the two earlier starting points moved in opposite directions. Here is a guess from the five new starting points: the fresh-words bonus could have little or no effect on the count of commands because the five changes add up to almost zero.

The rise in the share of words that are not repeats was smaller here than the largest rise on the earlier page (64 percent to 92 percent in one starting point). The five new starting points gave rises between 3 and 13 percentage points which suggests the 92 percent run was an unusually strong run.

## Finding 3: the story bonus cancels most of the fresh-words bonus when both are on

- With both bonuses on the best string covered 2.6 scenes on average which is close to the 2.4 scenes of the story bonus alone.
- With both bonuses on the share of words that are not repeats was 66 percent which is close to the 64 percent of the plain setting and below the 73 percent of the fresh-words bonus alone.
- The change in the share against the plain setting moved both ways (up 7 and up 8 and down 5 and up 1 and no change).
- The count of commands fell to 7.4 on average which is close to the 7.8 of the story bonus alone.

Finding 3 agrees with the guess on the earlier page that the two bonuses pull in opposite directions because commands that sit side by side in the story share most of their words.

## A side result about story order

Sorting the picked commands into story order cut the number of scene changes or left the number the same in all twenty runs. A scene change means a jump from one scene to a different scene between neighboring commands. In the plain setting the scene changes went from 11 to 6 and from 9 to 6 and from 6 to 3 and from 6 to 5 and from 9 to 6.

## All twenty runs

Each line gives the count of commands in the best string and then the count of scenes and then the share of words that are not repeats.

- Plain starting point 31: 14 commands and 7 scenes and 60 percent.
- Plain starting point 32: 13 commands and 7 scenes and 67 percent.
- Plain starting point 33: 8 commands and 4 scenes and 67 percent.
- Plain starting point 34: 12 commands and 6 scenes and 61 percent.
- Plain starting point 35: 11 commands and 7 scenes and 67 percent.
- Story starting point 31: 11 commands and 3 scenes and 45 percent.
- Story starting point 32: 6 commands and 2 scenes and 72 percent.
- Story starting point 33: 6 commands and 2 scenes and 67 percent.
- Story starting point 34: 10 commands and 2 scenes and 50 percent.
- Story starting point 35: 6 commands and 3 scenes and 78 percent.
- Fresh-words starting point 31: 11 commands and 5 scenes and 73 percent.
- Fresh-words starting point 32: 10 commands and 5 scenes and 70 percent.
- Fresh-words starting point 33: 11 commands and 5 scenes and 79 percent.
- Fresh-words starting point 34: 13 commands and 5 scenes and 67 percent.
- Fresh-words starting point 35: 11 commands and 7 scenes and 79 percent.
- Both starting point 31: 8 commands and 3 scenes and 67 percent.
- Both starting point 32: 4 commands and 2 scenes and 75 percent.
- Both starting point 33: 7 commands and 2 scenes and 62 percent.
- Both starting point 34: 7 commands and 2 scenes and 62 percent.
- Both starting point 35: 11 commands and 4 scenes and 67 percent.

## What stays unproven

- Five starting points per setting is still a small number which means the averages could shift with more runs.
- Every run used the list of 10000 commands as changed on 12 November 2026 (four words about highly vulnerable people were swapped out) so the plain runs on this page are not exact repeats of the runs on the earlier page.
- The strength of each bonus was left at the earlier values (the fresh-words bonus at 0.4) and other strengths could give other results.
- No person has rerun the twenty runs which means every number on this page is a single unconfirmed analysis by one AI chatbot.

## How to check this page

The program files sit in the folder boring-things/research-program-files/word-evolution-scripts in this repository and need the program Node.js and Python.

- The command "bash bonus_runs.sh" starts all twenty runs four at a time and took about one hour on a machine with two processor cores.
- The command "python3 bonus_runs_read.py" reads the twenty result files and prints every number on this page.

## Who made this page

An AI chatbot (Claude) ran the tests and wrote this page.

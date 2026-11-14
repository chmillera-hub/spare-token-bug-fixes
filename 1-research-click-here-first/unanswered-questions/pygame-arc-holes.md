# Why the same thick pygame arc can look different in a new project

## Link to the original question

https://discuss.python.org/t/101403

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 with pygame 2.6.1 and pygame-ce 2.5.8 without a screen and no other person has rerun the test yet which means the page is unconfirmed. The picture and the code of the asker were not readable so the answer is one possibility that fits the report.

## The question

On 6 August 2025 somebody asked on the Python help forum why a curly bracket drawn with pygame line and arc calls with thick lines looks correct in an old PyCharm project and looks different after copying the same code into a new project.
The asker wondered about an accidental setting change or an installed package.
The post had zero replies when the forum list was read on 12 November 2026.

## What the test shows

Two separate Python environments drew the same arc (6 pixels thick from 20 to 250 degrees inside a 200 by 200 box).

- The package named pygame (version 2.6.1) left 70 white holes inside the band of the arc.
- The package named pygame-ce (version 2.5.8) left 0 white holes inside the band of the arc.
- The two pictures sit in this folder under the names arc-pygame.png and arc-pygame-ce.png.

Both packages are imported with the same line (import pygame) so the same code can run on either package without any visible sign in the code.

## Best-guess answer

One possibility that fits the report is that the two PyCharm projects use different Python environments with different pygame packages or versions because every PyCharm project normally gets its own environment with its own installed packages.
A check worth running in both projects is the line print(pygame.version.ver, getattr(pygame, "IS_CE", False)) because the output shows the version and whether the community edition is installed.
Installing the same package and version in the new project as in the old project (through the package settings of the project) is the step that could bring the old look back.

The test file named arc_test.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.

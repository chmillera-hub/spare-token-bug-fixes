# Program files behind the research pages

This folder holds only program files and a researcher can rerun the tests with these files while a casual visitor can skip this folder.

- The folder voynich-scripts holds four Python files that compute the "next page" scores for the Voynich manuscript and the scripts expect the typed copies named ZL3b-n.txt and IT2a-n.txt and RF1b-e.txt from the site voynich.nu inside a folder named data.
- The folder page-splitting-scripts holds one Python file that deals a public-domain biology book (Project Gutenberg book number 2009) into four piles and computes the confusion scores.
- The folder word-evolution-scripts holds the copy-and-paste evolution programs and the builder for the 10000 commands and the file live_page.html which is the live slider page.
- The file many_commands_story_order.js in word-evolution-scripts runs with the command "node many_commands_story_order.js A 7" and the setting BONUS=1 in front of the command turns on the bonus for closeness in the story and the setting UNIQ=0.4 turns on the bonus for words that are not repeats.
- The folder mobius-strip-calculations holds the Python files behind the document named The Mobius Strip Picture of Physics.

# Three Bible selections fed to the same word evolution experiment

This page compares what ten copying agents build when the agents draw words and quotes from three different selections of the World English Bible which is a modern English translation that anyone may copy freely.
An AI model (Claude) ran the test on 11 November 2026 and no other person has rerun the test yet which means every number here is a single unconfirmed analysis.

## How the experiment works

- Every quote is a piece of 3 words or more and at most 44 letters cut from the chosen text which means some quotes are parts of sentences.
- Ten separate agents each start from one random word and every paste copies a string with a chance of adding or swapping or changing one whole word and no deleting.
- The added words are drawn from the same selection and common words are drawn more often because the draw follows how often each word appears.
- A reader favors strings that hold more different complete quotes and a longer quote earns more credit and a half-finished quote earns partial credit.
- Earlier versions of the experiment changed one letter at a time and the letter version became too slow for large quote lists (about 100 to 500 pastes per second) while the word version ran about 600000 to 1000000 pastes per second on the same machine.

## The three selections

- Claude selection: 1837 quotes from 41 well-known passages of about 10000 words such as Genesis 1 and Psalm 23 and the Sermon on the Mount and the love chapter in First Corinthians.
- Charles selection: 38236 quotes from ten whole books which are Psalms and Proverbs and Ecclesiastes and Isaiah and Jeremiah and Matthew and Mark and Luke and John and Romans.
- Words of Jesus: 6198 quotes cut only from the words that red-letter Bibles print in red (about 38500 words) in Matthew and Mark and Luke and John.
- An earlier run used thirteen books for the Charles selection and included the words of Jesus from Acts and Revelation and Charles asked for Genesis and Galatians and Hebrews and those two extra sources to be removed.

## What the agents built after 2000 minutes of experiment time

Claude selection (about 10 quotes per agent):

- One agent: "i will deliver him / and you know me / and your father / before him all the / for i was hungry / with all your strength / when he saw him / heaven and in your sight / and love remain / and be thankful"
- Another agent: "and with all your might / and we are his / like a father has / and know my heart / and be exceedingly glad / yourselves on the earth / for i was hungry / for it is written / and be thankful / and he in god / out of heaven saying"

Charles selection (about 13 quotes per agent):

- One agent: "and dont sin / you righteous people / that i may live / upward for the wise / things to your heart / and will have / and there they will be / with his brothers / so he will come / but those who were / all of the disciples / you wont believe / not to the flesh"
- Another agent: "he is yahweh / and all the righteous / the heart of the wise / should eat and drink / are in the earth / like the wilderness / and will rejoice / themselves in him / to the sword / take away therefore / and you shall have them / for the works which the"

Words of Jesus (about 11 quotes per agent):

- One agent: "when you pray / as in heaven / but sinners to repentance / word of the kingdom / but know this / and not perceive / given to god / and to return / distress in the land / but you dont believe / but because of the multitude / and you in me / of the synagogues"
- Another agent: "which of you / and to the nations / and the birds / and you shall have them / for from now on / resurrection of the righteous / and will tell him / the father himself / this is the will of / and are life / you know him / you will live also / and i in you"

## Differences that can be counted

- The most used content words for the words of Jesus were "father" and "life" and "believe" and "go" and "know" and "world".
- The most used content words for the Charles selection were "disciples" and "yahweh" and "come" and "righteousness" and "father" and "righteous".
- The most used content words for the Claude selection were "earth" and "heaven" and "father" and "know" and "sight" and "love".
- The words "will" and "shall" made up 5 percent of the built quotes for the Charles selection and 4 percent for the words of Jesus and 2 percent for the Claude selection.
- The words "you" and "your" made up 9 percent of the built quotes for the Claude selection and 8 percent for the words of Jesus and 6 percent for the Charles selection.
- A warning about the "you" count: the share for the words of Jesus was 11 percent in the earlier run and 8 percent after two small sources were removed which means a gap of 3 points is within the run-to-run noise of this test.

## Limits

- The agents mostly built short common quotes because a short quote made of common words needs fewer lucky draws which means rare and famous lines seldom appear.
- The counts come from the best string of each of ten agents in one run per selection which is a small sample.
- A word such as "energy" for the feel of a text cannot be measured by this test and the counts above only describe which words appear.
- The reader counts quotes and has no sense of meaning which means the built strings are stacks of separate quotes and not flowing passages.

## Try the program

- Open this address in a web browser to run the program with a button for each of the three selections: https://htmlpreview.github.io/?https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/1-research-click-here-first/bible-word-evolution-live-program.html
- The address above depends on a free outside service named htmlpreview and nobody has tested the address yet which means the address might fail.
- The second way is to download the program file from this address and open the downloaded file in any web browser: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/1-research-click-here-first/bible-word-evolution-live-program.html

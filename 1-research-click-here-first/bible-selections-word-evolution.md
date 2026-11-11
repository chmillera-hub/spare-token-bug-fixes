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

## The same strings with connecting words added by hand

The AI model (Claude) took six of the strings above and added only connecting words such as "because" and "while" and "so" between the quotes and added no new nouns and no new action words which means every added word is marked with stars and every quote stays in the order the agents produced.
The added words are choices made by the AI model and are not part of the Bible text.

Claude selection:

- i will deliver him and you know me and your father *because* before him all the *while* for i was hungry *yet* with all your strength *then* when he saw him *in* heaven and in your sight and love remain and be thankful
- and with all your might and we are his *just* like a father has and know my heart and be exceedingly glad *among* yourselves on the earth for i was hungry *and* for it is written and be thankful and he in god *as if* out of heaven saying

Charles selection:

- and dont sin you righteous people *so* that i may live upward for the wise *with* things to your heart and will have and there they will be with his brothers so he will come but those who were *with* all of the disciples *whom* you wont believe *but* not to the flesh
- he is yahweh and all the righteous *with* the heart of the wise should eat and drink *while* are in the earth like the wilderness and will rejoice themselves in him *until* to the sword take away therefore and you shall have them for the works which the

Words of Jesus:

- when you pray as in heaven but sinners to repentance *by the* word of the kingdom but know this and not perceive *whatever* given to god and to return *from* distress in the land but you dont believe but because of the multitude and you in me *out* of the synagogues
- which of you and to the nations and the birds and you shall have them for from now on *the* resurrection of the righteous and will tell him *that* the father himself *and* this is the will of *him* and are life *so if* you know him you will live also and i in you

What the connecting words changed:

- Connecting words made short stretches read like speech where two neighboring quotes happened to fit such as "so if you know him you will live also and i in you".
- Connecting words could not repair a quote that was cut in the middle of a sentence such as "for the works which the" because the missing part is a noun or an action word and the rule allowed no new nouns or action words.
- Each string needed only 4 to 6 added words because most quotes already begin with a connecting word such as "and" or "but" or "for".

## A second pass that also allows reference words already used in the string

Charles then widened the rule so that the AI model could add connecting words plus reference words such as "you" or "he" or "him" or "this" as long as the exact reference word already appears somewhere in the same string which means no new person or thing enters the string.

Claude selection:

- i will deliver him and you know me and your father *and i* before him all the *while* for i was hungry *yet you* with all your strength *then* when he saw him *from* heaven and in your sight *so you* and love remain and be thankful
- and with all your might and we are his *just* like a father has *his* and know my heart and be exceedingly glad *among* yourselves on the earth for i was hungry *and* for it is written *for yourselves* and be thankful and he in god *as if* out of heaven saying

Charles selection:

- and dont sin you righteous people *so* that i may live upward for the wise *with* things to your heart and will have *those* and there they will be with his brothers so he will come but those who were *with* all of the disciples *whom* you wont believe *for they* not to the flesh
- he is yahweh and all the righteous *with* the heart of the wise should eat and drink *while you* are in the earth like the wilderness and will rejoice themselves in him *until he* to the sword take away therefore and you shall have them for the works which the

Words of Jesus:

- when you pray as in heaven but sinners to repentance *by the* word of the kingdom but know this and not perceive *this* given to god and to return *you from* distress in the land but you dont believe but because of the multitude and you in me *out* of the synagogues
- which of you and to the nations and the birds and you shall have them for from now on *the* resurrection of the righteous and will tell him *that* the father himself *and* this is the will of *him* and are life *so if* you know him you will live also and i in you

What the reference words changed:

- A reference word helped most where a quote was missing the one who acts such as "while you are in the earth like the wilderness" and "to return you from distress in the land".
- A reference word could not supply a missing action word which means stretches such as "until he to the sword" still lack the word that says what he does.
- The second string from the words of Jesus did not change because the first pass had already used the reference word "him" that appears in the string.

## Two more runs with new random starting points

The AI model reran all three selections twice more with different random starting points to see which differences repeat.

Claude selection in the second run:

- "god made the expanse / on the earth / your male servant / you his saints / know that yahweh / you are there / and know my heart / your father who is in heaven / your heavenly father / and you visited me / who is my neighbor"
- "in the beginning / fill the earth / which is on the surface / listen to me / made in the earth / he said to him / and in your sight / heaven and in your sight / and your father has / for god is love"

Charles selection in the second run:

- "among the nations / by your name / for your loving kindness is good / and that which is / for all this / god is my salvation / and not spirit / no one answered / against all the / and there they will be / and against judah / which of you / into all the earth"
- "for who is god / because of your / therefore i love your / come with us / the neighbor and his / and not return / goodness of yahweh / and tell him / and it will be / he was troubled / as they went out / jesus came out / you from the father / righteousness through the"

Words of Jesus in the second run:

- "when you pray / he said to them / until you say / or in prison / and the last first / the lord is one / and i in him / for which of those / and go to the father / that you sent me"
- "judgment than for you / and not understand / that is to say / these will receive / and be killed / but when it is evil / and you will be blessed / and will tell him / why are you troubled / the hour comes / you dont believe me / for which of those / remain in me"

What repeated across all three runs:

- The word "earth" was the most used content word for the Claude selection in all three runs and "heaven" was in the top three in all three runs.
- The word "father" was the most used content word for the words of Jesus in all three runs and "know" or "believe" or "receive" appeared near the top each time.
- The words "yahweh" and "righteousness" appeared near the top for the Charles selection in all three runs while the rest of the top words changed from run to run which fits a much larger and more varied source.
- The exact quotes changed almost completely from run to run which means a single run shows one draw out of many possible draws.

## Limits

- The agents mostly built short common quotes because a short quote made of common words needs fewer lucky draws which means rare and famous lines seldom appear.
- The counts come from the best string of each of ten agents in one run per selection which is a small sample.
- A word such as "energy" for the feel of a text cannot be measured by this test and the counts above only describe which words appear.
- The reader counts quotes and has no sense of meaning which means the built strings are stacks of separate quotes and not flowing passages.

## Try the program

- Open this address in a web browser to run the program with a button for each of the three selections: https://htmlpreview.github.io/?https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/1-research-click-here-first/bible-word-evolution-live-program.html
- The address above depends on a free outside service named htmlpreview and nobody has tested the address yet which means the address might fail.
- The second way is to download the program file from this address and open the downloaded file in any web browser: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/1-research-click-here-first/bible-word-evolution-live-program.html

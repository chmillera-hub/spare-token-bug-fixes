# Agents that rebuild the Bible out of chopped key phrases

This page reports an experiment where a program chopped parts of the World English Bible into short key phrases and ten copying agents then tried to put pieces of the text back together.
An AI model (Claude) ran the test on 11 November 2026 and no other person has rerun the test yet which means every result here is a single unconfirmed analysis.

## How the text was chopped

- A key phrase is a short piece of about four words such as "i shall lack nothing" or "in green pastures".
- A program cut the text at punctuation marks and before linking words such as "and" and "for" and "in" and joined any one-word piece to a neighbor because one word alone rarely makes sense.
- Psalm 23 came out as "yahweh is my shepherd / i shall lack nothing / he makes me lie down / in green pastures / he leads me beside still waters / he restores my soul / he guides me / in the paths of righteousness / for his names sake".
- The cutting is done by simple rules and not by understanding which means some pieces are awkward such as "for you are" followed by "with me".

## The three selections

- Claude selection: 2342 different key phrases from 41 well-known passages.
- Charles selection: 43694 different key phrases from ten whole books which are Psalms and Proverbs and Ecclesiastes and Isaiah and Jeremiah and Matthew and Mark and Luke and John and Romans.
- Words of Jesus: 7463 different key phrases from the words that red-letter Bibles print in red in Matthew and Mark and Luke and John.

## How the experiment works

- Ten separate agents each start from one random key phrase and every paste copies a string with a chance of adding or swapping or changing one whole key phrase and no deleting.
- A reader gives one point for every pair of neighboring phrases in a string that are also neighbors in the Bible and a small credit for neighbors from the same chapter.
- A string may hold at most 24 key phrases.

## What the agents rebuilt after 1000 minutes of experiment time

Claude selection (about 23 of 24 phrases per agent sat inside a rebuilt stretch):

- [Genesis 1] god called the light day and the darkness he called night there was evening and there was morning
- [Psalm 27] in yahwehs house all the days of my life to see yahwehs beauty and to inquire
- [Matthew 6] but when you do merciful deeds dont let your left hand know what your right hand does so that your merciful deeds may be in secret
- [Matthew 6] neither do they spin yet i tell you that even solomon in all his glory was not dressed like one of these
- [John 15] i command these things to you that you may love one another

Charles selection (about 18 of 24 phrases per agent sat inside a rebuilt stretch):

- [Psalm 10] and the fatherless break the arm of the wicked
- [Jeremiah 29] when you search for me
- [Mark 5] he said to her daughter cheer up
- [Luke 5] i have not come to call the righteous
- [Luke 12] how god clothes the grass in the field
- [Isaiah 33] but there yahweh will be with us jesus said to him you shall love the lord your god

Words of Jesus (about 22 of 24 phrases per agent sat inside a rebuilt stretch):

- [Matthew 5] before you you are the salt of the earth
- [Matthew 25] good and faithful servant you have been faithful
- [Luke 12] that i have come to give peace in the earth
- [John 17] and they have believed that you sent me i made known to them your name
- [John 17] which you have given me that they may be one
- [Matthew 5] the lord your vows but i tell you love your enemies

## What the experiment showed

- Whole phrases made the output far more readable than whole words or single letters because every unit already makes some sense alone and the agents only had to find the right neighbors.
- The longest rebuilt stretch in every selection was 6 key phrases in a row which is about 25 words.
- Some rebuilt stretches jump between two places in the Bible at a phrase that occurs in both places such as "i tell you" or "jesus said to him" which produced blends such as "the lord your vows but i tell you love your enemies" and "but there yahweh will be with us jesus said to him you shall love the lord your god".
- The jumps happen because the reader checks one pair of neighbors at a time and a common phrase has many true neighbors.
- The large Charles selection rebuilt less (18 phrases against 22 or 23) because the chance that a random phrase is the true neighbor of another phrase falls as the list grows.
- The key phrase version ran about 2400000 to 2900000 pastes per second on the test machine which is faster than the word version.

## One agent per selection from a second run with generic words added by hand

The AI model ran the key phrase experiment a second time and took the whole best string of one agent per selection and joined the rebuilt stretches with only the most generic words which means connecting words and reference words such as "those" and "him" and pointing words such as "here" and "over there" and no new action words or thing words.
Every added word is marked with stars and the stretches stay in the order of the Bible.

Claude selection (all eleven stretches came from Matthew 5):

- for they shall inherit the earth blessed are those *here* for great is your reward in heaven *and those* who are in the house *with him* who is in heaven for that is how *and so* to the ancient ones you shall not make false vows but i tell you dont swear *at him* who is angry with his brother while you are with him on the way *there so* pluck it out and throw it away for it is more profitable for you *than those others* if anyone sues you to take away your coat

Charles selection (stretches from Psalm 24 and Psalm 89 and Proverbs 8 and Isaiah 52 and Matthew 9 and Matthew 12):

- and those who were before you in that day says yahweh of armies yahweh says *to them* before your face who will prepare your way before you most certainly i tell you *this* by the way for the sword of the enemy *over there and* from there says yahweh with the sword *to those others* and sinners jesus answered them i told you *so when* they asked him what then are you elijah he said *that to them*

Words of Jesus (stretches from Matthew 5 and 6 and 11 and 17 and 25):

- for they shall inherit the earth blessed are those who have been persecuted *here* before you most certainly i tell you if you have faith with him then he will sit on the throne of his glory *and those* who hate you bless those *others* on the earth i wish it were already kindled *there* in the marketplaces *and not* the best seats in the synagogues *for those* with you how long will i bear with you for everyone *here* and traded with them i tell you and much more *than that*

What the joined key phrase strings show:

- Each string needed only 6 to 8 added word groups to read as one passage because each rebuilt stretch is already several words of real Bible text.
- The joined key phrase strings read far more like a sermon than the joined word strings did because whole stretches such as "blessed are those who have been persecuted" arrive intact.
- The meaning of each joined string is new and belongs to no Bible passage because the stretches come from different verses and the added words are choices made by the AI model.

## The same three strings with the stretches rearranged into the most sensible order

Charles then allowed the AI model to drop the chapter labels and to put the rebuilt stretches in any order and to add the same generic words as before (connecting words and reference words and pointing words) with the goal of the most sensible sounding passage.
The words inside each stretch stay in Bible order and every added word is marked with stars.

Claude selection:

- *to those* who are in the house *and to him* who is angry with his brother while you are with him on the way *and* to the ancient ones you shall not make false vows but i tell you dont swear *and* if anyone sues you to take away your coat pluck it out and throw it away for it is more profitable for you for great is your reward in heaven *with him* who is in heaven for that is how *those before you* for they shall inherit the earth blessed are those

Charles selection:

- they asked him what then are you elijah he said *to them* and sinners jesus answered them i told you *of him* before your face who will prepare your way before you most certainly i tell you *that he* and those who were before you in that day says yahweh of armies yahweh says *this* from there says yahweh with the sword *so not* by the way for the sword of the enemy

Words of Jesus:

- with you how long will i bear with you for everyone *there* in the marketplaces the best seats in the synagogues and traded with them i tell you and much more *yet those* who hate you bless those *others* for they shall inherit the earth blessed are those who have been persecuted *here* before you most certainly i tell you if you have faith with him then he will sit on the throne of his glory *over all those* on the earth i wish it were already kindled

What rearranging changed:

- Free order let each string open with a scene and close with a blessing or a wish which the Bible order could not do because Bible order is fixed by chapter number.
- The Charles selection gained the most because the six stretches became one exchange (a question and an answer and a promise and a warning) where Bible order had scattered the speakers.
- Every added word in the three strings is a connecting word or a reference word or a pointing word which means no new action word or thing word entered any string.

## Five versions of one words of Jesus string graded against the writing rules in this folder

The AI model took the eight rebuilt stretches of the words of Jesus string above and made five versions and graded each version against the seven sentence rules in the page named writing-rules-for-clear-chatbot-replies in this folder.
Each rule earns 0 or 1 or 2 points which gives a top score of 14 and the grades are the judgment of the AI model and no second reader checked the grades.
The seven rules are: a sentence can be understood alone and a reason is attached to each claim and labels are explained and people and things are named in place of pointing words and no short clipped sentences and one claim plus reason per sentence and no commas.

Version 1 (Bible order and nothing added) scored 6 of 14:

- for they shall inherit the earth blessed are those who have been persecuted before you most certainly i tell you if you have faith with him then he will sit on the throne of his glory who hate you bless those on the earth i wish it were already kindled in the marketplaces the best seats in the synagogues with you how long will i bear with you for everyone and traded with them i tell you and much more
- The version lost points because the whole text is one run-on sentence that stacks about eight claims and names nobody.

Version 2 (Bible order with generic joining words) scored 6 of 14:

- for they shall inherit the earth blessed are those who have been persecuted *here* before you most certainly i tell you if you have faith with him then he will sit on the throne of his glory *and those* who hate you bless those *others* on the earth i wish it were already kindled *there* in the marketplaces *and not* the best seats in the synagogues *for those* with you how long will i bear with you for everyone *here* and traded with them i tell you and much more *than that*
- The joining words made the text flow better and the score did not move because none of the seven rules measures flow and the text is still one run-on sentence.

Version 3 (Bible order cut into sentences) scored 7 of 14:

- for they shall inherit the earth blessed are those who have been persecuted *here* before you. most certainly i tell you if you have faith with him then he will sit on the throne of his glory. *and those* who hate you bless those *others* on the earth. i wish it were already kindled *there* in the marketplaces *and in* the best seats in the synagogues. with you how long will i bear with you for everyone *here* and traded with them. i tell you and much more *than that*.
- Sentence breaks raised the score for one claim per sentence and the last sentence became short and clipped which cost a point.

Version 4 (rearranged so that each sentence pairs a claim with a reason) scored 10 of 14:

- with you how long will i bear with you for everyone *there* in the marketplaces *and in* the best seats in the synagogues *because those* and traded with them i tell you and much more. *those* who hate you bless those *others* for they shall inherit the earth blessed are those who have been persecuted *here* before you. most certainly i tell you if you have faith with him then he will sit on the throne of his glory *over all those*. on the earth i wish it were already kindled *for all of those here*.
- Rearranging let every sentence carry a claim and a reason joined by "because" or "for" or "if" and removed the clipped sentence.

Version 5 (reference words tied to a group named in the same sentence) scored 11 of 14:

- with you how long will i bear with you for everyone *there* in the marketplaces *and in* the best seats in the synagogues *because those same ones* and traded with them i tell you and much more. *those* who hate you bless those *same ones* for they shall inherit the earth blessed are those who have been persecuted *here* before you. most certainly i tell you if you have faith with him then he will sit on the throne of his glory *over everyone*. on the earth i wish it were already kindled *because of all of you here*.
- Tying "those same ones" to "everyone in the marketplaces" and to "those who hate you" earned one point for naming.

Why the score stops at 11:

- The rule about naming people and things asks for names in place of pointing words while the joining rule from Charles allows only pointing words and other generic words which means the two rules pull against each other.
- The words "him" and "he" and "it" in the stretches point at someone or something the stretches never name and no generic word can supply the name.
- The label "throne of his glory" stays unexplained because an explanation would need new thing words.

## One finished passage per selection made the same way as version 5

The AI model took the best string of a second agent from each selection and went straight to the method of version 5 which means free order and sentence breaks and a claim with a reason in each sentence and generic words only.
Every added word is marked with stars and the grades use the same seven rules with a top score of 14.

Claude selection (10 of 14) from the stretches "on the earth there was evening" and "herbs yielding seed after their kind and it was so god saw everything" and "who mourn for they shall be comforted" and "and be exceedingly glad for great is your reward in heaven" and "who were before you you are the salt of the earth" and "who is in secret" and "at a woman to lust after her has committed adultery" and "yes and your no be no" and "who is evil but whoever strikes you" and "you shall love your neighbor and hate your enemy":

- on the earth there was evening *and* herbs yielding seed after their kind and it was so god saw everything. *those* who mourn for they shall be comforted *here* and be exceedingly glad for great is your reward in heaven. *those* who were before you you are the salt of the earth *for him* who is in secret. *anyone here* at a woman to lust after her has committed adultery *so* yes and your no be no. *as for him* who is evil but whoever strikes you *then* you shall love your neighbor and hate your enemy *no longer*.

Charles selection (9 of 14) from the stretches "in heart if the foundations are destroyed" and "i have set yahweh always before me whose sandal strap im" and "who rose up against me and by" and "in labor they will look on him" and "who has had boldness to approach me says yahweh shouldnt my soul be avenged" and "neither has he gone into captivity" and "the kingdom of heaven is at hand":

- i have set yahweh always before me whose sandal strap im *under because* the kingdom of heaven is at hand. *even* in heart if the foundations are destroyed neither has he gone into captivity *with those* who rose up against me and by *them*. in labor they will look on him who has had boldness to approach me says yahweh *for* shouldnt my soul be avenged.

Words of Jesus (10 of 14) from the stretches "they persecuted the prophets who were" and "and whoever says you fool will be" and "and not sacrifice for i came not" and "on an old garment for the patch would tear away" and "women there has not arisen anyone greater than john the baptizer" and "for you to enter into gods kingdom before you most certainly i tell you i havent found" and "even the chosen ones behold i have told you beforehand" and "and prepare a place for you":

- they persecuted the prophets who were *before you and* even the chosen ones behold i have told you beforehand. women there has not arisen anyone greater than john the baptizer *yet* for you to enter into gods kingdom before you most certainly i tell you i havent found *anyone here*. *for all of you* and not sacrifice for i came not on an old garment for the patch would tear away. *here with you* and prepare a place for you *yet* and whoever says you fool will be *apart from all of you*.

Notes on the three passages:

- The Claude selection passage scored 10 because five sentences each carry a claim and a reason while "him who is in secret" and "him who is evil" name nobody.
- The words "no longer" were added to the stretch "you shall love your neighbor and hate your enemy" because the stretch quotes an old saying that the speaker in Matthew 5 goes on to reject and the two generic words keep the passage from teaching hatred of an enemy.
- The Charles selection passage scored 9 because the stretches came from six different books and three of the stretches were cut in the middle of a thought such as "whose sandal strap im" and "who rose up against me and by".
- The line "shouldnt my soul be avenged" is a question spoken by yahweh in the book of Jeremiah and the passage keeps the line as a question and does not present harm to any person as good.
- The words of Jesus passage scored 10 because each sentence pairs a claim with "yet" or "for" while "for all of you and not sacrifice" lacks the thing that is wanted in place of sacrifice which is the word "mercy" in the source.

## The same passages after Charles allowed naming words that already appear in the string

Charles widened the joining rule so that the AI model could also add a naming word such as "the earth" or "god" or "the synagogues" as long as that naming word already appears somewhere in the same string which means no person or thing from outside the string enters the passage.
Every added word is marked with stars and the grades use the same seven rules with a top score of 14.

Version 6 of the words of Jesus string from the five-version section (12 of 14 and up from 11):

- with you how long will i bear with you for everyone *there* in the marketplaces *and in* the best seats in the synagogues *because those in the synagogues* and traded with them i tell you and much more. *those* who hate you bless those *in the marketplaces* for they shall inherit the earth blessed are those who have been persecuted *on the earth* before you. most certainly i tell you if you have faith with him then he will sit on the throne of his glory *over the earth*. on the earth i wish it were already kindled *this faith in all of you here*.

Claude selection (12 of 14 and up from 10):

- on the earth there was evening *and* herbs yielding seed after their kind and it was so god saw everything. *those* who mourn for they shall be comforted *on the earth* and be exceedingly glad for great is your reward in heaven. *those* who were before you you are the salt of the earth *for god* who is in secret. *anyone* at a woman to lust after her has committed adultery *so* yes and your no be no *before god*. *as for the enemy* who is evil but whoever strikes you *then* you shall love your neighbor and hate your enemy *no longer*.

Charles selection (10 of 14 and up from 9):

- i have set yahweh always before me whose sandal strap im *under because* the kingdom of heaven is at hand. *even* in heart if the foundations *of the kingdom* are destroyed neither has he gone into captivity *with those* who rose up against me and by *their boldness against yahweh*. in labor they will look on him who has had boldness to approach me says yahweh *for* shouldnt my soul be avenged.

Words of Jesus (12 of 14 and up from 10):

- they persecuted the prophets who were *before you and* even the chosen ones behold i have told you beforehand. *among* women there has not arisen anyone greater than john the baptizer *yet* for you to enter into gods kingdom before you most certainly i tell you i havent found *a place*. *a place for the chosen ones* and not sacrifice for i came not on an old garment for the patch would tear away *the garment*. *in gods kingdom* and prepare a place for you *yet* and whoever says you fool will be *apart from gods kingdom*.

What the naming words changed:

- Reused naming words lifted every score by 1 or 2 points because phrases such as "god who is in secret" and "the enemy who is evil" and "apart from gods kingdom" now say who or what a sentence is about.
- The Charles selection gained the least because the seven stretches share few naming words and the words "he" and "him" inside the stretches still point at people the stretches never name.
- Reused naming words also let the AI model steer meaning more strongly than generic words could (for example "this faith in all of you here" decides what "it" refers to) which means the passages now carry more of the choices of the AI model and less of the chance output of the agents.

## Limits

- The reader rewards text that matches the Bible and has no sense of meaning which means the agents rebuild the source and do not write anything new.
- One run per selection with ten agents is a small sample.
- The rule-based cutting sometimes splits a thought in an odd place.

## Try the program

- Open this address in a web browser to run the program with a button for each of the three selections: https://htmlpreview.github.io/?https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/1-research-click-here-first/bible-key-phrase-evolution-live-program.html
- The address above depends on a free outside service named htmlpreview and nobody has tested the address yet which means the address might fail.
- The second way is to download the program file from this address and open the downloaded file in any web browser: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/1-research-click-here-first/bible-key-phrase-evolution-live-program.html

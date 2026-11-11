# Agents that rebuild the Bible out of chopped key phrases

Warning about a wording change: Charles replaces the name "yahweh" with the word "god" everywhere in the Bible programs and in the newer results as a personal reading choice that helps Charles follow the quotes which means the quotes differ from the World English Bible at every place where the World English Bible prints the name and a reader who wants the original wording can open the World English Bible itself.

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

## A special rule for the words of Jesus selection: the names of the speaker and of God may be added freely

Charles added a rule for the words of Jesus selection only: the AI model may add "the father" and "jesus" and "the christ" and "god" and "yahweh" wherever a sentence needs one of those names even when the name appears nowhere in the string.
Every added word is marked with stars and the grades use the same seven rules with a top score of 14.

First string (13 of 14 and up from 12):

- with you how long will i *jesus* bear with you for everyone *there* in the marketplaces *and in* the best seats in the synagogues *because those in the synagogues* and traded with them i tell you and much more. *those* who hate you bless those *in the marketplaces* for they shall inherit the earth blessed are those who have been persecuted *on the earth* before you. most certainly i tell you if you have faith with him *the christ* then he will sit on the throne of his glory *beside the father over the earth*. on the earth i wish it were already kindled *this faith in god in all of you here*.

Second string (13 of 14 and up from 12):

- they persecuted the prophets who were *before you and* even the chosen ones *of god* behold i *jesus* have told you beforehand. *among* women there has not arisen anyone greater than john the baptizer *yet* for you to enter into gods kingdom before you most certainly i tell you i havent found *a place apart from the father*. *the father and* not sacrifice for i *the christ* came not on an old garment for the patch would tear away *the garment*. *with the father in gods kingdom* and prepare a place for you *yet* and whoever says you fool will be *apart from god*.

What the special rule changed:

- The names closed the gap that no earlier rule could close because "i" now has the name "jesus" beside the word and "him" and "he" now have "the christ" beside the words.
- Both strings reached 13 of 14 and the one missing point comes from labels that stay unexplained such as "the throne of his glory".
- The special rule applies to one selection only which means the scores of the words of Jesus passages can no longer be compared fairly with the scores of the other two selections.
- The AI model chose which name goes with each "he" and "him" from knowledge of the source verses and a wrong choice would put words about one person onto another person.

## Special words of three kinds may fill the gaps: naming words and action words and describing words

Charles widened the joining rule again so that each selection has a list of special words that may be added in any gap even when the special word appears nowhere in the string.
The AI model counted every word in each selection and then sorted the most used words by hand into naming words and action words and describing words and kept about 12 of each kind.
Only the exact listed form of a word was used which means "made" is allowed in a selection where "made" is listed while "makes" is not allowed.
The word "seed" was added to the words of Jesus list because Charles named the word and not because the word ranks high by count and the word "love" ranks about 38th by count in the words of Jesus (44 uses).

Claude selection special words:

- Naming words: god and yahweh and love and earth and father and time and day and heaven and man and light and son and heart.
- Action words: made and give and know and tell and saw and see and keep and heard and called and seek and put and make.
- Describing words: good and evil and blessed and right and great and holy and wicked and righteous and secret and perfect and living and new.

Charles selection special words:

- Naming words: yahweh and god and man and jesus and son and people and lord and day and king and house and land and heart.
- Action words: says and know and tell and give and see and say and made and make and take and heard and hear and answered.
- Describing words: good and evil and great and wicked and righteous and holy and high and right and wise and blessed and dead and poor.

Words of Jesus special words:

- Naming words: father and man and son and god and kingdom and lord and heaven and world and house and life and day and earth and love and seed plus the names jesus and christ and yahweh from the earlier special rule.
- Action words: tell and see and know and give and sent and say and hear and take and believe and enter and receive and made.
- Describing words: good and evil and little and great and blessed and greater and dead and eternal and last and righteous and right and full.

The same four strings as the last two sections were joined again by hand with the wider rule and every added word is marked with stars.
The grades use the same seven rules with a top score of 14 and the AI model graded passages that the AI model wrote which means the grades are a rough guide and not an outside measurement.

Words of Jesus first string (14 of 14 and up from 13):

- with you how long will i *jesus* bear with you for everyone in the marketplaces *and in* the best seats in the synagogues *made the house of god a house of the world* and traded with them i tell you and much more. *the father sent love to those* who hate you *so* bless those *in the marketplaces* for they shall inherit the earth blessed are those who have been persecuted *for the kingdom* before you. most certainly i tell you if you have faith with him *the christ* then he will sit on the throne of his glory *which the father made great in heaven*. on the earth i wish it were already kindled *the good seed of love that the father sent to the world*.

Words of Jesus second string (14 of 14 and up from 13):

- they persecuted the prophets who were *sent* before you and even the chosen ones *of god* behold i *jesus* have told you beforehand. *among* women there has not arisen anyone greater than john the baptizer *yet* for you to enter into gods kingdom before you most certainly i tell you i havent found *a place apart from the father*. *the father sent the son to give love* and not sacrifice for i *the christ* came not on an old garment for the patch would tear away *the garment*. *believe so the father and the son enter the house in heaven* and prepare a place for you *yet* and whoever says you fool will be *last in the kingdom*.

Claude selection (13 of 14 and up from 12):

- on the earth there was evening *and god made* herbs yielding seed after their kind and it was so god saw everything *good*. *blessed are those* who mourn for they shall be comforted *on the earth* and be exceedingly glad for great is your reward in heaven. *the righteous* who were before you *heard* you are the salt of the earth *from the father* who is in secret. *a man who saw evil* at a woman to lust after her has committed adultery *in the heart so keep your yes* yes and your no be no *before god*. *god saw the man* who is evil but whoever strikes you *give the man love because* you shall love your neighbor and hate your enemy *no longer*.

Charles selection (12 of 14 and up from 10):

- i have set yahweh always before me *the great king* whose sandal strap im *under because* the kingdom of heaven is at hand. *the righteous man answered* in heart if the foundations *of the house* are destroyed *the wise people know the righteous man* neither has he gone into captivity *with the wicked people* who rose up against me and by *evil made the land poor*. *the people of the land* in labor they will look on him *the holy king* who has had boldness to approach me says yahweh *and the lord answered* shouldnt my soul be avenged.

What the three kinds of special words changed:

- Action words gave the largest gain because a gap can now hold a full small claim such as "the father sent love to those" where the earlier rules could only hold a pointer such as "those".
- Describing words let a passage say which kind of person a sentence is about such as "the righteous man" and "the wicked people" which is why the Charles selection gained 2 points after gaining the least under every earlier rule.
- Both words of Jesus strings reached the top score while the gain was only 1 point each because the earlier rule had already lifted both strings to 13.
- The added words now carry a large share of the meaning (for example "the father sent the son to give love" stands where the source verse has "i desire mercy") which means the passages read more like sentences written by the AI model around Bible fragments than like chance output of the agents.
- The ending "last in the kingdom" is milder than the source verse about the word "fool" and that mildness is a choice of the AI model and not a finding.
- The line "shouldnt my soul be avenged" stays a question spoken by yahweh in the book of Jeremiah and the passage does not present harm to any person as good.

What the program does with the same lists:

- The live program now lets agents place single joining words from the generic list and from the special list of the chosen selection and the reader gives credit when the word before the joining word and the word after the joining word each sit beside the joining word somewhere in the source.
- In one run of 6 million pastes per selection the agents kept mostly generic joining words such as "and" and "there" and "with them" and almost no special words because the two-sided check is easier to pass for very common words.
- The average count of phrases inside rebuilt stretches per agent was 29.4 for the Claude selection and 15.5 for the Charles selection and 21.0 for the words of Jesus.
- The joining words chosen by the program read as filler because the program checks word pairs and has no test of meaning which means the hand joining above is still far ahead of the program.

## One chapter against one chapter: John 10 and Psalm 88

Charles asked for the same process on two single chapters which means the key phrase cutting and the evolution run and the special word lists and the hand joining were all repeated on John chapter 10 and on Psalm 88 from the World English Bible.

Size of each source:

- John 10 holds 799 words that the cutting rule turned into 193 different key phrases.
- Psalm 88 holds 288 words that the cutting rule turned into 75 different key phrases.

What the agents did in a run of 3 million pastes per chapter:

- Every agent in both chapters ended with all 32 pieces inside rebuilt stretches because a single chapter has so few phrases that finding true neighbors is easy (the whole-book selections reached only about 15 to 29 of 32).
- The agents dropped every joining word in both chapters because a rebuilt phrase pair earns more credit than a joining word and a small source always offers a rebuilt pair.
- The best John 10 string held 13 short stretches and the best Psalm 88 string held 11 short stretches and the longest stretch was 6 phrases in both chapters which means the agents shuffled the chapter into short true pieces and did not rebuild the chapter in order.

Special words for John 10 with counts:

- Naming words: sheep 16 and father 11 and shepherd 6 and jesus 6 and hand 6 and voice 5 and life 5 and works 5 and door 4 and jews 4 and god 3 and demon 3.
- Action words: know 6 and believe 6 and lay 4 and answered 4 and tell 3 and listen 3 and follow 3 and hear 2 and take 2 and snatch 2.
- Describing words: good 5 and hired 3 and own and eternal and true and blind.

Special words for Psalm 88 with counts:

- Naming words: yahweh 4 and day 2 and prayer 2 and soul 2 and pit 2 and grave 2 and wrath 2 and friends 2 and wonders 2 and terrors 2 and god 1 and night 1.
- Action words: cried 2 and made 2 and cut 2 and remember and turn and enter and show and rise and praise and spread and reject and hide.
- Describing words: dead 2 and afflicted 2 and full and dim and dark and lowest and darkest and fierce and near and loving.

John 10 joined by hand from the best string of agent 1 (13 of 14) with added words marked by stars:

- *jesus answered the jews* as i told you my sheep hear my voice and i know them and they follow me i give eternal life to them. the good shepherd lays down his life for the sheep *because the sheep know the voice of the shepherd* whenever he brings out his own sheep he goes *to the door*. *the jews answered* and said to him how long will you hold us for they dont know the voice of strangers jesus spoke this parable to them but they didnt understand. jesus therefore said to them again most certainly *no one can take the sheep out* of my fathers hand i and the father are one. *so the jews take* stones again to stone him jesus answered them *for which of the good* works do you stone me the jews answered him we dont stone you *for good works*. *jesus answered* if i dont do the works of my father *do not believe* but if i do them though you dont believe me believe the works. others said these are not the sayings of one possessed *by a demon because the works are good*.

Psalm 88 joined by hand from the best string of agent 1 (12 of 14) with added words marked by stars:

- *yahweh god* i have cried in the morning *and in the night* on you daily yahweh i have spread out my hands to you *because* my prayer comes before you yahweh why do you reject my soul. i am afflicted and ready to die from my youth up while i suffer your terrors i am distracted your fierce wrath has gone over me *the afflicted soul* like the slain who lie in the grave whom you remember no more. you have laid me in the lowest pit in the darkest depths *because* your wrath lies heavily on me you have afflicted me with all your waves. your terrors have cut me off they came around me like water all day long *and the dark night cut the day* from me and my friends. *show your wonders* in the dark or your righteousness *in the night so the afflicted soul may rise and praise yahweh*.

What the comparison showed:

- John 10 has many speakers and many action words about relationship such as "know" and "believe" and "follow" and "hear" while Psalm 88 has one voice speaking to "you" and naming words about a low place such as "pit" and "grave" and "wrath" and "terrors".
- John 10 repeats a few words many times ("sheep" 16 times and "father" 11 times) while Psalm 88 repeats almost nothing (the top word "yahweh" appears 4 times) which means the special word list for Psalm 88 is thin and nearly every allowed word is a one-time word.
- Both hand-joined passages scored about as high as the passages from the large selections after far fewer rule changes because every stretch comes from one chapter and already shares one subject.
- The added words in the John 10 passage mostly restore what the chapter says (for example "by a demon" finishes a line the cutting rule had split) which means the high score reflects a small and connected source more than skill in joining.
- Psalm 88 in the source ends in darkness with no turn toward relief and the closing words "so the afflicted soul may rise and praise yahweh" are a choice of the AI model built from two questions in the psalm ("do the departed spirits rise up and praise you" and "are your wonders made known in the dark").
- The John 10 passage reports that people picked up stones and the passage keeps the question "for which of the good works do you stone me" as a question which means the passage does not present harm to any person as good.

## A personal rule from Charles: one word for God in the selections Charles chose

Charles set a personal rule for the selections that Charles chose: the name "yahweh" is replaced by the word "god" everywhere because Charles wants one word for God and keeps the word "lord" because "lord" connects with Christ for Charles.
The rule applies to the Charles selection and to the words of Jesus and to the two single chapters and the rule does not apply to the Claude selection.
The sections above this section were written before the rule and still show the older wording.

What the rule changed:

- The Charles selection had 1189 key phrases that held the name and the selection now has 43651 different key phrases (down from 43694) because some phrases became identical after the replacement.
- The word "god" now appears about 2750 times in the Charles selection because the 1687 uses of the name were added to the 1064 uses of "god".
- The words of Jesus and John 10 held no key phrase with the name so only the special word list of the words of Jesus changed (the name was removed from the list).
- Psalm 88 held the name 4 times and now reads "god" in those 4 places.
- The Charles special naming words are now god and man and jesus and son and people and lord and day and king and house and land and heart and earth.
- A few phrases now repeat the word such as "god the god of my salvation" because the source reads "yahweh the god of my salvation".
- The form "yahwehs" (which means "belonging to yahweh" because the cutting rule strips the mark of possession) became "gods" and a reader could mistake "gods" for more than one god.

Charles selection passage under the rule:

- i have set god always before me *the great king* whose sandal strap im *under because* the kingdom of heaven is at hand. *the righteous man answered* in heart if the foundations *of the house* are destroyed *the wise people know the righteous man* neither has he gone into captivity *with the wicked people* who rose up against me and by *evil made the land poor*. *the people of the land* in labor they will look on him *the holy king* who has had boldness to approach me says god *and the lord answered* shouldnt my soul be avenged.

Psalm 88 passage under the rule:

- *god* i have cried in the morning *and in the night* on you daily god i have spread out my hands to you *because* my prayer comes before you god why do you reject my soul. i am afflicted and ready to die from my youth up while i suffer your terrors i am distracted your fierce wrath has gone over me *the afflicted soul* like the slain who lie in the grave whom you remember no more. you have laid me in the lowest pit in the darkest depths *because* your wrath lies heavily on me you have afflicted me with all your waves. your terrors have cut me off they came around me like water all day long *and the dark night cut the day* from me and my friends. *show your wonders* in the dark or your righteousness *in the night so the afflicted soul may rise and praise god*.

## Newest rules: one word for God everywhere and adjacent pronouns may be deleted and punctuation may be added

Charles made three rule changes at once:

- The name "yahweh" is now always replaced by the word "god" in every selection and every Bible program because Charles wants one word for God (this is a personal reading choice and the warning at the top of this page says so).
- When the AI model adds a naming word right beside a pronoun the AI model may delete that pronoun so that "i *jesus* bear with you" becomes "*jesus* bear with you" because the doubled wording reads badly.
- The AI model may add periods and commas and question marks and quote marks and other neutral break marks wherever a break helps a reader because the key phrase cutting had removed every mark.

Every added word is still marked with stars and every deleted pronoun is listed under the passage and punctuation marks are not starred because every mark in these passages was added by the AI model.
The grades use the same seven rules with a top score of 14 and the AI model graded passages that the AI model wrote which means the grades are a rough guide.

### Three fresh strings from the selections Charles chose

Charles selection first fresh string (12 of 14):

- *the wise man has* sworn *to god,* "i will not forget your word, *because* the entrance of your words gives light in the house *of the poor*." *the man heard the word* from god. god says, "*take heart* in yourselves, and those who dwell *in the land*." *the man answered,* "according to your word, god." *the wicked made evil,* yet they have not prevailed against me, *because* the ox knows his owner *and the wise man knows god* and turned my steps to your statutes. let those who are with them *hear:* "it will happen in that day," says god, "*the lord* will bring *the high and wicked* down *to the earth*." *the people of the land heard and* said, "this is truly the prophet." others said, "*this man is righteous*."
- Deleted pronouns: "i" before "have sworn" (and "have" became "has" under the grammar rule below) and "i" before "the lord" and "them" where "the high and wicked" now stands and "they" before "said".

Charles selection second fresh string (11 of 14):

- *the people answered,* "we dont know." jesus said to them, "take heed, *because* a good tree cant produce evil fruit, and broad is the way that doesnt grow good *fruit*." *what good man* who says to a father, "*hear*," will give *the son* a stone? or if he asks *for a house* with grain, *will say, "take a stone* or vinegar"? *the people* stand up together, "assemble yourselves, all of you," and saying, "you are the christ." *jesus answered,* "i will give you *a house on good earth*. *the house the wicked man made on poor land* before the pigs, and great was its fall." *jesus says,* "i will be with you, *and not with the evil* which brings about mischief, *because* it is the glory *of god that* all men will come to you."
- Deleted pronouns: "him" before "the son" and "they" before "stand up together".
- The sentence about grain and vinegar stays weak because the two small stretches "with grain" and "or vinegar" share no subject with the stretches around them.

Words of Jesus fresh string (13 of 14):

- "*hear* the son of man, who is *sent from the father, because the man who hears jesus* and believes *the father* who sent me *receives eternal life*. dont forbid him. *the man who receives a little one* receives me, and he who loves son *and father in the love of god receives the kingdom*. *tell the good from the evil, because* whatever is more than these is of the evil one. *the kingdom of heaven is a house* in which there will *be the life* that you see, for i tell you that unless your righteousness exceeds *the world, the little* which he has will be taken away. throw out the unprofitable servant. the king will answer them, 'most certainly i tell you, this generation will not pass away before you. most certainly i tell you, all sins of the descendants of man will be forgiven, including their blasphemies, *because the father sent the son to give love to the world*.'"
- Deleted pronouns: "him" before "the father".
- The line "throw out the unprofitable servant" comes from a parable about a servant and a master and the passage adds nothing to the line which means the passage does not present harm to any person as good.

### The six earlier passages again under the newest rules

Words of Jesus first string (14 of 14):

- "with you, how long will *jesus* bear with you? for everyone in the marketplaces, *and in* the best seats in the synagogues, *made the house of god a house of the world* and traded with them, i tell you, and much more. *the father sent love to those* who hate you, *so* bless those *in the marketplaces*, for they shall inherit the earth. blessed are those who have been persecuted *for the kingdom* before you. most certainly i tell you, if you have faith with *the christ*, then he will sit on the throne of his glory, *which the father made great in heaven*. on the earth, i wish it were already kindled: *the good seed of love that the father sent to the world*."
- Deleted pronouns: "i" before "jesus" and "him" before "the christ".

Words of Jesus second string (14 of 14):

- "they persecuted the prophets who were *sent* before you, and even the chosen ones *of god*. behold, *jesus has* told you beforehand: *among* women there has not arisen anyone greater than john the baptizer, *yet* for you to enter into gods kingdom before you, most certainly i tell you, i havent found *a place apart from the father*. *the father sent the son to give love* and not sacrifice, for *the christ* came not on an old garment, for the patch would tear away *the garment*. *believe, so the father and the son enter the house in heaven* and prepare a place for you; *yet* and whoever says 'you fool' will be *last in the kingdom*."
- Deleted pronouns: "i" before "the christ" and "i" before "have told" (and "have" became "has" under the grammar rule below).

Claude selection (13 of 14):

- on the earth there was evening, *and god made* herbs yielding seed after their kind, and it was so. god saw everything *good*. *blessed are those* who mourn, for they shall be comforted *on the earth*, and be exceedingly glad, for great is your reward in heaven. *the righteous* who were before you *heard*, "you are the salt of the earth," *from the father* who is in secret. *a man who saw evil* at a woman, to lust after her, has committed adultery *in the heart; so keep your yes* "yes" and your no be "no" *before god*. *god saw the man* who is evil; but whoever strikes you, *give the man love, because* you shall love your neighbor, and hate your enemy *no longer*.

Charles selection (13 of 14 and up from 12):

- i have set god always before me, *the great king* whose sandal strap im *under, because* the kingdom of heaven is at hand. *the righteous man answered* in heart, "if the foundations *of the house* are destroyed, *the wise people know the righteous man*: neither has he gone into captivity *with the wicked people* who rose up against me and by *evil made the land poor*." *the people of the land* in labor, they will look on *the holy king* who has had boldness to approach me, says god, *and the lord answered,* "shouldnt my soul be avenged?"
- Deleted pronouns: "him" before "the holy king".

John 10 (14 of 14 and up from 13):

- *jesus answered the jews,* "as i told you, my sheep hear my voice, and i know them, and they follow me. i give eternal life to them. the good shepherd lays down his life for the sheep, *because the sheep know the voice of the shepherd*. whenever he brings out his own sheep, he goes *to the door*." *the jews answered* and said to him, "how long will you hold us?" for they dont know the voice of strangers. jesus spoke this parable to them, but they didnt understand. jesus therefore said to them again, "most certainly, *no one can take the sheep out* of my fathers hand. i and the father are one." *so the jews take* stones again to stone him. jesus answered them, "*for which of the good* works do you stone me?" the jews answered him, "we dont stone you *for good works*." *jesus answered,* "if i dont do the works of my father, *do not believe*; but if i do them, though you dont believe me, believe the works." others said, "these are not the sayings of one possessed *by a demon, because the works are good*."

Psalm 88 (13 of 14 and up from 12):

- *god,* i have cried in the morning *and in the night* on you daily. god, i have spread out my hands to you, *because* my prayer comes before you. god, why do you reject my soul? i am afflicted and ready to die from my youth up. while i suffer your terrors, i am distracted. your fierce wrath has gone over me, *the afflicted soul*, like the slain who lie in the grave, whom you remember no more. you have laid me in the lowest pit, in the darkest depths, *because* your wrath lies heavily on me. you have afflicted me with all your waves. your terrors have cut me off. they came around me like water all day long, *and the dark night cut the day* from me and my friends. *show your wonders* in the dark, or your righteousness *in the night, so the afflicted soul may rise and praise god*.

What the newest rules changed:

- Quote marks gave the largest gain because quote marks show who is speaking and the passages with several speakers (John 10 and the Charles selection) each rose by 1 point.
- Question marks turned lines such as "why do you reject my soul" and "for which of the good works do you stone me" back into questions which a reader could not tell from the bare words.
- Deleting an adjacent pronoun removed doubled wording such as "i jesus" and "him the christ" and the deletion only works where the grammar still holds afterward.
- The passages that already scored 14 could not rise and those passages still read more smoothly because sentence breaks now fall where a reader expects a break.
- The live programs carry the one-word-for-God rule and the warning while the pronoun rule and the punctuation rule exist only in the hand joining because the programs have no test of meaning or grammar.

## Grammar rule: a word may change form when a naming word replaces a pronoun

Charles added a smoothing rule for every selection: when a naming word replaces a pronoun and the swap breaks the grammar the AI model may change the form of the nearby word so that the sentence stays correct (for example "i have told you" becomes "*jesus has* told you" because "jesus have told you" reads wrongly).
A changed word is marked with stars the same way an added word is marked.

Where the rule changed a passage in the section above:

- Words of Jesus second string: "behold, i *jesus* have told you beforehand" became "behold, *jesus has* told you beforehand".
- Charles selection first fresh string: the opening "*the wise man says to god:* i have sworn" became "*the wise man has* sworn *to god*".
- The other seven passages needed no change because every swap in those passages already left correct grammar (for example "how long will *jesus* bear with you" is correct because the word "will" takes the plain form "bear").
- Both changed passages keep the same grade because the grades were already counting those sentences as understandable and the change removes an awkward spot without adding meaning.
- The rule also widens what the pronoun deletion rule can do because a pronoun that could not be deleted before (such as the "i" in "i have told") can now be replaced.

## Names of the live programs

The three older Bible programs differ by the size of the piece that the agents copy and not by Bible selection so the programs are now named by method and three further pages open the key phrase method on one selection each.

- Bible Evolution Method 1: Letters copies single letters and uses the Claude selection only: https://claude.ai/artifact/Rk7TreKWL498TLBQi885x6
- Bible Evolution Method 2: Single Words copies whole words and has a button for each selection: https://claude.ai/artifact/3VEDvP27dnjcmbSNtBdkVY
- Bible Evolution Method 3: Key Phrases copies short phrases and has a button for each selection: https://claude.ai/artifact/8n9q5vuPKvNhn6R7fSZzKK
- Bible Key Phrases: Claude Selection opens the key phrase method on the 41 passages picked by the AI model: https://claude.ai/artifact/PK8tNEMDZM2eVaCfuNSxdR
- Bible Key Phrases: Charles Version opens the key phrase method on the ten whole books picked by Charles: https://claude.ai/artifact/4pJdWtCH4ahdFjsb4GVb8Q
- Bible Key Phrases: Jesus Version opens the key phrase method on the words of Jesus in the four gospels: https://claude.ai/artifact/Bzcg2eYnte9cTc7wtpBArz
- Each link opens for other people only after Charles shares that page from the Claude app.

## Limits

- The reader rewards text that matches the Bible and has no sense of meaning which means the agents rebuild the source and do not write anything new.
- One run per selection with ten agents is a small sample.
- The rule-based cutting sometimes splits a thought in an odd place.

## Try the program

- Open this address in a web browser to run the program with a button for each of the three selections: https://htmlpreview.github.io/?https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/1-research-click-here-first/bible-key-phrase-evolution-live-program.html
- The address above depends on a free outside service named htmlpreview and nobody has tested the address yet which means the address might fail.
- The second way is to download the program file from this address and open the downloaded file in any web browser: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/1-research-click-here-first/bible-key-phrase-evolution-live-program.html

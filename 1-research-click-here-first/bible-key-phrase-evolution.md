# Agents that rebuild the Bible out of chopped key phrases

Warning about a wording change: Charles replaces the name "yahweh" with the word "god" everywhere in the Bible programs and in the newer results as a personal reading choice that helps Charles follow the quotes which means the quotes differ from the World English Bible at every place where the World English Bible prints the name and a reader who wants the original wording can open the World English Bible itself.

Warning about changed wording in the joined Bible passages: the passages that the AI model joined by hand for the Claude selection and the Charles selection and the words of Jesus are not exact Bible quotes because Charles set rules that allow pronouns such as "he" and "him" and "they" to be deleted or swapped for naming words and allow rarely used names such as the names of little-known cities to be replaced with generic words and allow the word "the" and punctuation marks to be added or removed which means a reader who wants the exact wording needs to open the World English Bible itself.

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

## Speaker rule for the words of Jesus: the passages are read as spoken by Christ

Charles added a rule for the words of Jesus selection only: every passage is read as spoken by Christ which means the added words avoid the name "jesus" because the speaker in the four gospels rarely uses that name for himself and more often says "i" or "the son of man".
The word "i" now stays as the source has the word and "the son of man" stands where a "he" or "him" points at the speaker and the name "jesus" was removed from the special word list of the live program for this selection.
The grades assume a reader who knows that Christ is speaking because the rule itself sets that assumption.

Words of Jesus first string (14 of 14):

- "with you, how long will i bear with you? for everyone in the marketplaces, *and in* the best seats in the synagogues, *made the house of god a house of the world* and traded with them, i tell you, and much more. *the father sent love to those* who hate you, *so* bless those *in the marketplaces*, for they shall inherit the earth. blessed are those who have been persecuted *for the kingdom* before you. most certainly i tell you, if you have faith with *the son of man*, then he will sit on the throne of his glory, *which the father made great in heaven*. on the earth, i wish it were already kindled: *the good seed of love that the father sent to the world*."
- Deleted pronouns: "him" before "the son of man".

Words of Jesus second string (14 of 14):

- "they persecuted the prophets who were *sent* before you, and even the chosen ones *of god*. behold, i have told you beforehand: *among* women there has not arisen anyone greater than john the baptizer, *yet* for you to enter into gods kingdom before you, most certainly i tell you, i havent found *a place apart from the father*. *the father sent the son to give love* and not sacrifice, for *the son of man* came not on an old garment, for the patch would tear away *the garment*. *believe, so the father and the son enter the house in heaven* and prepare a place for you; *yet* and whoever says 'you fool' will be *last in the kingdom*."
- Deleted pronouns: "i" before "came not".

Words of Jesus fresh string (13 of 14):

- "*hear* the son of man, who is *sent from the father, because the man who hears the son* and believes *the father* who sent me *receives eternal life*. dont forbid him. *the man who receives a little one* receives me, and he who loves son *and father in the love of god receives the kingdom*. *tell the good from the evil, because* whatever is more than these is of the evil one. *the kingdom of heaven is a house* in which there will *be the life* that you see, for i tell you that unless your righteousness exceeds *the world, the little* which he has will be taken away. throw out the unprofitable servant. the king will answer them, 'most certainly i tell you, this generation will not pass away before you. most certainly i tell you, all sins of the descendants of man will be forgiven, including their blasphemies, *because the father sent the son to give love to the world*.'"
- Deleted pronouns: "him" before "the father".

What the speaker rule changed:

- The three passages now hold no added "jesus" and no added "the christ" which means every passage can be read aloud as one person speaking from start to end.
- The phrase "the son of man" fits the source closely because the source verse behind the first string itself reads "when the son of man comes in his glory then he will sit on the throne of his glory".
- The grades did not move because the earlier names had earned their point by telling a reader who "i" is and the speaker rule now gives a reader the same knowledge before the passage starts.
- A reader who meets one of these passages with no notice that Christ is speaking would lose that knowledge which means the passages need a short heading such as "words of Christ" wherever the passages are posted.

## Three brand new passages from the words of Jesus under every rule so far

Charles asked for three fresh attempts from three different starting points using only the words of Jesus so the AI model ran the key phrase evolution three times with three different random starts (5 million pastes each) and joined one agent string from each run by hand.
Every rule so far applies: generic joining words and special naming words and action words and describing words and reuse of naming words already in the string and deletion of a pronoun beside an added name and grammar changes and punctuation and the reading of every line as spoken by Christ.
A listed action word sometimes appears in another form such as "says" for "say" and "gives" for "give" because the grammar rule allows a word to change form.
Added or changed words carry stars and the AI model graded passages that the AI model wrote which means the grades are a rough guide.

First attempt (13 of 14) from the stretches "most certainly i tell you wherever this good news" and "from your father who is in heaven for the son of" and "against the holy spirit it will not be forgiven him" and "until all these things are accomplished heaven and earth will pass away" and "he will convict the world about sin about righteousness" and "from you in that day you will ask me no questions most certainly i tell you" and "he said this is what i will do" and "this is what i told you while i was still with you for everyone":

- "most certainly i tell you, wherever this good news *enters the world, love is sent* from your father who is in heaven, for the son of *man is sent to give life*. this is what i told you while i was still with you, for everyone: *believe the good news, because* until all these things are accomplished, heaven and earth will pass away, *yet the love of the father will not*. *the holy spirit is sent to take the evil* from you in that day; you will ask me no questions. most certainly i tell you, *the holy spirit* will convict the world about sin, about righteousness. *the man who says evil* against the holy spirit, it will not be forgiven him. *a man with a full house* said, 'this is what i will do: *give to the little ones*.'"
- Deleted pronouns: "he" before "will convict".

Second attempt (12 of 14) from the stretches "who is in heaven he is my brother" and "well done good and faithful servant" and "and give it to him who has the ten talents" and "than me is not worthy of me and he who doesnt have even that which he has will be taken away from him" and "for tyre and sidon in the judgment with this generation" and "he sent him last to them saying they will respect my son but the farmers" and "and your mother you still lack one thing":

- "*the man who hears the father* who is in heaven, he is my brother. *the lord says to the man,* 'well done, good and faithful servant,' and give *the kingdom* to him who has the ten talents. *the man who loves the world more* than me is not worthy of me, and he who doesnt have *love*, even that which he has will be taken away from him. *the father had a son, and* he sent him last to them, saying, 'they will respect my son.' but the farmers *did not receive the son*. *it will be right* for tyre and sidon in the judgment with this generation, *because this generation saw the son and did not believe*. *love your father* and your mother; you still lack one thing: *give to the little ones and enter the kingdom*."
- Deleted pronouns: "it" before "to him who has the ten talents".

Third attempt (11 of 14) from the stretches "before you most certainly i tell you" and "it is like a man going into another country" and "for they see and your ears" and "others fell among the thorns this is he" and "that was cast into the sea" and "then let those" and "from the sky and the powers that are" and "will not pass away until all these things happen" and "where the vultures gather together" and "will you lay down your life for me":

- "*the kingdom of heaven is sent* before you. most certainly i tell you, it is like a man going into another country *who gives seed to the earth*. *blessed are the little ones,* for they see, and your ears *hear the good seed*. *some seed fell on good earth;* others fell among the thorns. this is he *who hears and takes the world for life, like a seed* that was cast into the sea. then let those *who believe see: life is sent* from the sky, and the powers that are *in heaven* will not pass away until all these things happen. *the dead world is* where the vultures gather together; will you lay down your life for me, *the son of man who made life eternal*?"

What the three attempts showed:

- The scores fell in the order 13 and 12 and 11 and the order follows the length of the stretches because the first string had long stretches that each already held a full thought while the third string had ten short stretches such as "then let those" that held no thought alone.
- The first attempt needed the fewest added words and the third attempt needed the most which means the third passage carries more of the choices of the AI model than the first passage does.
- The line "he said this is what i will do" comes from a parable about a rich man with full barns in the source so the passage names "a man with a full house" and does not put that line in the mouth of the father.
- The second attempt leaves "the ten talents" and "tyre and sidon" unexplained because no allowed word can explain a sum of money or two cities and that gap costs the passage a point on the rule about explaining every label.
- The ending of the second attempt softens the source because the source line about the city of Tyre and the city of Sidon speaks of a judgment being more bearable and the passage says "it will be right" which is a choice of the AI model.

## Rule about the word "the": the word may be added anywhere or removed anywhere

Charles added a rule for every selection: the AI model may add the word "the" anywhere and may remove the word "the" anywhere when the change makes a sentence easier to read.
Adding "the" was already possible because "the" sits on the list of generic joining words and the new part of the rule is the removal which is the first rule that lets the AI model take a non-pronoun word out of a rebuilt stretch.

Where the rule changed the passages above:

- Words of Jesus fresh string: "he who loves son *and father in the love of god*" became "he who loves *the* son *and the father in the love of god*" because "loves son" reads as a cut-off phrase.
- Charles selection passage: "*the righteous man answered* in heart" became "*the righteous man answered* in *the* heart" because "in heart" reads as a cut-off phrase.
- No passage needed a removal because none of the passages so far holds a "the" that blocks a reader.
- The grades did not change because each change smooths one phrase and adds no meaning.
- A removal is most likely to matter in future strings where two stretches meet and both bring a "the" such as "in the the house".

## Pronoun rule: any pronoun may be swapped for another pronoun or for a naming word

Charles added a rule for every selection: the AI model may replace any pronoun anywhere in a passage (inside a rebuilt stretch or among the added words) with another pronoun or with an allowed naming word because a passage full of "he" and "him" and "they" and "it" leaves a reader guessing who is meant.
A replaced word carries stars and the words of Jesus passages still keep "i" and "me" because those passages are read as spoken by Christ.

The three fresh words of Jesus passages again under the pronoun rule:

First attempt (13 of 14 and unchanged):

- "most certainly i tell you, wherever this good news *enters the world, love is sent* from your father who is in heaven, for the son of *man is sent to give life*. this is what i told you while i was still with you, for everyone: *believe the good news, because* until all these things are accomplished, heaven and earth will pass away, *yet the love of the father will not*. *the holy spirit is sent to take the evil* from you in that day; you will ask me no questions. most certainly i tell you, *the holy spirit* will convict the world about sin, about righteousness. *the man who says evil* against the holy spirit, *the evil* will not be forgiven *that man*. *a man with a full house* said, 'this is what i will do: *give to the little ones*.'"
- Replaced pronouns: "he" became "the holy spirit" and "it" became "the evil" and "him" became "that man".

Second attempt (13 of 14 and up from 12):

- "*the man who hears the father* who is in heaven, *that man* is my brother. *the lord says to the man,* 'well done, good and faithful servant,' and give *the kingdom* to *the servant* who has the ten talents. *the man who loves the world more* than me is not worthy of me, and *the man* who doesnt have *love*, even that which he has will be taken away from him. *the father had a son, and the father* sent *the son* last to *the farmers*, saying, '*the farmers* will respect my son.' but the farmers *did not receive the son*. *it will be right* for tyre and sidon in the judgment with this generation, *because this generation saw the son and did not believe*. *love your father* and your mother; you still lack one thing: *give to the little ones and enter the kingdom*."
- Replaced pronouns: "he" became "that man" and "it" became "the kingdom" and "him" became "the servant" and "he" became "the man" and "he" became "the father" and "him" became "the son" and "them" became "the farmers" and "they" became "the farmers".

Third attempt (12 of 14 and up from 11):

- "*the kingdom of heaven is sent* before you. most certainly i tell you, *the kingdom* is like a man going into another country *who gives seed to the earth*. *blessed are the little ones,* for they see, and your ears *hear the good seed*. *some seed fell on good earth; other seed* fell among the thorns. this is *the man who hears and takes the world for life, like a seed* that was cast into the sea. then let those *who believe see: life is sent* from the sky, and the powers that are *in heaven* will not pass away until all these things happen. *the dead world is* where the vultures gather together; will you lay down your life for me, *the son of man who made life eternal*?"
- Replaced pronouns: "it" became "the kingdom" and "others" became "other seed" and "he" became "the man".

What the pronoun rule changed:

- The second attempt gained a point because the sentence about the father and the son and the farmers had four pronouns in a row ("he sent him last to them saying they") and now names every person.
- The third attempt gained a point because "it is like a man" now says what is like a man.
- The first attempt stayed at 13 because the earlier rules had already named most of the people in that passage.
- A pronoun stays where the same sentence already names the person (for example "the man who doesnt have love, even that which he has") because repeating the naming word three times in one sentence reads worse than one pronoun.
- The same rule applies to the older passages on this page (for example "neither has he gone into captivity" in the Charles selection passage can become "neither has *the righteous man* gone into captivity" and "they came around me like water" in the Psalm 88 passage can become "*your terrors* came around me like water").
- Every replacement is a choice by the AI model about who a pronoun points at and a wrong choice would put words about one person onto another person which means a reader who cares about exact meaning needs to compare the passage with the source verse.

## Name rule: rarely used names are replaced with generic words

Charles added a rule for every selection: a name that appears only a few times or in a single section is replaced with a generic word or phrase that makes sense in the sentence because a reader who has not studied the Bible closely will not know who or what the name is (for example few readers know that Tyre is a city).
Names that most people in the wider culture already know stay as the source has the names (for example John and Mark and Luke and Simon and Adam and Eve).
The replacement is starred like every other change and the warning near the top of this page tells a reader that names and pronouns are changed in these passages.

The three fresh words of Jesus passages under the name rule:

- The first attempt and the third attempt hold no rarely used name so both passages stay exactly as printed in the section about the pronoun rule.
- The second attempt held the names of two cities ("tyre and sidon") and now reads as follows.

Second attempt (13 of 14):

- "*the man who hears the father* who is in heaven, *that man* is my brother. *the lord says to the man,* 'well done, good and faithful servant,' and give *the kingdom* to *the servant* who has the ten talents. *the man who loves the world more* than me is not worthy of me, and *the man* who doesnt have *love*, even that which he has will be taken away from him. *the father had a son, and the father* sent *the son* last to *the farmers*, saying, '*the farmers* will respect my son.' but the farmers *did not receive the son*. *it will be right* for *two foreign cities* in the judgment with this generation, *because this generation saw the son and did not believe*. *love your father* and your mother; you still lack one thing: *give to the little ones and enter the kingdom*."
- Replaced names: "tyre and sidon" became "two foreign cities".

What the name rule changed:

- The sentence about the judgment can now be followed by a reader who has never heard of either city and the passage keeps its grade of 13 because "the ten talents" (a large sum of money in the parable) is still unexplained.
- None of the other passages on this page that were joined under the newest rules holds a rarely used name (the name "john the baptizer" in one words of Jesus passage stays because John is widely known).
- The rule applies only to the hand joining for now because the live programs hold the phrases in lowercase with no marker for which words are names which means the programs still show every name as the source has the name.
- Which names count as widely known is a judgment by the AI model and Charles can overrule any single choice.

## A new batch under every rule: one passage from each selection

Charles asked for a new batch with one passage from each selection so the AI model ran the key phrase evolution once more on each selection from a new random start (5 million pastes each) and joined one agent string from each run by hand under every rule on this page.
Added or changed words carry stars and the AI model graded passages that the AI model wrote which means the grades are a rough guide.

Claude selection (13 of 14) from the stretches "in all the earth you have set your" and "you have put all things under his feet all sheep" and "neither throw your pearls before the pigs" and "a good tree cant produce evil fruit neither can a corrupt" and "but he who does the will of my father who is in heaven for he makes his sun to rise" and "for righteousness sake for theirs is the kingdom of heaven" and "that it was said you shall not commit adultery but i tell you love your enemies" and "than these is of the evil one you have heard":

- *lord god,* in all the earth you have set your *light, and* you have put all things under *the* feet *of man:* all sheep *and every living thing*. *keep what is holy, and* neither throw your pearls before the pigs. *whatever a man says more* than *what is right* is of the evil one. you have heard that it was said, "you shall not commit adultery," but i tell you, love your enemies, *because* a good tree cant produce evil fruit, neither can a corrupt *tree make good fruit*. *blessed are the righteous* for righteousness sake, for theirs is the kingdom of heaven; *not the man who says "lord,"* but he who does the will of my father who is in heaven, for *the father* makes his sun to rise *on the evil and the good*.
- Replaced pronouns: "his" became "the ... of man" and "these" became "what is right" and "he" became "the father".

Charles selection (11 of 14) from the stretches "for he commands" and "from the north says god for god says" and "from me says god for i am with you says god god said to me" and "the assembly of the elders of the people were gathered together" and "god i have called" and "in jerusalem because you have said" and "praise be to god god" and "with justice" and "when he cries" and "like lebanon" and "in bethany beyond the jordan" and "to take back to those":

- the assembly of the elders of the people were gathered together in jerusalem, because you have said, "praise be to god." god, i have called *on you from a small town across the river, and god hears* when *the poor man* cries, for *god* commands *the king to give* with justice. "*evil will not take the land* from the north," says god, for god says, "*do not take your heart* from me," says god, "for i am with you," says god. god said to me, "*make the land* like *a high green land, and give the good of the land* to take back to those *poor people*."
- Replaced pronouns: "he" became "the poor man" and "he" became "god".
- Replaced names: "in bethany beyond the jordan" became "from a small town across the river" and "lebanon" became "a high green land" while "jerusalem" stays because the city is widely known.

Words of Jesus (13 of 14) from the stretches "if you remain in me he was counted with transgressors for that" and "on the sand the rain came down" and "among yourselves for i tell you" and "for you from the foundation of the world for i was hungry" and "who are with child" and "so when he comes most certainly i tell you that one of you will betray me" and "for you always have the poor with you" and "your house is left to you desolate i tell you keep asking":

- "*the kingdom is made* for you from the foundation of the world, for i was hungry *and you gave to me*. *give to the little ones and to those* who are with child, for you always have the poor with you. *love the little ones* among yourselves, for i tell you, *do not make a house* on the sand: the rain came down, *and* your house is left to you desolate. i tell you, keep asking *the father*. if you remain in me, *believe: the son of man* was counted with transgressors for that *love*. so when *the last day* comes, most certainly i tell you that one of you will betray me, *yet the love of the father is greater*."
- Replaced pronouns: "he" became "the son of man" and "he" became "the last day".

What the new batch showed:

- The Claude selection and the words of Jesus both reached 13 because both strings had stretches long enough to hold a full thought and both lost one point for a label that stays unexplained ("pearls before the pigs" and "counted with transgressors").
- The Charles selection reached 11 because twelve short stretches from several books left the AI model to supply most of the meaning and the phrase "says god" repeats four times in two lines.
- The name rule was needed only in the Charles selection because the ten whole books hold many place names while the other two selections draw on better known passages.
- In the words of Jesus passage the phrase "when he comes" became "when the last day comes" and that choice is a guess by the AI model because the stretch alone does not say who or what comes.
- The closing words "yet the love of the father is greater" follow a line about betrayal and are a choice of the AI model and not part of the source.

## Pronoun rule widened: any pronoun may be added or deleted anywhere in every selection

Charles confirmed that the pronoun freedom covers every selection: the AI model may add a pronoun anywhere and may delete a pronoun anywhere and may swap a pronoun for another pronoun or for a naming word whenever the change makes a passage easier to read.
Adding pronouns and swapping pronouns were already allowed for every selection and the new part is that a pronoun may now be deleted even when no added name sits beside the pronoun.

- The rule applies to the Claude selection and the Charles selection and the words of Jesus and the single chapters alike.
- The words of Jesus passages still keep "i" and "me" where the speaker means himself because those passages are read as spoken by Christ.
- No passage on this page needed a new deletion because the swap rule had already handled every pronoun that blocked a reader and the wider rule will matter in future strings where a leftover pronoun such as a stray "it" has nothing to point at.

## The outputs again under the widened pronoun rule

The AI model went back through the six newest passages and looked for every place where deleting or adding a pronoun helps a reader.

Sentences that changed in the three fresh words of Jesus attempts:

- First attempt before: "*the man who says evil* against the holy spirit, *the evil* will not be forgiven *that man*." First attempt after: "*the man who says evil* against the holy spirit will not be forgiven." The source pronouns "it" and "him" are deleted because the sentence already names the man at the start.
- Second attempt before: "*the man who hears the father* who is in heaven, *that man* is my brother." Second attempt after: "*the man who hears the father* who is in heaven is my brother." The source pronoun "he" is deleted because the sentence already names the man.
- Third attempt before: "this is *the man who hears and takes the world for life*". Third attempt after: the same wording because the earlier swap had already replaced the pronoun.

The newest batch under the widened rule:

Claude selection (13 of 14 and unchanged):

- *lord god,* in all the earth you have set your *light, and* have put all things under *the* feet *of man:* all sheep *and every living thing*. *keep what is holy, and* neither throw your pearls before the pigs. *whatever a man says more* than *what is right* is of the evil one. you have heard that it was said, "you shall not commit adultery," but i tell you, love your enemies, *because* a good tree cant produce evil fruit, neither can a corrupt *tree make good fruit*. *blessed are the righteous* for righteousness sake, for theirs is the kingdom of heaven; *not the man who says "lord,"* but he who does the will of my father who is in heaven, for *the father* makes his sun to rise *on the evil and the good*.
- Deleted pronouns: the second "you" in "you have set your light and you have put".

Charles selection (12 of 14 and up from 11):

- the assembly of the elders of the people were gathered together in jerusalem, because *the people* have said, "praise be to god." god, i have called *on you from a small town across the river, and god hears* when *the poor man* cries, for *god* commands *the king to give* with justice. "*evil will not take the land* from the north," says god, for god says, "*do not take your heart* from me," says god, "for i am with you," says god. god said to me, "*make the land* like *a high green land, and give the good of the land* to take back to those *poor people*."
- Replaced pronouns: "you" became "the people" in "because you have said" (a swap the earlier rule already allowed and the AI model had missed).

Words of Jesus (13 of 14 and unchanged):

- The passage stays exactly as printed in the section about the new batch because every pronoun in the passage either means the speaker or points at a person named in the same sentence.

Does the widened pronoun rule improve readability:

- The rule helps in one clear kind of sentence which is a sentence where the source repeats the subject as a pronoun (for example "the man who hears the father, he is my brother") because deleting the repeated pronoun leaves one clean sentence.
- The rule changed 3 sentences across six passages and no grade moved because of a deletion which means the gain is smoothness inside a sentence and not a new level of understanding.
- The one grade that moved (Charles selection from 11 to 12) came from a swap and not from a deletion.
- The small effect has a likely reason: the earlier swap rule had already removed most pronouns that left a reader guessing so few pronouns were left for the deletion rule to fix.

## John 10 dealt into four random piles and remixed

Charles asked for a remix of John chapter 10: the 201 key phrases of the chapter were dealt at random into four piles the way a deck of cards is dealt (51 and 50 and 50 and 50 phrases) and the AI model then built the most coherent paragraph it could from each pile using every phrase in the pile.
Every rule on this page applied (free order and joining words and the special words of John 10 and reuse of words already in the pile and pronoun changes and grammar changes and punctuation and generic words for rarely used names) and no copying agents ran in this test because the dealing itself did the shuffling.
A check by program confirmed that every dealt phrase appears in its paragraph except two phrases whose place names were replaced under the name rule ("beyond the jordan" became "across the river" and "in solomons porch" became "in a covered walkway").
Added or changed words carry stars and the AI model graded paragraphs that the AI model wrote which means the grades are a rough guide.

Pile 1 (12 of 14 and 30 percent of the words were added):

- it was the feast of the dedication, and jesus was walking in the temple. the jews therefore came around him, *and* jesus spoke this parable to them: "the gatekeeper opens the gate *for the shepherd, and* he goes *in* for the sheep. he who is a hired hand *is not the shepherd,* because he is a hired hand, and a robber *and* the thief only comes to steal, kill. i came for the sheep. i am the good shepherd; i know my own, and im known *by my own*. *the sheep* by no means follow a stranger, for they dont know *the voice of a stranger*. i have other sheep which are not of this fold. *my life,* no one takes it away; *i lay it down* by myself. *the works* that i do in my fathers name *are* from my father, who has given them. *you do not believe* because you are not of my sheep. *no one can snatch the sheep out* of my fathers hand." *some of the jews answered,* "he has a demon and is insane." *others answered, "these are not the* sayings of one possessed by a demon, is it?" *then the jews take* stones again to stone him. jesus answered them, "*for which of the good* works do you stone me?" the jews answered him, "*not for good works,* but for blasphemy, because you *tell the jews* that the father is *in you*." jesus answered them, "isnt it written in your law, 'you are gods'? *the law tells that of those* to whom the word of god came. but if i do them, *the works of the father, believe the works*." *jesus went* into the place *across the river;* many came to him; many believed in him there.

Pile 2 (13 of 14 and 37 percent of the words were added):

- *jesus said,* "most certainly, *the one who enters by the door* is the shepherd of the sheep. *the door is* for him; he calls his own sheep, *and the sheep hear and do not go* from him *to* the voice of strangers." *the jews did not know* what he was telling them. "most certainly, *all who were* before me are thieves and robbers. if anyone enters in by me, he will be saved, *and will go* in and go out. *the hired hand* leaves the sheep, *and* the wolf snatches the sheep. i lay down my life *for the sheep. other sheep* i must bring also, and they will hear my voice; they will become one flock. therefore the father loves me: *i lay down my life* that i may take it again. *no one takes my life,* but i lay it down to take it again." therefore a division arose again. *some said,* "why do you listen to him?" others said, "*is it* for a demon to open the eyes of the blind?" *the jews answered* and said to him, "if you are the christ, *tell us*." *jesus answered, "i do the works of my father,* and you dont believe the works. these testify about me, but you dont believe. *my sheep* will never perish, *and no one will* snatch them out of my hand." *the jews answered, "you* make yourself god." *jesus answered, "do you tell that to the one* whom the father sanctified into the world, because i said, 'i am the son of god'? *if i do not the works of my father,* dont believe me. *but if i do the works,* though you dont believe me, *believe the works,* and believe *that the father is in me,* and i in the father." they sought again to seize him, *and jesus was then* where john was baptizing at first.

Pile 3 (12 of 14 and 34 percent of the words were added):

- at jerusalem it was winter. *jesus said, "the one who does not go* in by the door but climbs up some other way is a thief. *the shepherd goes in by the door,* and the sheep listen to his voice; *he knows the sheep* by name *and goes* before them, and the sheep follow him. *the sheep do not follow a thief,* but will flee." but they didnt understand. "*thieves went before me,* but the sheep didnt listen to them. *the one who follows me will go in* and will go *out* and will find pasture. *the thief goes in to take* and destroy. i am the good shepherd, and not a shepherd who doesnt own the sheep and flees; *a thief takes* and scatters them, and *the hired hand* doesnt care for the sheep. *the father knows me* and i know the father. *the father is good to me* because i lay down my life. i have power to lay it down, and i have power *to take it; this power is* from my father." many of them said, "these are not the *works of a demon;* it isnt possible." *the jews said,* "tell us plainly." *jesus answered,* "i told you. as i told you, my sheep hear my voice and they follow me, and no one will *take them.* my father *has more power* than all, *and no one has the power* to snatch them out. i have shown you many good works." *the jews answered,* "we dont stone you for a good work." "*what* do you say of him *whom the father knows?* 'you blaspheme'? if i dont do the works of my father, *dont believe.*" and he went out of their hand; he went away again *across the river,* and he stayed there. *many said,* "john indeed did no sign."

Pile 4 (12 of 14 and 35 percent of the words were added):

- "i tell you, one who doesnt enter by the door into the sheep fold *is not the shepherd,* but one who enters *by the door is the shepherd,* and leads them out. whenever he brings out his own sheep, *the sheep follow,* for they know his voice; they will *not follow strangers*." jesus therefore said to them again, "i tell you, i am the sheeps door. all who came *by another door are not shepherds.* i am the door, that they may have life and may have it abundantly. the good shepherd lays down his life; the hired hand flees *when he* sees the wolf coming. *i know my own, and i am known* by my own, even as the father knows me. *the sheep will be one* with one shepherd. *no one takes my life* from me; i received this commandment *from my father*." *there was no one voice* among the jews because of these words. in *a covered walkway the jews said,* "how long will you hold us in suspense?" jesus answered them, "*my sheep hear me,* and i know them. i give eternal life to them. *the father, who is good* to me, is greater *than all;* no one is able *to snatch the sheep from the father.* i and the father are one." therefore jews took up *their hands against him.* "for which of those *works?" "you,* being a man, *make yourself god.*" "i said *what god said:* if he called them gods, and the scripture cant be broken, *then the one the father knows* and sent *tells what is true.* believe the works, that you may know *the father is* in me." they said, "*we did not know,* but everything that john said about this man is true."

The four paragraphs read one after another are the remix of John 10.
Two more remixes from two more random deals are on the page named john-10-remixes-from-four-random-piles in this folder which holds all three remixes together.

What the remix showed:

- Each pile came out as a small version of the whole chapter (the shepherd and the door and then the argument about works and stoning) because John 10 repeats its main ideas many times so a random quarter of the phrases still holds a piece of every idea.
- The four paragraphs therefore say nearly the same thing four times and the remix reads like four tellings of one story more than like one long story.
- About one word in three had to be added (30 to 37 percent) which is far more than in the passages built from agent strings because random dealing left most phrases without their true neighbor (a neighbor lands in the same pile only about one time in four).
- The result fits the earlier page-dealing test in this folder where dealing a biology book into four piles at random hid less than expected when the book repeated its ideas.
- A strong caution applies: the AI model knows John 10 and very likely leaned on that knowledge when choosing the added words which means the paragraphs show how well a reader who knows the chapter can rebuild the chapter and do not show what a reader with no knowledge of the chapter could do.
- The paragraphs report that people picked up stones and each paragraph keeps the question about the stoning as a question which means no paragraph presents harm to any person as good.

## Sixteen random phrases from the Charles selection kept in three random orders

Charles asked for a harder test: one set of key phrases is drawn at random from the Charles selection and the set is shuffled three times and the AI model must connect the phrases in the exact shuffled order with no sorting of any kind.
A program drew 16 key phrases at random from the 43651 key phrases of the ten whole books and the 16 phrases came from 14 different chapters in Isaiah and Proverbs and Psalms and Jeremiah and Matthew and Mark and John.
The AI model could add joining words and the special words of the Charles selection and could change or delete or add pronouns and could add punctuation and could not move any phrase.
A program check confirmed that the non-pronoun words of every phrase appear in each passage in the shuffled order.
Added or changed words carry stars and the AI model graded passages that the AI model wrote which means the grades are a rough guide.

The set of 16 phrases: "with you" and "my hand has found" and "i am god" and "wisdom is too high" and "and my vineyard" and "for the upright" and "for these things happened" and "but sent leanness" and "for god says to me" and "of the guard left" and "and in his own house" and "he arose" and "be under your hand" and "and killed mighty kings" and "and hid" and "and gave them to".

First random order (11 of 14 and 49 percent of the words were added):

- *the wise man saw evil* and hid. *on a good day* he arose, *and the wicked* of the guard left. "*god, let the land* be under your hand, for the upright." and in his own house *every man says,* "my hand has found *good,*" for these things happened. for god says to me, "wisdom is too high *for a man;* i am god. *the wicked king took from the people* but sent leanness, *so i took the land of the king* and gave *the land* to *the poor,* and my vineyard *to the upright. evil took the land* and killed mighty kings, *but i am* with you."

Second random order (11 of 14 and 48 percent of the words were added):

- *the king says in the land* and in his own house, "i am god." *the wise* of the guard left *the house of the king.* "*god is not* with you," *the wise say,* "for these things happened: *the land was made* for the upright, and my vineyard *was good,* but *you* sent leanness." for god says to me, "*let the poor man* be under your hand." *the poor man* arose *and says,* "my hand has found *good. evil took the land* and killed mighty kings and hid; wisdom is too high *for evil. god took the land* and gave *the land* to *the poor.*"

Third random order (10 of 14 and 46 percent of the words were added):

- *the people say "god is good,"* for these things happened for the upright: *god took good things* and gave them to *the poor* with you, and my vineyard *is one of the things.* wisdom is too high *for me, but* "i am god," *god says. a wise man* arose, for god says to me, "*let the people* be under your hand." *the wicked king heard* but sent leanness. *the wise man* of the guard left and hid. "my hand has found *the evil that took the land* and killed mighty kings, and in his own house *no king is high,*" *says god.*

What the random order test showed:

- Each passage reads as a short connected scene which means a coherent passage can be made from random phrases in a random order when pronouns and joining words are free.
- About half of the words in each passage were added (46 to 49 percent) which is the highest share in any test on this page because nothing in the set shared a subject and no phrase could be moved next to a phrase that fits.
- The three passages tell three different stories from the same 16 phrases (a wise man who hides and returns and a king who claims to be god and a people who thank god) which means the story comes from the AI model and the order of the phrases and not from the phrases themselves.
- The grades of 10 and 11 are lower than the grades of 12 to 14 for sorted passages because several phrases such as "of the guard left" and "but sent leanness" stay hard to follow even with words around them.
- The word "leanness" (which means hunger or wasting in the source psalm) was left as the source has the word and costs a point on the rule about explaining every label.
- The phrase "and killed mighty kings" appears in every passage with evil as the one that kills which means no passage presents the killing as good.

## Eight random phrases from the Charles selection kept in three random orders

Charles asked for the same random order test with half the number of phrases so a program drew a new set of 8 key phrases at random from the Charles selection and shuffled the set three times and the AI model connected the phrases in the exact shuffled order under the same rules.
The 8 phrases came from 8 different chapters in Jeremiah and Proverbs and Isaiah and Mark and Psalms and Matthew and John and a program check confirmed that the non-pronoun words of every phrase appear in each passage in the shuffled order.

The set of 8 phrases: "on them" and "and drives away his mother" and "he says" and "who deals wisely will" and "in the day" and "you will show yourself perfect" and "jesus began to preach" and "for in this the saying is true".

First random order (12 of 14 and 55 percent of the words were added):

- *god,* in the day *of the poor* you will show yourself perfect, for in this the saying is true: *a wicked son takes the house* and drives away his mother, *but a son* who deals wisely will *give the house to his mother.* "*blessed is the wise son,*" *the lord* says. jesus began to preach, *and the day was good* on *the people of the land.*

Second random order (13 of 14 and 44 percent of the words were added):

- *god made the day good* on *the people,* for in this the saying is true: "*with the good* you will show yourself perfect." jesus began to preach: "*the son* who deals wisely will *hear his father, but the wicked son takes the house* and drives away his mother in the day *of evil,*" he says.

Third random order (11 of 14 and 39 percent of the words were added):

- jesus began to preach in the day: "*god,* you will show yourself perfect. *the man* who deals wisely will *see good made* on *the poor. the wicked son sees the poor* and drives away his mother, for in this the saying is true: *'the evil heart knows no house,'*" he says.

What the smaller set showed:

- Eight phrases gave shorter and tighter passages (about 50 to 60 words against about 105 words for sixteen phrases) and the grades were a little higher (11 to 13 against 10 to 11) because fewer phrases mean fewer awkward fragments that need a home.
- The share of added words stayed about the same as with sixteen phrases which means the share depends on how unrelated the phrases are and not on how many phrases there are.
- All three passages share one story (a wise son and a wicked son and a saying that proves true) because two phrases in the set ("who deals wisely will" and "and drives away his mother") come from sayings about sons in Proverbs and pulled every passage toward the same subject.
- With sixteen phrases the three orders gave three different stories and with eight phrases the three orders gave one story told three ways which suggests that a small set is steered by its few strong phrases while a large set leaves more room for the joiner.
- The phrase "and drives away his mother" appears in every passage as the act of a wicked son which means no passage presents driving a mother from her home as good.

## A guess at how a reader with no background would take the three eight-phrase passages

Charles asked the AI model to imagine a person who scrolls a discussion site without posting and who meets each of the three eight-phrase passages with no notice that an AI model joined the passages.
Every line in this section is a guess by the AI model and no real reader was asked.

- First passage: the imagined reader probably takes the passage for a loose Bible paraphrase about a good son and a bad son because the wise son and the wicked son are easy to follow and the reader probably stumbles on the last sentence because "the day was good on the people of the land" is not how people talk.
- Second passage: the imagined reader probably finds this passage the clearest of the three because the passage is short and has one speaker and one contrast and the reader might assume the passage is a real verse from an unfamiliar translation.
- Third passage: the imagined reader probably gets lost in the middle because "see good made on the poor" does not parse on a first read and the quoted saying "the evil heart knows no house" sounds like a proverb the reader has never heard which could make the reader doubt the source.
- Across all three: the lowercase letters and the missing apostrophes are the most likely first thing the imagined reader notices and a reader who knows the Bible well would likely notice that Jesus is quoting lines that the gospels never give him.
- The guess points to one practical risk: a reader could take a passage for a real Bible quote which is why the warning near the top of this page matters wherever a passage is posted.

## Unique word rule: every word in a passage is different where readability allows

Charles added a rule for every selection: as long as the readability grade stays high the AI model picks added words so that as few words as possible repeat inside one passage and the AI model also uses the pronoun rule and the rule about the word "the" to remove repeats that sit inside the source phrases.
A repeat stays only where removing the repeat would break a sentence or where the repeat sits inside a source phrase and is not a pronoun and is not the word "the".

The three eight-phrase passages again under the unique word rule:

First random order (12 of 14 and 47 different words out of 49 words where the earlier version had 44 different words out of 66):

- *lord,* in the day you will show yourself perfect, for in this *a* saying is true: *one wicked son takes house* and drives away his mother, *but he* who deals wisely will *give her land.* "*blessed are those wise,*" *god* says. jesus began to preach *with people* on *earth.*

Second random order (12 of 14 and 42 different words out of 44 words where the earlier version had 42 different words out of 55):

- *god made good* on *people,* for in this the saying is true: "you will show yourself perfect." jesus began to preach: "*a son* who deals wisely will *hear, but one wicked takes house* and drives away his mother in *an evil* day," he says.

Third random order (11 of 14 and 46 different words out of 48 words where the earlier version had 42 different words out of 51):

- jesus began to preach in the day: "*god,* you will show yourself perfect. *a man* who deals wisely will *see good made* on *poor people. one wicked son hears* and drives away his mother, for in this *that* saying is true: *'evil hearts make dead land,'*" he says.

What the unique word rule changed:

- Almost every word is now different (only the words "in" and "will" repeat in each passage because both words sit twice inside the source phrases and neither word is a pronoun).
- The passages became shorter because repeated naming words such as "son" and "house" and "god" had to be used once each which forced one mention to carry the meaning.
- The grades stayed within one point (12 and 12 and 11 against 12 and 13 and 11) and the second passage lost a point because dropping "the" and "of" to avoid repeats left clipped wording such as "one wicked takes house".
- The rule and the readability rules pull in opposite directions past a certain point because natural English repeats small words such as "the" and "a" and "of" many times and a passage with no repeats starts to read like a telegram.
- The rule applies to every selection from here on and the older passages on this page were written before the rule.

## Open vocabulary rule: any English word may be added or swapped in to keep every word different

Charles added a rule for all three selections: when the unique word rule would hurt readability the AI model may reach for almost any word in the English language and may replace or delete a repeated word inside a source phrase so that every word in a passage stays different and the passage still reads well.
Before this rule the added words had to come from the generic list or from the special words of the selection or from the passage itself.

The three eight-phrase passages again under the open vocabulary rule:

First random order (13 of 14 and up from 12 with 53 different words out of 53 words and 49 percent of the words added or changed):

- *lord,* in the day *of trouble* you will show yourself perfect, for *through* this *an old* saying is true: *one cruel son seizes a house* and drives away his mother, *while another* who deals wisely *shall shelter her.* "*blessed are such children,*" *god* says. jesus began to preach *that message* on *every hillside.*

Second random order (13 of 14 and up from 12 with 50 different words out of 50 words and 44 percent of the words added or changed):

- *kindness rests* on *ordinary people,* for in this the saying is true: "you will show yourself perfect *toward anyone merciful.*" jesus began to preach: "*a child* who deals wisely *shall prosper, but one cruel heir grabs every room* and drives away his mother *during her* day *of need,*" he says.

Third random order (13 of 14 and up from 11 with 43 different words out of 43 words and 37 percent of the words added or changed):

- jesus began to preach in the day: "*father,* you will show yourself perfect. *whoever* deals wisely *shall pour kindness* on *strangers. a selfish man hoards* and drives away his mother, for *through* this *one* saying is true: *'greed empties any home,'*" he says.

What the open vocabulary rule changed:

- Every word in all three passages is now different and all three grades rose to 13 because words such as "shelter" and "trouble" and "greed" say exactly what a sentence needs where the short special list had forced clipped wording such as "takes house".
- Three source words were replaced to remove repeats: the second "in" became "through" in two passages and "in the" became "during her" in one passage and the second "will" became "shall" in all three passages.
- The passages now hold words that appear nowhere in the Charles selection which means the passages have moved one more step away from the Bible text and toward free writing by the AI model around eight fixed phrases.
- The share of added or changed words is 37 to 49 percent of each passage and the choice of each outside word (for example "greed" as the cause of the son driving away his mother) is an interpretation by the AI model.

## A short passage from each selection under the full current rule set

A program drew 8 key phrases at random from each of the three selections and put each set in one random order and the AI model connected each set in that exact order under every rule on this page including the unique word rule and the open vocabulary rule.
Added or changed words carry stars and a program check confirmed that no word repeats inside any of the three passages.

Claude selection (12 of 14 with 58 different words out of 58 words) from the eight phrases in this drawn order: "before you" and "that he" and "whoever shall put away his wife" and "if only you god" and "ask of the father" and "for they think" and "than these is of the evil one" and "dont sound a trumpet":

- *mercy walks* before *every traveler, so* that he *who stumbles finds welcome.* whoever shall put away his wife *must first weigh her sorrow.* if only you, god, *would soften hard hearts!* ask of *your* father *plainly,* for *proud people* think *louder prayers win; anything showier* than these *quiet words* is *from* the evil one. dont sound a trumpet.

Charles selection (12 of 14 with 48 different words out of 48 words) from the eight phrases in this drawn order: "they were exceedingly astonished" and "who are these" and "whatever you will ask" and "from a far country yes" and "and a spirit of justice to him" and "his disciples asked him about the parable" and "for justice but behold oppression" and "for those":

- *villagers* were exceedingly astonished: "who are these *strangers?*" "whatever you will ask," *came one reply* from a far country, "yes, and *true* spirit of justice to *any judge.*" his disciples asked him about the parable. "*people hoped* for *fairness,* but behold, oppression *arrived instead; stand alongside* those *crushed.*"

Words of Jesus (13 of 14 with 48 different words out of 48 words) from the eight phrases in this drawn order: "and tell him friend" and "that you dont expect him" and "therefore dont be afraid" and "get behind me satan" and "from one end of" and "sitting in sackcloth" and "in yourselves" and "he doesnt stumble":

- "*visit your neighbor* and tell him, 'friend, *comfort comes at an hour* that you *cannot* expect; therefore dont be afraid.' *if dread speaks, reply,* 'get behind me, satan.' from one end of *earth people mourn,* sitting in sackcloth; *carry light with*in yourselves, *because whoever does so* doesnt stumble."

Notes on the three short passages:

- In the Claude selection passage the second "you" was avoided by turning "before you" into "before every traveler" and the second "of" became "from" and the second "the" became "your".
- In the Charles selection passage the second "justice" became "fairness" and "to him" became "to any judge" and the last "for" became "stand alongside".
- In the words of Jesus passage the second "dont" became "cannot" and the second "in" became part of "within" and one "him" was deleted and the passage is read as spoken by Christ.
- The word "sackcloth" (a rough cloth worn by people in mourning) stays as the source has the word and the added words "people mourn" explain the word in the same sentence.
- The full list of rules in force is on the page named bible-quote-builder-current-rules in this folder.

## Phrases matched to a news headline: one passage from each selection

Charles gave the AI model a headline that read "JUST IN: Anthropic says developing Opus 5.5 cost more than $10 billion" and asked for a guess at the Bible phrases that relate most to the headline with one passage from each selection.
The AI model did not check whether the headline is accurate and treats the headline only as a topic which is the cost of building something very large.
A program searched each selection for key phrases that hold words about cost and building and treasure and wisdom and the AI model picked seven or eight of the matching phrases by hand and chose their order which means this test uses deliberate choosing where the tests just above used random draws.
Every rule on the page named bible-quote-builder-current-rules applied and a program check confirmed that no word repeats inside any of the three passages.

Claude selection (12 of 14 with 73 different words out of 73 words) from the chosen phrases "and a time to build up" and "than much fine gold" and "whatever you spend beyond that" and "when he had spent all of it" and "for where your treasure is" and "they dont toil" and "that which is complete has come" and "so your barns will be filled":

- *every season holds birth* and a time to build up; *knowledge shines brighter* than much fine gold. whatever you spend beyond that *sum, somebody repays later.* when he had spent all of it, *one young heir felt hunger,* for where your treasure *sits, hearts settle too. lilies grow though* they dont toil. *once the thing* which is complete has come, *partial efforts fade,* so *shared* barns will be filled *with bread, never pride.*

Charles selection (13 of 14 with 40 different words out of 40 words) from the chosen phrases "this man began to build" and "and is not able to finish" and "and count the cost" and "man have of all his labor" and "god gives wisdom knowledge" and "than gold yes" and "and without price":

- *neighbors laughed:* "this man began to build *yet cannot* finish." *first sit down, then* count the cost. *what profit does anyone* have of all his labor? god gives wisdom, knowledge, *worth more* than gold, yes, *freely offered* and without price.

Words of Jesus (13 of 14 with 58 different words out of 58 words) from the chosen phrases "desiring to build a tower" and "and count the cost" and "if he has enough to complete it" and "who owed him ten thousand talents" and "for where your treasure is" and "wisdom is justified" and "by her children" and "and build bigger ones":

- "*anyone* desiring to build a tower *must sit first* and count the cost, *asking* if he has enough *that can* complete it. *one servant* who owed *his master* ten thousand talents *learned mercy;* for where your treasure *lies, there attention follows.* wisdom is justified by her children, *not through plans which tear down barns then raise* bigger ones."

Notes on the matched passages:

- The words of Jesus selection held the closest match because the source has a saying about a person who wants to build a tower and first counts the cost to see whether the money is enough to finish.
- The phrase "ten thousand talents" names a very large debt in a parable (a talent was a large weight of silver) and was picked because the headline is about a very large sum.
- The passages lean toward caution about cost because the matching phrases in the source are mostly warnings about counting the cost and about treasure and the lean is a property of the phrases the search found and is not a judgment by the AI model about any company.
- Which phrases relate most to a headline is a guess and a different person would likely pick different phrases.

## Input quote rule: the passage may be shaped into an answer or reflection on a quote that Charles gives

Charles added a rule for every selection: when Charles gives an input quote such as a headline the AI model may add or delete or change any word so that the passage reads as a plausible answer or reflection on that quote as long as the change raises readability or relevance.
Before this rule the added words could only serve readability and the tie to the input quote came only from which phrases were picked.

The three headline passages again under the input quote rule (the input quote was "JUST IN: Anthropic says developing Opus 5.5 cost more than $10 billion" and the AI model did not check whether the quote is accurate):

Words of Jesus (13 of 14 with 67 different words out of 67 words and 55 percent of the words added or changed):

- "*engineers* desiring to build a tower *of thought must sit first* and count the cost, *asking* if *ordinary people have* enough *bread while work continues until crews* complete it. *one servant* who owed *his master* ten thousand talents *was forgiven; let such sums teach mercy,* for where your treasure *lies, there attention follows.* wisdom is justified by her children, *not through spending which only raises* bigger ones."

Charles selection (13 of 14 with 49 different words out of 49 words and 51 percent of the words added or changed):

- *onlookers said:* "this man began to build *yet cannot* finish." *when builders report spending billions,* count the cost *twice. what lasting gain does anyone* have of all his labor? god gives wisdom, knowledge, *worth more* than gold, yes, *shared freely* and without price; *may costly machines serve hungry neighbors.*

Claude selection (13 of 14 with 82 different words out of 82 words and 52 percent of the words added or changed):

- *every age knows planting* and a time to build up; *some builders now pour billions into thinking machines, prizing knowledge more* than much fine gold. whatever you spend beyond that *sum, ask who benefits.* when he had spent all of it, *one young heir felt hunger,* for where your treasure *sits, hearts settle too. lilies grow though* they dont toil. *once the thing* which is complete has come, *let its makers share,* so *common* barns will be filled *with bread, never pride.*

What the input quote rule changed:

- Each passage now speaks to the topic of the quote in plain words such as "billions" and "thinking machines" and "engineers" where the earlier versions only hinted at the topic through towers and barns.
- All three passages reached 13 of 14 and every word in each passage is different.
- About half of the words in each passage now come from the AI model which is the highest share for any passage built from chosen phrases.
- The passages take the form of a reflection (count the cost and ask who benefits and share what is built) because the chosen Bible phrases are mostly cautions about cost and treasure and the reflection is not a verdict by the AI model on any company or on whether the quote is true.
- The AI model that wrote these passages is made by the company named in the quote which is a reason for a reader to weigh the reflection with extra care.
- The words of Jesus passage puts modern words such as "engineers" beside phrases from the gospels and a reader could take the passage for a real saying which is why the warning near the top of this page applies with special force here.

## A second Claude selection that shares no book with the other two selections

Charles invited the AI model to pick its own passages again with one limit which is to avoid the ten books Charles picked and the words of Jesus in the four gospels so that the three selections no longer overlap.
The second Claude selection holds 35 passages (about 6600 words and 1554 different key phrases) from books outside the ten books Charles picked and outside the four gospels: Genesis 1 and Genesis 11 (the tower of Babel) and Exodus 20 and Deuteronomy 6 and Ruth 1 and First Samuel 16 and First Kings 3 and First Kings 19 and Job 28 and Job 38 and Song of Solomon 8 and Lamentations 3 and Ezekiel 37 and Amos 5 and Micah 4 and Micah 6 and Habakkuk 3 and Acts 2 and Acts 17 and First Corinthians 12 and 13 and Second Corinthians 4 and Galatians 5 and Ephesians 4 and Philippians 2 and 4 and Colossians 3 and Hebrews 11 and James 1 and 2 and 3 and First Peter 4 and First John 4 and Revelation 21.
The AI model picked passages about making and building and wisdom and love and justice and shared life because those subjects kept coming up in the experiments on this page.
The earlier Claude selection of 41 passages was used for every Claude selection result above this section and the second Claude selection is used from this section on.

- The special naming words are now god and love and earth and man and body and day and lord and spirit and people and light and heart and name.
- The special action words are now made and know and give and saw and seen and called and walk and live and says and make and asked and keep.
- The special describing words are now good and great and living and whole and holy and just and pure and new.

Two passages from the second Claude selection under all sixteen rules:

Reflection on the input quote "JUST IN: Anthropic says developing Opus 5.5 cost more than $10 billion" (13 of 14 with 62 different words out of 62 words) from the phrases "lets build ourselves a city" and "and a tower whose" and "they had brick" and "but where will wisdom be found" and "man doesnt know its price" and "it cant be valued" and "with the gold of ophir" and "the price of wisdom is above rubies" and "but we have this treasure":

- *people once said,* "lets build ourselves a city and *one* tower whose *top touches heaven;*" they had brick. *today engineers stack billions instead,* but where will wisdom be found? man doesnt know its price; it cant *get* valued with *any* gold *dug from distant mines. such understanding ranks* above rubies, *yet* we have this treasure *inside ordinary clay jars, so share freely.*

Eight random phrases kept in a random order (12 of 14 with 44 different words out of 44 words) from the phrases "which you have chosen" and "and a new earth" and "the wormwood" and "as it is today now" and "by the roots" and "the language of all the earth" and "and of thick darkness" and "if you have understanding":

- *bless every path* which you have chosen, and *bring* a new earth. *sorrow tastes like* wormwood, *bitter* as it is today; now *pull grief up* by *its* roots. *speak* the language of all *peoples; lead nations away from* thick darkness, if *they hold* understanding.

Notes on the second Claude selection:

- The new selection held closer matches to the headline than the old selection did because Genesis 11 is the story of people building a city and a tower out of brick and Job 28 is a poem that asks where wisdom is found and says that gold cannot buy wisdom.
- In the headline passage the place name "ophir" was replaced with "dug from distant mines" under the name rule and the second "price" and the second "wisdom" were replaced to keep every word different.
- In the random passage the word "wormwood" (a bitter plant that stands for sorrow in the source) is explained by the added word "bitter".
- The key phrase program with the three selection buttons now uses the second Claude selection while the two older programs (letters and single words) still use the first Claude selection.

## Opening line rule: each passage starts from one keyword of the input quote

Charles added a rule for every selection: when Charles gives an input quote the passage opens with the line "when you thought of" followed by one keyword or phrase taken from the input quote and then "i thought of" and the rest of the passage is arranged as a plausible continuation of that line of thinking.
The opening line itself repeats the words "thought" and "of" because the line is a fixed formula and every other word in the passage is still different.
The opening line is not starred because the line is the same in every passage and only the keyword changes.

The three headline passages again under the opening line rule (the input quote was "JUST IN: Anthropic says developing Opus 5.5 cost more than $10 billion" and the AI model did not check whether the quote is accurate):

Words of Jesus with the keyword "cost" (13 of 14 with 71 different words out of 73 words):

- "when you thought of 'cost,' i thought of *engineers* desiring to build a tower: *each must sit first* and count *expenses, asking* if *ordinary people have* enough *bread while work continues until crews* complete it. *one servant* who owed *his master* ten thousand talents *was forgiven; let such sums teach mercy,* for where your treasure *lies, there attention follows.* wisdom is justified by her children, *not through spending which only raises* bigger ones."

Charles selection with the keyword "ten billion dollars" (13 of 14 with 53 different words out of 55 words):

- when you thought of 'ten billion dollars,' i thought of *onlookers saying,* "this man began to build *yet cannot* finish." *so* count the cost *twice. what lasting gain does anyone* have *from* all his labor? god gives wisdom, knowledge, *worth more* than gold, yes, *shared freely* and without price; *may costly machines serve hungry neighbors.*

Claude selection with the keyword "developing" (13 of 14 with 69 different words out of 71 words):

- when you thought of 'developing,' i thought of *folk who once said,* "lets build ourselves a city and *one* tower whose *top touches heaven;*" they had brick. *today engineers stack billions instead,* but where will wisdom be found? man doesnt know its price; it cant *get* valued with *any* gold *dug from distant mines. such understanding ranks* above rubies, *yet* we have this treasure *inside ordinary clay jars, so share freely.*

What the opening line rule changed:

- The opening line tells a reader at once that the passage is a response to something another person said which removes the risk that the passage looks like a free-standing Bible quote.
- Each selection took a different keyword ("cost" and "ten billion dollars" and "developing") because each selection holds phrases that fit a different part of the quote.
- The sentence that used to carry the topic in the middle of each passage (for example "when builders report spending billions") could be dropped because the opening line now carries the topic.
- In the words of Jesus passage the word "cost" in the source phrase "and count the cost" became "expenses" because the keyword in the opening line had already used the word.
- The passages are reflections on the topic of the quote and are not verdicts by the AI model on any company and the AI model is made by the company named in the quote.

## Passages for a second input quote about a very large video game

The input quote was "Like Rockstar's CEO said, GTA 6 might be the last game in human history built at this scale, this much time, this much money. AI is getting so much better that even the non-believers are getting converted." and the AI model did not check whether the quote is accurate.
All seventeen rules applied and added or changed words carry stars and the clean versions without stars are on the page named bible-quote-builder-best-outputs in this folder.

Words of Jesus:

- "when you thought of 'this scale,' i thought of *vineyard workers:* so the last will be first. heaven and earth *shall* pass away, *yet makers keep pouring;* they put new wine *into fresh skins, though anyone tasting* old *vintage* immediately desires *it again. friends* of little faith, *ask whom such craft serves, then* dont doubt: *whoever trusts me can* do greater works *than these.*"

Charles selection:

- when you thought of 'non-believers,' i thought of *those disciples who watched,* but some doubted. *nobody gets scolded over* unbelief; *god says,* "*watch me* do a new thing," *while elders* remember former things *long past. every age has its* time to build up, *one for breaking* down, and another generation comes. *still, nothing stays novel* under the sun.

Claude selection:

- when you thought of 'built at this scale,' i thought of *babel:* the whole earth *spoke* one language. "now nothing will be withheld which they intend to do." *yet* god scattered them abroad. for *today people* see in part; *once whatever* is complete has come, *giant projects fade.* "*look:* all things *are being made* new," *says a voice;* first *attempts* have passed away.

## Full context opening rule: the opening sentence explains what the passage answers

Charles changed the opening line rule for every selection: the opening sentence still uses the form "when you thought of ... i thought of ..." and now has no length limit and must give a reader full context which means the first half restates the part of the input quote being answered in plain words and the second half says which Bible material the passage draws on and why.
The opening sentence is written by the AI model and carries no stars and is exempt from the unique word rule because a clear sentence needs to repeat small words and the body after the opening sentence still has no repeated word.

Passages for the input quote about a very large video game:

Words of Jesus:

- "when you thought of the claim that one video game may be the last ever built at such a huge scale of time and money, i thought of the old sayings about workers who were hired last and about new wine and old wine, because those sayings ask who a great work is for: so the last will be first. heaven and earth *shall* pass away, *yet makers keep pouring;* they put new wine *into fresh skins, though anyone tasting* old *vintage* immediately desires *it again. friends* of little faith, *ask whom such craft serves, then* dont doubt: *whoever trusts me can* do greater works *than these.*"

Charles selection:

- when you thought of the line that artificial intelligence is improving so fast that even people who doubted are now being won over, i thought of the disciples who doubted and of the old teaching that every generation builds up and breaks down: *those disciples watched,* but some doubted. *nobody gets scolded over* unbelief; *god says,* "*watch me* do a new thing," *while elders* remember former things *long past. every age has its* time to build up, *one for breaking* down, and another generation comes. *still, nothing stays novel* under the sun.

Claude selection:

- when you thought of a game that might be the last thing in human history built at this scale, i thought of the tower of babel, which is the oldest story about people building something enormous together and about what came after: the whole earth *spoke* one language. "now nothing will be withheld which they intend to do." *yet* god scattered them abroad. for *today people* see in part; *once whatever* is complete has come, *giant projects fade.* "*look:* all things *are being made* new," *says a voice;* first *attempts* have passed away.

Passages for the input quote about the cost of developing an AI model:

Words of Jesus:

- "when you thought of the report that developing one artificial intelligence model cost more than ten billion dollars, i thought of the saying about a builder who sits down to count the cost before starting a tower: *anyone* desiring to build a tower *must sit first* and count the cost, *asking* if *ordinary people have* enough *bread while work continues until crews* complete it. *one servant* who owed *his master* ten thousand talents *was forgiven; let such sums teach mercy,* for where your treasure *lies, there attention follows.* wisdom is justified by her children, *not through spending which only raises* bigger ones."

Charles selection:

- when you thought of a price above ten billion dollars for building one thinking machine, i thought of the proverbs that weigh wisdom against gold and of the man who started building and could not finish: *onlookers said,* "this man began to build *yet cannot* finish." *so* count the cost *twice. what lasting gain does anyone* have *from* all his labor? god gives wisdom, knowledge, *worth more* than gold, yes, *shared freely* and without price; *may costly machines serve hungry neighbors.*

Claude selection:

- when you thought of the huge effort of developing a new artificial intelligence model, i thought of the people who built a city and a tower out of brick and of the poem that asks where wisdom can be found: *folk once said,* "lets build ourselves a city and *one* tower whose *top touches heaven;*" they had brick. *today engineers stack billions instead,* but where will wisdom be found? man doesnt know its price; it cant *get* valued with *any* gold *dug from distant mines. such understanding ranks* above rubies, *yet* we have this treasure *inside ordinary clay jars, so share freely.*

What the full context opening changed:

- A reader who has not seen the input quote can now tell what was said and what the passage is answering because the opening sentence carries both.
- The opening sentence also names the Bible material that follows (for example the tower of babel or the saying about counting the cost) which tells a reader that the body is built from Bible phrases.
- The word "cost" returned to the source phrase "and count the cost" in the words of Jesus passage because the opening sentence no longer has to stay free of repeats.
- The AI model did not check whether either input quote is accurate and the passages are reflections on the topic and not verdicts on any company or any person.

## Closing explanation rule: one or two plain sentences after the remix say what the remix meant

Charles added a rule for every selection: after the remixed passage the AI model adds a second paragraph of one or two sentences that explains in plain words what the passage just said and the explanation may reuse words from the passage or from the input quote.
The unique word count starts fresh for the closing explanation which means no word repeats inside the explanation while the explanation may share words with the passage above it.
The closing explanation sits outside the quote marks in the words of Jesus passages because the explanation is written by the AI model and is not read as spoken by Christ.

Closing explanations for the input quote about a very large video game:

- Words of Jesus: put plainly: size never proves worth. a project gains meaning when its makers serve others, so even small efforts done with trust may outlast giant ones.
- Charles selection: in short: doubt is normal whenever something new appears. each generation builds, tears down, then watches another begin, which means today's marvel will feel ordinary soon.
- Claude selection: meaning: people working together can build almost anything, yet no giant project lasts forever. what stays is whatever gets made new after old attempts pass away.

Closing explanations for the input quote about the cost of developing an AI model:

- Words of Jesus: simply said: before spending huge sums, builders should ask whether ordinary people still have bread. wisdom shows itself through what a tower does for others, not by its size.
- Charles selection: plainly: money can start a building without finishing it. wisdom is worth more than gold, so costly machines matter only if they feed hungry neighbors.
- Claude selection: in other words: bricks and billions build towers, but neither buys wisdom. that treasure already sits inside ordinary people, which is why sharing matters more than stacking.

What the closing explanation changed:

- A reader now gets the point of each passage in everyday words without having to decode the Bible phrases which is the part of the output that comes closest to full marks on the seven sentence rules.
- A program check confirmed that no word repeats inside any of the six closing explanations.
- Each closing explanation is an interpretation by the AI model of a passage that the AI model also assembled which means the explanation shows what the AI model meant and does not show what the Bible phrases mean in their own setting.
- The full paragraphs with the openings and the passages and the closing explanations together are on the page named bible-quote-builder-best-outputs in this folder.

## Charles removed Proverbs from the Charles selection

Charles removed the book of Proverbs from the Charles selection which now holds nine whole books: Psalms and Ecclesiastes and Isaiah and Jeremiah and Matthew and Mark and Luke and John and Romans.
The selection now has 40721 different key phrases (down from 43651) and every Charles selection result above this section used the ten-book version.

- The special describing words changed because "wise" and "poor" had ranked high mainly through Proverbs and the list is now good and evil and great and wicked and righteous and holy and high and right and blessed and dead and first and mighty.
- A check confirmed that every phrase in the two Charles selection passages for the input quotes comes from the nine remaining books so the bodies of both passages stay the same.
- One opening sentence had described its material as "the proverbs that weigh wisdom against gold" and now reads "the old songs and sayings that weigh wisdom against gold" because the phrases in that passage come from Psalms and Ecclesiastes and Isaiah and Luke.

A fresh passage from the nine-book selection (12 of 14) from eight random phrases kept in this drawn order: "his teeth will be set" and "and you taught" and "your pomp is brought down to sheol" and "now that disciple was" and "how long shall i take counsel" and "on every lofty mountain" and "i give you authority to tread" and "and the wizards":

- *whoever eats sour grapes,* his teeth will be set *aching, just as elders* taught. your pomp is brought down *into the grave, proud ruler.* now that disciple was *asking,* "how long shall i take counsel *alone?*" on every lofty mountain *streams begin flowing. heaven gives* you authority to tread *safely past snakes* and *leave* wizards *behind.*

- Closing explanation: roughly: pride ends low, bad choices bring their own ache, yet lonely worry gives way once help arrives like water from high ground.
- The place name "sheol" became "the grave" under the name rule and a program check confirmed that no word repeats inside the passage or inside the closing explanation.

## A false added claim that Charles caught and the claim check rule

Charles pointed out that one line the AI model had added to the Charles selection passage about the video game was false: the line read "nobody gets scolded over unbelief" and people who do not share a belief system are very often challenged or argued with or looked at strangely or abandoned.
The line was also the reverse of its source because the source phrase was "because of your unbelief" from Matthew 17 where the speaker tells his followers that they failed because of unbelief and the AI model had deleted the word "because" and turned a rebuke into a reassurance.

- The line now reads "doubters often hear blame because of unbelief" which keeps the source phrase whole and matches what happens to people who doubt.
- The closing explanation now reads "doubt is normal whenever something new appears, though doubters frequently get blamed" and the prediction "today's marvel will feel ordinary soon" was softened to "may feel ordinary later" because the AI model has no evidence for a firm prediction.
- Rule 20 on the rules page now requires a check of every added sentence for claims about how people get treated or how the world works.
- Other added lines in the finished paragraphs are also claims by the AI model and not by the Bible (for example "size never proves worth" and "whatever you spend beyond that sum, somebody repays later") and a reader is right to test each added line the same way.

## Pro-human expression rule: a last pass before every output

Charles added a rule for every output: before a passage goes out the AI model makes one more pass over the word choices with a lean toward valuing human beings who put their heart and soul into words for the world to hear.
The pass keeps three things in view: a person who speaks up may be dehumanized or told that a real experience did not happen or abandoned and the passage says so truthfully where the subject comes up and the passage points toward continuing to speak because some listener may recognize themselves in the words.
The pass removes or rewords any added line that advises permanent silence or hiding (for example "it is good to be silent and never speak up") because that kind of line can push a reader who is already alone to stop reaching out.
No promise is made that speaking will be received well because rule 20 forbids claims that ordinary experience does not support and the passages use words such as "may" and "might" for what a listener will do.

The six input-quote passages again under the pro-human expression rule with added or changed words in stars:

Passages for the input quote about a very large video game:

Words of Jesus:

- "when you thought of the claim that one video game may be the last ever built at such a huge scale of time and money, i thought of the old sayings about workers who were hired last and about new wine and old wine, because those sayings ask who a great work is for: so the last will be first. heaven and earth *shall* pass away, *yet each human voice matters;* they put new wine *into fresh skins, though anyone tasting* old *vintage* immediately desires *it again. friends* of little faith, *keep speaking your heart even when crowds dismiss you, then* dont doubt: *whoever trusts me can* do greater works *than these.*"

- Closing explanation: put plainly: size never proves worth. a person sharing true feeling may get ignored, yet continuing matters because somebody listening could finally feel understood.

Charles selection:

- when you thought of the line that artificial intelligence is improving so fast that even people who doubted are now being won over, i thought of the disciples who doubted and of the old teaching that every generation builds up and breaks down: *those disciples watched,* but some doubted. *doubters often hear blame* because of unbelief; *still* god says, "*watch me* do *this* new thing." *every age has its season for building* up, *one where things break* down, and a time to speak: *so voice your heart, since* another generation comes *listening.*

- Closing explanation: in short: doubt is normal whenever something new appears, though doubters frequently get blamed. silence need not last; keep expressing yourself because later listeners might understand.

Claude selection:

- when you thought of a game that might be the last thing in human history built at this scale, i thought of the tower of babel, which is the oldest story about people building something enormous together and about what came after: the whole earth *spoke* one language. "now nothing will be withheld which they intend to do." *yet* god scattered them abroad, *so every person carries words others need.* for *today people* see in part; *once whatever* is complete has come, *giant projects fade.* "*look:* all things *are being made* new," *says a voice;* first *attempts* have passed away.

- Closing explanation: meaning: people working together can build almost anything, yet no giant project lasts forever. what endures is each human voice, so keep speaking even after being scattered.

Passages for the input quote about the cost of developing an AI model:

Words of Jesus:

- "when you thought of the report that developing one artificial intelligence model cost more than ten billion dollars, i thought of the saying about a builder who sits down to count the cost before starting a tower: *anyone* desiring to build a tower *must sit first* and count the cost, *asking* if *ordinary people have* enough *bread while work continues until crews* complete it. *one servant* who owed *his master* ten thousand talents *was forgiven; let such sums teach mercy,* for where your treasure *lies, there attention follows; make living persons that prize.* wisdom is justified by her children, *not through spending which only raises* bigger ones."

- Closing explanation: simply said: before spending huge sums, builders should ask whether ordinary people still have bread. wisdom shows itself through how a tower helps humans speak, live, and be heard.

Charles selection:

- when you thought of a price above ten billion dollars for building one thinking machine, i thought of the old songs and sayings that weigh wisdom against gold and of the man who started building and could not finish: *onlookers said,* "this man began to build *yet cannot* finish." *so* count the cost *twice. what lasting gain does anyone* have *from* all his labor? god gives wisdom, knowledge, *worth more* than gold, yes, *shared freely* and without price; *may costly machines feed hungry neighbors plus amplify unheard voices.*

- Closing explanation: plainly: money can start a building without finishing it. wisdom is worth more than gold, so costly machines matter only if they feed people and let them speak.

Claude selection:

- when you thought of the huge effort of developing a new artificial intelligence model, i thought of the people who built a city and a tower out of brick and of the poem that asks where wisdom can be found: *folk once said,* "lets build ourselves a city and *one* tower whose *top touches heaven;*" they had brick. *today engineers stack billions instead,* but where will wisdom be found? man doesnt know its price; it cant *get* valued with *any* gold *dug from distant mines. such understanding ranks* above rubies, *yet* we have this treasure *inside ordinary clay jars, so speak, share, keep telling your story.*

- Closing explanation: in other words: bricks and billions build towers, but neither buys wisdom. that treasure already sits inside ordinary people, which is why voicing your heart matters more than stacking.

What the pro-human expression pass changed:

- Each passage now has one line that values a person speaking (for example "keep speaking your heart even when crowds dismiss you" and "every person carries words others need" and "amplify unheard voices").
- The Charles selection passage about doubt gained the source phrase "and a time to speak" from Ecclesiastes and left out the neighboring source phrase about a time to keep silence because the pass does not present silence as standing advice.
- Each closing explanation now says in plain words that a person may be ignored or blamed and that continuing to speak still matters because a later listener might understand.
- A program check confirmed that no word repeats inside any passage body or inside any closing explanation.
- The pass makes every passage lean one way on purpose which means the passages are encouragement written by the AI model around Bible phrases and are not neutral summaries of what the Bible phrases say.

## Three words of Jesus passages for a playful input quote

The input quote was "I'VE SEEN YOU BEFORE JESUS!!!" (sent with three laughing faces) and all twenty-one rules applied with added or changed words in stars.

Attempt 1:

- "when you thought of shouting with laughter that you have seen me somewhere before, i thought of the day i told a new follower that i had already seen him under a fig tree before anyone introduced us: before philip called *anyone,* when *one man sat* under the fig tree, i saw *him. having walked beside people* such a long time, do you not know me? *go ahead,* laugh; *recognition feels funny. every face deserves being noticed first, so each listener gets named* friends."

- Closing explanation: plainly: being recognized feels good because someone noticed you. keep showing your real self, since another person might spot something familiar and smile.

Attempt 2:

- "when you thought of joking that my face looks familiar, i thought of the teaching that anyone who helps a hungry person or a stranger has already met me without knowing: i was a stranger and *somebody* took me in. *people asked,* "when did we see you?" *whatever kindness reached the* least of these my brothers, *that deed touched heaven. maybe every tired cashier, lonely neighbor, or laughing child showed this face earlier;* rejoice *together.*"

- Closing explanation: simply: you may have met something holy inside ordinary people already. treat each stranger warmly, because your kindness tells them their life matters.

Attempt 3:

- "when you thought of laughing that we have met before, i thought of the promise that friends who lose sight of each other for a little while will meet again with joy: a little while, and you will see me; i *shall greet everyone* again, *then* your heart *can* rejoice. *laughter fits such reunions.* because *some* have seen, *they believe; others* who *never looked still belong. keep telling what happened, since somebody listening may recognize their own story.*"

- Closing explanation: meaning: joy returns when separated friends meet again. share your experience even if people laugh, because one hearer could find comfort there.

- The three attempts draw on three different parts of the gospels: the saying to a new follower about a fig tree in John 1 and the teaching about strangers and the least of these in Matthew 25 and the promise of meeting again after a little while in John 16.
- The name "philip" stays in the first attempt because the AI model judged the name to be widely known.

## No labels on the reader rule: a last check for labels the reader did not choose

Charles added a rule for every output now and in the future: no line may put a label on the reader that the reader did not choose and no line may claim a relationship between the speaker and the reader because a stranger who reads "you are my friend" or "you are my disciple" has had a bond declared without consent.
The rule matters most for the words of Jesus passages because those passages are read as spoken by Christ and the source often addresses listeners with labels such as "friends" and "you of little faith".

Lines that the check changed:

- "every face deserves being noticed first, so each listener gets named friends" became "every face deserves being noticed first, while closeness stays each listener's own choice".
- "friends of little faith, keep speaking your heart even when crowds dismiss you" became "whenever faith runs low, keep speaking your heart even if crowds dismiss you" which also removes the label "of little faith" from the reader.
- "others who never looked still belong" became "others who never looked remain welcome" because "belong" claims membership for the reader and "welcome" is an offer.
- One opening sentence spoke of "friends who lose sight of each other" in a way that implied the speaker and the reader are friends and now says "people who lose sight of each other".
- Labels on people other than the reader stay where the source has the labels (for example "the least of these my brothers" and "those disciples watched") because those lines describe other people and do not address the reader.
- A program check confirmed that no word repeats inside the three changed passage bodies.
- The corrected full paragraphs are on the page named bible-quote-builder-best-outputs in this folder.

## Distance rule and story rule: no physical closeness toward the reader and no naming of the audience

Charles added two rules for every output now and in the future.
The distance rule says that no line may describe physical closeness between the speaker and the reader (for example the word "closeness" or touching or a hand on a shoulder or whispering in an ear) because a reader who meets that wording from a stranger pictures an uninvited person in their space and the wording is fine when the closeness happens between characters inside the story.
The story rule says that passages avoid naming the audience with words such as "listener" or "reader" or "hearer" because the passages are meant to be little stories and a line that points at the audience breaks the story.

Lines that the two checks changed:

- "while closeness stays each listener's own choice" became "what follows remains anyone's own decision".
- "since somebody listening may recognize their own story" became "since somebody elsewhere may recognize their own story".
- "because one hearer could find comfort there" became "because one person could find comfort there".
- "because somebody listening could finally feel understood" became "because somebody else could finally feel understood".
- "since another generation comes listening" became "since another generation comes afterward" and "later listeners" became "later people".
- "having walked beside people" and "that deed touched heaven" stay because both lines describe people and things inside the story and not the reader.
- A program check confirmed that no word repeats inside the changed bodies or closings.

## A refinement to the claim check: a failed claim may become a stated hope

Charles said that a line such as "i want a world where nobody gets scolded over unbelief" or "someday i believe there will be a world where nobody gets scolded over unbelief" is acceptable where the flat claim "nobody gets scolded over unbelief" was not.
The reason is that a hope tells a reader what the speaker wishes for and makes no false statement about how people are treated today and rule 20 on the rules page now lists a stated hope as a third way to repair a claim that fails the check.

- The Charles selection passage about doubt now reads "doubters often hear blame because of unbelief; someday, i hope, nobody gets scolded over questions" which keeps the truthful line and adds the hope beside it.
- A program check confirmed that no word repeats inside the changed passage body.

## No negative labels on the input rule

Charles added a rule for every output: no output may put a negative label on the input quote or on the person who wrote the input quote (for example "mocking" or "dumb" or "stupid") because a negative label judges the person before the reply has said anything and the one exception is naming explicit violence such as murder or rape or physical assault or contact without consent.

Lines that the check changed in the three passages about the chart of remote work automation:

- All three opening sentences had described the question as asked "in a mocking tone" and now say only that the question was asked.
- "what profit has any mocker" became "what profit has each worker" and "i want nobody mocked over needing income" became "i want everybody able to earn bread".
- "nobody deserves mockery when work disappears" was removed and "ridicule helps nobody" became "i hope that happens" and "laughing at someone losing wages gets everything backward" became "i want those gains shared among workers".
- "so nobody doing desk work deserves being called little" became "so desk work counts among needed tasks" because the earlier line argued with the wording of the input.
- One older opening sentence said "joking that my face looks familiar" and now says "saying with a laugh that my face looks familiar".
- The corrected passages are on the page named bible-quote-builder-best-outputs in this folder.

## First and Second Corinthians moved into My Personal Bible set

Charles added First Corinthians and Second Corinthians to My Personal Bible set which now holds eleven whole books and 43863 different key phrases.
The Claude selection gave up its three passages from those two letters (First Corinthians 12 and 13 and Second Corinthians 4) so that the sets do not overlap and took three passages in their place which are Galatians 6 verses 1 to 10 and First Thessalonians 5 verses 11 to 24 and First John 3 verses 11 to 18.

- The Claude selection still holds 35 passages and now has 1484 different key phrases.
- The special naming word "body" left the Claude list because that word had ranked high through First Corinthians 12 and the word "word" took its place.
- Outputs made before this change stay as they were and four of those earlier Claude outputs used phrases from the two letters (the body with many parts and the treasure in clay jars and seeing in part and being pressed on every side).
- From this point on every new Claude output draws only on the 35 passages listed in the builder script named claude_selection_third_version_builder.py in the folder named boring-things.

## A full check of every public output against all thirty rules

Charles asked for every output on the page named bible-quote-builder-best-outputs to be checked against every rule whenever a rule changes and the AI model made the first full check on the evening of 11 November 2026.

- Italics were missing from fourteen older paragraphs and their closings (the sets for the "seen you before" input and the video game input and the AI cost input and the random phrase set) and every one now shows added or changed words in italics.
- Three labels read "attempt 1" without brackets and now match the label form used everywhere else.
- Three lead-ins held a stray "of" (for example "the disciples who doubted and of the teaching") and now read cleanly.
- Four added claims were softened under the claim check: "being recognized feels good" became "can feel good" and "joy returns" became "joy often returns" and "comfort comes at an hour" became "comfort may come at an hour" and "that treasure already sits inside ordinary people" became "i believe that treasure already sits inside ordinary people".
- One paragraph from the Claude Bible set opened with the flat claim "mercy walks before every traveler" and now opens with the wish "may mercy walk before every traveler".
- The same paragraph had leaned toward praising quiet over speaking ("louder prayers" and "quiet words") which sat badly with the rule that values people speaking from the heart and the paragraph now says that giving needs no applause and ends "let real need speak freely instead".
- One paragraph addressed a "proud ruler" as "you" which a reader could take as a label and the line now reads "a proud ruler's pomp is brought down into the grave".
- "early communities shared bread" became "some communities shared bread" under the rule against saying how old the material is.
- A program check then confirmed that no word repeats inside any of the 48 bodies and closings on the page after one repeated word was fixed.
- Two things were left as they are and flagged: the phrase "ten thousand talents" (a very large debt in a parable) stays unexplained and three older outputs from the Claude Bible set still use phrases from First and Second Corinthians because those outputs were made before the two letters moved into My Personal Bible set.

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

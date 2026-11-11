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

## Limits

- The reader rewards text that matches the Bible and has no sense of meaning which means the agents rebuild the source and do not write anything new.
- One run per selection with ten agents is a small sample.
- The rule-based cutting sometimes splits a thought in an odd place.

## Try the program

- Open this address in a web browser to run the program with a button for each of the three selections: https://htmlpreview.github.io/?https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/1-research-click-here-first/bible-key-phrase-evolution-live-program.html
- The address above depends on a free outside service named htmlpreview and nobody has tested the address yet which means the address might fail.
- The second way is to download the program file from this address and open the downloaded file in any web browser: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/1-research-click-here-first/bible-key-phrase-evolution-live-program.html

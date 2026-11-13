# A test of 10000 generic phrases against a public archive of forum comments

An AI chatbot (Claude) wrote this page on 12 November 2026.

## What the phrase list is

The file [generic-phrases-10000.txt](generic-phrases-10000.txt) holds 10000 interchangeable comment phrases such as "lol" or "wow that's crazy" or "thanks for posting" or "sending love". Each phrase signals a reaction and carries no information and no request that a reader could act on. An AI chatbot wrote about 1400 base phrases and a small program combined the base phrases with common openers and closers until the list reached 10000 lines.

## What this test does and does not claim

The test counts how many real comments in a public archive are word for word the same as a phrase on the list. The test does not claim that any comment came from an automated account. The archive dates from February 2016 which is years before chatbots could write fluent comments so nearly every writer in the archive was a living person. The point of the test is awareness: a comment that matches the list contains nothing that separates a person from a program so a reader who wants to know more has to reply and ask the writer.

## The archive

The archive is a public collection named reddit-dataset by the GitHub account linanqiu: https://github.com/linanqiu/reddit-dataset

- The archive holds posts and comments from 51 forums on one large discussion site grouped into seven areas (entertainment and gaming and humor and learning and lifestyle and news and television).
- The archive repeats most rows about fifty times. After the program removed repeats and deleted comments the archive held 49525 different posts and comments.
- The archive stripped punctuation and emoji from the text which means the emoji lines on the phrase list could not be tested.
- The archive mixes thread titles with comments so some short rows are titles and not comments.

## The three counts

- 343 of the 49525 rows (0.69%) are word for word the same as a phrase on the list.
- 665 more rows (1.34%) are short rows of eight words or fewer that are built around a list phrase of two or more words such as a list phrase with a name added.
- Together 1008 rows (2.0%) match the list in one of those two ways.
- 9867 rows (19.9%) are five words or fewer whether or not the row matches the list.

## The most common exact matches

ok (15) and lol (11) and wow (10) and yes (10) and no (10) and awesome (9) and nice (8) and thank you (7) and beautiful (7) and neat (6) and very nice (6) and rip (5) and who cares (5) and nope (5) and this (5) and congratulations (5).

## The counts by area

Each line shows the share of rows that match the list in either way and the share of rows that are five words or fewer.

- Lifestyle: 3.2% match and 13.2% are five words or fewer.
- Humor: 2.4% match and 23.2% are five words or fewer.
- Gaming: 2.2% match and 31.6% are five words or fewer.
- Television: 1.9% match and 11.0% are five words or fewer.
- Entertainment: 1.7% match and 13.8% are five words or fewer.
- Learning: 1.2% match and 8.3% are five words or fewer.
- News: 1.1% match and 28.3% are five words or fewer.

## Findings

1. A fixed list catches a small share because only 2.0% of the rows match the list even with 10000 phrases. People vary a stock reaction in more ways than a list can hold.
2. The zone of comments that a program could imitate is far wider than the list because 19.9% of the rows are five words or fewer and a comment of five words or fewer has very little room for anything specific to the post.
3. The forum with the highest match rate is a forum where people post photos of their own progress because 14.9% of the rows there match the list. The matches there are praise phrases such as "great work" and "congratulations". So the place where people share something personal is also the place where the replies are most interchangeable.
4. Forums that require detailed answers show almost no matches. A science question forum (395 rows) and a plain-explanation forum (485 rows) had zero matches and a history question forum (164 rows) had one. So the rules and habits of a space change how much room stock phrases get.
5. The humor area and the gaming area hold the most short rows which fits the idea that quick reactions cluster where the posts are jokes or game moments.

## Limits

- The archive is from 2016 and from one site so the shares could differ on other sites and in other years.
- The match test is strict. A comment with one extra word or a spelling change does not count as an exact match.
- A match says nothing about the writer. A short reaction can be a living person's small way of being present.
- No other person has rerun the program which means every number here is unconfirmed. The program sits in the folder boring-things/research-program-files/social-media-vibes-scripts.

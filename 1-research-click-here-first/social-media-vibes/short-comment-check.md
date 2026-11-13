# The five-words-or-fewer check

An AI chatbot (Claude) wrote this page on 13 November 2026. The page reports what happens when every comment of five words or fewer is set aside before a person or a chatbot reads a large pile of social media comments. No other person has rerun the counts which means every number here is unconfirmed.

## What the check is

A program counts the words in each comment. A comment with five words or fewer goes into a separate pile. A comment with six words or more stays in the main pile for reading. The check needs one line of code and needs no judgment about meaning.

## What the check does to a large public archive

The archive is a public collection of 49525 different posts and comments from 51 forums on one large discussion site. The page named [generic-phrases-test.md](generic-phrases-test.md) in this folder describes the archive.

- 9867 of the 49525 rows have five words or fewer which is 19.9 percent of the rows.
- Those 9867 short rows hold about 1.5 percent of all the words in the archive. So the check sets aside one row in five and gives up very little text.
- The most common short rows are "ok" and "lol" and "wow" and "yes" and "no" and "awesome" and "nice" and "thank you".
- About one third of a random sample of 70 short rows were bare numbers or web links which are leftovers of how the archive was collected and not comments. So the check also clears out junk rows.

The share of rows at other cut-off points:

- One word or fewer: 7.7 percent of the rows.
- Three words or fewer: 13.2 percent of the rows.
- Five words or fewer: 19.9 percent of the rows.
- Eight words or fewer: 30.6 percent of the rows.
- Ten words or fewer: 36.8 percent of the rows.
- Twenty words or fewer: 58.5 percent of the rows.

The share of short rows differs by the kind of forum:

- Gaming forums: 31.6 percent of the rows have five words or fewer.
- News forums: 28.3 percent.
- Humor forums: 23.2 percent.
- Entertainment forums: 13.8 percent.
- Lifestyle forums: 13.2 percent.
- Television forums: 11.0 percent.
- Learning forums: 8.3 percent.

## What the check shows about the three threads in this folder

- The thread about a famous executive who lost his job: 18 of 171 comments have five words or fewer which is 10.5 percent. The middle comment runs 14 words. The short comments are quick reactions such as "Poor man." and "Doormat energy." and "Put him behind bars."
- The thread about blocking a chatbot on home wifi: 9 of 364 comments have five words or fewer which is 2.5 percent. The middle comment runs 33 words. The short comments are blunt commands and verdicts such as "Do it." and "Nope." and "Mate just send her packing."
- The thread about an executive who answered messages within minutes: 13 of 247 comments have five words or fewer which is 5.3 percent. The middle comment runs 20 words. The short comments are verdicts and dismissals such as "Are you dumb?" and "You should delete your account."
- The owner's 6020 public comments: 67 comments have five words or fewer which is 1.1 percent.

The three threads hold 40 short comments in total. None of the 40 short comments describes a behavior together with a reason for the behavior. So in these three threads the check would have set aside 40 comments and would have lost zero comments that teach a reader what to do and why.

The share of short comments also says something about the kind of thread. A thread built on a news story about a famous person drew the most short reactions. A thread where a person asked for advice drew long replies because advice takes room. So the share of short comments works as a quick reading of whether a crowd came to react or came to explain.

## What the check can lose

- A short comment can be a real invitation. The owner of this repository wrote the two words "go on" 49 times to ask another person to continue. The check would set those invitations aside.
- A short comment can be a real question. About 4.6 percent of the short rows in the archive begin with a question word such as "why" or "what" or "who". One short comment in the executive thread asks "Which one?"
- So the safer use is to set short comments aside in a separate pile and to keep the short questions for a second look. Deleting the short comments would throw away the invitations and the questions.

## What the check cannot do

- The check cannot catch a long comment that says nothing specific. A list of 10000 hollow phrases of six words or more matched 2 of the 39658 longer rows in the archive word for word. So a long hollow comment passes the length check and passes a phrase list too.
- The check does not save much reading by word count because the short rows hold about 1.5 percent of the words. The saving is in the number of items a reader has to judge which drops by about one fifth in the archive.

## How the check can help with a large pile of comments

1. Count the words in every comment and move the comments of five words or fewer into a separate pile.
2. Keep the short comments that begin with a question word or end with a question mark because a short question can open a conversation.
3. Give the main pile of longer comments to a person or a chatbot for closer reading such as looking for comments that describe a behavior a reader can picture.
4. Report the share of short comments as a finding because the share shows whether the crowd mostly reacted or mostly explained.

## How to rerun the counts

The counting program is the file named short-comment-check.py in the social-media-vibes-scripts folder inside the boring-things folder of this repository.

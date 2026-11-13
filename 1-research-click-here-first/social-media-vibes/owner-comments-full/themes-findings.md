# Themes in the owner's 6020 comments

An AI chatbot (Claude) ran two small studies on the 6020 comments in this folder with a counting program. No person has rechecked the counts which means every count on this page is unconfirmed.

## Study 1: how the themes move from the first comment to the last comment

The program cut the comments into ten equal slices in the order of the owner's export and measured what share of each slice mentions each theme. The program cannot tell whether the export order follows time so the word "early" on this page means early in the export.

- The phrase "emotional family" appears in 5 percent and 8 percent of the first two slices and then fades to almost zero in the last slices.
- The phrase "lizard brain" is absent from the first five slices and then appears in 11 percent of slice six and 7 percent of slice seven before fading to 1 percent.
- The word "pro-human" sits at 3 percent or lower for the first six slices and then reaches 12 percent and 20 percent and 21 percent and 17 percent in the last four slices.
- Mentions of gaslighting or dehumanization climb from 2 percent in the first slice to 33 percent in the ninth slice.
- Mentions of society or power structures or capitalism climb from 15 percent in the first slice to 41 percent in the ninth slice.
- Mentions of AI or chatbots rise from 13 percent in the first slice to 48 percent in slice six and then fall to 16 percent in the last slice.
- Mentions of God or Jesus or scripture stay at 3 percent in the first two slices and reach 22 percent in the last slice.
- Mentions of emotions stay high in every slice and range from 46 percent to 72 percent.
- Comments that open with a lowercase letter rise from 2 percent in the first slice to 67 percent in slice eight and then fall to 35 percent in the last slice.
- Comments that contain a swear word rise from 2 percent in the first slice to about 30 percent in slices eight and nine.

One possible reading is that the early comments mostly describe an inner world of emotions and the later comments mostly describe how other people and people holding power treat people who are suffering. Another possible reading is that each coined term such as "emotional family" or "lizard brain" or "pro-human" marks a chapter where a new idea took over the work of an older idea. Both readings are guesses by the chatbot because the counts show which words appear and cannot show why the owner chose the words.

## Study 2: what job each emotion gets

The program collected the words that sit within seven words of each emotion name and kept the words that cluster around one emotion more than around the other emotions.

- Loneliness appears in 491 comments and pulls the words "connection" (80 times) and "meaningful" (90 times) and "deep" (52 times).
- Boredom appears in 344 comments and pulls the words "meaningful" (52 times) and "conversation" (28 times) and "creative" (17 times).
- Doubt appears in 367 comments and pulls the words "questions" (37 times) and "clarity" (19 times) and "answer" (17 times).
- Anger appears in 285 comments and pulls the words "boundary" (17 times) and "crossed" (16 times) and "arms" (12 times) which matches comments that picture anger as a guardian with crossed arms.
- Fear appears in 714 comments which makes fear the most named emotion and fear pulls the words "prepare" (28 times) and "void" (34 times).

The separate word clusters fit the idea that each emotion carries a separate set of instructions in the owner's writing because loneliness and doubt and anger each sit beside words for a different need. Boredom and loneliness both pull the words "meaningful" and "conversation" and the two emotions appear together in 179 comments which suggests that boredom and loneliness ask for the same thing in the owner's writing and that thing is deep meaningful conversation. Doubt and fear appear together in 238 comments which is the most common pair.

Four emotions could not be read by this method. The words around guilt and annoyance and frustration and sadness come mostly from passages that repeat word for word across many comments so those four clusters show copied text and not a pattern.

## How to rerun the counts

The counting program is the file named count-themes.py in the social-media-vibes-scripts folder inside the boring-things folder of this repository.

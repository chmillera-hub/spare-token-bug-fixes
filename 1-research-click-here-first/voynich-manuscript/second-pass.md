# A second pass on the Voynich spelling-pattern tests

November 12 2026

## What this page is

The page named findings.md in this folder reports spelling-pattern tests on the Voynich manuscript which is a handwritten book from the early 1400s that nobody has been able to read. The page named findings.md says no other person has rerun the tests. This page reports a second pass by an AI chatbot (Claude) in a new working session on 12 November 2026.

The second pass had three parts.

- Part one reran the four original programs without any change to see whether the same numbers come out.
- Part two wrote a new program that shares no code with the original programs to see whether the main result survives different measuring choices.
- Part three recounted the pages that end at a paragraph end and added a check that does not depend on marks added by the people who typed the text.

A second pass by the same kind of AI chatbot is weaker evidence than a rerun by a person because the same kind of chatbot could repeat the same kind of mistake.

## Words used on this page

- A folded sheet is one large piece of calfskin folded in half which gives two leaves and four pages.
- The sheet partner of a page is the page that sits beside that page when the folded sheet is opened flat.
- The forward step goes from the back of the first leaf of a folded sheet to the front of the second leaf of the same folded sheet.
- The backward step goes from the back of the second leaf of a folded sheet to the front of the first leaf of the same folded sheet.
- A "next page" score ranks the true page among all candidate pages by the same scribe in the same section so 0.50 means chance and 1.00 means the top match.

## Part one: the original programs give the same numbers again

The typed copies of the manuscript came from two public GitHub repositories because the workspace of the chatbot could not reach the site voynich.nu. The two repositories held files with identical digital fingerprints and one repository lists the same fingerprint for the copy named ZL version 3b dated 13 May 2025.

Every number that the rerun printed matched the page named findings.md.

- The back of a leaf as the continuation of the front of the same leaf scored 0.67 across 68 leaves again.
- The facing page in the bound book scored 0.54 across 46 pairs again.
- The forward step scored 0.79 across 26 sheets again and the sheet partner was the top match in 9 of 26 cases again.
- The backward step scored 0.54 across 31 cases again.
- A different sheet in the same bundle scored 0.51 across 83 comparisons again.
- All 36 measurement settings printed again and the forward step scored between 0.54 and 0.88 across the 36 settings while the backward step scored between 0.40 and 0.63.

## Part two: a new program with different measuring choices

Every measuring choice in the new program was fixed before the first run because the page named findings.md warns that several versions were tried before the final version. The new program differs from the original programs in four ways.

- The new program reads the typed copy with a parser written from scratch.
- The new program compares the last third of the lines of one page with the first third of the lines of another page where the original programs compared four lines with four lines.
- The new program counts two-letter chunks where the main original test counted three-letter chunks.
- The new program measures closeness with a different formula (a formula named Jensen-Shannon divergence which compares how often each chunk appears).

Results of the new program on the copy named ZL (the copies named IT and RF gave results within 0.05 of the ZL results on every line):

- The forward step scored 0.78 across 30 sheets which agrees with the original 0.79.
- A shuffle test put a randomly chosen candidate page in place of the true sheet partner 100000 times and no shuffle scored as high as 0.78 which means the forward step result is very unlikely to be luck.
- The facing page in the bound book scored 0.54 across 44 pairs which agrees with the original 0.54.
- The back of a leaf as the continuation of the front of the same leaf scored 0.73 across 74 leaves which is a little higher than the original 0.67.
- The backward step scored 0.63 across 35 cases which is higher than the original 0.54.

## The part of the original finding that looks weaker

The page named findings.md says the hand of a scribe moved one way through each folded sheet because the forward step scored 0.79 and the backward step scored 0.54. The second pass supports a softer version of that claim.

- The backward step in the new program scored 0.63 and resampling the 35 cases gave a likely range from 0.52 to 0.73 which sits above chance.
- The gap between the forward step (0.78) and the backward step (0.63) was 0.15 and a shuffle of the forward and backward labels produced a gap that large about 3 times in 100.
- A wrong-ends control compared the top lines of the first page with the bottom lines of the sheet partner which reverses the direction of reading. The wrong-ends control scored 0.67 and the right ends scored 0.78.
- The right ends beat the wrong ends on 14 sheets and lost on 10 sheets and tied on 6 sheets and a sign-flip test produced a gap that large about 7 times in 100.

Here is a guess about what the numbers mean. Two effects could be mixed together. The first effect could be that all four pages of one folded sheet share spelling habits because a scribe wrote the whole folded sheet in one sitting. The second effect could be a smaller extra match in the forward direction because the scribe wrote the four pages in order. The second pass supports the first effect strongly and supports the second effect only weakly because 3 in 100 and 7 in 100 are not rare enough to rule out luck.

## Part three: pages that end at a paragraph end

The page named findings.md says 176 of 177 pages with running text end exactly at a paragraph end. No program for that count was in the repository so the chatbot wrote a new counting program.

- The recount found 175 of 176 ordinary pages ending at a paragraph end and 204 of 206 pages when the fold-out pages are included. The recount is one page away from the original count and the reason for the one-page gap is unknown.
- The count has a weak spot because the paragraph-end marks were added by the people who typed the text. A typist could mark the bottom of every page as a paragraph end by habit.
- A line-length check avoids the weak spot because a line that ends a paragraph usually stops short of the right margin. Lines inside a paragraph were shorter than 0.8 of the usual line length on the same page only 7 percent of the time (3012 lines). Lines that end a paragraph in the middle of a page were that short 75 percent of the time (472 lines). The last line of a page was that short 85 percent of the time (175 pages).

The line-length check supports the claim that pages end where paragraphs end because the last line of a page behaves like a paragraph-ending line and not like a line inside a paragraph.

## What stays unproven

- No person has rerun either pass which means every number on this page is still unconfirmed by a human.
- The second pass used the same typed copies as the first pass so a mistake inside the typed copies would affect both passes.
- The second pass cannot show whether the writing has meaning because spelling habits could drift in the same way in real language and in invented filler.
- The chatbot still could not open the full journal article from October 2026 about folded sheets so the overlap with that article is still unknown.

## How to check this page

The programs are named second_pass.py and paragraph_ends.py and sit in the folder boring-things/research-program-files/voynich-scripts in this repository. Both programs need Python with the numpy package and the three typed copies inside a folder named data. The program second_pass.py takes a few minutes and the program paragraph_ends.py takes a few seconds.

## Who made this page

An AI chatbot (Claude) ran the tests and wrote this page.

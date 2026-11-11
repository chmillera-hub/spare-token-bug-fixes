# Voynich manuscript page-order tests and text evolution experiments

This folder holds plain-language findings and the scripts behind the findings so that a future researcher can rerun every number.
One AI model (Claude) ran every test in a single working session on 11 November 2026 and no other person has rerun the tests yet which means every number here is a single unconfirmed analysis.

## Part 1: Voynich manuscript

The Voynich manuscript is a handwritten book from the early 1400s that remains unread because no proposed decoding has survived checking by other researchers.
The tests here do not decode any word because the tests only count spelling patterns in a typed copy of the text (a "transcription" which means volunteers replaced each symbol with a keyboard letter).

### Method

The main test gives a "next page" score to a pair of pages by comparing three-letter chunks in the last four lines of one page with the first four lines of another page because the spelling habits of a writer drift slowly and pages written back to back share habits.
The score ranks the true candidate page among all candidate pages by the same scribe in the same section so 0.50 means chance and 1.00 means the top match.

### Results

- The back of a leaf scored 0.67 as the continuation of the front of the same leaf across 68 leaves which shows the test detects real back-to-back writing.
- The facing page in the bound book scored 0.54 across 46 pairs which is near chance and suggests the bound order is not the writing order.
- The step from the back of the first leaf of a folded sheet to the front of the second leaf of the same folded sheet scored 0.79 across 26 sheets and the sheet partner was the top match in 9 of 26 cases where chance predicts about 2.
- The same sheet partner in the reverse direction scored 0.54 across 31 cases which suggests the scribe's hand moved one way through each folded sheet.
- A different sheet in the same bundle scored 0.51 across 83 comparisons which suggests the effect belongs to the single folded sheet and not to the bundle.
- The pattern held in three transcriptions (ZL and IT and RF) and under 36 measurement settings.
- 176 of 177 pages with running text end exactly at a paragraph end which means almost no paragraph runs across a page break.
- The 24 folded sheets by scribe 1 in the plant section differ along one main word-habit contrast and sheets in the same bundle sit close together on the contrast (about 1 chance in 800 under shuffling) which could mean the binder kept piles of sheets together.
- Sheets by different scribes matched in word mix at 0.30 and sheets by the same scribe matched at 0.53 while two halves of one sheet matched at 0.56 which argues against a separate cipher for every sheet and leaves a per-scribe difference open.

### What is not new and what might be new

A study published in October 2026 in the journal Digital Medievalist ("Singulion Structure and the Voynich Manuscript") had already reported that the two halves of a folded sheet resemble each other more than facing pages do.
The direction test and the same-bundle control and the paragraph-end count might be additions but the author of this folder could not open the full journal article to check.

### Limits

- The test tracks the order in which a scribe wrote and cannot show the order a reader was meant to follow.
- The order of the sheets remains unknown because sheet-to-sheet scores were only slightly above chance.
- Several versions of the analysis were tried before the ranking version which raises the risk of a lucky result.

### Files

- `voynich/t4.py` holds the main "next page" test and the 36-setting robustness grid.
- `voynich/t5.py` holds the same-bundle control and the sheet-to-sheet tests.
- `voynich/t6.py` and `voynich/t7.py` hold the word-habit contrast among sheets and the bundle clustering test.
- The scripts expect the transcription files `ZL3b-n.txt` and `IT2a-n.txt` and `RF1b-e.txt` in a `data/` folder and the files are available from the site voynich.nu.

## Part 2: splitting a book into piles to hide the meaning

The test cut a public-domain biology book (Project Gutenberg book number 2009) into 1000 equal pages and dealt the pages into four piles in four ways.
A "confusion score" for a pile is 100 minus the average of three surviving connection percentages (next page in the same pile and similar pages in the same pile and other uses of rare words in the same pile) and no human readers were tested.

- The whole book scores 0 by definition.
- Four quarters in book order score about 35.
- Four random piles score about 75 because luck leaves about a quarter of neighboring pages together.
- Dealing in strict turns scores about 86 because no two neighboring pages share a pile.
- A deal tuned by computer search scores about 90.
- 972 of 999 page breaks in the biology book cut a sentence while the Voynich manuscript ends a paragraph at 176 of 177 page ends which suggests the Voynich manuscript would be hard to hide by whole-page splitting.

File: `page-splitting/split_test.py` expects the book text at `data/origin_of_species_2009.txt`.

## Part 3: copy-and-paste text evolution

A pool of 300 strings starts as single letters and each paste copies one string with a chance of an added letter or a letter swap or a letter change and no deleting.
A "reader" chooses which strings get copied and the reader is a letter-pattern scorer and not a mind.

- With no reader the pool becomes gibberish with about 1 percent real words.
- A reader who copies the most English-looking string freezes the pool on a two-letter word because every added letter looks worse.
- Forcing one letter onto every string at intervals breaks the freeze and a forced letter every 5 minutes of experiment time gave 90 percent real words across 135 letters while a forced letter every second gave about 2 percent real words.
- A reader with a bonus for command patterns (action word then pointing word then thing word) evolved commands only when partial credit existed as stepping stones (about 1 to 2 commands per string with partial credit and 0 without).
- A reader who favors closeness to a list of 10000 sensible commands reached an exact command such as "wash my dogs" within about 15 to 28 minutes of experiment time with no forcing and about 80 percent of the pool became the same single command.
- Forced letters hurt the closeness reader because a fixed target has a fixed length and extra letters only move a string away from the target.
- Known loophole: a letter changed into a space beside another space disappears because the scripts merge double spaces which works as a hidden form of deleting.

Files: `text-evolution/evolution_forced_letters.py` (letter-pattern reader) and `text-evolution/exp.js` (command-pattern reader) and `text-evolution/cmds.js` plus `text-evolution/near.js` (10000-command closeness reader) and `text-evolution/live_page.html` (a live page with sliders that runs in a web browser).

# Centering histogram bars on whole numbers

## Link to the original question

https://ask.sagemath.org/question/83318/

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 with matplotlib version 3.11.2 (the drawing library that the Sage histogram command uses according to a comment on the question) and no other person has rerun the test yet which means the page is unconfirmed. The Sage command itself was not tested.

## The question

On 4 July 2025 somebody asked on the SageMath question board how to make the bars of a histogram of whole numbers sit symmetrically around each value.
The call histogram([1,1,1,1,1,1,2,1,1,2,2,2,2,4,4,3,4]) drew the bar for 1 shifted to the right and the bar for 4 shifted to the left and the asker had nudged the data by hand as a workaround.
A commenter pointed toward matplotlib and the question had zero answers when the board was read on 12 November 2026.

## What the test shows

- The default call cuts the range from 1 to 4 into 10 equal bins with edges 1.0 and 1.3 and 1.6 and so on. The value 1 falls into the bin from 1.0 to 1.3 (drawn to the right of 1) and the value 4 falls into the bin from 3.7 to 4.0 (drawn to the left of 4) which is exactly the shift in the question.
- With bin edges at the half numbers 0.5 and 1.5 and 2.5 and 3.5 and 4.5 the four bars were centered at exactly 1 and 2 and 3 and 4 and the counts were 8 and 5 and 1 and 3 which matches the data.

## Best-guess answer

Giving the bin edges at half numbers fixes the picture without touching the data.
In matplotlib:

bins = np.arange(min(data) - 0.5, max(data) + 1.5, 1)
plt.hist(data, bins=bins, rwidth=0.9)

In Sage the matching call worth trying is histogram(data, bins=[0.5, 1.5, 2.5, 3.5, 4.5]) because the Sage command passes the bins option on to matplotlib as far as the page author knows and that call was not tested for this page.

The test file named centred_bars.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.

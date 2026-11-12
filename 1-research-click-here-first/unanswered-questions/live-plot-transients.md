# Keeping fast spikes visible in a live matplotlib plot while drawing fewer points

## Link to the original question

https://discourse.matplotlib.org/t/26255

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the tests in a single chat on 12 November 2026 on matplotlib version 3.11.2 without a screen and no other person has rerun the tests yet which means the page is unconfirmed. The timings come from a machine without a display so the timings are rough and the page answers only the parts of the post that a test could settle.

## The question

On 29 July 2026 somebody on the matplotlib forum described a live display of sensor data arriving at about 2000 samples per second: a rolling line plot with a spectrogram below.
The asker reported a sharp drop in frame rate after adding the spectrogram and visible skipping after bursts and lost spikes when thinning the data and asked four things about figure layout and burst handling and live plotting versus logging and the choice of display backend.
The post had zero replies when the forum list was read on 12 November 2026.

## What the tests show

- Thinning by keeping every 10th sample lost a one-sample spike of height 25 in the test.
- Thinning by keeping the smallest and the largest value of every screen column kept the spike. The test drew 1600 points in place of 8000 points and the largest drawn value was still 25.
- Redrawing the line took about 48 milliseconds with all 8000 points and about 23 milliseconds with the 1600 smallest-and-largest points.
- Redrawing the spectrogram picture took about 16 milliseconds while computing the spectrogram numbers took about 0.06 milliseconds so the drawing costs far more than the mathematics.

## Best-guess answer for the tested parts

The smallest-and-largest thinning answers the question about plotting every sample while staying fast because every spike survives and the number of drawn points depends on the width of the screen and not on the amount of data:

def minmax_decimate(y, columns):
    n = (y.size // columns) * columns
    blocks = y[:n].reshape(columns, -1)
    out = np.empty(columns * 2)
    out[0::2] = blocks.min(axis=1)
    out[1::2] = blocks.max(axis=1)
    return out

One possibility for the frame rate drop is the cost of redrawing the spectrogram picture on every frame so redrawing the spectrogram on every fifth or tenth frame while the line updates on every frame is worth testing.

## What stays open

The questions about two figures versus one figure and about live plotting versus logging and about the best display backend were not tested because the test machine had no display.

The test file named live_plot_speed.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.

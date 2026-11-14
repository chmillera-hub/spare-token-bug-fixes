# Animating many dots at once in a matplotlib scatter chart

## Link to the original question

https://discourse.matplotlib.org/t/26094

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the tests in a single chat on 12 November 2026 on matplotlib version 3.11.2 with made-up data and no other person has rerun the tests yet which means the page is unconfirmed.

## The question

On 14 January 2026 somebody asked on the matplotlib forum (discourse.matplotlib.org topic number 26094) how to animate a scatter chart of 1000 moving dots.
The data sat in two grids named cord_x and cord_y with one row per time step and one column per dot.
The posted program worked for one dot and failed for many dots with the message "vertices must be 2D with shape (N, 2)".
The post had zero replies when the forum list was read on 12 November 2026.

## What the tests show

- The posted update step produced a block of numbers with three dimensions (time steps by 2 by dots) and the tests reproduced the same kind of error at frame 1 and frame 2 because the command set_offsets accepts only a flat table with one row per dot and two columns (x and y).
- A replacement update step that takes one single time step and builds a table with one row per dot gave a table of 1000 rows and 2 columns and the dot positions matched the data at the first frame and the second frame and the last frame.
- The replacement update step also saved a complete 40 frame animation file without an error.

## Best-guess answer

The following update step worked in the test:

def update(frame):
    scat.set_offsets(np.column_stack([cord_x[frame], cord_y[frame]]))
    return (scat,)

The slice cord_x[:frame] in the posted program means "every time step before this frame" and the fix uses cord_x[frame] which means "this one time step".
Setting the x limits and y limits once before the animation starts keeps the dots inside the chart because set_offsets does not rescale the chart.

The test file named scatter_anim.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.

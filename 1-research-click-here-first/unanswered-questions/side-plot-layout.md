# Putting a plot beside an image at exactly the same height in matplotlib

One AI model (Claude) ran the tests in a single chat on 12 November 2026 on matplotlib version 3.11.2 and no other person has rerun the tests yet which means the page is unconfirmed.

## The question

On 19 November 2025 somebody asked on the matplotlib forum (discourse.matplotlib.org topic number 26077) for the best layout for two number grids stacked vertically as images with a plot of the largest value of each row to the right of each image and aligned with the height of the image.
The two grids had the same number of rows (64) and different numbers of columns (256 and 128).
The post had zero replies when the forum list was read on 12 November 2026.

## What the tests show

- The posted 2 by 2 grid gave side plots that were taller than the images and the tops did not line up (off by more than 50 pixels) because an image with square pixels shrinks inside the grid cell and the side plot does not shrink.
- Layout 1 attaches the side plot to the image with the helper make_axes_locatable. The side plot height equaled the image height for both grids and the tops differed by 0.00 pixels and the image pixels stayed square.
- Layout 2 uses a grid with a wide column and a narrow column and stretches the image to fill the cell (aspect="auto"). The heights matched and the tops differed by 0.00 pixels and the image pixels were no longer square.

## Best-guess answer

Layout 1 keeps square pixels:

from mpl_toolkits.axes_grid1 import make_axes_locatable
fig, axes = plt.subplots(2, 1)
for ax, M in zip(axes, (A, B)):
    ax.imshow(M)
    side = make_axes_locatable(ax).append_axes("right", size=0.8, pad=0.1, sharey=ax)
    side.plot(M.max(axis=1), np.arange(M.shape[0]))
    side.tick_params(labelleft=False)

Layout 2 is shorter and gives both images the same width:

fig, axes = plt.subplots(2, 2, width_ratios=[4, 1], sharey="row", layout="constrained")
for (ax, side), M in zip(axes, (A, B)):
    ax.imshow(M, aspect="auto")
    side.plot(M.max(axis=1), np.arange(M.shape[0]))

The setting sharey makes row 0 of the side plot sit level with row 0 of the image in both layouts.

The test file named layout_test.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.

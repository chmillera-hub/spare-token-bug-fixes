# Why an image drawn with imshow lands in the wrong place on a polar chart

## Link to the original question

https://discourse.matplotlib.org/t/26078

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the tests in a single chat on 12 November 2026 on matplotlib version 3.11.2 with a small made-up array and no other person has rerun the tests yet which means the page is unconfirmed.

## The question

On 19 November 2025 somebody asked on the matplotlib forum (discourse.matplotlib.org topic number 26078) why a large grid of depth values looked wrong on a polar chart (a round chart where position is given by a compass angle and a distance from the center).
Each column of the grid had a compass direction between 214 and 314 degrees and each row had a tilt angle above or below the horizon.
The posted program drew the grid with the command imshow and the asker reported a wrong angle range and clipping at the top and distance labels that did not match the data.
The post had zero replies when the forum list was read on 12 November 2026.

## What the tests show

- With imshow the colored area covered compass angles from 180 to 360 degrees when the data belonged between 214 and 314 degrees. The command imshow draws a flat rectangular picture and does not bend the picture around the center of a polar chart.
- With imshow the distance axis ran from about 100 to 2127 because the posted program handed the smallest and largest depth values to imshow as the edges of the picture. Depth is the quantity shown by color so the depth values do not belong on the distance axis.
- With the command pcolormesh the colored area covered compass angles from 214 to 315 degrees which matches the data. The command pcolormesh receives the angle of every column and a distance for every row and bends each cell into the correct wedge.

## Best-guess answer

Replacing imshow with pcolormesh fixed the angle range in the test:

theta = np.radians(orientations)
radius = inclinations - inclinations.min()
mesh = ax.pcolormesh(theta, radius, depth[::rf, ::rf], cmap="viridis", shading="auto")
ax.set_rlim(0, radius.max())
fig.colorbar(mesh, ax=ax, label="depth (m)")

The lists theta and radius need the same thinning as the grid (orientations[::rf] and inclinations[::rf]) when the grid is thinned with rf.
Using the tilt angle as the distance from the center is an assumption made for this page because the post did not say which quantity belongs on the distance axis.

The test file named polar_image.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.

# Drawing one value per cell position as colour on a U-shaped outline in matplotlib

## Link to the original question

https://discourse.matplotlib.org/t/26080

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) wrote the drawing program and ran the program in a single chat on 12 November 2026 on matplotlib version 3.11.2 with made-up numbers and no other person has rerun the program yet which means the page is unconfirmed.

## The question

On 26 November 2025 somebody asked on the matplotlib forum whether pyplot can show a cell death percentage for each of 20 cell positions as colour intensity on a drawing shaped like an intestinal crypt (a U-shaped pocket) in place of an ordinary line chart.
The asker proposed making a heatmap and warping the picture into the crypt shape and mirroring the picture.
The post had zero replies when the forum list was read on 12 November 2026.

## What the program does

The answer is yes and no picture warping is needed because matplotlib can draw each cell directly as a small four-sided patch placed along a curve.

- A helper function describes the centre line of half a crypt: a quarter circle at the bottom followed by a straight wall going up.
- The centre line is cut into 20 equal pieces and each piece becomes one patch with a fixed thickness.
- Every patch is drawn twice (once on the right and once mirrored on the left).
- A PatchCollection colours the patches from the list of 20 values and supplies the colour bar.

## What the checks show

- The program drew 40 cells (20 positions on each side).
- Position 5 (the largest made-up value) came out darker than position 1.
- The left copy and the right copy of every position received the same colour.
- The picture named crypt-example.png in this folder shows the result: a red U shape with the darkest cells at positions 4 and 5 and position numbers beside the wall.

## Best-guess answer

Replacing the made-up list named index in the program with the real 20 percentages gives the wanted picture.
The radius of the bottom curve and the length of the wall and the cell thickness are three numbers at the top of the helper function that can be changed to match a real crypt drawing.

The program named crypt_heatmap.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.

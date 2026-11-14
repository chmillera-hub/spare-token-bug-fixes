# Speeding up point-inside-polygon lookups with one bulk call

## Link to the original question

https://discuss.python.org/t/88825

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 with the Python library shapely version 2.2.0 on made-up data and no other person has rerun the test yet which means the page is unconfirmed. The real script and data of the asker were not used so the page tests one part of the problem only.

## The question

On 19 April 2025 somebody asked on the Python help forum how to speed up a script that takes more than two weeks for one year of data.
The script checks more than a million drifting particles every hour for 30 days against 207 coral reef polygons with a loop that builds one point per particle and asks a spatial index and runs a "within" test.
The post had zero replies when the forum list was read on 12 November 2026.

## What the test shows

The test used 207 irregular made-up polygons and 200000 made-up particle positions for one time step.

- A loop with one point object and one index lookup per particle took about 1.6 seconds for 200000 particles (measured on 20000 particles and scaled up).
- One bulk call for all particles took 0.10 seconds which is about 16 times faster.
- Both methods agreed on which particles are inside a polygon.
- Scaled to one million particles and 720 hourly steps the loop needs about 1.6 hours and the bulk call needs about 6 minutes.

## Best-guess answer

The bulk route in shapely 2 replaces the inner loop with two calls:

tree = shapely.STRtree(polygons)                      # built once
pts = shapely.points(xs, ys)                          # all particle positions of one time step
pt_idx, poly_idx = tree.query(pts, predicate="within")

The result is two lists of matching numbers: particle number and polygon number for every particle that sits inside a polygon.
Even the loop in the test is far faster than two weeks so one possibility is that most of the run time of the real script sits somewhere other than the lookup (for example reading the data file hour by hour or building objects inside the loop) and timing each part of the real script is the step that would show where the two weeks go.

The test file named point_in_polygon.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.

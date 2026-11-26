# Programs behind the shadow test

These eight Python programs produced the numbers and the pictures on the page named shadow-finding.md in the Mobius strip folder. Each program needs Python with the numpy and scipy and pillow and matplotlib packages. Each program takes the name of an output folder as the last word of the command.

- shadow_variety.py builds the sphere and the flat circle and the flat square and the cube and the lumpy rock and the untwisted loop and the Mobius strip and counts the different shadows of each shape and counts openings and dents and runs the reshaping pools.
- shadow_stretchproof.py repeats the count after stretching every shadow to an even spread so that stretched copies of one shadow count as one shadow.
- wavy.py builds the wavy shapes and counts the different shadows. The command word plain gives the ordinary count and the command word proof gives the count with stretching removed.
- wavy_fine.py repeats the count for the sphere and the cube and the wavy sphere and the wavy cube at the stricter setting of 8 parts in 100.
- hole_light.py traces the lit patch that passes through the middle of the Mobius strip at tilts from 0 to 90 degrees in twelve directions and draws the picture of the lit patch.
- reverse_test.py searches 1200 poses for look-alike pictures to measure how well the pose of the strip can be read back from the lit patch alone and from the whole shadow and checks that a left-handed strip in the right pose casts the same shadow as a right-handed strip.
- make_full_gallery.py draws every different shadow of each shape.
- make_wavy_gallery.py draws the five most different shadows of each wavy shape after wavy.py has been run with the command word plain.

The file named shadow_results.json holds the ordinary counts and the file named stretchproof_results.json holds the counts with stretching removed and the file named hole_light_results.json holds the size and shape of the lit patch at every tested tilt. The file named reverse_results.json holds the numbers from the reverse test.

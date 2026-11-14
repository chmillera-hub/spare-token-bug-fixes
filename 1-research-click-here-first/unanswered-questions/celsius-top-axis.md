# A second axis in degrees Celsius with ticks exactly above the data points

## Link to the original question

https://discourse.matplotlib.org/t/26117

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 on matplotlib version 3.11.2 with made-up data and no other person has rerun the test yet which means the page is unconfirmed.

## The question

Somebody asked on the matplotlib forum (discourse.matplotlib.org topic number 26117 created 13 February 2026) whether a chart with inverse temperature on the x axis (1 divided by the temperature in Kelvin) can carry a second axis that shows degrees Celsius with the ticks lined up with the data points and not with the ticks of the first axis.
The asker had tried the commands ax.secondary_xaxis and ax.twiny without success.
The post had zero replies when the forum list was read on 12 November 2026.

## What the test shows

The second axis is possible with ax.secondary_xaxis because that command accepts a pair of conversion formulas and a hand-picked list of tick positions.
In the test the top axis showed the labels 25 and 50 and 100 and 200 and 400 and each top tick sat exactly above the matching data point (a sideways gap of 0.0 pixels).

## Best-guess answer

The following lines worked in the test where temps_c holds the Celsius temperature of every data point:

secax = ax.secondary_xaxis("top", functions=(lambda x: 1.0 / x - 273.15, lambda c: 1.0 / (c + 273.15)))
secax.set_xticks(temps_c)
secax.set_xlabel("temperature (°C)")

The first formula turns an x value (1/K) into Celsius and the second formula turns Celsius back into an x value.
The command set_xticks is the step that puts the ticks above the data points because the ticks are given in Celsius at the measured temperatures.
Matplotlib can print a "divide by zero" warning while setting up the axis because matplotlib tries the formulas on the value 0 and the warning did not change the result in the test.

The test file named celsius_axis.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.

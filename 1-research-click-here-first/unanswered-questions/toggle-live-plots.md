# Switching between two live charts in one matplotlib window

One AI model (Claude) ran the test in a single chat on 12 November 2026 on matplotlib version 3.11.2 without a screen and no other person has rerun the test yet which means the page is unconfirmed.

## The question

On 19 December 2025 somebody asked on the matplotlib forum (discourse.matplotlib.org topic number 26086) about a small-screen Raspberry Pi project with a live 2 by 2 grid of charts and a live scatter chart.
The asker wanted to know whether clearing a figure keeps the window open and whether two live views can be toggled and what the best method for switching is.
The post had zero replies when the forum list was read on 12 November 2026.

## What the test shows

The test kept one single figure and switched the view four times.

- Calling fig.clf() removed every chart from the figure and the figure number stayed 1 and the window object stayed the same object and the count of open figures stayed 1. Clearing a figure therefore does not close the window.
- After each switch the figure held 4 charts (the grid view) or 1 chart (the scatter view) as expected.
- A key press handler switched the view when the t key event arrived.

## Best-guess answer

One figure with one redraw function per view worked in the test:

def draw_grid():
    fig.clf()
    axes = fig.subplots(2, 2)
    (draw the four live charts on axes)

def draw_scatter():
    fig.clf()
    ax = fig.add_subplot(1, 1, 1)
    (draw the live scatter chart on ax)

A variable remembers which view is active and a timer made with fig.canvas.new_timer(interval=1000) calls the active redraw function once per second and a key press handler or a button flips the variable.
The timer and the key press were tested without a real screen so behavior on a real Raspberry Pi display is untested.

The test file named toggle_views.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.

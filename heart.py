import math
import textwrap
import time
import tkinter
import turtle


HEART_COLOR = "blue"      
BACKGROUND = "white"
TEXT_COLOR = "deeppink"
HEART_SIZE = 11          
BEATS_PER_SECOND = 0.85   


screen = turtle.Screen()
screen.setup(700, 800)
screen.bgcolor(BACKGROUND)
screen.title("For You")

# Ask for the name and the message
name = screen.textinput("Her name", "Whose heart is this for?") or "My Love"
message = screen.textinput("Your message", "Write something to make her smile:") \
    or "You are loved, today and always."

screen.tracer(0)  

# Heading with her name
title_pen = turtle.Turtle(visible=False)
title_pen.penup()
title_pen.color(TEXT_COLOR)
title_pen.goto(0, 240)
title_pen.write(name, align="center", font=("Georgia", 40, "bold"))

# Message, wrapped so long messages fit on the screen
message_pen = turtle.Turtle(visible=False)
message_pen.penup()
message_pen.color(TEXT_COLOR)
wrapped = textwrap.fill(message, width=38)
lines = wrapped.count("\n") + 1
message_pen.goto(0, -230 - 26 * lines)
message_pen.write(wrapped, align="center", font=("Georgia", 18, "italic"))

# The heart
heart_pen = turtle.Turtle(visible=False)
heart_pen.color(HEART_COLOR, HEART_COLOR)
heart_pen.pensize(2)


def draw_heart(scale):
    """Redraw the heart at the given size."""
    heart_pen.clear()
    heart_pen.penup()
    heart_pen.begin_fill()
    for step in range(101):
        t = 2 * math.pi * step / 100
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        heart_pen.goto(x * scale, y * scale + 20)
        heart_pen.pendown()
    heart_pen.end_fill()


def bump(phase, centre, width):
    """A smooth little hill, used to make each 'thump' of the heartbeat."""
    return math.exp(-((phase - centre) / width) ** 2)


start = time.perf_counter()

try:
    while True:
        # phase goes 0 -> 1 once per heartbeat
        phase = ((time.perf_counter() - start) * BEATS_PER_SECOND) % 1
        pulse = bump(phase, 0.12, 0.05) + 0.6 * bump(phase, 0.32, 0.06)
        draw_heart(HEART_SIZE * (1 + 0.12 * pulse))
        screen.update()
        time.sleep(0.02)
except (turtle.Terminator, tkinter.TclError):
    pass  # the window was closed
from turtle import *

def triangle (line_length, line_width, colour):
    pensize (line_width)
    color (colour)
    for i in range(3):
        forward(line_length)
        right(120)
        
triangle (200, 20, 'red')
penup()
goto(-200, -300)
pendown()
triangle (100, 10, 'green')
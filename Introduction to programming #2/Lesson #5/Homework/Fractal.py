from turtle import *

def fractal (order, size):
    if order == 1:
        forward(size)
    else:
        forward (size)
        left (60)
        fractal (order - 1, size/3)
        backward(size/3)
        right (120)
        fractal (order - 1, size/3)
        backward(size/3)
        left (60)
        
left(90)
speed(10)
fractal(5, 200)
exitonclick()
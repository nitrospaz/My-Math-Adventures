from turtle import *
shape('turtle')
speed(0)
def square(sidelength):
    for i in range(4):
        forward(sidelength)
        right(90)
def spiral():
    length = 5
    for i in range(60):
        square(length)
        right(5)
        length += 5
spiral()

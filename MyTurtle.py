# annotations are after the commands
from turtle import *
# imports everything (*) from the turtle module
shape('turtle')
# when making drawings with the turtle module the shape command defines the shape of our pointer
speed(0)
# sets the speed of the drawing 0 is fastest
def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)
# makes a single square
def square60():
    for i in range(60):
        square()
        right(5)
# makes a square then turns right 5 degrees and draws another square 60 times
# makes a circle out of squares
# range starts counting at 0 so 60 is actually 0-59
def triangle(sidetri=100):
    for i in range(3):
        forward(sidetri)
        right(120)
# makes a single triangle, remember to use the exterior angle not the interior
def polygon(n=6):
    for i in range(n):
        forward(20)
        right(360/n)
# draws a polygon of whatever number (using exterior angles)
# exterior angles of polygon = 360/n where n = number of sides
def spiral():
    length = 5
    for i in range(200):
        triangle(length)
        right(5)
        length += 5
def star(starlength=100):
    for i in range(5):
        forward(starlength)
        right(144)
def starspiral():
    spstlength = 5
    for i in range(200):
        star(spstlength)
        right(5)
        spstlength += 5

# when calling functions remember to add () to the end

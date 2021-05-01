t = 0 # global variable assignment

def setup():
    size(600,600) # width,height of canvas, becomes default width and height variables if used
    rectMode(CENTER) #rotate the squares about their centers

def tri(length):
    '''Draws an equilateral triangle around the 
    center of the triangle'''
    triangle(0,-length, 
             -length*sqrt(3)/2, length/2, 
             length*sqrt(3)/2, length/2)

def draw():
    global t #local variable assignment referencing that we are using the global variable assignment t
    background(255) #white
    translate(width/2,height/2) # moves 0,0 point, not picture, from top left corner
    rotate(radians(t)) # t has to be defined locally, adding 5*t increases the frequency of the rotation
    for i in range(12):
        pushMatrix() # save this orientation
        translate(200,0)
        rotate(radians(t))
        tri(60)
        popMatrix() # return to saved orientation
        rotate(radians(360/12))
    t += 1

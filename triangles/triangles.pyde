'''single equilateral triangle rotating'''
def setup():
    size(600,600)
    rectMode(CENTER)
    
t = 0

def draw():
    background(255) # erases leftover triangles in background
    global t
    translate(width/2,height/2)
    rotate(radians(t))
    #triangle(0,0,100,100,200,-200) 
    # x and y coordinates for all three verticies non equilateral tri
    tri(200)
    t +=0.5

def tri(length):
    '''Draws and equilateral triangle around the 
    center of the triangle'''
    triangle(0,-length, 
             -length*sqrt(3)/2, length/2, 
             length*sqrt(3)/2, length/2)

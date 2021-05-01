t = 0 # global variable assignment

def setup():
    size(600,600) # width,height of canvas, becomes default width and height variables if used
    rectMode(CENTER) #rotate the squares about their centers

def draw():
    global t #local variable assignment referencing that we are using the global variable assignment t
    background(255) #white
    # ellipse(200,100,20,20) # x-coordinate, y-coordinate, width, height
    translate(width/2,height/2) # moves 0,0 point, not picture, from top left corner
    #rotate(radians(20)) #rotate uses radians, radians converts degrees
    #rect(50,100,100,60) # x(of top left corner),y(of top left corner),width,height
    rotate(radians(t)) # t has to be defined locally, adding 5*t increases the frequency of the rotation
    for i in range(12):
        pushMatrix() # save this orientation
        translate(200,0)
        rotate(radians(t))
        rect(200,0,50,50)
        popMatrix() # return to saved orientation
        rotate(radians(360/12))
    t += 1

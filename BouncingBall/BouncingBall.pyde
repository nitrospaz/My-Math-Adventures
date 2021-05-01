xcor = 700/2
ycor = 700/2
xvel = 12
yvel = 9

def setup():
    size(700,700)
            
def draw():
    global xcor,ycor,xvel,yvel
    background(0) #black
    xcor += xvel
    ycor += yvel
    #if ball reaches wall, switch direction
    if xcor > width or xcor < 0:
        xvel = -xvel
    if ycor > height or ycor <0:
        yvel = -yvel
    #draw ball
    ellipse(xcor,ycor,20,20)
    

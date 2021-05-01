r1 = 100 # radius of big circle
r2 = 10 # Radius of small circle
t = 0 # Time variable
circlelist = []


def setup():
    size(600,600)
    
def draw():
    global t, circlelist
    background(200) #grey
    # Move to left-center of screen
    translate(width/4,height/2)
    noFill() # Don't color the circle
    stroke(0) #black outline
    ellipse(0,0,2*r1,2*r1)
    
    #circling ellipse
    fill(255,255,0) #yellow
    y = r1*sin(t)
    x = r1*cos(t)
    #add point to circlelist
    circlelist = [y] + circlelist[:249]
    ellipse(x,y,r2,r2)
    
    #green line and circle
    stroke(255,0,0)
    line(x,y,200,y)
    fill(255,0,0)
    ellipse(200,y,10,10)
    #loop over circlelist to leave a trail
    for i,c in enumerate(circlelist):
        #small circle for trail
        ellipse(200+i,c,5,5)
    
    t += 0.05

# set the range of x values
xmin = -10
xmax = 10

# range of y values
ymin = -10
ymax = 10

# calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    xscl = width / rangex
    yscl = -height / rangey
    
def draw():
    global xscl, yscl
    background(255) # white
    translate(width/2,height/2) # move origin to center
    grid(xscl,yscl) # draw the grid
    graphFunction()
    
def f(x): # define the equation to be graphed
    return 6*x**3 + 31*x**2 + 3*x - 10

def graphFunction():
    x = xmin
    while x <= xmax:
        stroke(255,0,0) # red line
        line(x*xscl,f(x)*yscl,(x+0.1)*xscl,f(x+0.1)*yscl)
        x += 0.1
    
def grid(xscl,yscl): # draw the grid
    strokeWeight(1) # line weight
    stroke(0,255,255) # color of the line cyan
    for i in range(xmin,xmax + 1): # drawing grid lines vertical
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
    for i in range(ymin,ymax+1): # drawing grid lines horizontal
        line(xmin*xscl,i*yscl,xmax*xscl,i*yscl)
    stroke(0) # black
    line(0,ymin*yscl,0,ymax*yscl) # y axis line
    line(xmin*xscl,0,xmax*xscl,0) # x axis line
    
# test circle
#    fill(0)
#    ellipse(3*xscl,6*yscl,10,10)


    

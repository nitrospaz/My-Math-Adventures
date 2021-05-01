def setup():
    size(600,600)
    rectMode(CENTER)
    colorMode(HSB)
    
def draw():
    #white background
    background(0)
    translate(20,20)
    for x in range(20):
        for y in range(20):
            # distance from first coordiante set to the second
            d = dist(30*x,30*y,mouseX,mouseY)
            fill(0.5*d,255,255)
            rect(30*x,30*y,25,25)

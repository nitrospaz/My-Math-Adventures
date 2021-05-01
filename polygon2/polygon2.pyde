def setup():
    size(600,600)
    
def draw():
    translate(width/2,height/2)
    polygon(3,100) # 3 sides, vertices 100 units from center
    
def polygon(sides,sz):
    beginShape()
    for i in range(sides):
        step = radians(360/sides)
        vertex(sz*cos(i * step),
               100*sin(i * step))
    endShape(CLOSE)

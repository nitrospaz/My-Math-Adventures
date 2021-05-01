def setup():
    size(600,600)
    
def draw():
    translate(width/2,height/2)
    beginShape()
    for i in range(6):
        vertex(100*cos(radians(60*i)),
               100*sin(radians(60*i)))
        # 100 is the radius = r*cos(60*i)
    '''house shape
    vertex(100,100)
    vertex(100,200)
    vertex(200,200)
    vertex(200,100)
    vertex(150,50)'''
    endShape(CLOSE)

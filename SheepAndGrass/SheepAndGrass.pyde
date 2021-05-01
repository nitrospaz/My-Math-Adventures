#add a screen counter and track and export the ammounts to an excel sheet 
from random import choice

WHITE = color(255)
BROWN = color(102,51,0)
RED = color(255,0,0)
GREEN = color(0,102,0)
YELLOW = color(255,255,0)
PURPLE = color(102,0,204)
colorList = [WHITE,RED,YELLOW,PURPLE]

class Sheep:
    def __init__(self,x,y,col):
        self.x = x #x-position
        self.y = y #y-position
        self.sz = 10 #size
        self.energy = 20 #energy level
        self.col = col
        
    def update(self):
        #make sheep walk randomly
        move = 5 #max it can move in any direction, less makes them move and die faster
        self.energy -= 1 #walking takes energy
        if self.energy <= 0:
            sheepList.remove(self)
        if self.energy >= 50:
            self.energy -= 30 #giving birth takes energy
            #add another sheep to list
            sheepList.append(Sheep(self.x,self.y,self.col))
        self.x += random(-move,move)
        self.y += random(-move,move)
        #"wrap" the world Asteroids-style
        if self.x > width:
            self.x %= width
        if self.y > height:
            self.y %= height
        if self.x < 0:
            self.x += width
        if self.y < 0:
            self.y += height
        #find the patch of grass you are on in the grass list
        xscl = int(self.x / patchSize)
        yscl = int(self.y / patchSize)
        grass = grassList[xscl * rows_of_grass + yscl]
        if not grass.eaten:
            self.energy += grass.energy
            grass.eaten = True
        
        fill(self.col) #each sheep gets its own color
        ellipse(self.x,self.y,self.sz,self.sz)
        
class Grass:
    def __init__(self,x,y,sz):
        self.x = x
        self.y = y
        self.energy = 5 #energy in this patch of grass
        self.eaten = False #hasen't been eaten yet
        self.sz = sz
        
    def update(self):
        if self.eaten:
            if random(1000) < 5:
                self.eaten = False
            else:
                fill(BROWN)
        else:
            fill(GREEN)
            
        rect(self.x,self.y,self.sz,self.sz)
        
sheepList = [] #list to store sheep
grassList = [] #list to store grass
patchSize = 5 #size of each patch of grass
        
def setup():
    global rows_of_grass
    size(600,600)
    rows_of_grass = height/patchSize
    noStroke()    
    #create the inital ammount of sheep
    for i in range(30):
        sheepList.append(Sheep(random(width),random(height),choice(colorList)))
   
    #create the grass
    for x in range(0,width,patchSize):
        for y in range(0,height,patchSize):
            grassList.append(Grass(x,y,patchSize))
        
def draw():
    background(255)
    #update the grass first
    for grass in grassList:
        grass.update()
        
    #then the sheep
    for sheep in sheepList:
        sheep.update()

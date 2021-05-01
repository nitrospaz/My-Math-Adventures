ballList=[] #empty list to put balls in

class Ball:
    def __init__(self,x,y): #if you get an error "this constructor takes no arguments" check to see that you have two underscores and that you speled init correctly. lol.
        '''How to initiate a ball'''
        self.xcor = x
        self.ycor = y
        self.xvel = random(-2,2)
        self.yvel = random(-2,2)
        #add color
        self.col = color(random(255),
                         random(255),
                         random(255))
           
    def update(self):
        self.xcor += self.xvel
        self.ycor += self.yvel
        #if ball reaches wall, switch direction
        if self.xcor > width or self.xcor < 0:
            self.xvel = -self.xvel
        if self.ycor > height or self.ycor <0:
            self.yvel = -self.yvel
        #add color
        fill(self.col)
        #draw ball
        ellipse(self.xcor,self.ycor,20,20)
    
def setup():
    size(600,600)
    for i in range(40):
        ballList.append(Ball(random(width),random(height))) #if you get an error "this constructor takes no arguments" check to see that you have two underscores and that you speled init correctly. lol.
       
def draw():
    background(0) #black
    for ball in ballList:
        ball.update()

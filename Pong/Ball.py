import random

class Ball():
    def __init__(self, pg, win, width, height):
        self.width = width
        self.height = height
        self.pg = pg
        self.win = win
        self.centerX = width/2
        self.centerY = height/2
        self.velsX = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
        self.velsY = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
        self.rect = self.pg.Rect(0,0,20,20)
        
    def show(self):
        self.rect.center = (self.centerX,self.centerY)
        self.pg.draw.rect(self.win, [150,150,150], self.rect)
    def random_vel(self):
        self.velX = 0
        self.velY = 0
        while self.velX == 0 and self.velY == 0:
            self.velX = random.choice(self.velsX)
            self.velY = random.choice(self.velsY)
        while self.velX > -5 and self.velX < 5 and self.velY > -5 and self.velY < 5:
            self.velX = random.choice(self.velsX)
            self.velY = random.choice(self.velsY)
    def Move(self):
        self.centerX += self.velX
        self.centerY += self.velY
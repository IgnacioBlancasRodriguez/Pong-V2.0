class Player():
    def __init__(self, pg, win, height, width,offset):
        self.pg = pg
        self.win = win
        self.width = 20
        self.height = 94
        self.offset = offset
        self.centerX = width/2-self.width/2+self.offset
        self.centerY = height/2-self.height/2
        self.player_img = self.pg.Rect(self.centerX,self.centerY,self.width,self.height)
    def show(self):
        self.player_img.center = (self.centerX,self.centerY)
        self.pg.draw.rect(self.win, [150,150,150], self.player_img)
    def Move_Y(self, amount):
        self.centerY += amount
import pygame as pg
import Player
import Ball
import sys

pg.init()

#Global variables
inGame = True
width = 900
height = 700
amount = 5
points1 = 0
points2 = 0
win1 = False
win2 = False

font = pg.font.Font("fonts/AtariST8x16SystemFont.ttf",100)
text1 = font.render(str(points1),False,[150,150,150])
text2 = font.render(str(points2),False,[150,150,150])
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect1.center = (width/2-225,height/2-250)
textRect2.center = (width/2+225,height/2-250)
bg = pg.image.load("images/Pong.png")
favicon = pg.image.load("images/logo.png")
black_bg = pg.image.load("images/bg.png")
win = pg.display.set_mode((width,height))
pg.display.set_caption("Pong")
pg.display.set_icon(favicon)
ball = Ball.Ball(pg,win,width,height)
ply = Player.Player(pg,win,height,width,-350)
ply2 = Player.Player(pg,win,height,width,350)

ball.random_vel()

while inGame:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            inGame = False
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        ply.Move_Y(-amount)
    elif keys[pg.K_DOWN]:
        ply.Move_Y(amount)
    elif keys[pg.K_w]:
        ply2.Move_Y(-amount)
    elif keys[pg.K_s]:
        ply2.Move_Y(amount)
    
    if ball.centerY+10 >= height:
        pg.mixer.init()
        pg.mixer.music.load("sounds/hit.wav")
        pg.mixer.music.play()
        if ball.velX > 0:
            ball.velsX = [1,2,3,4,5]
        elif ball.velX < 0:
            ball.velsX = [-5,-4,-3,-2,-1]
        ball.velsY = [-5,-4,-3,-2,-1]
        ball.random_vel()
        ball.velsY = [-5,-4,-3,-2,-1,1,2,3,4,5]
        ball.velsX = [-5,-4,-3,-2,-1,1,2,3,4,5]
    elif ball.centerY-10 <= 0:
        pg.mixer.init()
        pg.mixer.music.load("sounds/hit.wav")
        pg.mixer.music.play()
        if ball.velX > 0:
            ball.velsX = [0,1,2,3,4,5]
        elif ball.velX < 0:
            ball.velsX = [-5,-4,-3,-2,-1,0]
        ball.velsY = [0,1,2,3,4,5]
        ball.random_vel()
        ball.velsY = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
        ball.velsX = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
    elif ball.centerX-10 <= 0:
        pg.mixer.init()
        pg.mixer.music.load("sounds/point.wav")
        pg.mixer.music.play()
        points2 += 1
        ball.centerX = width/2
        ball.centerY = height/2
        ball.random_vel()
    elif ball.centerX+10 >= width:
        pg.mixer.init()
        pg.mixer.music.load("sounds/point.wav")
        pg.mixer.music.play()
        points1 += 1
        ball.centerX = width/2
        ball.centerY = height/2
        ball.random_vel()
    
    if ball.rect.colliderect(ply.player_img):
        pg.mixer.init()
        pg.mixer.music.load("sounds/hit.wav")
        pg.mixer.music.play()
        if ball.velY > 0:
            ball.velsY = [1,2,3,4,5]
        elif ball.velY < 0:
            ball.velsY = [-5,-4,-3,-2,-1]
        ball.velsX = [5,4,3,2,1]
        ball.random_vel()
        ball.velsX = [-5,-4,-3,-2,-1,1,2,3,4,5]
        ball.velsY = [-5,-4,-3,-2,-1,1,2,3,4,5]
    elif ball.rect.colliderect(ply2.player_img):
        pg.mixer.init()
        pg.mixer.music.load("sounds/hit.wav")
        pg.mixer.music.play()
        if ball.velY > 0:
            ball.velsY = [1,2,3,4,5]
        elif ball.velY < 0:
            ball.velsY = [-5,-4,-3,-2,-1]
        ball.velsX = [-5,-4,-3,-2,-1]
        ball.random_vel()
        ball.velsX = [-5,-4,-3,-2,-1,1,2,3,4,5]
        ball.velsY = [-5,-4,-3,-2,-1,1,2,3,4,5]


    ball.Move()
    text1 = font.render(str(points1),False,[150,150,150])
    text2 = font.render(str(points2),False,[150,150,150])

    win.blit(bg, (0,0))
    win.blit(text1, textRect1)
    win.blit(text2, textRect2)
    ply.show()
    ply2.show()
    ball.show()
    pg.display.update()

    if points1 >= 7 or points2 >= 7:
        pg.mixer.init()
        pg.mixer.music.load("sounds/dead.wav")
        pg.mixer.music.play()
        if points1 == 7:
            win1 = True
        elif points2 == 7:
            win2 = True
        inGame = False
while win1 or win2:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            win1 = False
            win2 = False
    
    win.blit(black_bg, (0,0))

    if win1:
        win_text = font.render("Player 1 won", False, [255,255,255])
        win_rect = win_text.get_rect()
        win_rect.center = (width/2, height/2)
    elif win2:
        win_text = font.render("Player 2 won", False, [255,255,255])
        win_rect = win_text.get_rect()
        win_rect.center = (width/2, height/2)
    win.blit(win_text, win_rect)
    pg.display.update()

pg.quit()

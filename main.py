from issgraph import *
import sys, random

screen = Graphics(800, 600)

_img = Img.img("token.png")

class Player:
    speed = 0.4
    x = 50
    y = 50
    c_delay = 50
    img = Img.scale(_img, 50, 50)

chumps = []
chump_img = Img.scale(_img, 32, 32)

#class
player = Player()

while True:
    for e in screen.game():
        if e.type == screen.shouldClose(): sys.exit()
    screen.title("Cream n Chump")
    screen.paint(200, 200, 255)
    screen.image(player.img, player.x, player.y)
    
    for chump in chumps:
        screen.image(chump_img, chump[0], chump[1])
        if Utils.collide(player.x, player.y, chump[0], chump[1], 40):
            chumps.remove(chump)
    
    if Utils.keys(Utils.KEYS["right"]):
        player.x += player.speed
    if Utils.keys(Utils.KEYS["left"]):
        player.x -= player.speed
    if Utils.keys(Utils.KEYS["up"]):
        player.y -= player.speed
    if Utils.keys(Utils.KEYS["down"]):
        player.y += player.speed
    
    player.c_delay -= 1
    
    if player.c_delay < 1:
        chumps.append([random.randrange(0, 800), random.randrange(0, 600)])
        player.c_delay = random.randrange(0, 1000)
    
    screen.update()
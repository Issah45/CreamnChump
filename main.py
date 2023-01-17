from issgraph import *
import sys, random

screen = Graphics(800, 600)

_img = Img.img("token.png")
img = Img.scale(_img, 50, 50)

c_delay = 50

speed = 0.4
x = 50
y = 50

coins = []
coins.append([140, 180])
coins.append([500, 410])
coin_img = Img.scale(_img, 32, 32)

while True:
    for e in screen.game():
        if e.type == screen.shouldClose(): sys.exit()
    screen.title("Cream n Chump")
    screen.paint(200, 200, 255)
    screen.image(img, x, y)
    
    for coin in coins:
        screen.image(coin_img, coin[0], coin[1])
        if Utils.collide(x, y, coin[0], coin[1], 40):
            coins.remove(coin)
    
    if Utils.keys(Utils.KEYS["right"]):
        x += speed
    if Utils.keys(Utils.KEYS["left"]):
        x -= speed
    if Utils.keys(Utils.KEYS["up"]):
        y -= speed
    if Utils.keys(Utils.KEYS["down"]):
        y += speed
    
    c_delay -= 1
    
    if c_delay < 1:
        coins.append([random.randrange(0, 800), random.randrange(0, 600)])
        c_delay = random.randrange(0, 1000)
    
    screen.update()
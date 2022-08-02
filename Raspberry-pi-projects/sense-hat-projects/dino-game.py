from sense_hat import *
import random
from time import sleep

sense = SenseHat()

sense.clear()
game_over = False
points = 0
obstacle_x = random.randrange(3,6)
dino_x = 0
dino_y = 6

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
k = (0, 0, 0)
w = (255, 255, 255)
c = (0, 255, 255)
y = (255, 255, 0)
o = (255, 128, 0)
n = (255, 128, 128)
p = (128, 0, 128)
d = (255, 0, 128)
l = (128, 255, 128)

rmon4 = [k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         w, w, w, w, w, w, w, w
]	

def dino_run():
    global dino_x
    if dino_x < 7:
        dino_x += 1
        sleep(0.5)

def dino_jump():
    global dino_y
    global dino_x
    sense.set_pixel(dino_x, dino_y, g)
    dino_y -= 1
    sense.set_pixel(dino_x, dino_y, g)
    sleep(0.2)
    for x in range(0,2):
        dino_x += 1
        sense.set_pixel(dino_x, dino_y, g)
        sleep(0.2)
    dino_y += 1
    sense.set_pixel(dino_x, dino_y, g)

def update():
    global obstacle_x
    sense.set_pixel(dino_x, dino_y, g)
    sense.set_pixel(obstacle_x, 6, w) 
    sleep(0.2)

def background():
    sense.set_pixels(rmon4)

def reset():
    global dino_x
    global dino_y
    global obstacle_x
    dino_y = 6
    dino_x = 0
    obstacle_x = random.randrange(3,6)
while True:
    for event in sense.stick.get_events():
        # print("DEBUG: event.direction=", event.direction)
        if event.direction == "middle" and event.action == "pressed":
            dino_jump()
    background()
    dino_run()
    update()
    if dino_x == 7 and dino_y == 6:
        reset()
    points += 19
    if dino_x == obstacle_x and dino_y == 6:
        sense.show_message("Game Over!")
        sense.show_message(f"Score: {points}")
        break
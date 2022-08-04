from sense_hat import *
import random
from time import *
import threading

sense = SenseHat()

sense.clear()
game_over = False
points = 0
obstacle_x = random.randrange(3,6)
dino_x = 0
dino_y = 6
run_time = 1

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

day = [k, w, w, w, k, k, w, w,
         k, k, k, k, k, k, w, w,
         k, k, k, w, k, k, k, k,
         k, k, w, w, w, k, k, w,
         w, k, k, k, k, k, w, w,
         w, w, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         w, w, w, w, w, w, w, w
]	

night = [w, k, k, k, w, w, k, k,
         w, w, w, w, w, w, k, k,
         w, w, w, k, w, w, w, w,
         w, w, k, k, k, w, w, k,
         k, w, w, w, w, w, k, k,
         k, k, w, w, w, w, w, w,
         w, w, w, w, w, w, w, w,
         k, k, k, k, k, k, k, k
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
    for i in range(0,2):
        dino_x += i
        sense.set_pixel(dino_x, dino_y, g)
        sleep(0.1)
    dino_y += 1
    sense.set_pixel(dino_x, dino_y, g)
    
def update():
    sense.set_pixel(dino_x, dino_y, g)
    sleep(0.05)

def background():
    sense.set_pixels(day)
    sense.set_pixel(obstacle_x, 6, w)

def night_background():
    sense.set_pixels(night)
    sense.set_pixel(obstacle_x, 6, k)

def reset():
    global dino_x
    global dino_y
    global obstacle_x
    dino_y = 6
    dino_x = 0
    obstacle_x = random.randrange(3,6)


def dino_move():
    global points
    while True:
        for event in sense.stick.get_events():
            if event.direction == "middle" and event.action == "pressed":
                dino_jump()
        dino_run()
        update()
        if dino_x == 7 and dino_y == 6:
            reset()
        points += 2
        if dino_x == obstacle_x and dino_y == 6:
            sense.show_message("Game Over!")
            sense.show_message(f"Score: {points}")
            break

def change_background():
    wake_up = time.now() + 60
    is_day = True
    while True:
        if time.now() > wake_up:
            if is_day:
                background()
            else:
                night_background
        wake_up = time.now() + 60

Thread1 = threading.Thread(target=change_background)
Thread2 = threading.Thread(target=dino_move)

Thread1.start()
Thread2.start()

Thread1.join()
Thread2.join()
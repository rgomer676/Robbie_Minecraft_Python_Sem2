from sense_hat import SenseHat
sense = SenseHat()
from time import sleep
from random import randint

blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blank = (0, 0, 0)
direction = "right"
score = 0
pause = 0.5
dead = False
remove = True

slug = [ [2, 4],  [3, 4],  [4, 4] ]
vegetables = []

def draw_slug():
    for segment in slug:
        sense.set_pixel(segment[0], segment[1], green)

def move():
    global remove
    remove = True
    global score
    global pause
    last = slug[-1]
    first = slug[0]
    next = list(last)
    if direction == "right":
        if last[0] + 1 == 8:
            next[0] = 0
        else:
            next[0] = last[0] + 1
    elif direction == "left":
        if last[0] - 1 == -1:
            next[0] = 7
        else:
            next[0] = last[0] - 1
    elif direction == "down":
        if last[1] + 1 == 8:
            next[1] = 0
        else:
            next[1] = last[1] + 1
    elif direction == "up":
        if last[1] - 1 == -1:
            next[1] = 7
        else:
            next[1] = last[1] - 1
    if next in vegetables:
        vegetables.remove(next)
        score += 1
        if score % 5 == 0:
            remove = False
            pause = pause * 0.8
    slug.append(next)
    sense.set_pixel(next[0], next[1], green)
    if remove == True:
        sense.set_pixel(first[0], first[1], blank)
        slug.remove(first)

def joystick_moved(event):
    global direction
    direction = event.direction

def make_veg():
    new = slug[0]
    while new in slug:
        x = randint(0, 7)
        y = randint(0, 7)
        new = [x, y]
        sense.set_pixel(x, y, red)
        vegetables.append(new)
        for veg in vegetables:
            sense.set_pixel(veg[0], veg[1], red)
        

sense.clear()


draw_slug()
while dead == False:       
    sense.stick.direction_any = joystick_moved
    move()
    while len(vegetables) < 3:
        make_veg()  
    sleep(pause)
    for x in slug:
        if slug.count(x)>1:
            dead = True
            sense.show_message(str(score))

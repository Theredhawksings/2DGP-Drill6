from operator import truediv

from pico2d import *
import random

open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('run_animation.png')
hand = load_image('hand_arrow.png')

hx = 0
hy = 0

def handupdate():
    global hx, hy
    hx = random.randrange(100, 700)
    hy = random.randrange(100, 500)


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

x=400
y=300
frame = 0
running = True

while running:

    clear_canvas()
    ground.draw(400, 300)

    handupdate()

    a = (hy - y) / (hx - x)
    b = y - x * a

    if (x >= hx):
        for x in range(x, hx + 1, -1):
            clear_canvas()
            ground.draw(400, 300)
            hand.clip_draw(0, 0, 50, 52, hx, hy, 100, 104)
            y = a * x + b
            character.clip_draw(frame * 64, 128, 64, 64, x, y, 128, 128)
            update_canvas()
            frame = (frame + 1) % 4
            delay(0.01)

    elif (x < hx):
        for x in range(x, hx + 1, 1):
            clear_canvas()
            ground.draw(400, 300)
            hand.clip_draw(0, 0, 50, 52, hx, hy, 100, 104)
            y = a * x + b
            character.clip_draw(frame * 64, 64, 64, 64, x, y, 128, 128)
            update_canvas()
            frame = (frame + 1) % 4
            delay(0.01)

    handle_events()
    delay(0.1)

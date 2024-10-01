from pico2d import *


open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('run_animation.png')
had = load_image('hand_arrow.png')

x=400
y=300
frame = 0

while True:
    clear_canvas()
    ground.draw(400, 300)

    x +=0
    y +=0

    frame = (frame + 1) % 4

    character.clip_draw(frame*64, 128, 64, 64, x, y, 128, 128)

    update_canvas()
    #handle_events()
    delay(0.05)

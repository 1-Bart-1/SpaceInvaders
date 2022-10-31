from time import sleep
from sense_hat import SenseHat

from player import Player
from weapon import Weapon
from Ufo import Ufo

from Utils import *

sense = SenseHat()
sense.low_light = True

score_num = 0

direction = "still"

y = [0, 0, 0]    # Setter bakgrunnsfargen til svart
g = [255,255,255]
start_screen = [
y, y, y, g, g, y, y, y,
y, y, y, g, g, y, y, y,
y, y, y, g, g, y, y, y,
y, y, g, g, g, g, y, y,
y, y, g, g, g, g, y, y,
y, g, g, g, g, g, g, y,
g, g, g, g, g, g, g, g,
g, g, y, g, g, y, g, g
]
bg = [
y, g, g, g, g, g, y, y,
g, g, g, g, g, g, g, y,
g, y, y, g, y, y, g, y,
g, g, g, g, g, g, g, y,
g, g, g, y, g, g, g, y,
y, g, g, g, g, g, y, y,
y, g, y, g, y, g, y, y,
y, y, y, y, y, y, y, y
]

player = Player()
weapon = Weapon(player.player_position)
ufo = Ufo()

sense.clear()

def reset(score_num):
    score_num = 0
    for bullet in weapon.bullets:
        weapon.bullet_delete(bullet)
    ufo.reset_pos()
    return score_num

def update(shooting, playing, score_num):
    sense.clear()
    player.movement(direction)
    weapon.update_x(int(player.player_position))
    if not ufo.draw(): playing = False

    if shooting:
        shooting = weapon.shoot()

    if list_and_object_overlap(player.positions, ufo.pos):
        playing = False
    
    if list_and_object_overlap(weapon.bullets, ufo.pos):
        score_num += 1
        weapon.bullet_delete(weapon.bullets[0])
        ufo.reset_pos()

    return shooting, playing, score_num

def render():
    for position in player.positions:
            sense.set_pixel(position[0], position[1], player.playerColor)

    return True


running = True
shooting = False
playing = False
start = True
while running:
    if sense.get_gyroscope_raw()['x'] < -2: shooting = True

    direction = "still"
    for event in sense.stick.get_events():
        direction = event.direction
        if event.action == "pressed":
            if direction == "down":
                if playing == False: running = False
                playing = False
            elif direction == "up":
                start = False
                playing = True
            elif not playing and ufo.angriness > 0:
                ufo.angriness = speed_up(ufo.angriness, direction)
                sense.show_letter(str(ufo.angriness))
                sleep(0.5)

    
    if playing:
        old_score_num = score_num
        shooting, playing, score_num = update(shooting, playing, score_num)
        if old_score_num != score_num: update_file(score_num)
        render()
    else: 
        score_num = reset(score_num)
        if start:
            sense.set_pixels(start_screen)
        if not start: sense.set_pixels(bg)
    sleep(1/10)

sense.set_pixels(bg)
sleep(0.5)
sense.clear(y)

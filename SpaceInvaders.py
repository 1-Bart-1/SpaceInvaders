from time import sleep
from sense_hat import SenseHat

from player import Player
from weapon import Weapon
from Ufo import Ufo

from Utils import *

sense = SenseHat()
sense.low_light = True


direction = "still"

y = [0, 0, 0]    # Setter bakgrunnsfargen til hvit

g = [255,255,255]

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

sense.clear()

player = Player()
weapon = Weapon(player.player_position)
ufo = Ufo()

def reset():
    pass

def update(shooting, running):
    sense.clear()
    player.movement(direction)
    weapon.update_x(int(player.player_position))
    if not ufo.draw(): running = False

    if shooting:
        shooting = weapon.shoot()

    if list_and_object_overlap(player.positions, ufo.pos):
        playing = False
    
    if list_and_object_overlap(weapon.bullets, ufo.pos):
        print("deleting bullet and ufo")
        weapon.bullet_delete(weapon.bullets[0])
        ufo.reset_pos()

    return shooting, playing

def render():
    for position in player.positions:
            sense.set_pixel(position[0], position[1], player.playerColor)

    return True


running = True
shooting = False
playing = False
while running:
    if sense.get_gyroscope_raw()['x'] < -2: shooting = True

    direction = "still"
    for event in sense.stick.get_events():
        direction = event.direction
        if event.action == "pressed":
            if direction == "down":
                playing = False
                running = False
            if direction == "up":
                playing = True
    
    if playing:
        shooting, playing = update(shooting, playing)
        render()
    else: 
        reset()
        
    sleep(1/10)

sense.set_pixels(bg)
sleep(0.5)
sense.clear(y)


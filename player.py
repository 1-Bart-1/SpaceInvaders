from time import sleep
from sense_hat import SenseHat

from Utils import in_bounds

sense = SenseHat()


x = playerColor = [0,0,255]         # Setter spiller farge til blå
z = enemyColor = [0, 255, 0]        # Setter fiendenes farge til rød
y = backgroundColor = [255, 255, 255]    # Setter bakgrunnsfargen til hvit
t = 0


class Player():
    def __init__(self) -> None:
        self.player_position = 2
        self.playerColor = [0,0,255] # Setter spiller farge til blå
        self.y = 6
        self.speed = 0.5
        self.positions = []
    

    def update_positions(self):
        self.positions.clear()
        self.positions.append([int(self.player_position),int(self.y)])
        self.positions.append([int(self.player_position), int(self.y+1)])
        self.positions.append([int(self.player_position+1), int(self.y+1)])
        self.positions.append([int(self.player_position-1), int(self.y+1)])
   

    def movement(self, direction):
        if direction == "left":
            if 1 <= self.player_position - self.speed <= 6:
                self.player_position -= self.speed

        if direction == "right":
            if 1 <= self.player_position + self.speed <= 6:
                self.player_position += self.speed
        
        self.update_positions()

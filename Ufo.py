# Importing packages used in the code for the ufo
from sense_hat import SenseHat
from random import randint
from time import sleep

# Importing project files needed
from Utils import objects_overlap


# Stating sense as a variable for SenseHat
sense = SenseHat()


class Ufo():
    def __init__(self):
        ## ---- UFO color ----

        # Stating a variable for the temeprature value from the SenseHat
        self.rpi_temp = int(sense.temp)

        # Making a empty list for the (R, G, B) values for the ufo object color
        self.ufo_color = (255, 255, 255)

        # Setting the number of pixels the ufo will move per time unit (maximum: 9)
        self.angriness = 2

        # A list for the ufo position
        self.pos = [self.random(), 0]

    def reset_pos(self):
        self.pos = [self.random(), 0]

    def set_color(self):
        # If statement to check enviromental temperature to adjust the color of the ufo object
        if (self.rpi_temp <10):
            # If temp. is lower than 10 degrees, the ufo object will be blue
            self.ufo_color = (0, 0, 255)
        elif (self.rpi_temp >35):
            # If temp. is above 35 degrees, the ufo object will be red
            self.ufo_color = (255, 0, 0)
        else:
            # If the temperature is in the range between 10 and 35, the ufo object will be orange
            self.ufo_color = (255, 69, 0) # nice

    # ---- Function declaration ----

    # Function to generate a random x-axis position for the ufo object at each start, returns position
    def random(self):
        # Randint generates a random position from x-axis pos. 1-6 to fit the gamescreen.
        random_x = randint(1,6)
        return random_x


    # Function for creating the ufo object and managing the y-axis movement
    def draw(self):
        self.set_color()
        # Checking if the ufo object y-axis value is below 8
        if (int(self.pos[1] + self.angriness*0.05) < 8):
            # Set a led pixel in the ufo object color
            sense.set_pixel(int(self.pos[0]), int(self.pos[1]), self.ufo_color)
            # Increase the ufo object y-axis value with the desired number of leds
            self.pos[1] += self.angriness*0.05
        else:
            # If the ufo object y-axis value is bigger than 7, set value to 7 to avoid error
            self.pos[1] = 0
            return False
            # Ends the loop
        return True
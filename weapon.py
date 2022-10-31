from time import sleep
from sense_hat import SenseHat 

from Utils import objects_overlap

sense = SenseHat()

class Weapon():
    def __init__(self, player_pos) -> None:
        self.L = [player_pos, 6] #midlertidlig possisjon (skal være player_pos)

        self.bullets = []
        self.collor_blue = (0,255,0) #fargen til skuddet
        self.c = 1
        self.speed = 1
        
    def update_x(self, x):
        self.L[0] = x

    def get_colour(self):
        return (0,int(sense.temp*2),255) #setter fargen til bullet basert på temperatur (mer lilla)

    def bullet_draw(self, l):
        sense.set_pixel(l[0],l[1],self.get_colour()) #tegner bulleten

    def bullet_del(self, l):
        sense.set_pixel(l[0],l[1],(0,0,0)) #sletter bulleten

    def bullet_init(self, po): #lager en ny bullet, tar inn player posisjonen og lager et skudd 1 pixel over den
        p = [po[0],po[1]]
        self.bullet_draw(p)
        self.bullets.append(p)

    def bullet_move(self):
        for i in self.bullets: 
            if not i[1]==0: #går gjennom hver "bullet" og sjekker at den ikke har nådd kanten
                self.bullet_del(i)
                i[1]-=1 #flytter bullet en pixel frem
                self.bullet_draw(i)
            else:
                self.bullet_delete(i)
                

    def bullet_delete(self, bullet):
        self.bullet_del(bullet) #fjerner pixelen med bulleten 
        self.bullets.remove(bullet) #fjerner bullet fra listen så listen med bullets ikke blir uendelig lang

    def shoot(self):
        if self.c == 1:
            self.bullet_init(self.L)
        self.bullet_move()
        if self.c < 8:
            self.c += self.speed
        else:
            self.c = 1
            return False
        return True

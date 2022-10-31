#Importerer bibliotek
from time import sleep
from sense_hat import SenseHat

#Importerer nødvendig prosjekt filer
from Utils import in_bounds

#Setter sense til en variabel av SenseHat
sense = SenseHat()


x = playerColor = [0,0,255]         # Setter spiller farge til blå
z = enemyColor = [0, 255, 0]        # Setter fiendenes farge til rød
y = backgroundColor = [255, 255, 255]    # Setter bakgrunnsfargen til hvit


class Player():
    def __init__(self) -> None:
        self.player_position = 2        #Setter spillerens x-akse posisjon
        self.playerColor = [0,0,255]    #Setter spiller farge til blå
        self.y = 6                      #Setter spilerens y-akse posisjon
        self.speed = 0.5                #Setter spillerens hastighet
        self.positions = []             #Oppretter en liste for spillerens posisjon
    

    def update_positions(self): #Oppdaterer listen av pixler som er avhengig av spillerens posisjon: spilleren består av 4 pixler
        self.positions.clear()
        self.positions.append([int(self.player_position),int(self.y)])
        self.positions.append([int(self.player_position), int(self.y+1)])
        self.positions.append([int(self.player_position+1), int(self.y+1)])
        self.positions.append([int(self.player_position-1), int(self.y+1)])
   

    def movement(self, direction):                          #Sjekker om det skal utføres en bevegelse, og returnerer de nye posisjonene
        if direction == "left":                             #Sjekker om den får et "left" input
            if 1 <= self.player_position - self.speed <= 6: #Sjekker om spilleren vil holde seg innenfor banens areal
                self.player_position -= self.speed          #lager spillerens nye posisjonsverdier

        if direction == "right":                            #Sjekker om den får et "right" input
            if 1 <= self.player_position + self.speed <= 6: 
                self.player_position += self.speed
        
        self.update_positions() 
        return self.positions   #Returnerer den oppdaterte verdien

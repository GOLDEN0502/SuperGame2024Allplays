import os
import msvcrt
class Player:
    health = 3 
    coordX = 1
    coordY = 1
    def MoveRight(self):
        os.system('cls')
        self.coordX += 1
        print(self.coordY*'\n' + self.coordX*" " + '@')
    def MoveLeft(self):
        os.system('cls')
        self.coordX -= 1
        print(self.coordY*'\n' + self.coordX*" " + '@')
    def MoveUp(self):
        os.system('cls')
        self.coordY -= 1
        print(self.coordY*'\n' + self.coordX*" " + '@')
    def MoveDown(self):
        os.system('cls')
        self.coordY += 1
        print(self.coordY*'\n' + self.coordX*" " + '@')

P = Player()
lock = 20

while 1:
    uinput = msvcrt.getch().decode('ASCII')
    if(uinput == 'd' and P.coordX < lock  or uinput == 'D' and P.coordX < lock):   
        P.MoveRight()
    if(uinput == 'A' and P.coordX > 0 or uinput == 'a' and P.coordX > 0):    
        P.MoveLeft()
    if(uinput == 'W' and P.coordY > 0 or uinput == 'w' and P.coordY > 0):
        P.MoveUp()
    if(uinput == 'S' and P.coordY < lock or uinput == 's' and P.coordY < lock):
        P.MoveDown()

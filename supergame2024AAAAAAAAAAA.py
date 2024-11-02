import os
import msvcrt

class Field:
    def __init__(self, size, p):
        self.size = size
        self.arr = [[0 for _ in range(size)] for _ in range(size)]
        self.arr[p.coordX][p.coordY] = 1

    def UpdateField(self, p):
        self.arr[p.prevX][p.prevY] = 0
        self.arr[p.coordX][p.coordY] = 1

    def PrintField(self):
        os.system('cls')
        for i in range(self.size):
            for j in range(self.size):
                if self.arr[j][i] == 0:
                    print(" ", end="")
                elif self.arr[j][i] == 1:
                    print("@", end="")
            print("|")
        print("_" * self.size)

class Player:
    def __init__(self, health, coordX, coordY):
        self.health = health
        self.coordX = coordX
        self.coordY = coordY
        self.prevX = coordX  
        self.prevY = coordY 

    def MoveRight(self):
        self.prevX = self.coordX
        self.prevY = self.coordY
        self.coordX += 1

    def MoveLeft(self):
        self.prevX = self.coordX
        self.prevY = self.coordY
        self.coordX -= 1

    def MoveUp(self):
        self.prevX = self.coordX
        self.prevY = self.coordY
        self.coordY -= 1

    def MoveDown(self):
        self.prevX = self.coordX
        self.prevY = self.coordY
        self.coordY += 1

P = Player(3, 1, 1)
f = Field(20, P)
lock = 19

while(1):
    f.PrintField()
    uinput = msvcrt.getch().decode('ASCII')
    
    if (uinput == 'd' or uinput == 'D') and P.coordX < lock:
        P.MoveRight()
        f.UpdateField(P)
    
    if (uinput == 'a' or uinput == 'A') and P.coordX > 0:
        P.MoveLeft()
        f.UpdateField(P)
        
    if (uinput == 'w' or uinput == 'W') and P.coordY > 0:
        P.MoveUp()
        f.UpdateField(P)
        
    if (uinput == 's' or uinput == 'S') and P.coordY < lock:
        P.MoveDown()
        f.UpdateField(P)

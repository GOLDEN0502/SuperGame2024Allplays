import os
import msvcrt
import random
import sys
  
score = 0


class Coin:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def UpdateCoin(self):
        self.x = random.randint(1, 19)
        self.y = random.randint(1, 19)
        
class Enemy:
    def __init__(self, xe,ye,):
        self.xe = xe
        self.ye = ye
        self.prevxe = xe
        self.prevye = ye
        
    def UpdateEnemy(self):
        self.prevxe = self.xe
        self.prevye = self.ye
        a = random.randint(0, 1)
        b = random.randint(0, 1)
        if( a == 0 and b == 0 and self.prevxe != 1):
            self.xe -= 1
        if( a == 0 and b == 1 and self.prevxe != 17):
            self.xe += 1
        if( a == 1 and b == 0 and self.prevye != 1):
            self.ye -=1
        if( a == 1 and b == 1 and self.prevye != 17):
            self.ye += 1

class Field:
    def __init__(self, size, p):
        self.size = size
        self.arr = [[0 for _ in range(size)] for _ in range(size)]
        self.arr[p.coordX][p.coordY] = 1

    def UpdateField(self, p):
        self.arr[e.prevxe][e.prevye] = 0
        self.arr[c.x][c.y] = 2
        self.arr[p.prevX][p.prevY] = 0
        self.arr[e.xe][e.ye] = 3
        self.arr[p.coordX][p.coordY] = 1

    def PrintField(self):
        os.system('cls')
        for i in range(self.size):
            for j in range(self.size):
                if self.arr[j][i] == 0:
                    print(" ", end="")
                elif self.arr[j][i] == 1:
                    print("@", end="")
                elif self.arr[j][i] == 2:
                    print("o", end="")
                elif self.arr[j][i] == 3:
                    print("Z", end="")
                    
            print("|")
        print("_" * self.size)
        print(score)
        print(P.health)
            
        
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
coinX = random.randint(1, 19)
coinY = random.randint(1, 19)
c = Coin(coinX, coinY)
enemyXE = random.randint(1, 15)
enemyYE = random.randint(1, 15)
e = Enemy(enemyYE,enemyXE)
lock = 19


while(1):
    if (P.coordX == c.x) and (P.coordY == c.y):
        c.UpdateCoin()
        score += 1
    if (P.prevX == e.prevxe) and (P.prevY == e.prevye):
        P.health -= 1

        if(P.health <= 0) :
         
            sys.exit(0)
        
    e.UpdateEnemy()


        
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

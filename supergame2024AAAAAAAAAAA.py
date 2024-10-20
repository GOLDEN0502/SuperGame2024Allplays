import os
import msvcrt
b = 1
c = 1
move = 0
lock = 100
while 1:
    uinput = msvcrt.getch().decode('ASCII')
    if(uinput == 'd' and move < lock or uinput == 'D' and move < lock):
        move += 1
        os.system('cls')
        b+=1
        print(c*'\n' + b*" " + '@')    
    if(uinput == 'A' and move < lock or uinput == 'a' and move < lock):
        move += 1
        os.system('cls')
        b-=1
        print(c*'\n' + b*" " + '@')    
    if(uinput == 'W' and move < lock or uinput == 'w' and move < lock):
        move += 1
        os.system('cls')
        c = c-1
        print(c*'\n' + b*" " + '@')
    if(uinput == 'S' and move < lock or uinput == 's' and move < lock):
        move += 1
        os.system('cls')
        c = c+1
        print(c*'\n' + b*" " + '@')  

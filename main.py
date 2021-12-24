import random
import os

AllElements = {11, 12, 13, 21, 22, 23, 31, 32, 33}
T = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
mtE = {11, 12, 13, 21, 22, 23, 31, 32, 33}
k: int = 0
kk: int = 0
counter = 0
winnerstate = True


def searchforindex(matrix, number):
    i, j, = 0, 0
    for row in matrix:
        i += 1
        for element in row:
            j += 1
            if j == 4:
                j = 1
            if element == number:
                global k, kk
                k = i-1
                kk = j-1


def printer():
    print("o moves to",move,":\n")
    print(" ", T[0][0], " | ", T[0][1], " | ", T[0][2])
    print("--------------------")
    print(" ", T[1][0], " | ", T[1][1], " | ", T[1][2])
    print("--------------------")
    print(" ", T[2][0], " | ", T[2][1], " | ", T[2][2])
    print("\n______________________________________________________________")
    # print("Chances", chances)
    # print("mtE", mtE)
    # print("random", move)
    print("\n")


def win():
    print("WINNER IS x\n")
    os.system("xcowsay -t5 Namba jeychitom Mara & cowsay -f dragon Namba jeychitom Mara | lolcat")
    os.system("toilet We Won | lolcat")


def lost():
    print("WINNER IS o\n")
    os.system("xcowthink -t5 Ungala ennamo nu nenaichenA vro, ipadi paniteengaley & cowsay *You: am I a joke to you | lolcat")
    print("\033[6;32m","**********You LOST**********","\033[0m")
    os.system("cowsay -f elephant *Computer: hehehe....          Challenge panariya man nee? Ungaluku lam teaching seripattu varadhu coaching dhan| lolcat")


def win_chk():
    global winnerstate
    # winner choose algorithm
 # horizontal

    for i in range(0, 3):
        if T[i] == ['x ', 'x ', 'x ']:
            win()
            winnerstate = False
    for i in range(0, 3):
        if T[i] == ['o ', 'o ', 'o ']:
            lost()
            winnerstate = False
    

 # vertical
    if T[0][0] == T[1][0] == T[2][0]:
        if T[0][0] == 'x ':
            win()
        else:
            lost()
        winnerstate = False
    if T[0][1] == T[1][1] == T[2][1]:
        if T[0][1] == 'x ':
            win()
        else:
            lost()
        winnerstate = False
    if T[0][2] == T[1][2] == T[2][2]:
        if T[0][2] == 'x ':
            win()
        else:
            lost()
        winnerstate = False
 

 # cross
    if T[0][2] == T[1][1] == T[2][0]:
        if T[0][2] == 'x ':
            win()
        else:
            lost()
        winnerstate = False
    elif T[0][0] == T[1][1] == T[2][2]:
        if T[0][0] == 'x ':
            win()
        else:
            lost()
        winnerstate = False


# MAIN 
os.system("figlet Welcome to | lolcat")
os.system("figlet -w150 The Great Kirikalan | lolcat -p 10000000")
os.system("figlet Magic show | lolcat")
print("\nPlot :\n")
print(" 11 | 12 | 13 ")
print("---------------")
print(" 21 | 22 | 23 ")
print("---------------")
print(" 31 | 32 | 33 ")
print("______________________________________________________________\n")


while(counter < 4):
    # declarations
    chances = {22}
    k: int = 0
    kk: int = 0

    # input from player x
    while(True):
        try:
            ce = int(input("Your turn x: "))
        except ValueError:
            print("\033[6;31m","Error: x supports only integer values within the scope of the table","\033[0m")
            continue
        if ce not in mtE:
            print("\033[6;31m","ERROR: Place occupied, retry another place.","\033[0m")
        else:
            break

    if 22 not in mtE or ce == 22:
        chances.remove(22)

# marks position for player x
    searchforindex(T, ce)
    if T[k][kk] in mtE:
        mtE.remove(T[k][kk])
    T[k][kk] = "x "

# game end algorithm
    win_chk()
    if winnerstate == False:
        break

# main algorithm
    for i in {1, -1, 10, -10}:
        q = abs(ce + i)
        if q in AllElements and q in mtE and q not in chances:
            chances.add(q)

# computer generates random positon for player o NOTE: random.choice does not support set so convert into tuple to use
    try:
        move = random.choice(list(chances))
    except IndexError:
        #print("\nchances:",chances,"\nmove:",move,"\nmtE:",mtE)
        move = random.choice(list(mtE))

# marks position for player o
    searchforindex(T, move)
    if move in mtE:
        mtE.remove(move)
    T[k][kk] = "o "

    printer()

# game end algorithm
    win_chk()
    if winnerstate == False:
        break

    counter += 1

if winnerstate:
    print("Match DRAW")
    os.system("xcowsay -t5 You can Do it BUGGAA")
print("\n______________________________________________________________\n")

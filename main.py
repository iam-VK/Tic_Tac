# x 11 31 22 33
# o 21 32 23
# Traceback (most recent call last):
#   File "D:\Hard Drive\Code Library\python\Tic Tac\main.py", line 70, in <module>
#     move = random.choice(tuple(chances))
#   File "D:\Hard Drive\Program Files (Hard Drive)\Python 3.9.6\lib\random.py", line 346, in choice
#     return seq[self._randbelow(len(seq))]
# IndexError: tuple index out of range
import random

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
    # print("11   12  13")
    # print("21   22  23")
    # print("31   32  33")

    print("\n")
    print("Out :\n")
    print(" ", T[0][0], " | ", T[0][1], " | ", T[0][2])
    print("--------------------")
    print(" ", T[1][0], " | ", T[1][1], " | ", T[1][2])
    print("--------------------")
    print(" ", T[2][0], " | ", T[2][1], " | ", T[2][2])
    print("Chances", chances)
    print("mtE", mtE)
    print("random", move)
    print("\n")


while(counter < 4):
    # declarations
    chances = {22}
    k: int = 0
    kk: int = 0

    # input from player x
    ce = int(input("x="))

    if 22 not in mtE or ce == 22:
        chances.remove(22)

# marks position for player x
    searchforindex(T, ce)
    # print(k,kk)
    if T[k][kk] in mtE:
        mtE.remove(T[k][kk])
    T[k][kk] = "x "

# main algorithm
    for i in {1, -1, 10, -10}:
        q = abs(ce + i)
        if q in AllElements and q in mtE and q not in chances:
            chances.add(q)

# computer generates random positon for player o NOTE: random.choice does not support set so convert into tuple to use
    move = random.choice(tuple(chances))

# marks position for player o
    searchforindex(T, move)
    if move in mtE:
        mtE.remove(move)
    T[k][kk] = "o "

    printer()

    # winner choose algorithm
    # horizontal
    for i in range(0, 3):
        if ['x ', 'x ', 'x '] == T[i]:
            print("Winner is x")
            winnerstate = False

        elif ['o ' * 3] == T[i]:
            print("Winner is o")
            winnerstate = False

    # vertical
    if T[0][1] == T[1][1] == T[2][1]:
        print("Winner is", T[0][1])
        winnerstate = False
    elif T[0][2] == T[1][2] == T[2][2]:
        print("Winner is", T[0][2])
        winnerstate = False

    # cross
    elif T[0][2] == T[1][1] == T[2][0]:
        print("Winner is", T[0][2])
        winnerstate = False
    elif T[0][0] == T[1][1] == T[2][2]:
        print("Winner is", T[1][1])
        winnerstate = False

    if winnerstate == False:
        break

# game end algorithm
    counter += 1

if winnerstate:
    print("Match DRAW")

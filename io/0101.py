import random

xle = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
def show(xle):
    """выводит игровое поле"""
    for i in xle:
        print(i, end=" ")
        print(end="\n")

def focus(xle):
    """ход добавляет ход игрока"""
    try:
        x = int(input("ваш ход х = "))
        y = int(input("ваш ход у = "))
    except:
        print("error")
        pass
    if x <=3 and y <=3:
        if xle[y][x] != "X" and xle[y][x] != "O":
            xle[y][x] = "X"
    else:
        print("нет такого хода или он занят")

def prompt(xle):
    """машина делает ход"""
    xm = random.randint(0,2)
    ym = random.randint(0,2)
    while True:
        if xle[ym][xm] != "X" and xle[ym][xm] != "O":
            xle[ym][xm] = "O"
            break
        else:
            continue

def win_player(a):
    """определяет победителя"""
    for i in range(3):
        a = 0
        for j in range(3):
            if xle[i][j] == "X" or xle[j][i] == "X":
                a += 1
            if xle[0][0] == "X" and xle[1][1] == "X" and xle[2][2] == "X":
                a += 3
            if xle[0][2] =="X" and xle[1][1] == "X" and xle[2][0] == "X":
                a += 3
            if a == 3:
                return True
def win_machine(b):
    """определяет победителя"""
    for i in range(3):
        b = 0
        for j in range(3):
            if xle[i][j] == "O" or xle[j][i] == "O":
                b += 1
            if xle[0][0] == "O" and xle[1][1] == "O" and xle[2][2] == "O":
                b += 3
            if xle[0][2] =="O" and xle[1][1] == "O" and xle[2][0] == "O":
                b += 3
            if b == 3:
                return True

while True:
    show(xle)
    focus(xle)
    if win_player("X") == True:
        print("победил игрок")
        show(xle)
        break
    show(xle)
    prompt(xle)
    if win_machine("O") == True:
        print("победил компьютер")
        show(xle)
        break










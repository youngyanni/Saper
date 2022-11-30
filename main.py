import random


def startGame(N):
    P = [-2] * N * N
    PM = [0] * N * N
    createGame(PM)
    finishState = isFinish(PM, P)
    while finishState > 0:
        show(P)
        x, y = goPlayer()
        print(x, y)
        P[x * N + y] = PM[x * N + y]
        finishState = isFinish(PM, P)
    return finishState


def show(pole):
    for i in range(N):
        for j in range(N):
            print(str(pole[i * N + j]).rjust(3), end="")
        print()


def createGame(PM):
    rng = random.Random()
    n = M
    while n > 0:
        i = rng.randrange(N)  # случайное целое [0; N)
        j = rng.randrange(N)
        if PM[i * N + j] != 0:
            continue
        PM[i * N + j] = -1
        n -= 1
    for i in range(N):
        for j in range(N):
            if PM[i * N + j] >= 0:
                PM[i * N + j] = getTotalMines(PM, i, j)


def getTotalMines(PM, i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            p = i + k
            z = j + l
            if p < 0 or p >= N or z < 0 or z >= N:
                continue
            if PM[p * N + z] < 0:
                n += 1
    return n


def goPlayer():
    global x, y
    x = random.randint(1, 10) - 1
    y = random.randint(1, 10) - 1
    return x, y


def isFinish(PM, P):
    for i in range(N * N):
        if P[i] != -2 and PM[i] < 0: return -1
        if P[i] == -2 and PM[i] >= 0: return 1
    return -2


if __name__ == '__main__':
    global N, M,x,y
    N, M = (5, 10)  # Размер поля
    while True:
        result = startGame(N)
        if result == -1:
            print("Вы проиграли")
        else:
            print("Вы выиграли")

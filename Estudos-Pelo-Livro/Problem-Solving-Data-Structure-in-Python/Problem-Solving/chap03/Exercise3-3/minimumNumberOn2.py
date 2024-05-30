import random
# import time

def randomListGenerator():
    randomlist = []

    for i in range(0, 150000):
        n = random.randint(1,200000)
        randomlist.append(n)

    # print(randomlist)
    return randomlist


def minimumNumberOn2(NumberList):

    minimo = ''

    for i in range(0, len(NumberList)):
        minimo = NumberList[i]
        for j in range(0, len(NumberList)):
            if minimo > NumberList[j]:
                minimo = NumberList[j]

    return minimo

# print('minimumNumberOn2 is: %d. Time cost: %10.20f seconds'%minimumNumberOn2(randomListGenerator()))

import random
# import time

def randomListGenerator():
    randomlist = []

    for i in range(0, 150000):
        n = random.randint(1,200000)
        randomlist.append(n)

    return randomlist

def minimumNumberOn(NumberList):

    minimo = NumberList[0]

    for i in range(1,len(NumberList)):
        if minimo > NumberList[i]:
            minimo = NumberList[i]

    return minimo

# print('minimumNumberOn is: %d. Time cost: %10.20f seconds'%minimumNumberOn(randomListGenerator()))  
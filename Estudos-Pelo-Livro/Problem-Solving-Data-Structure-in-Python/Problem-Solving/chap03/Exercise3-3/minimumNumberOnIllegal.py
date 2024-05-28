import random
import time

def randomListGenerator():
    randomlist = []

    for i in range(0, 150000):
        n = random.randint(1,200000)
        randomlist.append(n)

    # print(randomlist)
    return randomlist

start = time.time()
print(f'Minimo: {min(randomListGenerator())}')
end = time.time()
print(f'Tempo de custo: {end - start}')
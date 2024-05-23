# To make from O(n2) to O(n)
# Try to proof mathematically that the code below is not possible to reduce in O(log n)
# Try to see the process to count letters of a phrase is an combinatorial process. You can see any book about.

import time

while True:
    start = time.time()

    letra = input('Digite uma frase ou [s] para sair: ')
    letra = letra.lower()
    ranking_sort = {}

    if letra == 's':
        break

    for i in letra:
        if i in ranking_sort:
            ranking_sort[i] += 1
        else:
            ranking_sort[i] = 1

    result = {k: v for k, v in sorted(ranking_sort.items(), key=lambda item: item[1], reverse=True)}

    print("Quantidade de aparicoes das letras e ordem decrescente:")
    print("Size of the phrase: ", len(letra))
    for key, value in result.items():
        print(f'{key}: {value}')
    end = time.time()

    print("Time cost: ", end - start)
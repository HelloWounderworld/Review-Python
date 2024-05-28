# Determine a funcao T(n) do codigo abaixo

# Por fim, determine o O(f(n)) sendo f(n) a funcao dominante do T(n).

import time

def sumOfNCubicTerms(n):
    start = time.time()
    
    theSum = 0
    for i in range(1, n+1):
        theSum += i**3

    end = time.time()

    return theSum, end - start

def sumOfArquimedesMethodsCubicTerms(n):
    start = time.time()

    sumOfNTerms = ((n*(n+1)) // 2)**2
    
    end = time.time()

    return sumOfNTerms, end - start

# print('sumOfNCubicTerms is: %d. Time cost: %10.20f seconds'%sumOfNCubicTerms(100000000000000000000))
print('sumOfArquimedesMethodsCubicTerms is: %d. Time cost: %10.20f seconds'%sumOfArquimedesMethodsCubicTerms(100000000000000000000))
# Generalize para n elevado a m somas possiveis.

# Determine a funcao T(n) do codigo abaixo

# Por fim, determine o O(f(n)) sendo f(n) a funcao dominante do T(n).

import time

def sumOfN(n):
    start = time.time()
    
    theSum = 0
    for i in range(1, n+1):
        theSum += i

    end = time.time()

    return theSum, end - start

def sumOfNByGaussMethod(n):
    start = time.time()

    sumOfNTerms = n*(n+1)/2
    
    end = time.time()   

    return sumOfNTerms, end - start

print('SumOfN is: %d. Time cost: %10.20f seconds'%sumOfN(10000000))
print('sumOfNByGaussMethod is: %d. Time cost: %10.20f seconds'%sumOfNByGaussMethod(10000000))

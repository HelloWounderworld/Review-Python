# Generalize para n elevado a m somas possiveis.

import time

def sumOfNSquareTerms(n):
    start = time.time()
    
    theSum = 0
    for i in range(1, n+1):
        theSum += i**2

    end = time.time()

    return theSum, end - start

def sumOfNByGaussMethodSquareTerms(n):
    start = time.time()

    sumOfNTerms = (n * (n+1) * (2 * n + 1))//6
    
    end = time.time()   

    return sumOfNTerms, end - start

print('SumOfNSquareTerms is: %d. Time cost: %10.20f seconds'%sumOfNSquareTerms(10000000000))
print('sumOfNByGaussMethodSquareTerms is: %d. Time cost: %10.20f seconds'%sumOfNByGaussMethodSquareTerms(10000000000))

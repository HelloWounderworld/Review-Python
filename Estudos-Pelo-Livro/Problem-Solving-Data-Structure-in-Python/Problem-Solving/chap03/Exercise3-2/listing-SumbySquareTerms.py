# Generalize para n elevado a m somas possiveis. - Nao da nao, ela depende da forma das somas anteriores

# Determine a funcao T(n) do codigo abaixo

# Por fim, determine o O(f(n)) sendo f(n) a funcao dominante do T(n).

# import time

def sumOfNSquareTerms(n):
    # start = time.time()
    
    theSum = 0
    for i in range(1, n+1):
        theSum += i**2

    # end = time.time()

    return theSum

def sumOfNByGaussMethodSquareTerms(n):
    # start = time.time()

    sumOfNTerms = (n * (n+1) * (2 * n + 1))//6
    
    # end = time.time()   

    return sumOfNTerms

# print('SumOfNSquareTerms is: %d. Time cost: %10.20f seconds'%sumOfNSquareTerms(1000000000))
# print('sumOfNByGaussMethodSquareTerms is: %d. Time cost: %10.20f seconds'%sumOfNByGaussMethodSquareTerms(1000000000))

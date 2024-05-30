# Generalize para n elevado a m somas possiveis.

# Determine a funcao T(n) do codigo abaixo

# Por fim, determine o O(f(n)) sendo f(n) a funcao dominante do T(n).

# import time

def sumOfN(n):
    
    theSum = 0
    for i in range(1, n+1):
        theSum += i

    return theSum

def sumOfNByGaussMethod(n):

    sumOfNTerms = n*(n+1)/2
   

    # return sumOfNTerms

# print('SumOfN is: %d. Time cost: %10.20f seconds'%sumOfN(10000000))
# print('sumOfNByGaussMethod is: %d. Time cost: %10.20f seconds'%sumOfNByGaussMethod(10000000))

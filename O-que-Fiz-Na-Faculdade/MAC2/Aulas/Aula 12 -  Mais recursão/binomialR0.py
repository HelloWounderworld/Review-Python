''' 
   MAC0122 Principios de Desenvolvimento de Algoritmos
  
   binomial: versão recursiva que calcula o numero binomial
             n-escolhe-k
'''

def binomialR(n,k):
    if n == 0 and k  > 0: return 0
    if n >= 0 and k == 0: return 1
    return binomialR(n-1,k) + binomialR(n-1, k-1)

def H(n):
    num = 0
    den = 1
    i = 1
    while i <= n:
        num = num*i + den
        den = den*i
        soma = num/den
        i = i + 1
    return soma
    

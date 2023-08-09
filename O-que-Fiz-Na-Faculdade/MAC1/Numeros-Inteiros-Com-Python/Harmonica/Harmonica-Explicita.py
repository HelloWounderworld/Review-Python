def H(n):
    if n == 1:
        return 1
    else:
        x = H(n-1)
        print("1/{}". format(n))
        soma = x + (1/n)
        return soma
        

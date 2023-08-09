def H(n):
    if n == 1:
        return 1
    else:
        x = H(n-1)
        soma = x + (1/n)
    return soma

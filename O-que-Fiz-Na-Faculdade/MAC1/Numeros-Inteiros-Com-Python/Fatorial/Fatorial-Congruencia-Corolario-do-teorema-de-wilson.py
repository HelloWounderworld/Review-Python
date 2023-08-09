def Teorema_Wilson(n):
    x = n-1
    prod = 1
    while x > 0:
        prod = prod * x
        x = x - 1
        
    y = prod
    z = y + 1
    x = n
    if (z%x == 0):
        x = n
        print(x, "E um numero primo")
        return True

    else:
        x = n
        print(x, "Nao e um numero primo")
        return False
main() # n! = n (n - 1)! é um processo recursivo


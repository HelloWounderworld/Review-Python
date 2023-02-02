def Teorema_Wilson():
    n = int(input("Entre com um número:"))
    prod=1
    for i in range(1,n):
        prod=prod*i
    y = prod
    z = y + 1
    x = n
    if (z%x == 0):
        x = n
        print(x, "E um numero primo")
        return True

    else:
        return False
Teorema_Wilson()

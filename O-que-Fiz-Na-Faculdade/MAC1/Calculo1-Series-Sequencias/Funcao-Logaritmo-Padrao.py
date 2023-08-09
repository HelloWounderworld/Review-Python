import math

def FuncaoLogaritmo():
    x = float(input("Entre com um número: "))
    if x <= 0:
        print("Tem que ser numero positivo caralho !!")
        return

    y = math.log1p(x)
    print(y)
FuncaoLogaritmo()

def fatorial_rec(n): # A linguagem recursiva, ao definir uma funçao, dentro da mesma funçao,pode ser colocadoa funçao
    n = int(input("Entre com o valor de n:"))
    if n == 1:
        return 1
    else: #else e uma opçao exclusiva
        fn = n * fatorial(n-1)
        return fn # se quiser poderia colocar diretamente return n * fatorial_rec(n-1)

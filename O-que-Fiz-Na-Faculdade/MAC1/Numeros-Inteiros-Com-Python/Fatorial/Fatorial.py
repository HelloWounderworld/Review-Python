def main():
    n = int(input("Entre com o valor de n:"))
    x = n
    prod = 1
    while x > 0:
        prod = prod * x
        x = x - 1
        
    y = prod
    z = y + 1
    w = n
    if z % w == 0:
        x = n
        print(x, "Nao e um numero primo")

    else:
        x = n
        print(x, "E um numero primo")

main() # n! = n (n - 1)! é um processo recursivo


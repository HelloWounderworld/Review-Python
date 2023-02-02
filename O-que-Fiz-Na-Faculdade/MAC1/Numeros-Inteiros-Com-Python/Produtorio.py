def main():
    n = int(input("Entre com o valor de n:"))
    x = 1
    prod = 1
    while x <= n:
        prod = prod * x
        x = x + 1
    print("O produtorio é", prod)

main()

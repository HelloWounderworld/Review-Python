def main():
    fim = 0
    while fim == 0:
        str = input("Entre com n ou digite 'fim'")
        if str != "fim": # Sinal != e diferente
            n = int(str)
            prod = 1
            x = n
            while x > 0:
                prod = prod * x
                x = x - 1
            print("O valor de", n, "!=", prod)
        else:
            fim = 1

main()


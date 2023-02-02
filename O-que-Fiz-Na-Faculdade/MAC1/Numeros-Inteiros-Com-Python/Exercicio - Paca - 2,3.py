def main():
    k = int(input("Entre com um valor inteiro: "))
    n = int(input("Entre com um valor inteiro: "))
    zero = 0
    while k > zero :
        n = n**k
        zero = zero + k
        print("Mostre-me o valores calculados: ", n)
    print("A potencia e: ", zero)
    print("O valor é: ", n)
main()

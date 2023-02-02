def main():
    while True:
        n = int(input("Entre com um valor inteiro: "))
        m = n - 1
        soma = 1
        while m >= soma:
            n = n*m
            m = m - 1
            print("Mostre me o processo: ", n)
        print("Fatorial do numero de entrada: ", n)
main()

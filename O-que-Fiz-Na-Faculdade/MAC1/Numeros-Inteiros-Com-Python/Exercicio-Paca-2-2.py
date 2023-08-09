def main():
    numero = int(input("Entre com um valor inteiro: "))
    soma = 0

    while (numero != 0):
        soma = numero + soma
        print("Soma dos valores consecutivos: ", soma)
        numero = int(input("Entre com um outro valor inteiro: "))
        
    print("Soma total e: ", soma)
main()

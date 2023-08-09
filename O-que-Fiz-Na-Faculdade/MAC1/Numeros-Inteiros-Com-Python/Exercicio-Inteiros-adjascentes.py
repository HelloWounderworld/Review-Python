def main():
    while (True):
        n= int(input("Entre com o valor de n: "))
        x = n // 10
        digito_2 = n%10
        Consequencia = False # Geralmente os booleanos funcionam como uma forma de conseguir parar de rodar o programa, como se colocasse um ponto final
        while x > 0 and Consequencia == False:
            digito_1 = x % 10
            if digito_1 == digito_2:
                Consequencia = True
                print("Mostre o valor: ", n)
                print("O digito adjascente: ")
            x = x // 10
            digito_1 = digito_2
        if Consequencia == True:
            print("Existem dois digitos adjascentes")
        else:
            print("Nao possui digitos adjascentes")

main()

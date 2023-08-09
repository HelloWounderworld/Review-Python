def main():
    n= int(input("Entre com o valor de n: "))
    x = n // 10
    digito_2 = n%10
    Consequencia = False # Geralmente os booleanos funcionam como uma forma de conseguir parar com o programa
    while x > 0 and not Consequencia:
        digito_1 = x % 10
        if digito_1 == digito_2:
            Consequencia = True
            print("Possui digitos adjascentes")
        x = x // 10
        digito_1 = digito_2
    if Consequencia:
        print("Existam 2 digitos, adjascentes iguais")
    else:
        print("Nao possui digitos adjascentes")
main()
    

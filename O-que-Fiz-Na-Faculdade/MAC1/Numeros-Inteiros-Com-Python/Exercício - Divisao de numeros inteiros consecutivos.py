#Dizemos que um número inteiro positivo é triangular se ele é o produto de três números inteiros consecutivos. Por exemplo, 120 é triangular,
#pois 4*5*6 é igual 120. Escreva um programa em Python que receba um valor inteiro positivo n, e verifica se ele é triangular.
while (True):
    i = 1
    n = int(input("Etre com o valor de n:"))
    condiçao = False
    while (i*(i+1)*(i+2)<=n and condiçao == False):
        if (i*(i+1)*(i+2) == n):
            n = i*(i+1)*(i+2)
            a = i
            b = (i+1)
            c = (i+2)
            print("Os numeros consecutivos sao:", a, b, c)
            print ("O valor e", n)
            print("E um numero inteiro positivo triangular")
            condiçao = True
        else:
            i = i + 1
    if (condiçao == False):
        print("Nao e um numero inteiro positivo triangular")
        print(input("Entra com outro numero:"))

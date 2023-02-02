#Dado um valor inteiro n, escreva um programa que verifique se n é primo ou não
while ( True ):
    n = int(input("Entre com um valor de n:"))
    i = 2
    Condiçao = False
    while(n > i*i and Condiçao == False):
        if (n%i != 0):
            i = i + 1
        else:
            print("Nao e um numero primo")
            Condiçao = True
    if(Condiçao == False):
        print("E um numero primo")
                
    

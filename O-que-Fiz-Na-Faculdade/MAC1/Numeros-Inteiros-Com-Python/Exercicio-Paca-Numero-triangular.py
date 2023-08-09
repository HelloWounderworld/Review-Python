def main():
    while True:
        n = int(input("Entre com um numero inteiro: "))
        soma = 0
        condiçao = True
        while ( (soma + 1)*(soma + 2)*(soma + 3) < n and condiçao == True):
            soma = soma + 1
            print("Revele o processo: ", soma)
        if (soma + 1)*(soma + 2)*(soma + 3) == n:
            print("E um numero triangular: ", n)
        else:
            print("Nao e um numero triangular: ", n)            
main()

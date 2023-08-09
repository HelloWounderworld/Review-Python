#Dado um inteiro positivo n, calcular e imprimir o valor da seguinte soma: 1/n + 2/(n-1) + 3/(n-2) + ... + n/1
def main():
    n = int(input("Entre com um valor n: "))
    soma = 0
    indice = 0
    contador = 1
    while(contador <= n):
        serie = (1 + soma)/(n-soma)
        print("Mostre o processo da serie: ", serie)
        indice = indice + serie
        print("Mostre o processo: ", indice)
        soma = soma + 1
        contador = contador + 1
    print("Valor da serie finita: ", indice)
main()



        

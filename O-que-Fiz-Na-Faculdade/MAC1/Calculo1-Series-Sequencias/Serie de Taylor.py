def pot(x,n): # Exercício, fazer essa mesma simulaçao apenas em uma função
    prod = 1
    while (n>0):
        prod = prod * x
        n = n - 1
    return prod

def fatorial(x):
    prod = 1
    while (x > 0):
        prod = prod * x
        x = x - 1
    return prod

def cosseno(x,r):
    soma = 0
    k = 0
    termo = pot(x,2*k)/fatorial(2*k)
    while(not termo < r):
        soma = soma + pot(-1,k)*termo
        print("Mostre - me o processo: ", soma)
        k = k + 1
        termo = pot(x,2*k)/fatorial(2*k)
    return soma

def main():
    n = int(input("Entre com um valor de n: "))
    x = float(input("Entre com um valor radiano: "))
    r = float(input("Entre com um valor do raio: "))
    print("O valor do cosseno ({})= {}". format(x,cosseno(x,r)))
main()
        
        

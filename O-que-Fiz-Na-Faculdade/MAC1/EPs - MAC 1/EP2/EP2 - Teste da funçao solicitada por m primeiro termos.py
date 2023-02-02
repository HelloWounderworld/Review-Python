def deixando_mais_preciso(n):
    if(0 < n <= 1000):
        m = n % 10
        
    elif(0 < n <= 100):
        m = n // 10

def fatorial(n):
    produtorio = 1
    while(n > 0):
        produtorio = produtorio*n
        n = n - 1
    return produtorio

def potencia(x,n):
    potencia = 1
    while(n > 0):
        potencia = potencia*x
        n = n - 1
    return potencia

def cosseno(x,n):
    somatorio = 0
    k = 0
    termo_geral = potencia(x,2*k)/fatorial(2*k)
    while(k <= n):
        somatorio = somatorio + potencia(-1,k)*termo_geral
        print("Valor do somatorio: ", somatorio)
        print("Numeros de somas feita: {}". format(k))
        k = k + 1
        termo_geral = potencia(x,2*k)/fatorial(2*k)
        
    return somatorio

def main():
    n = int(input("Entre com um valor inteiro positivo: "))
    x = float(input("Entre com um valor radiano: "))

    print("O valor do cosseno de {} obtido pela Serie de Taylor e: {}". format(x,cosseno(x,n)))

main()

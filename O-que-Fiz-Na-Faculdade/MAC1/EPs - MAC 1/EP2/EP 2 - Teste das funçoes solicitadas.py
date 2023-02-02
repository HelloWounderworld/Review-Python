def fatorial(n):
    produtorio = 1
    while (n > 0):
        produtorio = produtorio * n
        n = n - 1
        #print("Mostre - me o processo do produtorio: ", produtorio)
    return produtorio

def potencia(x,m):
    potencia = 1
    while(m > 0):
        potencia = potencia*x
        m = m - 1
        #print("Mostre-me o processo da potencia: ", potencia)
    return potencia
            
    
def cosseno(x,e):
    somatorio = 0
    k = 0
    termo_geral = potencia(x,2*k)/fatorial(2*k)
    while(not termo_geral < e):
        somatorio = somatorio + potencia(-1,k)*termo_geral
        #print("Releve-me o processo: ", somatorio)
        k = k + 1
        termo_geral = potencia(x,2*k)/fatorial(2*k)
    return somatorio
    

def main():
    n = int(input("Entre com um valor inteiro positivo: "))
    x = float(input("Entre com um valor radiano: "))
    e = float(input("Entre com um valor do raio: "))

    print("Valor da serie de Taylor de cosseno de {} e: {}". format(x,cosseno(x,e)))

main()
        

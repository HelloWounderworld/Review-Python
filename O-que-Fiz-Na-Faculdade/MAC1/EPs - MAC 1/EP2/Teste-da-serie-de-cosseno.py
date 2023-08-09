def cosseno_2(delta,M):
    soma = 0
    k = 0
    termo_geral = potencia(delta,2*k)/fatorial(2*k)
    while(k <= M):
        soma = soma + potencia(-1,k)*termo_geral
        print("Mostre-me o processo do fatorial: ", fatorial(2*k))
        print("Mostre-me o processo do potencial: ", potencia(delta,2*k))
        print("Mostre-me o processo do termo geral: ", termo_geral)
        print("Mostre-me o processo da soma: ", soma)
        print("*********************************************************************************")
        k = k + 1
        termo_geral = potencia(delta,2*k)/fatorial(2*k)
    return soma

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

x = float(input("Entre com um valor do intervalo a ser integrado: "))
while(not 0 < x < 3.1416):
    x = float(input("Entre com um valor do intervalo a ser integrado: "))
print("*********************************************************************************")
n = int(input("Quantas vezes deseja calcular a aproximaçao?\nDigite o valor inteiro positivo: "))
while(not n > 0):
    n = int(input("Quantas vezes deseja calcular a aproximaçao?\nDigite o valor inteiro positivo: "))
print("*********************************************************************************")
delta = x / n
print("O valor do intervalo a ser considerado: ", delta)
print("*********************************************************************************")
M = int(input("Ate quantos termos da serie o senhor deseja soma-lo ?\nDigite o valor: "))
p = 1
somatorio = 0
while(p <= n):
    
    delta = p*delta
    if(cosseno_2(delta,M) <= 0):
        
        somatorio = somatorio + (-1)*cosseno_2(delta,M)
        print("Valor do cosseno_2: ", cosseno_2(delta,M))
        print("Valor do Somatorio: ", somatorio)
    else:
        
        somatorio = somatorio + cosseno_2(delta,M)
        print("Valor do cosseno_2: ", cosseno_2(delta,M))
        print("Valor do Somatorio: ", somatorio)
    p = p + 1
    print("*********************************************************************************")

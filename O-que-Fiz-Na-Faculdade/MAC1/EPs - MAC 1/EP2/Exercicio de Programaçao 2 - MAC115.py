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

def cosseno_1(delta,e):
    soma = 0
    serie = 0
    k = 0
    termo_geral = potencia(delta,2*k)/fatorial(2*k)
    while(not termo_geral < e):
        soma = soma + potencia(-1,k)*termo_geral
        #print("Mostre-me o processo do fatorial calculado: ", fatorial(2*k))
        #print("Mostre-me o processo da potencia calculado: ", potencia(delta,2*k))
        #print("Mostre-me o valor do termo geral calculado: ", termo_geral)
        k = k + 1
        termo_geral = potencia(delta,2*k)/fatorial(2*k)
    #print("Valor do cosseno: ", soma)
    if(soma <= 0):
        serie = (-1)*soma    
    else:
        serie = soma
    #print("Valor da soma convertida: ", serie)
    return serie

def cosseno_2(delta,M):
    soma = 0
    serie = 0
    somatoria = 0
    k = 0
    termo_geral = potencia(delta,2*k)/fatorial(2*k)
    while(k <= (M - 1)):
        soma = soma + potencia(-1,k)*termo_geral
        #print("Mostre-me o processo do fatorial calculado: ", fatorial(2*k))
        #print("Mostre-me o processo da potencia calculado: ", potencia(delta,2*k))
        #print("Mostre-me o valor do termo geral calculado: ", termo_geral)
        k = k + 1
        termo_geral = potencia(delta,2*k)/fatorial(2*k)
    #print("Valor do cosseno: ", soma)
    if(soma <= 0):
        serie = (-1)*soma
    else:
        serie = soma
    #print("Valor da soma convertida: ", serie)
    return serie

def main():
    x = float(input("Entre com um valor do intervalo a ser integrado: "))
    while(not 0 < x < (3.1416/2)):
        x = float(input("Entre com um valor do intervalo a ser integrado: "))
    print("*********************************************************************************")
    n = int(input("Quantas vezes o senhor deseja dividir o intervalo e calcular a aproximaçao?\nDigite o valor inteiro positivo: "))
    while(not n > 0):
        n = int(input("Quantas vezes o senhor deseja calcular a aproximaçao?\nDigite o valor inteiro positivo: "))
    print("*********************************************************************************")
    Largura = float(x / n) #Essa sera a largura da escada
    print("O valor do delta ou largura da escada a ser considerado: ", Largura)
    print("*********************************************************************************")
        
    Forma_de_calculo = str(input("Prefere calcular de qual forma ?\nEscolha uma das seguintes opçoes:\n- 'Aproximaçao' - Digite numero 1 \n- 'Somando M primeiros termos' - Digite numero 2\nDigite a opçao desejada: "))
    
    while( not (Forma_de_calculo == "1" or Forma_de_calculo == "2")):
        Forma_de_calculo = str(input("Prefere calcular de qual forma ?\nEscolha uma das seguintes opçoes:\n- 'Aproximaçao' - Digite numero 1 \n- 'Somando M primeiros termos' - Digite numero 2\nDigite a opçao desejada: "))
        print("*********************************************************************************")  

    if(Forma_de_calculo == "1"):
        e = float(input("Retangulo 1\nEntre com um valor de Precisao: "))
        p = 1
        integral = 0
        infinitesimal = x / n
        delta = 0
        while(not e > 0):
            e = float(input("Retangulo 1\nEntre com um valor de Precisao: "))
        #print("*********************************************************************************")
        while(p <= n):
            delta = delta + Largura
            #print("Mostre-me o delta: ", delta)
            integral = integral + infinitesimal*cosseno_1(delta,e)
            p = p + 1
            #print("Mostre-me o integral calculado: ", integral)
            #print("*********************************************************************************")
        print("Retangulo 1\nPrecisao colocada: ", e)
        print("Resultado da integral do cosseno do intervalo {} e: {}". format(x,integral))
                
    else:
        M = int(input("Retangulo 2\nAte quantos termos da serie o senhor deseja soma-lo ?\nDigite o valor: "))
        p = 1
        integral = 0
        infinitesimal = x / n
        delta = 0
        while(not M > 0):
            M = int(input("Retangulo 2\nAte quantos termos da serie o senhor deseja soma-lo ?\nDigite o valor: "))
        #print("*********************************************************************************")
        while(p <= n):
            delta = delta + Largura
            #print("Mostre-me o delta: ", delta)
            integral = integral + infinitesimal*cosseno_2(delta,M)
            p = p + 1
            #print("Mostre-me o integral calculado: ", integral)
            #print("*********************************************************************************")
        print("Retangulo 2\nNumero de termos considerados na soma da Serie de Taylor do Cosseno: ", M)
        print("Resultado da integral do cosseno do intervalo {} pelo numero de termos {} e: {}". format(x,M,integral))
main()
                
                

        







        
            
        

def cria_matriz(lins,cols):
    print("Entrei na funçao cria_matriz")
    M = []
    # Poderia colocar a linha aqui, que será o mesmo resultado, mas se eu colocar aqui, caso eu troque as linhas todos os outros valores da mesma linha serao
    #trocados. Teste, coloque a linha aqui
    for i in range(lins):
        linha = []
        for j in range(cols):
            print("Mostre-me o indice i considerado: ", i)
            # Uma lista do mesmo valor igual ao numeros de linhas, feito isso pela multiplicaçao do numero de colunas
            valor = float(input("Entre com um valor que sera elemento de M {}x{}: ". format(i+1,j+1)))
            linha.append(valor)
            print("Mostre-me a linha: ", linha)
            print()
        M.append(linha)
        print("Mostre-me a matriz sendo construida: ", M)
        print()
    return M

def transposta(M):
    print("Entrei na funçao transposta")
    lins = len(M)
    cols = len(M[0])
    T = cria_matriz(cols,lins,0) #Aqui comecei com a nova matriz (matriz transposta) zerado
    print("Mostre-me o estado inicial da matriz transposta T: ", T)
    for i in range(lins):
        for j in range(cols):
            print("Mostre-me o indice i e j, respectivamente, {} e {}". format(i,j))
            T[j][i] = M[i][j]
            print("Mostre-me o elemento que sera colocado na matriz transposta: ", M[i][j])
            print("Mostre-me a matriz transposta que esta sendo construido: ", T)
            print()
    return T

def soma(A,B): #A e o B aqui sao matrizes, supondo que as duas possuem as mesmas dimençoes
    print("Entrei na funçao soma")
    lins = len(A)
    cols = len(B)
    C = cria_matriz(lins,cols,0)
    print("Mostre-me o estado inicial da matriz somado C: ", C[i][j])
    for i in range(lins):
        for j in range(cols):
            print("Mostre-me os indices i e j considerado, respectivamente, {} e {}". format(i,j))
            C[i][j] = A[i][j] + B[i][j]
            print("Mostre-me o elemento da matriz A que sera somado: ", A[i][j])
            print("Mostre-me o elemento da matriz B que sera somado: ", B[i][j])
            print("Mostre-me o elemento somado: ", C[i][j])
            print("Mostre-me a matriz C que e o resultado das somas dos elementos da matriz A e B: ", C)
            print()
    return C

def produto_escalar(a,b): # Aqui a e o b sao listas, e assumimos que possuem os mesmos numeros
     print("Entrei na funçao produto_escalar")
     soma = 0
     for i in range(len(a)):
         print("Mostre-me o indice i considerado: ", i)
         soma = soma + a[i]*b[i]
         print("Mostre-me a soma considerado: ", soma)
         print()
     return soma

#def produto_escalar(a,b): # Forma alternativa
    #soma = 0
    #for x,y in zip(a,b): # Comando zip cria uma lista de pares de valores
        #soma = soma + x*y
    #return soma

def multiplica(A,B):
    print("Entrei na funçao multiplica")
    lins = len(A)
    cols = len(B[0])
    C = cria_matriz(lins,cols,0)
    print("Mostre-me o estado da matriz inicial que sera o produto de duas matriz: ", C)
    for i in range(lins):
        for j in range(cols):
            print("Mostre-me o indice i e j que sera considerado, respectivamente, {} e {}". format(i,j))
            coluna = [B[k][j] for k in range(len(B))]
            print("Mostre-me a nova matriz coluna que esta sendo montada para o produto escalar: ", coluna)
            C[i][j] = produto_escalar(A[i],coluna)
            print("Mostre-me o resultado da multiplicaçao do elemento que sera incluso na nova matriz: ", C[i][j])
            print("Mostre-me a nova matriz que esta sendo construido: ", C)
            print()
            #C[i][j] = produto_escalar(A[i],[B[k][j] for k in range(len(B))])
    return C

# cubo = [[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]] Matriz 3D

#def main():
    #numero_de_linhas = int(input("Entre com um valor inteiro positivo que sera o numero de linhas: "))
    #numero_de_colunas = int(input("Entre com um valor inteiro positivo que sera o numero de colunas: "))
    #Matriz_A = [[]]*numero_de_linhas
    #Matriz_B = [[]]*numero_de_linhas
    #for i in range(numero_de_linhas):
        #for j in range(numero_de_colunas):
            #elemento_A = float(input("Entre com um valor que sera o elemento da Matriz_A {}x{}: ". format(i,j)))
            #elemento_B = float(input("Entre com um valor que sera o elemento da Matriz_B {}x{}: ". format(i,j)))
            #Matriz_A[i][j] = elemento_A
            #Matriz_B[i][j] = elemento_B
    #print("Mostre-me a Matriz_A que foi construida: ", Matriz_A)
    #print("Mostre-me a transposta da Matriz_A: ", transposta(Matriz_A))
    #print()
    #print("Mostre-me a Matriz_B que foi construida: ", Matriz_B)
    #print("Motre-me a transposta da Matriz_B: ", Matriz_B)
    #print()    
#main()

def main():
    n = int(input("Qual sera o numero de linha: "))
    m = int(input("Qual sera o numero de colna: "))
    print("Mostre-me a matriz que foi criado: ", cria_matriz(n,m))
    print()
main()

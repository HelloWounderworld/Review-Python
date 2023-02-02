'''Nome: Leonardo Takashi Teramatsu
   NºUSP: 9797083
   Materia: MAC0115 - Introduçao a Computaçao para Ciencias Exatas e Tecnologia - IF
   Prof: Marcel Parolin Jackowski '''

def Monta_Matriz(M,linha,coluna):
    
    for i in range(linha):
        Cobaia = []
        for j in range(coluna):
            elemento = int(input("Entre com um valor inteiro entre 1 a 9 que sera o elemento da matriz: "))
            Cobaia.append(elemento)
            print("Mostre-me a linha criada: ", Cobaia)
        M.append(Cobaia)
        print("Mostre-me a Matriz sendo Construida: ", M)
    return M

def Visualiza_Matriz(M):
    print("Matriz {}x{}: ". format(len(M),len(M[0])))
    for i in M:
        for j in i:
            print("{}". format(j). rjust(5), end="")
        print()

def Monta_Padrao(Lista):
    
    Quantidade = int(input("Quantos Padroes o senhor deseja criar ? Colque um valor inteiro: "))
    for j in range(Quantidade):
        Comprimento = int(input("Qual o Comprimento do Padrao o senhor deseja? Colque um valor: "))
        Padroes = []
        for i in range(Comprimento):
            elemento = int(input("Entre com um valor inteiro entre 1 a 9: "))
            Padroes.append(elemento)
        Lista.append(Padroes)
    return Lista

''' 
    Essa funcao serve para verificar se o primeiro elemento do padrao solicitado
    se encontra na matriz que foi montado. Caso o primeiro elemento do padrao se
    encontra a funcao retorna (linha,coluna), ou seja, a posicao elemento, se nao
    retorna -1 
'''
def ProcuraPrimeiroNumero(Retangulo, Padrao, i, j): 
    
    if i >= len(Retangulo):
        return -1

    for linha in range(i, len(Retangulo)):
        ini = 0
        if (linha == i):
            ini = j
        for coluna in range(ini, len(Retangulo[linha])):
            if (Padrao[0] == Retangulo[linha][coluna]):
                #print("O primeiro elemento do Padrao solicitado se encontra nessa matriz na posiçao: ({},{})". format(i,j))
                return (linha,coluna)
    return -1
   

'''
   Essa funcao verifica se um dado padrao solicitado, o seu tamanho cabe ou nao
   em uma matriz. Caso o tamanho dela couber na matriz e retornado 1, caso nao 
   retorna 0
'''
def VerificaSeCabe(Retangulo, t, direcao, i, j):
    v = [[0, 0], [-1, 0], [0, +1], [+1, 0], [0, -1]]
    
    dx = 0
    dy = 0
    dig2 = direcao % 10
    dig1 = direcao // 10
    
    dx += v[dig1][0]
    dy += v[dig2][1]
    l = 0
    while (l < t):
        if (i < len(Retangulo) and j < len(Retangulo[0]) and i >= 0 and j >= 0):
            l = l + 1
        else:
            return 0
        i = i + dx
        j = j + dy

    return 1

'''
    Essa funcao verifica se um dado padrao solicitado realmente se encontra
    dentro da matriz, para isso essa funcao faz um link com a funcao
    VerificaSeCabe, primeiro para analisa se tal padrao solicitado de fato cabe
    na matriz na direcao solicitado. 
    As direcoes que entram no parametro da funcao sao convertidos em direcoes 
    [[0, 0], [-1, 0], [0, +1], [+1, 0], [0, -1]] para facilitar a analise da
    direcao solicitado dentro da matriz. 
    Assim, caso o Padrao se encontrar na matriz a funcao retorna True, se nao
    retorna False.
'''
def AchaPadrao(Retangulo, Padrao, direcao, i, j):
    avalia = VerificaSeCabe(Retangulo, len(Padrao), direcao, i, j)
    
    if (avalia == 0):
        return False

    v = [[0, 0], [-1, 0], [0, +1], [+1, 0], [0, -1]]
    
    dx = 0
    dy = 0
    dig2 = direcao % 10
    dig1 = direcao // 10
    
    dx += v[dig1][0]
    dy += v[dig2][1]
    l = 0
    while (l < len(Padrao)):
        if (Padrao[l] != Retangulo[i][j]):
            return False
            
        i = i + dx
        j = j + dy
        l = l + 1
    
    return True
    
def testes():
    M = [ [1, 2, 3, 5, 6, 7, 8, 9],
          [1, 2, 3, 5, 0, 7, 8, 9],
          [2, 2, 3, 5, 6, 7, 8, 9],
          [1, 2, 3, 5, 6, 4, 8, 9],
          [1, 2, 3, 5, 4, 7, 8, 9],
          [1, 2, 3, 5, 6, 7, 4, 9],
          [1, 2, 3, 5, 6, 7, 8, 2],
          [1, 2, 2, 5, 6, 7, 8, 9] ]
    P = [1, 2, 3, 5, 6, 7, 8, 9]
    PK = [1,2,3,5,4]
    pos = ProcuraPrimeiroNumero(M, P, 0, 0) # (0, 0)
    assert pos == (0, 0)
    val = AchaPadrao(M, PK, 32, 0, 0)
    assert val == True
    val = AchaPadrao(M, P, 22, 3, 0)
    assert val == False
    val = AchaPadrao(M, P, 22, 3, 2)
    assert val == False
    pos = ProcuraPrimeiroNumero(M, P, 1, 1) # (3, 0)
    assert pos == (3, 0)
    val = VerificaSeCabe(M, 8, 32, 0, 0)
    assert val == 1
    val = VerificaSeCabe(M, 8, 33, 1, 1)
    assert val == 0
    val = VerificaSeCabe(M, 8, 11, 6, 6)
    assert val == 0
    val = VerificaSeCabe(M, 8, 11, 7, 7)
    assert val == 1
	
def main():
    testes()

    n = int(input("Entre com um valor inteiro positivo maior ou igual a 8 para a quantidade de linha: "))
    m = int(input("Entre com um valor inteiro positivo maior ou igual a 8 para a quantidade de coluna: "))
    Matriz = []
    Sequencias = []
    Dami = Monta_Matriz(Matriz,n,m) #Lembre-se cara sempre apos colocar em uma funçao e querer colocar isso em uma outra funçao atribua um nome
    Visualiza_Matriz(Dami)
    Padrao = Monta_Padrao(Sequencias)
    Direcao = [11, 22, 33, 44, 12, 32, 34, 14]
    T = {11 : 'Norte', 22 : 'Leste', 33 : 'Sul', 44 : 'Oeste', 12 : 'Nordeste' , 32 : 'Sudeste', 34 : 'Sudoeste', 14 : 'Noroeste'}	
    print("Numero de Padroes: ", len(Padrao))
    for padrao in Padrao:
        pos = ProcuraPrimeiroNumero(Dami, padrao, 0, 0)
        contador = 0
        while (pos != -1):
            for direcao in Direcao:
                i, j = pos
                Acha = AchaPadrao(Dami, padrao, direcao, i, j)
                if (Acha == True):                    
                    print("Esse padrao {} ocorre na matriz da posicao {} em direcao {}". format(padrao, pos, T[direcao]))
                    contador = contador + 1
            linha, coluna = pos
            coluna = coluna + 1
            if (coluna == len(Dami[0])):
                coluna = 0
                linha = linha + 1
            pos = (linha, coluna)
            pos = ProcuraPrimeiroNumero(Dami, padrao, linha, coluna)
        if (contador == 0):
            print("Esse padrao {} nao ocorre na matriz". format(padrao))
      
main()
        
    
    
                        
        
        
    
        
        
        
    
    
    
                
            
    

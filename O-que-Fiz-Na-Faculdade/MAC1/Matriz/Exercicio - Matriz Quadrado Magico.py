#2) Dizemos que uma matriz A é um quadrado mágico se A é quadrada e se o valor da soma dos elementos de cada linha e de cada coluna é o mesmo.
#Escreva uma função em Python que retorne True caso uma matriz A seja um quadrado mágico.
#Você pode decompor o problema em várias funções para facilitar a solução.

def quadrado(M):
    if len(M) != len(M[0]):
        return print("Nao e quadrado")
    return print("E quadrado")

def confere_magico(M):
    soma = 0
    elemento = 0
    elemento_coluna = 0
    i = 0
    j = 0
    l = 0
    
    while(i < len(M[0])):
        soma = soma + M[0][i]
        i = i + 1
        
    for linha in range(len(M)):
        while (j < len(M[0])):
            elemento = elemento + M[linha][j]
            j = j + 1
        if (elemento != soma):
            return print("Nao e quadrado magico")
    
    Matriz_coluna = []
    for j in range(len(M[0])):
        Dami = []
        for i in range(len(M)):
            Dami.append(M[i][j])
        Matriz_coluna.append(Dami)
    #Transposta = visualiza_matriz(Matriz_coluna)
            

    for i in range(len(Matriz_coluna)):
        while(l < len(Matriz_coluna[0])):
            elemento_coluna = elemento_coluna + Matriz_coluna[i][l]
            l = l + 1
        if (elemento_coluna != soma):
            return print("Nao e um quadrado magico")
    return print("E um quadrado magico")

def visualiza_matriz(M):
    print("Matriz {}x{}:". format(len(M),len(M[0])))
    for i in M:
        for j in i:
            print("{}". format(j). rjust(5), end = "")
        print()

def main():
    n = int(input("Qual o numero de linha da matriz: "))
    m = int(input("Qual o numero de coluna da matriz: "))
    Matriz = []
    for i in range(n):
        Cobaia = []
        for j in range(m):
            elemento = float(input("Digite um elemento: "))
            Cobaia.append(elemento)
        Matriz.append(Cobaia)
    Picture = visualiza_matriz(Matriz)
    Avalia = quadrado(Matriz)
    Etapa_final = confere_magico(Matriz)
main()
            


        
        
    
            
            
    
    




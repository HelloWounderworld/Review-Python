def imprime_matriz(M):
    print("Matriz{} x {}". format(len(M),len(M[0])))

    for linha in M:
        for coluna in linha:
            print("{}". format(coluna). rjust(5), end = "") 
            #rjust(5) = me fornece os espaços equivalente ao 5 digitos; end = "" funciona para nao dar mais os espaços; caso queira nao espaçar maise pular a linha end = "\n"
        print() #print() serve para pular a linha

def matriz(M):
    if (type(M) == list and len(M) > 0): # No caso de matriz, se eu colocar type(M) vai aparecer <class 'list'>, ou seja, a lista (ou matriz) possui sublistas
        # no type para ver se as sublistas sao de fato listas poderia ter feito type(M[:]) == list
        for i in range(len(M)):
            if ((type(M[i-1]) != list or type(M[i]) != list or len(M[i-1]) != len(M[i])): # Aqui falta ver se os elementos da sublistas sao floats. Exercicio !!!
                return False

        return True
    else:
        return False

def quadrada(M):
    return matriz(M) and len(M) == len(M[0])
# Aqui so compara com a primeira sublista. Logo precisaria colocar uma forma de contagem para analisar o len(M) com todas as outras sublistas

def simetrica(M):
    lins = len(M)
    cols = len(M[0])
    for i in range(lins):
        for j in range(cols):
            if (M[i][j] != M[j][i]):
                return False
    return True

def conta_zeros(lista):
    total = o
    for v in range(linta): #Caso eu coloque range( ,fim) a parte vago do range o python interpreta como 0
        if v == 0:
            total = total + 1
    return total

def main():
    c = [[0,0,0,0,1],[0,0,0,0,0],[0,1,0,0,0],[0,0,0,0,0]]
    linhas_nulas = 0
    colunas_nulas = 0
    for i in range(len(c)):
        if conta_zeros(c[i]) == len(c[i]):
            linhas_nulas = linhas_nulas + 1

    for j in range(len(c[0])):
        coluna = []
        for i in range(len(c)): # outra forma de fazer uma lista em uma linha: coluna = [c[i][j] for i in range(len(c))]
            coluna.append(c[i][j])

        if conta_zeros(coluna) == len(coluna):
            coluna_nulas = coluna_nulas + 1

    print("linhas nulas = ", linhas_nulas)
    print("colunas nulas = ", colunas_nulas)
main()

#Uma forma de fazer uma lista em uma linha: y = [expressao for item in sequencia if condiçao]
        
        

            
            

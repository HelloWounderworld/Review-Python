def imprime_matriz(M):
    print("Entrei na funçao imprime_matriz(M)")
    print("Matriz {} x {}". format(len(M),len(M[0])))

    for linha in M:
        for coluna in linha:
            print("{}". format(coluna). rjust(5), end = "") 
            #rjust(5) = me fornece os espaços equivalente ao 5 digitos; end = "" funciona para nao dar mais os espaços; caso queira nao espaçar maise pular a linha end = "\n"
        print() #print() serve para pular a linha

def matriz(M):
    print("Entrei na funçao matriz(M)")
    if (type(M) == list and len(M) > 0): # No caso de matriz, se eu colocar type(M) vai aparecer <class 'list'>, ou seja, a lista (ou matriz) possui sublistas
        # no type para ver se as sublistas sao de fato listas poderia ter feito type(M[:]) == list
        for i in range(len(M)):
            
            if (type(M[i-1]) != list or type(M[i]) != list or len(M[i-1]) != len(M[i])):
                return False # Aqui falta ver se os elementos da sublistas sao floats. Exercicio !!!
            
            for j in M[i]:
                print("Mostre-me o indice j que sera avaliado: ", j)
                if (type(j) == str):
                    print("Deu merda !!!!")
                    return False
        return True
        
    else:
        return False

def quadrada(M):
    print("Entrei na funçao quadrada(M)")
    return matriz(M) and len(M) == len(M[0]) and print("Mostre-me a matriz quadrada: ", matriz(M))
# Aqui so compara com a primeira sublista. Logo precisaria colocar uma forma de contagem para analisar o len(M) com todas as outras sublistas

def simetrica(M):
    print("Entrei na funçao simetrica(M)")
    lins = len(M)
    cols = len(M[0])
    for i in range(lins):
        for j in range(cols):
            print("Mostre-me o indice j: {}\nMostre-me o indice i: ". format(j,i))
            if (M[i][j] != M[j][i]):
                print("Nao e simetrica !!")
                return False
    return True

def conta_zeros(lista):
    print("Entrei na funçao conta_zeros")
    total = 0
    for v in lista: #Caso eu coloque range( ,fim) a parte vago do range o python interpreta como 0
        print("Mostre-me o elemento do v da lista que sera avaliado: ", v)
        if v == 0:
            total = total + 1
                
    return total and print("Total de zeros presentes na lista: ", total)

def main():
    c = [[0,0,0,0,1],[0,0,0,0,0],[0,1,0,0,0],[0,0,0,0,0]]
    linhas_nulas = 0
    colunas_nulas = 0
    for i in range(len(c)):
        print("Vou avaliar cada sublista")
        print("Mostre-me a sublista que sera avaliado: ", c[i])
        if conta_zeros(c[i]) == len(c[i]):
            linhas_nulas = linhas_nulas + 1
        print("Mostre-me total das linhas nulas que existem na matriz avaliado: ", linhas_nulas)

    for j in range(len(c[0])): # contanto que vc saiba que as outras sublistas possuem os mesmos numeros de elementos, os elementos da primeira
                               # e o suficiente nessa funçao para avaliar os elementos das outras colunas 
        coluna = []
        for i in range(len(c)): # outra forma de fazer uma lista em uma linha: coluna = [c[i][j] for i in range(len(c))]
            coluna.append(c[i][j])
            print("Mostre-me a coluna que está sendo montado: ", coluna)

        if conta_zeros(coluna) == len(coluna):
            colunas_nulas = colunas_nulas + 1
        print("Mostre-me total de colunas nulas: ", colunas_nulas)

    print("Pra finalizar a funçao main() linhas nulas = ", linhas_nulas)
    print("Pra finalizar a funçao main() colunas nulas = ", colunas_nulas)
    print("Pra finalizar a funçao main() avalia se e quadrado: ", quadrada(c))
    print(imprime_matriz(c))
main()
#Uma forma de fazer uma lista em uma linha: y = [expressao for item in sequencia if condiçao]
        
        

            
            

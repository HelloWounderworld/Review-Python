def le_matriz():
    linhas = int(input("Numero de linhas: "))
    colunas = int(input("Numero de colunas: "))
    matriz = []
    for i in range(linhas):
        print("Mostre-me os indices das linhas iteradas: ", i)
        print("Mostre-me as linhas que serao consideradas: ", range(linhas))
        linha = [] #linha = [0]*colunas no caso teria que usar linha[j] = float(input(" bla bla"))
        for j in range(colunas):
            print("Mostre-me os indices das colunas iteradas: ", j)
            print("Mostre-me as colunas que serao consideradas: ", range(colunas))
            linha.append(float(input("Entre com elemento ({},{}): ". format(i+1,j+1))))
            #linha[j] = float(input(" bla bla"))
            print("Mostre-me a linha construida: ", linha)
        matriz.append(linha)
        print("Mostre-me a matriz construida: ", matriz)

le_matriz()

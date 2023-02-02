def monta_sequencia(lista):
    n = ""
    while (n != "Fim"):
        n = str(input("Entre com um valor ou digite 'Fim': "))
        if (n == "Fim"):
            break
        lista.append(float(n))
    return lista

#def repetiçao(lista):
    #Cobaia = []
    #for i in lista:
        #Contido = False
        #for j in Cobaia:
            #if (i == j):
                #Contido = True
                #break
        #if not Contido:
            #Cobaia.append(i)
            #print(lista)
    #return lista

def repetiçao(lista):
    Cobaia = []
    for i in lista:
        if i not in Cobaia:
            Cobaia.append(i)
    return Cobaia

def main():
    sequencia = []
    lista = monta_sequencia(sequencia)
    print(lista)
    print(repetiçao(lista))
main()

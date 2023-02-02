#Contando somente elementos que na estao repetindo
def main():
    sequencia = []
    valor_str = ""
    while (valor_str != "fim"):
        valor_str = input("Entre com um valor ou 'fim': ")
        if (valor_str != "fim"):
            sequencia.append(float(valor_str))
            
    valores = []
    for x in sequencia:
        if x not in valores:
            valores.append(x)
            print(x) #Mostra o elemento nao presente dentro da lista
            print(valores) #Mostra todos os elementos listados no valores
            print(sequencia) #Mostra todos os elementos indexados na lista sequencia
main()

#Contando somente termos que nao esta repetindo
def main():
    sequencia = []
    valor_str = ""
    while (valor_str != "fim"):
        valor_str = input("Entre com um valor ou 'fim': ")
        if (valor_str != "fim"):
            sequencia.append(float(valor_str))
            
    valores = []
    for x in sequencia:
        contido = False
        for y in valores:
            if x == y:
                contido = True
                break # Esse comando imediatamente quebra um laço no caso corta o laço com " for y in valores"
        if not contido:
            valores.append(x)
            print(x)
main()

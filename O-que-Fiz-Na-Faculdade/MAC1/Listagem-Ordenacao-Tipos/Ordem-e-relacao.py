def main():
    str = input("Digite um valor ou 'fim'") #(**)
    if str == "fim":
        return
    anterior = int(str) # O valor do anterior daqui e tirado de (**)
    crescente = True
    while str != "fim":
        str = input("Entre com um valor ou 'fim': ") #(*)
        if str != "fim":
            proximo = int(str) # o valor do proximo aqui e tirado do (*)
            crescente = crescente and proximo > anterior
            #crescente = proximo > anterior
            print("Mostre: ", crescente)
            anterior = proximo
            print("Mostre: ", anterior)
            #crescente = proximo > crescente
            print("Mostre: ", crescente)
            if crescente == True:
                print("Os numeros estao me ordem crescente")
            else:
                print("Os numeros nao estao em ordem crescente")
main()
                

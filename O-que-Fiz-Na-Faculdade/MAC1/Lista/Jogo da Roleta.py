#Jogo da Roleta
def main():
    roleta = [0]*37 #Aqui ela multiplica o elemento por 37, ou seja, o 0 e um desses elementos, e nao e uma valor zero em si
    n = int(input("Entre com numero de jogadas: ")) #O numero de lançamento
    m = n # se quiser colocar atribuiçoes respectivas de i = 1 e m = n, entao i,m = 1,n
    i = 1
    print("n: ", n)
    print("m: ", m)
    print("i: ", i)
    while (n > 0):
        valor = int(input("Digite o valor do lançamento {}: ". format(i)))
        print("Valor: ", valor)
        roleta[valor] = roleta[valor] + 1
        print("Roleta[valor]: ", roleta[valor])
        n = n - 1
        print("n: ", n)
        print("m: ", m)
        i = i + 1
        print("i: ", i)

    for j in range(37):
        print("{}: frequencia = {}". format(j,(roleta[j]/m)*100))
main()

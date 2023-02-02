#Caso eu queira fazer com alguma entrada de n definida
#Listas sao Objetos multaveis. Objetos que sao imutaveis, por exemplo, sao os strings
import math
def main():
    seq = []
    n = 40
    
    while (n > 0):
        x = float(input("Entre com um valor: "))
        seq[40 - n] = x
        n = n - 1
        
    soma = 0    
    for i in range(len(seq)):
        soma = soma + seq[i]
    media = soma/len(seq)

    soma = 0
    for v in seq:
        soma = soma + (v - media)**2
    desvio = math.sqrt(soma/len(seq))
    print("A media e {} e o desvio padrao e {}". format(media,desvio))
main()

#O comando import cria uma biblioteca de funçoes onde podemos relacionar cada funçao definida com outras funçoes.
#Para isso usa-se o seguinte comando math."operaçoes aritmetica com as funçoes criadas"
import math
def main():
    seq = []
    n = int(input("Entre com n: "))
    
    while (n > 0):
        x = float(input("Entre com um valor: "))
        seq.append(x)
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
        
    

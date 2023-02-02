#Dado um valor positivo de n, escreva uma função que retorne 1 se n for palindromo, 0 caso contrário

def digitos(n):
    x = n
    total = 0
    while x > 0:
        x = x // 10 #O processo aqui e executado a divisao de inteiros ate o resultado do x = 0, quando resultar nisso, e o que o total fara a sua ultima execuçao
        total = total + 1
    return total
def main():
    n = int(input




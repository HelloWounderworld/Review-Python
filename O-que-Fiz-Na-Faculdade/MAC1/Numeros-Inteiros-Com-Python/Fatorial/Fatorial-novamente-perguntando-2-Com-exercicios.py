def fatorial(n): #Posso definir em função de alguma variável
    prod = 1
    x = n
    while x > 0:
        prod = prod * x
        x = x - 1
    return prod # Quando o comando return é executado, nada o que tiver abaixo desse comando é executado

def main():
    fim = 0
    while fim == 0:
        str = input("Entre com n ou digite 'fim'")
        if str != "fim": # Sinal != e diferente
            n = int(str)
            print("O valor de", n, "!=", fatorial(n))
        else:
            fim = 1

main() #Poderia ser colocado o def fatorial(n) antes do def main() ou depois do def main(), contanto que no final conclua com o main(), o programa pode sr executado

# Exercicio: Calcule o fatorial baseado na sua definiçao recursiva: n! = n(n-1)! e 1! = 1
# crie um programa que faça a conta: C = m!/(m-n)!n! para m e n inteiros positivos.

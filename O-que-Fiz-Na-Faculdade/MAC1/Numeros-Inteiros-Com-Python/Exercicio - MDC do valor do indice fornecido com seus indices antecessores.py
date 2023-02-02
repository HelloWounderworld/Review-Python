#Dados um inteiro positivo n e uma sequência de n inteiros positivos, determinar o máximo divisor comum a todos eles
def MDC(n):
    MDC = 1
    while(n >= MDC):
        if(n % MDC == 0):
            print("O Maximo divisor comum do", MDC, "-esimo da sequencia com o valor do indice fornecido pela sequencia: ", MDC)
            MDC = MDC + 1
        else:
            print("O Maximo divisor comum do", MDC, "-esimo da sequencia com o valor do indice fornecido pela sequencia: ", 1) 
            MDC = MDC + 1
    return print("Valor do indice fornecido: ", MDC - 1)

def main():
    n = int(input("Forneça um valor para o indice da sequencia: "))
    print(MDC(n))
main()

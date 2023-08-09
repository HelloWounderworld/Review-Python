#Dados x real e n natural, calcular uma aproximação para cos x através dos n primeiros termos da seguinte série:
#1 - x2/2! + x4/4! - x6/6! + ... + (-1)k * x2k/(2k)! + ...
def fatorial(n):
    prod = 1
    x = 1
    while (n >= x):
        prod = prod*x
        x = x + 1
    return prod

def potencia(x,n):
    pot = 1
    while (n > 0):
        pot = pot * x
        n = n - 1
    return pot

def sen(x,r):
    soma = 0
    k = 0
    termo = potencia(x,2*k+1)/fatorial(2*k+1)
    while (not termo < r):
        soma = soma + potencia(-1,k)*termo
        k = k + 1
        termo = potencia(x,2*k+1)/fatorial(2*k+1)
    return soma

def main():
    n = int(input("Entre com um valor inteiro n: "))
    x = float(input("Entre com um valor radiano x: "))
    r = float(input("Entre com um valor de raio r: "))
    print("O valor da Serie de Taylor do sen({}) = {}". format(x,sen(x,r)))
main()
        
        

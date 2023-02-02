def fatorial(n):
    x = n
    prod = 1
    while x > 0:
        prod = prod * x
        x = x - 1
    return prod
def comb(m,n): #dentro do fatoriaa poderia colocar indefinidademente outros fatoriais e alem do mais definir opraçoes dentro dele com outros fatoriais que ainda assim sera precessado    
    num = fatorial(m)
    demon = fatorial(m-n)*fatorial(n) #Fatorial(m-n) o m-n e interpretado como um numero que tera que ser processadona opreçao definida em def fatorial(n)
    return num / demon

def main():
    n = int(input("Entre com o valor de n:"))
    m = int(input("Entre com o valor de m:"))
    print("O valor de C {},{}={}".format(m,n,comb(m,n)))
main()
    
    

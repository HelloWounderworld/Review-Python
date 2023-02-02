def fatorial(n):
    prod = 1
    m = 1
    while(n >= m):
        prod = prod * m
        Sequencia = print("Termo da sequencia: ", prod)
        m = m + 1
    return print("Sequencia para o indice: ", m - 1)

def main():
    n = int(input("Forneça um valor para o indice da sequencia: "))
    print(fatorial(n))
main()

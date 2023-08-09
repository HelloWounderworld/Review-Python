#Palindromo
def main():
    n = int(input("Entre com o valor de n:"))
    m = 0
    x = n
    while x > 0:
        dig = x % 10
        m = m * 10 + dig
        x = x // 10
        print("Mostre os valores dos restos da divisão:", dig)
    if m == n:
        print("{} é um palíndromo". format(n))
    else:
        print("{} não é um palíndromo". format(n))
main()

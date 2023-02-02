def digitos(n):
    x = n
    total = 0
    while x > 0:
        x = x // 10
        total = total + 1 # de forma abreviada é "total+=1"
    return total
def main():
    n = int(input("Entre com o valor de n:"))
    print("O valor e", digitos(n))

main()

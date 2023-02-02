def main():
    n = int(input("Entre com o valor de n: "))
    x = n
    total = 0
    while x > 0:
        Divisao = x % 10
        if Divisao % 2 == 0:
            total = total + 1
        x = x // 10
    print("total = {}". format(total))
main()
        

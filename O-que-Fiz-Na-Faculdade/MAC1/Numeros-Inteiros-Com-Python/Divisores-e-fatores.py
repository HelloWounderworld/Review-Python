def main():
    n = int(input("Entre com o valor de n: "))
    divisor = 2
    print(1)
    while(divisor <= n): # isso tem que funcionar enquanto n > 1
        resto = n % divisor
        if (resto == 0):
            print(divisor)
            n = n / divisor # essa conta é equivalente a esse comendo n /= divisor
        else:
            divisor = divisor + 1
main()

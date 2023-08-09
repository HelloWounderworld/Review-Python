def main():
    n = int(input("Entre com um valor inteiro n: "))
    m = int(input("Entre com um valor inteiro m: "))
    MDC = 2
    while( n >= MDC or m >= MDC):
        if(n % MDC == 0 and m % MDC == 0 and (MDC - 1) < MDC):
            print("Maximo divisor comum: ", MDC)
            MDC = n
        else:
            MDC = MDC + 1
main()
            

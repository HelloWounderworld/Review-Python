def main():
    while(True):
        n = int(input("Entre com algum ano: "))
        if(n % 4 == 0 and n % 100 != 0):
            print("E ano bissexto: ", n, True)
        else:
            print("Nao e ano bissexto: ", n, False)
main()

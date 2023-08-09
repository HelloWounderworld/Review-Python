def main():
    while (True):
        n = int(input("Entre com um valor inteiro n: "))
        m = int(input("Entre com um valor inteiro m: "))
        d = ((n/m)-(n//m))*10
        print("Mostre - me o processo: ", d)
        if (d >= 5):
            x = (n//m) + 1
            print("Mostre o valor arredondado: ", x)
        else:
            y = (n//m)
            print("Mostre o valor nao arredondado: ", y)
main()
        

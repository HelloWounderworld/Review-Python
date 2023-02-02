#def main():
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    if a<=b and b<=c:
        print(a, b, c)
    elif a<=c and c<=b:
        print(a, c, b)
    elif b<=a and a<=c:
        print(b, a, c)
    elif b<=c and c<=a:
        print(b, c, a)
    elif c<=b and b<=a:
        print(c, b, a)
    else:
        print(c, a, b)
main()

#def main():
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    if a<=b:
        if b<=c:
            print(a,b,c)
        elif c<=a:
            print(c, a, b)
        else:
            print(a,c,b)
    else:
        if c<=b:
            print(c, b, a)
        elif c<=a:
            print(b, c, a)
        else:
            print(b, a, c)
main()

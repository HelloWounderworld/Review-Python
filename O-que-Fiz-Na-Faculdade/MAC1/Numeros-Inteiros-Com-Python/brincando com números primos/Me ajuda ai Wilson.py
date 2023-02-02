def mdc(n,m):
    n1 = max(n,m)
    n2 = min(n,m)
    while n1%n2 != 0:
        n3 = n2
        n2 = n1%n2
        n1 = n3
    return n2

def Teorema_Wilson(n):
    print('valor de n:', n)
    prod=1
    for i in range(1,n):
        prod=prod*i
    y = prod
    z = y + 1
    x = n
    if (z%x == 0):
        x = n
        print(x, "E um numero primo")
        return True

    else:
        return False

def main():
    soma =25
    while soma>=1:
        print("soma:", soma)
        p = (2**soma)-1
        if p%2 != 0:
            n = Teorema_Wilson(p)
        soma=soma+1
        
main()

'''def main():
    soma = 50
    lista = set()
    while soma>=1:
        n = (2**soma)+1
        p = 0
        for i in range(1,n):
            if mdc(i,n) == 1:
                p = p+1
        if p == n-1:
            soma=soma+1
            lista.add(n)
            print(lista)
        else:
            soma = soma +1
main() 97972799'''
                        
        

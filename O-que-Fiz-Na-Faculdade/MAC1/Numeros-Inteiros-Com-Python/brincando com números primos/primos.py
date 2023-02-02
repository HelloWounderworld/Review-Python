def mdc(n,m):
    n1 = max(n,m)
    n2 = min(n,m)
    while n1%n2 != 0:
        n3 = n2
        n2 = n1%n2
        n1 = n3
    return n2

def main():
    soma = 1
    while soma >=1:
        m = (2**soma)-1
        p = 0
        for i in range(1,m):
            if mdc(m,i)==1:
                p = p +1
        if p == m-1:
            print(m)
            p= 0
            soma=soma+1
        else:
            p=0
            soma = soma +1
main()

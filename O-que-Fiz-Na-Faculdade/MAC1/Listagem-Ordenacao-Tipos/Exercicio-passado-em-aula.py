def fi(x):
    resp = 0
    if (x%3 == 0):
        resp = resp + x
    return resp

def main():
    n = int(input("Digite n: "))
    a = n*[0]
    i = 0
    while(i<n):
        a[i] = int(input("Digite um numero: "))
        i = i + 1
    print(a)
    k = n // 2
    i = 0
    while(i<k):
        if(a[i] > a[i+k]):
            a[i] = fi(a[i])
        else:
            a[i+k] = fi(i+k)
        i = i + 1
    print(a)

#simule isso no papel !
# valores que serao lidos: 15,2,36,48,5,99,28,86

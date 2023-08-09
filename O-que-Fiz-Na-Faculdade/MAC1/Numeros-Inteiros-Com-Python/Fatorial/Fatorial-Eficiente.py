def fatorial(n):
    if type(n) == type("Hello WonderWorld") or n < 0 or (n-int(n)) != 0:
        return fatorial(float(input("A funcao fatorial so esta definida para numeros naturais, favor escolher outro numero: ")))
    else:
        if n == 0:
            return 1
        else:
            return int(n*fatorial(n-1))
        
        

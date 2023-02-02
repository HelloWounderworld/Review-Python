while (True):
    s = str(input("Entre com elemento n:"))
    n = len(s)
    i = 0
    flag = True
    while (i<n):
        if (s[i] != s[n-i-1]):
            flag = False
        i = i+1
    if (flag == True):
        print("É um palindromo", s)
    else:
        print("Não é um palindromo", s)
        

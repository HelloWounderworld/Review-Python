"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[5])
print(variavel[-4])
print(variavel[4:])
print(variavel[4:7])
print(variavel[:5])
print(variavel[-8:-2])
print(len('aaaaaaaaa'))
print(len(variavel))
print(variavel[0:len(variavel):1])
print(variavel[0:len(variavel):2])
print(variavel[0:len(variavel):3])
print(variavel[0:len(variavel):-1])
print(variavel[0:len(variavel):-2])
print(variavel[-1:-10:-1])
print(variavel[-1:-10:-2])
print(variavel[::-1])
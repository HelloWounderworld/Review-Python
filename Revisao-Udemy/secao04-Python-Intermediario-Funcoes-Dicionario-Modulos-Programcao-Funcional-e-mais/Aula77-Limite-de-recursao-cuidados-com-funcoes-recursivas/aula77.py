# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
#import sys

#sys.setrecursionlimit(1004)

#def recursiva(inicio=0, fim=10):
    #print(inicio, fim)
    # Caso base
    #if inicio >= fim:
    #    return fim
    # Caso recursivo
    # contar até chegar ao final
    #inicio += 1
    #return recursiva(inicio, fim)

#print(recursiva(0, 1000))
#print(recursiva(0, 1001))

def fatorial(n):
    print(n)
    if n <= 1:
        return 1
    return n * fatorial(n-1)

print(fatorial(5))
print(fatorial(10))

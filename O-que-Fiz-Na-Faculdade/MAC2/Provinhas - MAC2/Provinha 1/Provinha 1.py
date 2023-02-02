def f(x):
    a = 0
    x = 2*x
    for i in range(len(x)):
        a += x[i]
    return a

def g(n,m):
    tmp = n 
    n = m
    m = tmp

def h(x):
    tmp = x[0]
    x[0] = x[1]
    x[1] = tmp

def main():
    i,j = 5,3
    xa = [1,2,3,4]
    xb = [1,[2,'oi'],[True, 3.14, 3]]
    s = 'mac0122'
    print('In [5]: len(xb)')
    print(type(len(xb)))
    print(len(xb))
    print()
    print('In [6]: len(s)')
    print(type(len(s)))
    print(len(s))
    print()
    print('In [7]: xb[1]')
    print(type(xb[1]))
    print(xb[1])
    print()
    print('In [8]: xb[2][1]')
    print(type(xb[2][1]))
    print(xb[2][1])
    print()
    print('In [9]: xb[2][3]')
    #print(type(xb[2][3]))
    #print(xb[2][3])
    print('Erro')
    print()
    print('In [10]: 2 in xb')
    print(type(2 in xb))
    print(2 in xb)
    print('A verificao acima usando a condicional logica in\n,como de usual em matematica, verifica a relacao de pertinencia de uma dado elemento sobre o conjunto\nno caso esse conjunto nesse contexto seria a lista que esta sendo verificado acima')
    print()
    print('In [11]: s[1:3]')
    print(type(s[1:3]))
    print(s[1:3])
    print(type('2' in s[1:3]))
    print('2' in s[1:3])
    print('Aqui tbm mostra que o uso da condicional logico in\nusado acima se aplica para uma string tbm')
    print()
    print('In [12]: f(xa)')
    print(type(f(xa)))
    print(f(xa))
    print()
    print('In [13]: xa')
    print(type(xa))
    print(xa)
    print()
    print('In [14]: k = g(i, j)')
    print(type(g(i,j)))
    print(g(i,j))
    print('Olha so ! Quando vc define uma funcao com variavel incluso nele\ncaso nao coloque nenhum return no final a ideia seria que nao retorne nada(none)!\nNo caso o tipo tbm seja um NoneType (Sem Tipo)')
    print()
    print('In [16]: i')
    print(type(i))
    print(i)
    print()
    print('In [18]: h(xc)\nIn [19]: xc')
    xc = xa
    h(xc)
    print(type(xc))
    print(xc)
    print()
    print('Em principio a lista na qual igualei xc foi a lista xa\ndonde quando realizo alguma mudanca nessa lista xc, automaticamente ocorre a mudanca da lista xa em conjunto\npor se tratar de uma copia raza')
    print('Caso a pessoa queira fazer alguma copia profunda (Deep copy)\nde uma lista generalizada devera fazer o tal comando xd = xa[:]')
    print()
    print('Aplicando o comando')
    xd= xa[:]
    h(xd)
    print('lista xd')
    print(type(xd))
    print(xd)
    print()
    print('lista xa')
    print(type(xa))
    print(xa)
    print()
    print('In [20]: xa')
    print(type(xa))
    print(xa)
main()

'''
Suponha ainda que fizemos as seguintes atribuições:

In [1]: i, j = 5, 3

In [2]: xa = [1, 2, 3, 4]

In [3]: xb = [1, [2, 'oi'], [True, 3.14, 3]]

In [4]: s = 'mac0122'

A seguir está uma transcrição de uma seção do Python Shell. Complete as lacunas (tipo e valor) do resultado da expressão correspondente. Se ocorrer um erro, escreva apenas ERRO.

In [5]: len(xb)
tipo : int
valor: 3

In [6]: len(s)
tipo : int
valor: 7

In [7]: xb[1]
tipo : list
valor: [2, 'oi']

In [8]: xb[2][1]
tipo : float
valor: 3.14

In [9]: xb[2][3]
tipo : ERRO
valor:

In [10]: 2 in xb
tipo : bool
valor: False

In [11]: s[1:3]
tipo : str
valor: 'ac'

In [12]: f(xa)
tipo : int
valor: 20

In [13]: xa
tipo : list
valor: [1, 2, 3, 4]

In [14]: k = g(i, j)
In [15]: k
tipo : NoneType
valor: None

In [16]: i
tipo : int
valor: 5

In [17]: xc = xa
In [18]: h(xc)
In [19]: xc
tipo : list
valor: [2, 1, 3, 4]

In [20]: xa
tipo : list
valor: [2, 1, 3, 4]
'''




    
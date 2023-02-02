import numpy as np

def main():
    print("In [2]: m = [[1, 2, 3],[3, 4, 5]]\nIn [3]: print(m+m)")
    m = [[1,2,3],[3,4,5]]
    print(m+m)
    print()
    print("In [4]: print(2*m)")
    print(2*m)
    print()
    print("In [5]: print(m+1)")
    #print(m+1)
    print("Isso m+1 da erro")
    print()
    print("In [6]: a = np.array(m)\nIn [7]: print(a)")
    a = np.array(m)
    print(a)
    print()
    print("In [8]: print(a[0:1,1:3])")
    print(a[0:1,1:3])
    print()
    print("In [9]: a.ndim\nOut [9]: 2")
    print(a.ndim)
    print("Esse comando leva em consideracao a quantidade, contando da\nprimeira lista,as listas que serao colocadas uma dentro da outra")
    print()
    print("In [10]: a.shape\nOut[10]: (2, 3)")
    print(a.shape)
    print()
    print("In [11]: a.size\nOut[11]: 6")
    print(a.size)
    print("Similar a ideia de saber a quantiade de elementos de uma matriz, ou seja, multiplica a linha e coluna")
    print()
    print("In [12]: b = a\nIn [13]: a[1,1] = -1\nIn [14]: print(b)")
    b = a
    a[1,1] = -1
    print(b)
    print("Aqui usa-se a mesma ideia de uma copia raza de uma lista")
    print()
    print("In [15]: c = np.full((3,2), -1)\nIn [16]: print(c+c)\nIn [17]: print(2*c)\nIn [18]: print(c+1)")
    c = np.full((3,2),-1)
    print(c+c)
    print()
    print(2*c)
    print()
    print(c+1)
main()

'''
Questão 1. Qual o valor da expressão posfixa 7 5 3 * + 4 3 2 - + + 10 /?

2.7

Questão 2. Converta para notação posfixa a expressão 10 + 3 * 5 / (16 - 4).

10 3 5 * 16 4 - / +

Questão 3. Considere a execução do algoritmo que calcula o valor de uma expressão 
posfixa aplicado sobre 7 5 3 * + 4 3 2 - + + 10 /. Qual o conteúdo da pilha de 
operandos antes do operador subtração ('-') ser examinado.

[22, 4, 3, 2]

Questão 4. A seguir está uma transcrição de uma seção do Python Shell. 
Complete as lacunas do resultado da expressão correspondente. 
Se ocorrer um erro, escreva apenas   ERRO.

In [1]: import numpy as np

In [2]: m = [[1, 2, 3],[3, 4, 5]]

In [3]: print(m+m)

[[1, 2, 3], [3, 4, 5], [1, 2, 3], [3, 4, 5]]

In [4]: print(2*m)

[[1, 2, 3], [3, 4, 5], [1, 2, 3], [3, 4, 5]]

In [5]: print(m+1)

ERRO

In [6]: a = np.array(m)

In [7]: print(a)

[[1 2 3] [3 4 5]]

In [8]: print(a[0:1,1:3])

[[2 3]]

In [9]: a.ndim

Out [9]: 2

In [10]: a.shape

Out[10]: (2, 3)

In [11]: a.size

Out[11]: 6

In [12]: b = a

In [13]: a[1,1] = -1

In [14]: print(b)

[[ 1 2 3] [ 3 -1 5]]

In [15]: c = np.full((3,2), -1)

In [16]: print(c+c)

[[-2 -2] [-2 -2] [-2 -2]]

In [17]: print(2*c)|

[[-2 -2] [-2 -2] [-2 -2]]

In [18]: print(c+1)|

[[0 0] [0 0] [0 0]]
'''


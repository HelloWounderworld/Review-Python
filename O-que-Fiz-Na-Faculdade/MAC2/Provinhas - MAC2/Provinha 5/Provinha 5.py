


'''
Questão 1. A seguir está uma transcrição de uma seção do Python Shell. Complete cada lacuna com o valor da expressão correspondente. Se ocorrer um erro, escreva apenas .%\(1mm]

In [1]: import numpy as np

In [2]: m = [[10, 11], [20, 21]]

In [3]: m+m

Out [3]: [10, 11], [20, 21], [10, 11], [20, 21]]

In [4]: 2*m

Out [4]: [[10, 11], [20, 21], [10, 11], [20, 21]]

In [5]: m+2

Out [5]: ERRO

In [6]: a = np.array(m)

In [7]: a

Out [7]:
array([[10, 11],
               [20, 21]])

In [8]: a[0:2,0:1]

Out [8]:
array([[10],
              [20]])

In [9]: a.ndim

Out [9]: 2

In [10]: a.shape

Out[10]: (2, 2)

In [11]: a.size

Out[11]: 4

In [12]: b = a

In [13]: a[1, 1] = -1

In [14]: b

Out[14]:
array([[10, 11],
              [20, -1]])

In [15]: c = np.full((3,2), 2)

In [16]: c+c

Out[16]:
array([[4, 4],
              [4, 4],
              [4, 4]])

In [17]: 2*c

Out[17]:
array([[4, 4],
              [4, 4],
              [4, 4]])

In [18]: c+2

Out[18]:
array([[4, 4],
              [4, 4],
              [4, 4]])

In [19]: a = np.full((2,3), 3)

In [20]: c = a.reshape(3,2)

In [21]: c[1,1] = 66

In [22]: a

Out[22]:
array([[ 3, 3, 3],
              [66, 3, 3]])

In [23]: b = np.full((2,3), -1)

In [24]: d = b.copy()

In [25]: d[1,1] = 77

In [26]: b

Out[26]:
array([[-1, -1, -1],
              [-1, -1, -1]])
'''


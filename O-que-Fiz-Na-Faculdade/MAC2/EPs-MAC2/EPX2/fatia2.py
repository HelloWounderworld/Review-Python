def fatia_max(p, r, v):
    '''(int, int, list) -> int, int, int

    RECEBE uma lista v[p:r] de números inteiros e RETORNA
    valores inteiros soma_max, e, d tais que

        soma_max == sum(v[e,d]) é a maior soma de uma fatia 
        v[i:j] com p <= i <= j <= r.
    
    Tem que ser O(n^2)
    '''
    soma_max = []
    tupla = {}
    q = 0
    while q < len(v[p:r]):
        for j in range(q+1):
            soma = 0
            for i in v[j+p:j+p+len(v[p:r])-q]:
                soma = soma + i
            soma_max.append(soma)
            tupla[soma] = (j+p,j+len(v[p:r])-q+p)
        q += 1
    nlin,ncol = tupla[max(soma_max)]
    return max(soma_max), nlin, ncol

#--------------------------------------------------------
def fatia_max_meio(p, q, r, v):
    '''(int, int, int, list) -> int, int, int

    RECEBE números inteiros p < q < r e uma lista v[p:r] de 
    números inteiros e RETORNA valores inteiros 
    soma_max, e, d tais que 

        soma_max==sum(v[e:d]) é a maior soma de uma fatia 
        v[i:j] com p <= i < q < j <= r.
    Tem que ser O(n)
    '''
    
        
    return soma_max, nlin, ncol

#--------------------------------------------------------
def fatia_max_div_conq(p, r, v):
    '''(int, int, list) -> int, int, int

    RECEBE uma lista lista v[p:r] de números inteiros e RETORNA
    valores inteiros soma_max, e, d tais que

        soma_max == sum(v[e,d]) é a maior soma de uma fatia 
        v[i:j] com p <= i <= j <= r.
    Tem que ser O(nlog(n))
    '''
    print("Vixe! Ainda não fiz a função fatia_max_div_conq()...")
    return -1, -1, -1


def main():
    v = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
    print('Teste fatia_max')
    print(fatia_max(0,10,v))
    print()
    print(fatia_max(2,9,v))
    print()
    print(fatia_max(3,9,v))
    print()
    print(fatia_max(7,10,v))
    print()
    print('Teste fatia_max_meio')
    print(fatia_max_meio(0,1,2,v))
    print()
    print(fatia_max_meio(0,2,3,v))
    print()
    print(fatia_max_meio(0,2,4,v))
    print()
    print(fatia_max_meio(0,2,5,v))
    print()
    print(fatia_max_meio(0,2,6,v))
    print()
    print(fatia_max_meio(0,3,6,v))
    print()
    print(fatia_max_meio(0,3,5,v))
    print()
    print(fatia_max_meio(3,5,6,v))
    print()
    print(fatia_max_meio(3,5,7,v))
    print()
    print('Teste fatia_max_div_conq')
    print(fatia_max_div_conq(0,10,v))
    print()
    print(fatia_max_div_conq(2,9,v))
    print()
    print(fatia_max_div_conq(3,9,v))
    print()
    print(fatia_max_div_conq(7,10,v))
main()

'''
   In [2]: v = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

    In [3]: fatia_max(0,10,v)
    Out[3]: (187, 2, 7)

    In [4]: fatia_max(2,9,v)
    Out[4]: (187, 2, 7)

    In [5]: fatia_max(3,9,v)
    Out[5]: (155, 5, 7)

    In [6]: fatia_max(7,10,v)
    Out[6]: (84, 9, 10)
    
    In [12]:v = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

    In [13]: fatia_max_meio(0,1,2,v)
    Out[13]: (-10, 0, 2)

    In [14]: fatia_max_meio(0,2,3,v)
    Out[14]: (49, 0, 3)

    In [15]: fatia_max_meio(0,2,4,v)
    Out[15]: (75, 0, 4)

    In [16]: fatia_max_meio(0,2,5,v)
    Out[16]: (75, 0, 4)

    In [17]: fatia_max_meio(0,2,6,v)
    Out[17]: (80, 0, 6)

    In [18]: fatia_max_meio(0,3,6,v)
    Out[18]: (90, 2, 6)

    In [19]: fatia_max_meio(0,3,5,v)
    Out[19]: (85, 2, 4)

    In [20]: fatia_max_meio(3,5,6,v)
    Out[20]: (31, 3, 6)

    In [21]: fatia_max_meio(3,5,7,v)
    Out[21]: (128, 3, 7)
    
    In [22]: v = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

    In [23]: fatia_max_div_conq(0,10,v)
    Out[23]: (187, 2, 7)

    In [24]: fatia_max_div_conq(2,9,v)
    Out[24]: (187, 2, 7)

    In [25]: fatia_max_div_conq(3,9,v)
    Out[25]: (155, 5, 7)

    In [26]: fatia_max_div_conq(7,10,v)
    Out[26]: (84, 9, 10)
'''


### Solução (a)

from bisect import bisect_left

def soma_zero_n2(v):
    '''(list) -> int
    Recebe uma lista `v` de números inteiros e retorna o número
    de pares que somam zero.

    Consum de tempo da função é O(n^2).
    '''
    cont = 0
    n = len(v)
    for i in range(n):
        for j in range(i+1,n):
            if v[i] + v[j] == 0:
                # print(v[i], v[j])
                cont += 1
    return cont
 

### Solução (b)

def soma_zero_nlgn(v): 
    '''(list) -> int
    Recebe uma lista `v` de números inteiros e retorna o número
    de pares que somam zero.

    Consumo de tempo da função é O(n lg n).

    A função altera a lista v. Para não alterarmos bastava
    fazermos v_sorted = sorted(v)
    '''
    cont = 0
    v.sort()
    n = len(v)
    for i in range(n):
        j = index_busca_binaria(v, -v[i], i+1, n) # consumo de tempo O(lg n)
        # j = index(v, -v[i], i+1, n) # alternativamente
        if j != None: cont += 1
    return cont


def index_busca_binaria(a, x, lo, hi):
    '''(list, item, int, int) -> int ou None

    Recebe uma lista ordenada a com n itens, um item x e dois inteiros lo e hi.
    Retorna um índice i em range(lo,hi) tal que a[i] <= x < a[i+1].
    Para essa afirmação fazer sentido suponha aqui que 
        * a[lo-1] é menos infinito e
        * a[hi  ] é mais  infinito.
    Pré-condição: suponha que os itens em a são distintos.  
    '''
    while lo < hi:
        mid = (lo + hi) // 2 # 
        if   a[mid] < x: lo = mid + 1 
        elif a[mid] > x: hi = mid
        else: return mid
    return None

# Mais especificamente, usaremos uma adaptação de `index` da página de `bisect`
def index(a, x, lo, hi):
    '''(list, item, int, int) -> int ou None
    >>> from bisect import bisect_left
    >>> lista = [1,3,5,7,9,11]
    >>> help(bisect_left)

    >>> bisect_left(lista,2,0,len(lista))
    1
    >>> bisect_left(lista,13,0,len(lista))
    6
    >>> bisect_left(lista,3,0,len(lista))
    1
    >>> bisect_left(lista,4,0,len(lista))
    2
    >>> bisect_left(lista,5,0,len(lista))
    2
    >>> bisect_left(lista,0,0,len(lista))
    0
    >>> 
    '''
    i = bisect_left(a, x, lo, hi)
    if i != len(a) and a[i] == x:
        return i
    return None # raise ValueError

### Solução (c)

def soma_zero_n(v):
    '''(list) -> int
    Recebe uma lista `v` de números inteiros e retorna o número
    de pares que somam zero.

    Consumo de tempo esperado da função é O(n).
    '''
    cont = 0
    numeros = set() # conjunto de valores
    n = len(v)
    for i in range(n):
        if -v[i] in numeros: # consumo de tempo esperado O(1)
            cont += 1
        numeros.add(v[i])    # consumo de tempo esperado O(1)
    return cont


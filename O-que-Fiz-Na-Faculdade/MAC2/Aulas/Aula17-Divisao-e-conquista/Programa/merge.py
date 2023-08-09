# -*- coding: utf-8 -*-
#---------------------------------------------------------
#
#  MAC0122 Princípios de Desenvolvimento de Algoritmos
#
#---------------------------------------------------------

def intercale(p,q,r,v):
    ''' (int,int,int,list) -> None

    Recebe uma lista v tal que 
    
        - v[p:q] é crescente e
        - v[q:e] é crescente 
        
    e rearranja os elementos de v de tal forma
    que v[p:r] seja crescente.
    
    Consumo de tempo é O(n) onde n = p-r
    '''
    # crie lista auxiliar
    w = []      
    i = p
    j = q
    while i < q and j < r:
        if v[i] < v[j]:
            w.append(v[i])
            i += 1
        else:
            w.append(v[j])
            j += 1
    
    # copie os elementos que sobraram em v[p:r]
    while i < q:
        w.append(v[i])
        i += 1
        
    # copie os elementos que sobrou
    while j < r:
        w.append(v[j])
        j += 1
        
    # copie w[0:r-p] para v[p:r]
    for i in range(r-p):
        v[p+i] = w[i]
        
        

#-----------------------------------------------        
def merge_sort(v):
    '''(list) -> None
    
    Recebe uma lista v[p:r] e rearranja seu elementos
    de maneira que fique crescente.
    '''
    n = len(v)
    if n > 1:
        p = 0
        q = n//2
        r = n
        merge_sort(v[p:q])
        merge_sort(v[q:r])
        intercale(p,q,r,v)


                
        
#-----------------------------------------------        
def merge_sortR(p,r,v):
    '''(int,int,list) -> None
    
    Recebe uma lista v[p:r] e rearranja seu elementos
    de maneira que fique crescente.
    '''
    if p < r-1:
        q = (p+r)//2
        merge_sort(p,q,v)
        merge_sort(q,r,v)
        intercale(p,q,r,v)


        
#--------------------------------------------
def merge_sortI(v):
    '''(list) -> None
    
    Recebe uma lista v e rearranja seu elementos de
    maneira que fiquem crescente.
    
    É uma implementação iterativa do Mergesort.
    '''
    n = len(v)
    b = 1
    while b < n:
        p = 0
        while p + b < n:
            r = p + 2*b
            if r > n: r = n
            intercale(p,p+b,r,v)
            p = p + 2*b
        b = 2*b            

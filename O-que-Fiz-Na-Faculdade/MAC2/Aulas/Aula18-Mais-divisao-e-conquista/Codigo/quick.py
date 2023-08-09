# -*- coding: utf-8 -*-
#-----------------------------------------------------------
#
#  MAC0122 Princípios de Desenvolvimento de Algoritmos
#
#-----------------------------------------------------------

def separe(p, r, v):
    ''' (int,int,list) -> int

    Recebe uma lista v[p:r] e rearranja seu elementos e
    retorna um índice q tais que

        v[p:q] <= v[q] < v[q+1:r]
    
    Consumo de tempo é O(n) onde n = p-r
    '''
    x = v[r-1] # pivo
    i = p-1
    for j in range(p,r): #A#
        if v[j] <= x:
            i += 1
            v[i],v[j] = v[j],v[i]
    return i


#-----------------------------------------------        
def quick_sort(p, r, v):
    '''(int,int,list) -> None
    
    Recebe uma lista v[p:r] e rearranja seu elementos
    de maneira que fique crescente.
    '''
    if p < r-1:
        q = separe(p,r,v)
        quick_sort(p,q,v)
        quick_sort(q+1,r,v)

#-----------------------------------------------
def separeR(p,r,v):
   x = v[p] # pivo
   e = p+1
   d = r-1
   while e <= d:
       while e <= d and v[e] <= x:
           e += 1
       while d >= e and v[d] >  x:
           d -= 1
       # v[e] >  x and v[p  :e] <= x 
       # v[d] <= x and v[d+1:r] >  x   
       if e < d:
           v[e],v[d] = v[d],v[e]
           e += 1
           d -= 1
   
   v[p],v[d] = v[d],v[p] 

   return d
        
#-----------------------------------------------        
def quick_sortR(v):
    '''(list) -> None
    
    Recebe uma lista v[p:r] e rearranja seu elementos
    de maneira que fique crescente.
    '''
    n = len(v)
    if n > 1:
        p = 0
        r = n
        q = separeR(p, r, v)
        quick_sortR(v[p:q])
        quick_sortR(v[q+1:r])



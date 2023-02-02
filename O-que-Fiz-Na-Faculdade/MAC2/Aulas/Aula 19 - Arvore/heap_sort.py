def peneira(i,m,v):
    f = 2*i
    while f < m:
        if f < m-1 and v[f] < v[f+1]:
            f += 1
        if v[i] >= v[f]:
            break
        v[i], v[f] = v[f], v[i]
        i = f
        f = 2*i

def heap_sort(n,v):
    for i in range((n-1)//2,0,-1):
        peneira(i,n,v)
    for i in range(n-1,1,-1):
        v[i], v[1] = v[1], v[i]
        peneira(1,i,v)
        
        
    

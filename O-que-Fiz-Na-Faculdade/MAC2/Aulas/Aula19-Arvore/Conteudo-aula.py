'''
conteudo da aula
'''
def imaior(e,d,v):
    maior = e
    for i in range(e,d):
        if v[i] > v[maior]:
            maior = i
    return maior

def selecao(v):
    n = len(v)
    for i in range(n-1,0,-1):
        im = imaior(i,n,v)
        v[i],v[im] = v[im],v[i]





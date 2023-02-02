'''
O consumo de tempo esperado para essa funcao seria O(n²), pois neste foi usado
o dicionario que mesmo sendo um tipo de lista, ela e um tanto diferente da lista
geral, pois a busca realizada nessa lista nao varre toda a lista, ou seja, a busca
no dicionario seria uma assintota de O(1).
'''

def conta_dict(a):
    conta = 0
    n = len(a)
    d ={}
    for k in range(n):
        d[a[k]] = k
    for i in range(n):
        for j in range(i+1,n):
            soma = a[i]+a[j]
            k = d.get(-soma)
            if k != None and k>j:
                conta += 1
    return conta


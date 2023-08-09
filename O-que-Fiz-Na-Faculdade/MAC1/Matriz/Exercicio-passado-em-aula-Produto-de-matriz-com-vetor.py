#3-) Dada uma matriz real A com m linhas e n colunas e um vetor v com n elementos. Determinar o produto escalar de A por v.

def produto_escalar(x,y):
    soma = 0
    for i in range(len(x)):
        soma = soma + x[i]*y[i]
    return soma

def produto(A,v):
    w = []
    for linha in A:
        w.append(produto_escalar(linha,v))
    return w

#Esse codigo so vale porque o v e um vetor. Se for uma outra matriz teria que colocar mais uma iteraçao.

# Simule no papel !!

'''
Esta funcao chamada forca bruta recebe uma lista com numeros e conta a quantidade
de trios de numeros, cuja ordem seja diferentes, e retorna essa quantidade de
numeros. No caso como o nome diz essa funcao e forca bruta pelo motivo dele usar
tres for's para realizar o processo. No caso, notacao assintotica essa funcao tera
um consumo de tempo de O(n³)
'''

def conta_fb(a):
    conta = 0
    n = len(a)
    for i in range(n):
        for j in range(i+1,n):
            soma = a[i] + a[j]
            for k in range(j+1,n):
                if soma + a[k] == 0:
                    conta += 1
    return conta


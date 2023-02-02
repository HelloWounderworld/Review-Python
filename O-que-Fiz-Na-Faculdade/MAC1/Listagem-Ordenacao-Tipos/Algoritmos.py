#Algoritmos de elementares de ordenaçao
#Escreva uma funçao crescente que recebe uma lista de sequencia e retorna "True" caso a sequencia estiver em ordem crescente e retorna "False" caso contrario.
def crescente(seq):
    '''list -> bool'''
    n = len(seq)
    i = 1
    cresce = True
    #Formas alternativas para essa funçao
    #while (i < n):
        #if (seq[i - 1) > seq[i]):
            #cresce = False
        #i = i + 1
    #return cresce
    
    while (i < n and cresce):
        if seq[i-1] > seq[i]:
            cresce = False
        i = i + 1
    return cresce

# Algoritmo de inserçao:
 #1-) Assume que a primeira posiçao da lista esta ordenada

 #2-) Sabemos que o elemento anteriores ao elemento novo estao ordenado

 #3-) Insira o elemento novo(seq[novo]) na posiçao adequada na sublista [0:novo] e desloca aos demais elementos para obter a lista ordenada

 #4-) novo = novo + 1 e repete a parte do passo ate o ultimo elemento

def insceçao(seq):
    n = len(seq)
    novo = 1
    while (novo < n):
        x = seq[novo]
        i = novo - 1
        while (i >= 0 and seq[i] > x):
            seq[i+1] = seq[i]
            seq[i] = x
            i = i - 1
        novo = novo + 1
    return seq

#Algoritmo de seleçao:
#Na primeira etapa, primeira posiçao e trocada pelo elemento que deve ocupar primeira posiçao

def seleçao(seq):
    n = len(seq)
    i = 0
    while (i < n-1):
        menor = i
        j = i + 1
        while (j < n):
            if (seq[j] < seq[menor]):
                menor = j
            j = j + 1
        anx = seq[i]
        seq[i] = seq[menor]
        seq[menor] = anx
        i = i + 1
    return seq

# Algoritmo - Bubble

def bubble(seq):
    n = len(seq)
    i = 0
    while (i < n-1):
        j = n - 1
        while (j > 0):
            if (seq[j] < seq[j-1]):
                anx = seq[j]
                seq[j] = seq[j-1]
                seq[j-1] = anx
            j = j - 1
        i = i + 1
    return seq
        




            
        
    

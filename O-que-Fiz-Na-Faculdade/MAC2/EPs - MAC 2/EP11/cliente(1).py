# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM OUTRO import ...
#------------------------------------------------------------------

'''

    Nome:Leonardo Takashi Teramatsu
    NUSP:9797083

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0122, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função 
        split(), strip(), map() e filter() para leitura dos dados
        no arquivo.

    Descrição de ajuda ou indicação de fonte:

'''

#-------------------------------------------------------------------
#
# Funções administrativas mergeX() e mergesortX()
#
#-------------------------------------------------------------------
def intercala(v, e, m, d):
    if len(v) == 2:
        if v[1] < v[0]:
            x = v[1]
            v[1] = v[0]
            v[0] = x
            return v
        else:
            return v
    else:
        lista = []
        esquerda = 0
        direita = m
        while esquerda < m and direita < d:
            if v[esquerda] < v[direita]:
                lista.append(v[esquerda])
                esquerda += 1
            else:
                lista.append(v[direita])
                direita += 1
        while esquerda < m:
            lista.append(v[esquerda])
            esquerda += 1
        while direita < d:
            lista.append(v[direita])
            direita += 1
        j = 0
        for i in range(e,d):
            v[i] = lista[j]
            j += 1
        return v
    
def mergeX(v, e, m, d):
    ''' (list, int, int, int) -> int

    RECEBE uma lista v tal que v[e:m] e v[m:d] estão em ordem crescente. 
    A função intercala essas fatias de forma que v[e:d] esteja em ordem crescente.

    RETORNA o número de transposições necessários para ordenar v[e:d].
    '''
    if len(v) == 2:
        if v[1] < v[0]:
            x = v[1]
            v[1] = v[0]
            v[0] = x
            return 1
        else:
            return 0
    else:
        transpos = 0
        lista = []
        esquerda = 0
        direita = m
        while esquerda < m and direita < d:
            if v[esquerda] < v[direita]:
                lista.append(v[esquerda])
                esquerda += 1
            else:
                lista.append(v[direita])
                direita += 1
                transpos = transpos + len(v[esquerda:m])
        while esquerda < m:
            lista.append(v[esquerda])
            esquerda += 1
        while direita < d:
            lista.append(v[direita])
            direita += 1
        j = 0
        for i in range(e,d):
            v[i] = lista[j]
            j += 1
        return transpos

def mergesortX(v, e=None, d=None):
    ''' (list, int, int) -> int

    Recebe uma lista v e dois inteiros que definem 
    um segmento de v que deve ser ordenado. 

    Quando e e d são None, a lista inteira deve ser ordenada.

    A função retorna o número de transposições resultantes da ordenação 
    de v[e:d].
    '''
    if e == None and d == None:
        return mergesortX(v,0,len(v))
    else:
        n = d-e
        if n <= 1:
            return 0
        p = 0
        q = 0
        r = 0
        m = (e+d) // 2
        p = p+mergesortX(v,e,m)
        q = q+mergesortX(v,m,d)
        r = r+mergeX(v[e:d],0,len(v[e:d])//2,len(v[e:d]))
        v[e:d] = intercala(v[e:d],0,len(v[e:d])//2,len(v[e:d]))
        return p+q+r



#-----------------------------------------------------------
class Cliente:
    '''
        Copie a sua classe Cliente do EP10 para aqui.

        Estenda essa classe adicionando os métodos:
           em_comum() e distanciaX()
        como especifado no enunciado.
 
        Coloque o seu código a seguir.
    '''
    def __init__(self,nome):
            self.nome = nome
            self.classificacao = {}
            self.classificacao_reverse = {}
            self.lista = []
    
    def put_classificacao(self,filmes):
        for i in range(len(filmes)):
            self.classificacao[i] = filmes[i]
            self.classificacao_reverse[filmes[i]] = i
    
    def __str__(self):
        x = self.nome+'\n'
        for i in range(len(self.classificacao)):
            x = x + '%d: %s\n' %(i,self.classificacao[i])
        return x
    
    def get_nome(self):
        return self.nome
    
    def get_classificacao(self):
        for i in range(len(self.classificacao)):
            self.lista.append(self.classificacao[i])
        return self.lista
    
    def distancia(self,other):
        if self.lista == other.lista:
            return 0
        else:
            lista_modelo = {}
            lista_compara = []
            ordem = 0
            for i in range(len(self.lista)):
                if self.lista[i] in other.lista:
                    lista_modelo[self.lista[i]] = ordem
                    ordem += 1
            for j in range(len(other.lista)):
                if other.lista[j] in lista_modelo:
                    lista_compara.append(lista_modelo[other.lista[j]])
            if len(lista_modelo) == 1 or len(lista_modelo) == 2:
                return 0
            else:
                transposicao = 0
                for i in range(0,len(lista_compara)):
                    for j in range(0,len(lista_compara)-1):
                        if lista_compara[j] > lista_compara[j+1]:
                            x = lista_compara[j+1]
                            lista_compara[j+1] = lista_compara[j]
                            lista_compara[j] = x
                            transposicao += 1
                return transposicao
            
    def em_comum(self,other):
        comum = []
        for i in other.classificacao_reverse:
            if i in self.classificacao_reverse:
                comum.append[self.classificacao[i]]
        return comum
    
    def distanciaX(self,other):
        comum = []
        for i in other.classificacao_reverse:
            if i in self.classificacao_reverse:
                comum.append[self.classificacao[i]]
        return mergesortX(comum,None,None)



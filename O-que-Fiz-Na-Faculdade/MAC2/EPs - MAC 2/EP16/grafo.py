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

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''

#-----------------------------------------------------------------
class Grafo:
    '''
        Siga as especificações do enunciado para construir a classe Grafo.

        Coloque o seu código a seguir.
    '''
    def __init__(self,strings = '',caractere = ' '):
        self.strings = strings
        self.caractere = caractere
        self.vertice = {}
        if self.strings != '':
            texto = open(self.strings,'r',encoding = 'utf-8')
            for i in texto:
                l = i.split('\n')
                lista = l[0].split(self.caractere)
                if lista[0] not in self.vertice:
                    self.vertice[lista[0]]=set()
                self.vertice[lista[0]].update(lista[1:])
                for j in lista[1:]:
                    if j not in self.vertice:
                        self.vertice[j] = set()
                        self.vertice[j].add(lista[0])
                    else:
                        self.vertice[j].add(lista[0])
    
    def __str__(self):
        x = ''
        if len(self.vertice) == 0:
            return x
        lista = list(self.vertice)
        lista.sort()
        for i in lista:
            x = x+'%s | ' %(i)
            lista = list(self.vertice[i])
            lista.sort()
            for j in range(0,len(lista)):
                if j == len(lista)-1:
                    x = x +'%s\n' %(lista[j])
                else:
                    x = x +'%s, ' %(lista[j])
        return x
        
    def insira_aresta(self,v,w):
        if v == '' or w == '':
            return ''
        else:
            if ' ' in v:
                lista = v.split(' ')
                for i in lista:
                    if i != '':
                        v = i
            if ' ' in w:
                lista = w.split(' ')
                for i in lista:
                    if i != '':
                        w = i
            if len(self.vertice) == 0:
                self.vertice[v] = set()
                self.vertice[v].add(w)
                self.vertice[w] = set()
                self.vertice[w].add(v)
            else:
                if v not in self.vertice:
                    self.vertice[v] = set()
                    self.vertice[v].add(w)
                    if w not in self.vertice:
                        self.vertice[w] = set()
                        self.vertice[w].add(v)
                    else:
                        self.vertice[w].add(v)
                        
                else:
                    self.vertice[v].add(w)
                    if w not in self.vertice:
                        self.vertice[w] = set()
                        self.vertice[w].add(v)
                    else:
                        self.vertice[w].add(v)
    
    def tem_vertice(self,v):
        if v not in self.vertice:
            return False
        return True
    
    def V(self):
        return len(self.vertice)
    
    def A(self):
        aresta = 0
        contados = []
        for i in self.vertice:
            for j in self.vertice[i]:
                if j not in contados:
                    aresta += 1
            contados.append(i)
        return aresta
    
    def vertices(self):
        lista = list(self.vertice)
        lista.sort()
        return lista
    
    def adjacentes(self,v):
        if v not in self.vertice:
            return 
        lista = list(self.vertice[v])
        lista.sort()
        return lista
    
    def grau(self,v):
        if v not in self.vertice:
            return 0
        return len(self.vertice[v])
    
    def tem_aresta(self,v,w):
        if v not in self.vertice:
            return False
        else:
            if w in self.vertice[v]:
                return True
            else:
                return False





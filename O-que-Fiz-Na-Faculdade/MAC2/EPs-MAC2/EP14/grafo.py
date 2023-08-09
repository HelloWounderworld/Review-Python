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
        if self.strings != '' and self.caractere == ' ':
            cobaia = {}
            for i in self.strings:
                d = i.split('\n')
                p = d[0].split(self.caractere)
                for j in range(1,len(p)):
                    if p[j] not in cobaia:
                        cobaia[p[j]] = [p[0]]
                    elif p[0] not in cobaia[p[j]] and p[0] != j:
                        cobaia[p[j]].append(p[0])
                if p[0] not in cobaia:
                    cobaia[p[0]] = []
                for j in range(1,len(p)):
                    if p[j] not in cobaia[p[0]]:
                        cobaia[p[0]].append(p[j])
            lista = list(cobaia)
            lista.sort()
            for i in lista:
                self.vertice[i] = cobaia[i]
            
        else:
            for i in self.strings:
                d = i.split('\n')
                p = d[0].split(self.caractere)
                if p[0] not in self.vertice:
                    self.vertice[p[0]] = []
                for j in range(1,len(p)):
                    self.vertice[p[0]].append(p[j])
                    if p[j] not in self.vertice:
                        self.vertice[p[j]] = []
                        self.vertice[p[j]].append(p[0])
                    else:
                        self.vertice[p[j]].append(p[0])
    
    def __str__(self):
        x = ''
        if len(self.vertice) == 0:
            return x
        if self.caractere == ' ':
            for i in self.vertice:
                x = x + i + ' | '
                self.vertice[i].sort()
                n = len(self.vertice[i])
                for j in range(n):
                    if j == n-1:
                        x = x + self.vertice[i][j] + '\n'
                    else:
                        x = x + self.vertice[i][j] + ', '
            return x
        else:
            for i in self.vertices:
                x = x + i + ' | '
                n = len(self.vertice[i])
                for j in range(n):
                    if j == n-1:
                        x = x + self.vertice[i][j] + '\n'
                    else:
                        x = x + self.vertice[i][j] + ', '
            return x
        
    def insira_aresta(self,v,w):
        if v == '' or w == '':
            return ''
        else:
            if len(self.vertice) == 0:
                self.vertice[v] = [w]
                self.vertice[w] = [v]
            else:
                if v not in self.vertice:
                    self.vertice[v] = [w]
                    if w not in self.vertice:
                        self.vertice[w] = [v]
                    else:
                        self.vertice[w].append(v)
                        
                else:
                    self.vertice[v].append(w)
                    if w not in self.vertice:
                        self.vertice[w] = [v]
                    else:
                        self.vertice[w].append(v)
    
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
        return list(self.vertice)
    
    def adjacentes(self,v):
        if v not in self.vertice:
            return 
        return self.vertice[v]
    
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





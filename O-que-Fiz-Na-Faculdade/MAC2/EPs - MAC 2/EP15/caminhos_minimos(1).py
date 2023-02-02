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

        Minha colega Maria me explicou o funcionamente da busca em largura.

    Descrição de ajuda ou indicação de fonte:

'''

from grafo import Grafo

# pode ser utilizado para clonar o grafo dado: grafo = copy.deepcopy(grafo_dado)
import copy 

class Caminhos_Minimos:
    '''
    Construa a sua classe abaixo.
    '''
    def __init__(self,Grafo,origem):
        self.Grafo = Grafo
        self.origem = origem
        self.distancias = {}
        self.anteriores = {}
        self.ordem = {}
        self.ordem_reverse = {}
        if self.origem in self.Grafo.vertice:
            conta = 0
            for i in self.Grafo.vertice:
                self.ordem[i] = conta
                self.ordem_reverse[conta]=i
                conta += 1
            n = len(self.Grafo.vertice)
            d = n*[n]
            d[self.ordem[self.origem]] = 0
            q = [self.ordem[self.origem]]
            while len(q) != 0:
                i = q.pop(0)
                for j in range(n):
                    if d[j] > d[i]+1 and self.ordem_reverse[j] in self.Grafo.adjacentes(self.ordem_reverse[i]):
                        d[j] = d[i]+1
                        self.anteriores[self.ordem_reverse[j]] = self.ordem_reverse[i]
                        q.append(j)
                q.sort()
            for i in range(len(d)):
                self.distancias[self.ordem_reverse[i]] = d[i]
                
    def __str__(self):
        x = 'Caminhos Minimos a partir de %s\n' %(self.origem)
        for i in self.Grafo.vertice:
            x = x + i +': '
            if self.distancias[i] != 0:
                x = x + '%d, ' %(self.distancias[i]) +'%s\n' %(self.anteriores[i])
            else:
                x = x + '%d, ' %(self.distancias[i]) +'None\n'
        return x
    
    def distancia(self,v):
        if v not in self.Grafo.vertice:
            return
        return self.distancias[v]
                
    def anterior(self,v):
        if v == self.origem:
            return
        return self.anteriores[v]
    
    def caminho(self,v):
        cobaia = [v]
        while v != self.origem:
            cobaia.append(self.anteriores[v])
            v = self.anteriores[v]
        lista = []
        for i in range(len(cobaia)):
            lista.append(cobaia[-i-1])
        return lista
    
    
    
# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
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
    monitores e colegas). Com exceção de material de MAC0110 ou MAC0122, 
    caso  você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''
from percolation import Percolation
import numpy as np
import random
import math
                 
class PercolationStats:
    '''Classe utilizada para estimar o limiar de percolação.
    '''
    def __init__(self,shape,T):
        self.shape = shape
        self.T = T
        self.fracoes = []
        self.media = []
        self.variancia = []
        
    def mean(self):
        x_t = 0
        for i in range(self.T):
            Cobaia = Percolation(self.shape)
            dictionary = {}
            tuplas = []
            for i in range(len(Cobaia.data)):
                for j in range(len(Cobaia.data[i])):
                    tuplas.append((i,j))
            for l in range(Cobaia.data.size):
                dictionary[i] = tuplas[i]
            while Cobaia.percolates() == False:
                x = random.randrange(Cobaia.data.size)
                nlin,ncol = tuplas[x]
                Cobaia.open(nlin,ncol)
            self.fracoes.append(Cobaia.no_open()/Cobaia.data.size)
            x_t = x_t + (Cobaia.no_open()/Cobaia.data.size)
        self.media.append(x_t/self.T)
        return x_t / self.T
    
    def stddev(self):
        soma = 0
        for i in self.fracoes:
            soma = soma + (self.media[0]-i)**2
        self.variancia.append(soma / (self.T - 1))
        return soma / (self.T - 1)
    
    def confidenceLow(self):
        return self.media[0]-((1.96*math.sqrt(self.variancia[0]))/(math.sqrt(self.T)))
    
    def confidenceHigh(self):
        return self.media[0]+((1.96*math.sqrt(self.variancia[0]))/(math.sqrt(self.T)))

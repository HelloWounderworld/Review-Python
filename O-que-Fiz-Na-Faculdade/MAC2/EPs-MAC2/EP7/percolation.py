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
    monitores e colegas). Com exceção de material de MAC0110 e MAC0122, 
    caso você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''
import numpy as np

#-------------------------------------------------------------------------
# se você quiser a classe Queue feita na aula, coloque o seu arquivo queue.py
# na mesma pasta do EP e descomente a linha abaixo
# from queue import Queue

#-------------------------------------------------------------------------- 
# constantes
BLOCKED = 0  # sítio bloqueado
OPEN    = 1  # sítio aberto
FULL    = 2  # sítio cheio

def coleta(array,lin,col,tupla):
    if lin == 0:
        if array[lin+1,col] == OPEN:
            tupla.append((lin+1,col))
            array[lin+1,col] = FULL
            coleta(array,lin+1,col,tupla)
            return tupla
    elif col == 0:
        if lin == len(array)-1:
            vizinhos = [array[lin-1,col],array[lin,col+1]]
            if OPEN not in vizinhos:
                return tupla
            else:
                tuplas = [(lin-1,col),(lin,col+1)]
                for i in tuplas:
                    nlin,ncol = i
                    if i not in tupla:
                        tupla.append(i)
                        array[nlin,ncol] = FULL
                        coleta(array,nlin,ncol,tupla)
                return coleta(array,nlin,ncol,tupla)
        else:
            vizinhos = [array[lin-1,col],array[lin+1,col],array[lin,col+1]]
            if OPEN not in vizinhos:
                return tupla
            else:
                tuplas = [(lin-1,col),(lin+1,col),(lin,col+1)]
                for i in tuplas:
                    nlin,ncol = i
                    if array[nlin,ncol] == OPEN:
                        if i not in tupla:
                            tupla.append(i)
                            array[nlin,ncol] = FULL
                            coleta(array,nlin,ncol,tupla)
                return coleta(array,nlin,ncol,tupla)
    elif col == len(array[lin]) - 1:
        if lin == len(array)-1:
            vizinhos = [array[lin-1,col],array[lin,col-1]]
            if OPEN not in vizinhos:
                return tupla
            else:
                tuplas = [(lin-1,col),(lin,col-1)]
                for i in tuplas:
                    nlin,ncol = i
                    if array[nlin,ncol] == OPEN:
                        if i not in tupla:
                            tuplas.append(i)
                            array[nlin,ncol] = FULL
                            coleta(array,nlin,ncol,tupla)
                return coleta(array,nlin,ncol,tupla) 
        else:
            vizinhos = [array[lin-1,col],array[lin+1,col],array[lin,col-1]]
            if OPEN not in vizinhos:
                return tupla
            else:
                tuplas = [(lin-1,col),(lin+1,col),(lin,col-1)]
                for i in tuplas:
                    nlin,ncol = i
                    if array[nlin,ncol] == OPEN:
                        if  i not in tupla:
                            tupla.append(i)
                            array[nlin,ncol] = FULL
                            coleta(array,nlin,ncol,tupla)
                return coleta(array,nlin,ncol,tupla)
    else:
        if lin == len(array)-1:
            vizinhos = [array[lin-1,col],array[lin,col-1],array[lin,col+1]]
            if OPEN not in vizinhos:
                return tupla
            else:
                tuplas = [(lin-1,col),(lin,col-1),(lin,col+1)]
                for i in tuplas:
                    nlin,ncol = i
                    if array[nlin,ncol] == OPEN:
                        tupla.append(i)
                        array[nlin,ncol] = FULL
                        coleta(array,nlin,ncol,tupla)
                return coleta(array,nlin,ncol,tupla)
        else:
            vizinhos = [array[lin-1,col],array[lin+1,col],array[lin,col-1],array[lin,col+1]]
            if OPEN not in vizinhos:
                return tupla
            else:
                tuplas = [(lin-1,col),(lin+1,col),(lin,col-1),(lin,col+1)]
                for i in tuplas:
                    nlin,ncol = i
                    if array[nlin,ncol] == OPEN:
                        if i not in tupla:
                            tupla.append(i)
                            array[nlin,ncol] = FULL
                            coleta(array,nlin,ncol,tupla)
                return coleta(array,nlin,ncol,tupla)

class Percolation:
    def __init__(self,shape):
        self.shape = shape
        self.data = np.full(self.shape,BLOCKED)
        
    def __str__(self):
        Percola = False
        for j in range(len(self.data[0])):
                if self.data[len(self.data)-1,j] == FULL:
                    Percola = True
                    break      
        Set = {0:' ',1:'o',2:   'x'}
        x = '+---'
        abertos = 0
        for i in range(len(self.data)):
            if i != 0:
                x = x + '+---'
            for j in range(len(self.data[i])):
                if j == len(self.data[i])-1:
                    x = x + '+\n|'
                else:
                    x = x + '+---'
            for l in range(len(self.data[i])):
                if l == len(self.data[i])-1:
                    if self.data[i,l] == OPEN or self.data[i,l] == FULL:
                        abertos+=1
                    x = x + ' %s |\n' %(Set[self.data[i,l]])
                else:
                    if self.data[i,l] == OPEN or self.data[i,l]==FULL:
                        abertos+=1
                    x = x + ' %s |' %(Set[self.data[i,l]])
        x = x + '+---'
        for t in range(len(self.data[0])):
            if t == len(self.data[0]) - 1:
                x = x + '+'
            else:
                x = x + '+---'
        lin,col = self.shape
        x = x +'\ngrade de dimensao: %dx%d' %(lin,col)
        x = x +'\nno. sitios abertos: %d' %(abertos)
        x = x +'\npercolou: %s' %(Percola)
        return x
    
    def open(self,lin,col):
        if lin == 0:
            if self.data[lin+1,col] == OPEN:
                x = coleta(self.data,lin,col,[(lin,col)])
                for i in x:
                    nlin,ncol = i
                    self.data[nlin,ncol] = FULL
            else:
                self.data[lin,col] = FULL      
        elif lin == len(self.data)-1:
            if col == len(self.data[lin])-1:
                vizinhanca = [self.data[lin-1,col],self.data[lin,col-1]]
                if FULL in vizinhanca:
                    x = coleta(self.data,lin,col,[(lin,col)])
                    for i in x:
                        nlin,ncol = i
                        self.data[nlin,ncol] = FULL
                else:
                    self.data[lin,col] = OPEN
            elif col == 0:
                vizinhanca = [self.data[lin-1,col],self.data[lin,col+1]]
                if FULL in vizinhanca:
                    x = coleta(self.data,lin,col,[(lin,col)])
                    for i in x:
                        nlin,ncol = i
                        self.data[nlin,ncol] = FULL
                else:
                    self.data[lin,col] = OPEN
            else:
                vizinhanca = [self.data[lin-1,col],self.data[lin,col-1],self.data[lin,col+1]]
                if FULL in vizinhanca:
                    x = coleta(self.data,lin,col,[(lin,col)])
                    self.data[nlin,ncol] = FULL
                else:
                    self.data[lin,col] = OPEN
                
        else:
            if col == 0 and 0< lin < len(self.data)-1:
                vizinhanca = [self.data[lin-1,col],self.data[lin+1,col],self.data[lin,col+1]]
                if FULL in vizinhanca:
                    x = coleta(self.data,lin,col,[(lin,col)])
                    for i in x:
                        nlin,ncol = i
                        self.data[nlin,ncol] = FULL
                else:
                    self.data[lin,col] = OPEN
            elif col == len(self.data[lin]) - 1 and 0<lin < len(self.data)-1:
                vizinhanca = [self.data[lin-1,col],self.data[lin+1,col],self.data[lin,col-1]]
                if FULL in vizinhanca:
                    x = coleta(self.data,lin,col,[(lin,col)])
                    for i in x:
                        nlin,ncol = i
                        self.data[nlin,ncol] = FULL
                else:
                    self.data[lin,col] = OPEN    
            elif lin< len(self.data)-1:
                vizinhanca = [self.data[lin-1,col],self.data[lin+1,col],self.data[lin,col-1],self.data[lin,col+1]]
                if FULL in vizinhanca:
                    x = coleta(self.data,lin,col,[(lin,col)])
                    for i in x:
                        nlin,ncol = i
                        self.data[nlin,ncol] = FULL
                else:
                    self.data[lin,col] = OPEN
                
        
    def is_open(self,lin,col):
        if self.data[lin,col] == OPEN or self.data[lin,col]==FULL:
            return True
        return False
        
    def is_full(self,lin,col):
        if self.data[lin,col] == 2:
            return True
        return False
    
    def percolates(self):
        for j in range(len(self.data[0])):
            if self.data[len(self.data)-1,j] == FULL:
                return True
        return False
    
    def no_open(self):
        aberto = 0
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i,j] == OPEN or self.data[i,j] ==FULL:
                    aberto+=1
        return aberto
    
    def get_grid(self):
        return self.data.copy()

'''
Antes de modificar e colocar no teste Drive
Nota
Revisado em domingo, 29 set 2019, 16:03 por Atribuição automática de nota
grade: 9,5 / 10,0

Relatório de avaliação[-]
__init__ e shape(): iniciando avaliação dos testes (vale 2 ponto(s))
__init__ e shape() passou em todos os testes :-)
__init__ e shape(): avaliação encerrada... (nota 2.0)

__str__(): iniciando avaliação dos testes (vale 0.5 ponto(s))
__str__() passou em todos os testes :-)
__str__(): avaliação encerrada... (nota 0.5)

is_open(): iniciando avaliação dos testes (vale 1 ponto(s))
is_open() passou em todos os testes :-)
is_open(): avaliação encerrada... (nota 1)

is_full(): iniciando avaliação dos testes (vale 1 ponto(s))
is_full() passou em todos os testes :-)
is_full(): avaliação encerrada... (nota 1)

percolates(): iniciando avaliação dos testes (vale 1 ponto(s))
percolates() passou em todos os testes :-)
percolates(): avaliação encerrada... (nota 1)

no_open(): iniciando avaliação dos testes (vale 1.5 ponto(s))
no_open() passou em todos os testes :-)
no_open(): avaliação encerrada... (nota 1.5)

get_grid(): iniciando avaliação dos testes (vale 1 ponto(s))
get_grid() passou em todos os testes :-)
get_grid(): avaliação encerrada... (nota 1)

open(): iniciando avaliação dos testes (vale 2 ponto(s))
Percolation((4, 4)).open(0, 3) não alterou grade corretamente (teste 7).
open() não passou no(s) teste(s) acima
open(): avaliação encerrada... (nota 1.5)

Seu programa não passou no(s) teste(s) acima. :-(

Fim da avaliação.
'''

'''
Nota
Revisado em quarta, 6 nov 2019, 16:17 por Atribuição automática de nota
grade: 7,5 / 10,0

Relatório de avaliação[-]
__init__ e shape(): iniciando avaliação dos testes (vale 2 ponto(s))
__init__ e shape() passou em todos os testes :-)
__init__ e shape(): avaliação encerrada... (nota 2.0)

__str__(): iniciando avaliação dos testes (vale 0.5 ponto(s))
__str__() passou em todos os testes :-)
__str__(): avaliação encerrada... (nota 0.5)

is_open(): iniciando avaliação dos testes (vale 1 ponto(s))
is_open() passou em todos os testes :-)
is_open(): avaliação encerrada... (nota 1)

is_full(): iniciando avaliação dos testes (vale 1 ponto(s))
Percolation((1, 2)).is_full(0,1) retornou valor errado (teste 1).
Percolation((5, 5)).is_full(4,3) retornou valor errado (teste 5).
is_full() não passou no(s) teste(s) acima
is_full(): avaliação encerrada... (nota 0.0)

percolates(): iniciando avaliação dos testes (vale 1 ponto(s))
percolates() passou em todos os testes :-)
percolates(): avaliação encerrada... (nota 1)

no_open(): iniciando avaliação dos testes (vale 1.5 ponto(s))
no_open() passou em todos os testes :-)
no_open(): avaliação encerrada... (nota 1.5)

get_grid(): iniciando avaliação dos testes (vale 1 ponto(s))
get_grid() passou em todos os testes :-)
get_grid(): avaliação encerrada... (nota 1)

open(): iniciando avaliação dos testes (vale 2 ponto(s))
Percolation((1, 2)).open((0, 1)) explodiu (teste 1).
Percolation((5, 5)).open((4, 3)) explodiu (teste 5).
Percolation((4, 4)).open(0, 3) não alterou grade corretamente (teste 7).
open() não passou no(s) teste(s) acima
open(): avaliação encerrada... (nota 0.5)

Seu programa não passou no(s) teste(s) acima. :-(

Fim da avaliação.
'''



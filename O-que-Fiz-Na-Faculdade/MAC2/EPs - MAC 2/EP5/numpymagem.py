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
    monitores e colegas). Com exceção de material de MAC0110, caso
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
import numpy as np
def show(array): 
    nlins, ncolns = array.shape
    x = str()
    for i in range(nlins):
        y = str()
        for j in range(ncolns):
            if j == (ncolns - 1):
                y = y + str(array[i,j])
            else:
                y = y + str(array[i,j]) + ',' + ' '
        x = x + y + '\n'
    return x
#-------------------------------------------------------------------------- 

class NumPymagem:
    '''
    Implementação da classe NumPymagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''
    def __init__(self,nlins = 0,ncolns = 0,valor=0):
        self.compara = np.arange(1).reshape(1,)
        self.nlins = nlins
        self.ncolns = ncolns
        self.valor = valor
        self.tamanho = self.nlins*self.ncolns
        if type(self.valor)==type(self.compara):
            self.data = self.valor
        else:
            self.data = np.full((self.nlins,self.ncolns),self.valor)
        
    def __str__(self):
        return show(self.data)
        
    def size(self):
        return self.data.shape
    
    def get(self,lin,col):
        return self.data[lin,col]
    
    def put(self,lin,col,valor):
        self.data[lin,col] = valor
    
    def crop(self,tlx=0,tly=0,brx=0,bry=0):
        if tlx==0 and tly==0 and brx==0 and bry==0:
            array = NumPymagem(self.nlins,self.ncolns,0)
            nlin,ncol = self.data.shape
            for i in range(nlin):
                for j in range(ncol):
                    array.put(i,j,self.data[i,j])
            return array
        else:
            if len(self.data)<=brx or len(self.data[0,:])<= bry :
                nlin, ncoln = self.data.shape
                if len(self.data)<=brx and bry<len(self.data[0,:]):
                    img_nova = NumPymagem(nlin-tlx,bry-tly,0)
                    for i in range(tlx,nlin):
                        for j in range(tly,bry):
                            img_nova.put(i-tlx,j-tly,self.data[i,j])
                    return img_nova
                elif brx<len(self.data) and len(self.data[0,:])<=bry:
                    img_nova = NumPymagem(brx-tlx,ncoln-tly)
                    for i in range(tlx,brx):
                        for j in range(tly,ncoln):
                            img_nova.put(i-tlx,j-tly,self.data[i,j])
                    return img_nova
                else:
                    img_nova = NumPymagem(nlin-tlx,ncoln-tly,0)
                    for i in range(tlx,nlin):
                        for j in range(tly,ncoln):
                            img_nova.put(i-tlx,j-tly,self.data[i,j])
                    return img_nova
            else:
                nlin , ncoln = self.data.shape
                if brx == 0 and bry == 0:
                    img_nova = NumPymagem(nlin-tlx,ncoln-tly)
                    for i in range(tlx,nlin):
                        for j in range(tly,ncoln):
                            img_nova.put(i-tlx,j-tly,self.data[i,j])
                    return img_nova
                img_nova = NumPymagem(brx-tlx,bry-tly,0)
                for i in range(tlx,brx):
                    for j in range(tly,bry):
                        img_nova.put(i-tlx,j-tly,self.data[i,j])
                return img_nova
    
    def paste(self,other,tlin,tcol):
        if 0<=tlin<len(self.data) and 0<=tcol<len(self.data[0,:]):
            if len(other.data)<=len(self.data[tlin:]):
                if len(other.data[0,:])<=len(self.data[tlin,tcol:]):
                    self.data[tlin:len(other.data)+tlin,tcol:len(other.data[0,:])+tcol] = other.data
                else:
                    self.data[tlin:len(other.data)+tlin,tcol:]=other.data[:,:len(self.data[tlin,tcol:])]
            else:
                if len(other.data[0,:])<=len(self.data[tlin,tcol:]):
                    self.data[tlin:,tcol:len(other.data[0,:])+tcol] = other.data[:len(self.data[tlin:]),:]
                else:
                    self.data[tlin:,tcol:] = other.data[:len(self.data[tlin:]),:len(self.data[tlin,tcol:])]
        else:
            if 0<=tcol<len(self.data[0,:]):
                if 0<tlin:
                    self.data
                else:
                    if tlin+len(other.data)<0:
                        self.data
                    else:
                        if tlin+len(other.data)<len(self.data):
                            if len(other.data[0,:])<len(self.data[0,tcol:]):
                                self.data[:tlin+len(other.data),tcol:tcol+len(other.data[0,:])] = other.data[-tlin:,:]
                            else:
                                self.data[:tlin+len(other.data),tcol:]=other.data[-tlin:,:len(self.data[0,tcol:])]
                        else:
                            if len(other.data[0,:])<len(self.data[0,tcol:]):
                                self.data[:,tcol:tcol+len(other.data[0,:])] = other.data[-tlin:-tlin+len(self.data),:]
                            else:
                                self.data[:,tcol:]=other.data[-tlin:-tlin+len(self.data),:len(self.data[0,tcol:])]                            
            elif 0<=tlin<len(self.data):
                if 0<tcol:
                    self.data
                else:
                    if tcol+len(other.data[0,:])<0:
                        self.data
                    else:
                        if tcol+len(other.data[0,:])<len(self.data[tlin,:]):
                            if len(other.data)<len(self.data[tlin:]):
                                self.data[tlin:tlin+len(other.data),:tcol+len(other.data[0,:])] = other.data[:,-tcol:]
                            else:
                                self.data[tlin:,:tcol+len(other.data[0,:])] = other.data[:len(self.data),-tcol:]
                        else:
                            if len(other.data)<len(self.data[tlin:]):
                                self.data[tlin:tlin+len(other.data),:]=other.data[:,-tcol:-tcol+len(self.data[tlin,:])]
                            else:
                                self.data[tlin:,:] = other.data[:tlin+len(self.data),-tcol:-tcol+len(self.data[tlin,:])]
            else:
                if 0<tlin or 0<tcol:
                    self.data
                else:
                    if tlin+len(other.data)<0 or tcol+len(other.data[0,:])<0:
                        self.data
                    else:
                        if tlin+len(other.data)<len(self.data):
                            if tcol+len(other.data[0,:])<len(self.data[0,:]):
                                self.data[:tlin+len(other.data),:tcol+len(other.data[0,:])]=other.data[-tlin:,-tcol:]
                            else:
                                self.data[:tlin+len(other.data),:]=other.data[-tlin:,-tcol:-tcol+len(self.data[0,:])]
                        else:
                            if tcol+len(other.data[0,:])<len(self.data[0,:]):
                                self.data[:,:tcol+len(other.data[0,:])]=other.data[-tlin:-tlin+len(self.data),-tcol:]
                            else:
                                self.data[:,:]=other.data[-tlin:-tlin+len(self.data),-tcol:-tcol+len(self.data[0,:])]
                                    
    def __add__(self,other):
        lista = np.array([0.0])
        if other.data.dtype == lista.dtype:
            lista = NumPymagem(self.nlins,self.ncolns,0.0)
            for i in range(self.nlins):
                for j in range(self.ncolns):
                    lista.put(i,j,self.data[i,j]+other.data[i,j])
            return lista
        else:
           lista = NumPymagem(self.nlins,self.ncolns,0)
           for i in range(self.nlins):
               for j in range(self.ncolns):
                   lista.put(i,j,self.data[i,j]+other.data[i,j])
           return lista 
    
    def __mul__(self,alpha):
        if type(alpha)==float:
            lista = NumPymagem(self.nlins,self.ncolns,0.0)
            for i in range(self.nlins):
                for j in range(self.ncolns):
                    lista.put(i,j,self.data[i,j]*alpha)
            return lista
        else:
            lista = NumPymagem(self.nlins,self.ncolns,0)
            for i in range(self.nlins):
                for j in range(self.ncolns):
                    lista.put(i,j,self.data[i,j]*alpha)
            return lista
    
    def pinte_disco(self,lin,col,raio,valor):
        nlins , ncols = self.data.shape
        for i in range(lin-raio,lin+raio+1):
            for j in range(col-raio, col+raio+1):
                if 0<=i<=(nlins-1) and 0 <= j <= (ncols-1):
                    if ((i-lin)**2+(j-col)**2)<raio**2:
                        self.data[i,j] = valor
    
    def pinte_retangulo(self,tlx,tly,brx,bry,valor):
        nlin, ncol = self.data.shape
        for i in range(tlx,brx):
            for j in range(tly,bry):
                if (0<= i < nlin) and (0<= j < ncol):
                    self.data[i,j] = valor
    
    def transpoe(self):
        self.data = np.transpose(self.data)
        self.nlins,self.ncolns = self.data.shape
    
    def rearranja(self,nlin,ncol):
        if nlin*ncol != self.nlins*self.ncolns:
            pass
        else:
            self.data = self.data.ravel().reshape(nlin,ncol)
            
    def espelha(self,eixo):
        if eixo == 'h':
            self.data = np.fliplr(self.data)
        elif eixo == 'v':
            self.data = np.flipud(self.data)
   

            

    # escreva aqui os métodos da classe Pymagem

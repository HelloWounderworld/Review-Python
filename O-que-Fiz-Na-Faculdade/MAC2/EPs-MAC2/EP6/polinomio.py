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
def verifica(lista):
    for i in lista:
        if i != 0:
            return False
    return True
class Polinomio:
    
    def __init__(self,coefs = []):
        self.coefs = coefs[:]
    
    def __str__(self):
        s = str()
        g = len(self.coefs)
        if g == 0:
            s += '0'
            return s
        for i in range(g):
            j = -i-1
            if j == -g:
                if self.coefs[j] < 0:
                    x = (-1)*self.coefs[j]
                    s = s+'-'+' '+str(x)
                elif self.coefs[j]>0:
                    s = s+'+'+' '+str(self.coefs[j])
                else:
                    if len(self.coefs)>1:
                        pass
                    elif len(self.coefs)==1:
                        s = s+str(self.coefs[j])
            elif j == -1:
                if self.coefs[j]<0:
                    x = (-1)*self.coefs[j]
                    s = s+'-'+' '+str(x)+'*x^%d'%(g+j)+' '
                elif self.coefs[j] > 0:
                    s = s + str(self.coefs[j])+'*x^%d'%(g+j)+' '
                else:
                    pass
            else:                
                if self.coefs[j]<0:
                    x = (-1)*self.coefs[j]
                    s = s + '-'+' '+str(x)+'*x^%d'%(g+j)+' '
                elif self.coefs[j]>0:
                    s = s+'+'+' '+str(self.coefs[j])+'*x^%d'%(g+j)+' '
                else:
                    pass
        return s
    
    def __call__(self,valor):
        soma = 0
        if valor == 0:
            return self.coefs[0]
        else:
            for i in range(len(self.coefs)):
                if i == 0:
                    soma = soma+self.coefs[i]
                else:
                    soma = soma + self.coefs[i]*(valor**i)
        return soma
    
    def __add__(self,other):
        if type(other) != int and type(other)!=float:
            x = len(self.coefs)
            y = len(other.coefs)
            polinomio = []
            if x < y:
                for i in range(x):
                    polinomio.append(self.coefs[i]+other.coefs[i])
                for j in range(x,y):
                    polinomio.append(other.coefs[j])
                return Polinomio(polinomio)
            elif y<x:
                for i in range(y):
                    polinomio.append(self.coefs[i]+other.coefs[i])
                for j in range(y,x):
                    polinomio.append(self.coefs[j])
                return Polinomio(polinomio)
            else:
                for i in range(x):
                    polinomio.append(self.coefs[i]+other.coefs[i])
                booleano = verifica(polinomio)
                if booleano == True:
                    return Polinomio([])
                return Polinomio(polinomio)
        else:
            polinomio = []
            x = self.coefs[0]+other
            polinomio.append(x)
            for i in range(1,len(self.coefs)):
                polinomio.append(self.coefs[i])
            booleano = verifica(polinomio)
            if booleano == True:
                return Polinomio([])
            return Polinomio(polinomio)
    
    def __radd__(self,other):
        if type(other)!= int and type(other)!=float:
            x = len(self.coefs)
            y = len(other.coefs)
            polinomio = []
            if x < y:
                for i in range(x):
                    polinomio.append(self.coefs[i]+other.coefs[i])
                for j in range(x+1,y):
                    polinomio.append(other.coefs[j])
                return Polinomio(polinomio)
            elif y<x:
                for i in range(y):
                    polinomio.append(self.coefs[i]+other.coefs[i])
                for j in range(y+1,x):
                    polinomio.append(self.coefs[j])
                return Polinomio(polinomio)
            else:
                for i in range(x):
                    polinomio.append(self.coefs[i]+other.coefs[i])
                booleano = verifica(polinomio)
                if booleano == True:
                    return Polinomio([])
                return Polinomio(polinomio)
        else:
            polinomio = []
            x = self.coefs[0]+other
            polinomio.append(x)
            for i in range(1,len(self.coefs)):
                polinomio.append(self.coefs[i])
            booleano = verifica(polinomio)
            if booleano == True:
                return Polinomio([])
            return Polinomio(polinomio)
    
    def __sub__(self,other):
        if type(other) != int and type(other)!=float:
            x = len(self.coefs)
            y = len(other.coefs)
            polinomio = []
            if x < y:
                for i in range(x):
                    polinomio.append(self.coefs[i]-other.coefs[i])
                for j in range(x,y):
                    polinomio.append((-1)*other.coefs[j])
                return Polinomio(polinomio)
            elif y<x:
                for i in range(y):
                    polinomio.append(self.coefs[i]-other.coefs[i])
                for j in range(y,x):
                    polinomio.append(self.coefs[j])
                return Polinomio(polinomio)
            else:
                for i in range(x):
                    polinomio.append(self.coefs[i]-other.coefs[i])
                booleano = verifica(polinomio)
                if booleano == True:
                    return Polinomio([])
                return Polinomio(polinomio)
        else:
            polinomio = []
            x = self.coefs[0]-other
            polinomio.append(x)
            for i in range(1,len(self.coefs)):
                polinomio.append(self.coefs[i])
            booleano = verifica(polinomio)
            if booleano == True:
                return Polinomio([])
            return Polinomio(polinomio)
    
    def __mul__(self,other):
        if type(other)!=int and type(other)!=float:
            z = Polinomio(self.coefs).grau()+Polinomio(other.coefs).grau()
            polinomio = []
            for i in range(0,z+1):
                soma = 0
                for j in range(len(self.coefs)):
                    for l in range(len(other.coefs)):
                        if j+l == i:
                            soma = soma + self.coefs[j]*other.coefs[l]
                polinomio.append(soma)
            return Polinomio(polinomio)
        else:
            polinomio = []
            for i in self.coefs:
                polinomio.append(i*other)
            booleano = verifica(polinomio)
            if booleano == True:
                return Polinomio([])
            return Polinomio(polinomio)
    
    def __rmul__(self,other):
        if type(other)!=int and type(other)!=float:
            z = Polinomio(self.coefs).grau()+Polinomio(other.coefs).grau()
            polinomio = []
            for i in range(0,z+1):
                soma = 0
                for j in range(len(self.coefs)):
                    for l in range(len(other.coefs)):
                        if j+l == i:
                            soma = soma + self.coefs[j]*other.coefs[l]
                polinomio.append(soma)
            return Polinomio(polinomio)
        else:
            polinomio = []
            for i in self.coefs:
                polinomio.append(i*other)
            booleano = verifica(polinomio)
            if booleano == True:
                return Polinomio([])
            return Polinomio(polinomio)
    
    def coeficientes(self):
        for i in range(len(self.coefs)):
            print(self.coefs[-i-1])
            if self.coefs[-i-1]!=0:
                if -i-1 == -1 :
                    lista = self.coefs[:]
                    self.coefs = lista
                    break
                else:
                    lista = self.coefs[:-i]
                    self.coefs = lista
                    break
        return self.coefs

    def grau(self):
        if len(self.coefs) == 0:
            return 0
        return len(self.coefs) - 1
    
    def derive(self):
        g = self.grau()
        if g <= 0:
            return Polinomio([])
        x = []
        for i in range(len(self.coefs)):
            x.append(self.coefs[i]*i)
        del(x[0])
        return Polinomio(x)



    
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

        Minha colega Maria me explicou que eu devia utilizar a função int() 
        quando fazemos leitura de números inteiros.

        No fórum escreveram para usar a função ...

        A minha solução foi baseada na descrição encontrada na 
        página https://stackoverflow.com/questions/15976333/

    Descrição de ajuda ou indicação de fonte:
'''
def boleano(lista):
    for i in lista:
        if 0<= i:
            return False
    return True
#------------------------------------------------------------
class Revendedora:
    ''' Recebe uma lista estoque com os comprimentos de rolos 
        disponíveis e atende pedidos fazendo controle desse 
        estoque.
    '''
    def __init__(self,estoque):
        self.estoque = estoque
        self.lista = []
        self.dicionario = {}
        for i in range(len(self.estoque)):
            self.lista.append(i)
            self.dicionario[-len(self.estoque)+i] = i
    def __str__(self):
        rolos = len(self.estoque)
        x = 'Estoque possui %d rolos:\n' %(rolos)
        for i in range(len(self.estoque)):
            x = x +'   '+'rolo %d: %d m\n' %(i,self.estoque[i])
        return x
    
    def atenda_encomenda(self,encomenda):
        x = boleano(encomenda)
        if x == True:
            print('Entrei, deu tudo negativo')
            print(encomenda)
            print()
            print('Dicionario que usarei:')
            print(self.dicionario)
            print()
            for i in range(len(encomenda)):
                encomenda[i] = self.dicionario[encomenda[i]]
            return encomenda
        else:
            for i in range(len(self.estoque)):
                for j in range(len(encomenda)):
                    if 0<= self.estoque[-1-i] - encomenda[j] and 0<=encomenda[j]:
                        y = encomenda[j]
                        self.estoque[-1-i] = self.estoque[-1-i] - encomenda[j]
                        encomenda[j] = -1-i
                        x = Revendedora(self.estoque).atenda_encomenda(encomenda)
                        if type(x) == list:
                            return x
                        else:
                            encomenda[j] = y
                            self.estoque[-1-i] = self.estoque[-1-i]+encomenda[j]
            return

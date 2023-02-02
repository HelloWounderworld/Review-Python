# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

'''

    Nome: Leonardo Takashi Teramatsu
    NUSP: 9797083

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
#-------------------------------------------------------------------------- 
def cria_imagem(n,m,p):
    x = []
    for i in range(n):
        y = []
        for j in range(m):
            y.append(p)
        x.append(y)
    return x

def clona_imagem(lista):
    x = []
    for i in range(len(lista)):
        y = []
        for j in range(len(lista[i])):
            y.append(lista[i][j])
        x.append(y)
    return x

def recorta_imagem(lista,n,m,p,q):
    x = []
    for i in range(n,p):
        y = []
        for j in range(m,q):
            y.append(lista[i][j])
        x.append(y)
    return x

def show(lista): #coloca dentro de __str__
    x = str()
    for i in range(len(lista)):
        y = str()
        for j in range(len(lista[i])):
            if j == (len(lista[i]) - 1):
                y = y + str(lista[i][j])
            else:
                y = y + str(lista[i][j]) + ',' + ' '
        x = x + y + '\n'
    return x

class Pymagem:
    '''
    Implementação da classe Pymagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''

    # escreva aqui os métodos da classe Pymagem
    def __init__(self,nlins,ncolns,valor=0):
        self.nlins = nlins
        self.ncolns = ncolns
        self.valor = valor
        self.tricks = cria_imagem(self.nlins,self.ncolns,self.valor)
        self.lista_assistente = []   
        
    def __str__(self):
        if len(self.tricks) == 0:
            return show(self.lista_assistente)
        return show(self.tricks)

    def size(self):
        return self.nlins , self.ncolns

    def get(self,lin,col):
        lista = self.tricks
        posicao = lista[lin][col]
        return posicao

    def put(self,lin,col,valor):
        self.tricks[lin][col] = valor
        return self.tricks
    
    def recorta_imagem(self,lista,n,m,p,q):
        x = []
        for i in range(n,p):
            y = []
            for j in range(m,q):
                y.append(lista[i][j])
            x.append(y)
        return x

    def crop(self,n=0,m=0,p=0,q=0):
        if n==0 and m==0 and p==0 and q==0:
            self.tricks = clona_imagem(self.tricks)
            return Pymagem(len(self.tricks),len(self.tricks[0]),self.tricks[0][0])
        else:
            img_nova = Pymagem(p-n,q-m)
            for i in range(n,p):
                for j in range(m,q):
                    img_nova.put(i-n,j-m,self.tricks[i][j])
            return img_nova

'''
Nota
Revisado em domingo, 18 ago 2019, 02:36 por Atribuição automática de nota
grade: 9,0 / 10,0

Relatório de avaliação[-]
__init__(): iniciando avaliação dos testes (vale 3 ponto(s))
__init__() passou em todos os testes :-)
__init__(): avaliação encerrada... (nota 3)

__str__(): iniciando avaliação dos testes (vale 1 ponto(s))
__str__() passou em todos os testes :-)
__str__(): avaliação encerrada... (nota 1)

size(): iniciando avaliação dos testes (vale 1 ponto(s))
size() passou em todos os testes :-)
size(): avaliação encerrada... (nota 1)

put(): iniciando avaliação dos testes (vale 1.5 ponto(s))
put() passou em todos os testes :-)
put(): avaliação encerrada... (nota 1.5)

get(): iniciando avaliação dos testes (vale 1.5 ponto(s))
get() passou em todos os testes :-)
get(): avaliação encerrada... (nota 1.5)

crop(): iniciando avaliação dos testes (vale 2 ponto(s))
Pymagem(4, 5, 0).crop(2, 1) retornou Pymagem de size (-2, -1).
Pymagem(4, 5, 0).crop().get(0,1) retornou 11
crop() não passou no(s) teste(s) acima
crop(): avaliação encerrada... (nota 1.0)

Seu programa não passou no(s) teste(s) acima. :-(

Fim da avaliação.
'''



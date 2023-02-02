# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

'''

    Nome:Leonardo Takashi Teramatsu
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

    def __init__(self,nlins,ncolns,valor=0):
        self.nlins = nlins
        self.ncolns = ncolns
        self.valor = valor
        self.tricks = cria_imagem(self.nlins,self.ncolns,self.valor)
              

    def __str__(self):
        return show(self.tricks)
    
    def __add__(self,other):
        x = []
        for i in range(len(self.tricks)):
            y = []
            for j in range(len(self.tricks[i])):
                y.append(self.tricks[i][j]+other.tricks[i][j])
            x.append(y)
        img_nova = Pymagem(len(x),len(x[0]))
        for i in range(len(x)):
            for j in range(len(x[i])):
                img_nova.put(i,j,x[i][j])
        return img_nova
    
    def __mul__(self,alfa):
        x = []
        for i in range(len(self.tricks)):
            y = []
            for j in range(len(self.tricks[i])):
                z = self.tricks[i][j]*alfa - int(self.tricks[i][j]*alfa)
                w = z*100 - int((z*10))*10
                if w >= 5:
                    z = (int(z*10) + 1)/10
                    t = int(self.tricks[i][j]*alfa) + z
                    y.append(t)
                else:
                    z = (int(z*10))/10
                    t = int(self.tricks[i][j]*alfa) + z
                    y.append(t)
            x.append(y)
        img_nova = Pymagem(len(x),len(x[0]))
        for i in range(len(x)):
            for j in range(len(x[i])):
                img_nova.put(i,j,x[i][j])
        return img_nova
    
    def paste(self,other,tlin,tcol):
        n,m = other.size()
        for i in range(n):
            for j in range(m):
                self.tricks[tlin+i][tcol+j] = other.get(i,j)
        return self.tricks
    
    def pinte_disco(self,lin,col,raio,val):
        for i in range(lin-raio,lin+raio+1):
            for j in range(col-raio, col+raio+1):
                if 0<=i<=(len(self.tricks)-1) and 0 <= j <= (len(self.tricks[i])-1):
                    if ((i-lin)**2+(j-col)**2)<raio**2:
                        self.tricks[i][j] = val
        return self.tricks
                    
    
    def pinte_retangulo(self,tlx=0,tly=0,brx=0,bry=0,val=0):
        for i in range(tlx,brx):
            for j in range(tly,bry):
                if (0<= i < len(self.tricks)) and (0<= j <len(self.tricks[i])):
                    self.tricks[i][j] = val
        return self.tricks
    
    def size(self):
        return self.nlins , self.ncolns
    
    def get(self,lin,col):
        lista = self.tricks
        posicao = lista[lin][col]
        return posicao
    
    def put(self,lin,col,valor):
        self.tricks[lin][col] = valor
        return self.tricks

    def crop(self,n=0,m=0,p=0,q=0):
        if n==0 and m==0 and p==0 and q==0:
            clone = clona_imagem(self.tricks)
            return Pymagem(len(clone),len(clone[0]),clone[0][0])
        else:
            if p<n or q<m :
                img_nova = Pymagem(len(self.tricks)-n,len(self.tricks[0])-m)
                for i in range(n,len(self.tricks)):
                    for j in range(m,len(self.tricks[i])):
                        img_nova.put(i-n,j-m,self.tricks[i][j])
                return img_nova
            img_nova = Pymagem(p-n,q-m)
            for i in range(n,p):
                for j in range(m,q):
                    img_nova.put(i-n,j-m,self.tricks[i][j])
            return img_nova
      
    
'''
Nota
Revisado em domingo, 25 ago 2019, 21:23 por Atribuição automática de nota
grade: 8,5 / 10,0

Relatório de avaliação[-]
__init__(): iniciando avaliação dos testes (vale 0.5 ponto(s))
__init__() passou em todos os testes :-)
__init__(): avaliação encerrada... (nota 0.5)

__str__(): iniciando avaliação dos testes (vale 0.5 ponto(s))
__str__() passou em todos os testes :-)
__str__(): avaliação encerrada... (nota 0.5)

size(): iniciando avaliação dos testes (vale 0.5 ponto(s))
size() passou em todos os testes :-)
size(): avaliação encerrada... (nota 0.5)

put(): iniciando avaliação dos testes (vale 0.5 ponto(s))
put() passou em todos os testes :-)
put(): avaliação encerrada... (nota 0.5)

get(): iniciando avaliação dos testes (vale 0.5 ponto(s))
get() passou em todos os testes :-)
get(): avaliação encerrada... (nota 0.5)

crop(): iniciando avaliação dos testes (vale 0.5 ponto(s))
Pymagem(4, 5, 0).crop().get(0,1) retornou 11
crop() não passou no(s) teste(s) acima
crop(): avaliação encerrada... (nota 0.0)

__add__(): iniciando avaliação dos testes (vale 1.5 ponto(s))
__add__() passou em todos os testes :-)
__add__(): avaliação encerrada... (nota 1.5)

__mul__(): iniciando avaliação dos testes (vale 1.5 ponto(s))
__mul__() passou em todos os testes :-)
__mul__(): avaliação encerrada... (nota 1.5)

paste(): iniciando avaliação dos testes (vale 1.5 ponto(s))
AVISO: Pymagem(4, 4, 0).paste(Pymagem(2, 2, 1),1,1) devia retornar None (método é mutador), retornou: <class 'list'>
AVISO: Pymagem(4, 4, 0).paste(Pymagem(2, 2, 1),0,0) devia retornar None (método é mutador), retornou: <class 'list'>
Pymagem(4, 4, 0).paste(Pymagem(2, 2, 1),0,3) explodiu.
Pymagem(4, 4, 0).paste(Pymagem(2, 2, 1),3,0) explodiu.
Pymagem(4, 4, 0).paste(Pymagem(2, 2, 1),3,3) explodiu.
Pymagem(2, 2, 1).paste(Pymagem(4, 4, 0),-1,-1) explodiu.
AVISO: Pymagem(3, 1, 1).paste(Pymagem(3, 1, 0),0,0) devia retornar None (método é mutador), retornou: <class 'list'>
paste() não passou no(s) teste(s) acima
paste(): avaliação encerrada... (nota 0)

pinte_disco(): iniciando avaliação dos testes (vale 1.5 ponto(s))
AVISO: Pymagem(5, 5, 0).pinte_disco(2, 2, 1, 1) devia retornar None (método é mutador), retornou: <class 'list'>
AVISO: Pymagem(5, 5, 0).pinte_disco(2, 2, 2, 1) devia retornar None (método é mutador), retornou: <class 'list'>
AVISO: Pymagem(5, 5, 0).pinte_disco(2, 2, 3, 1) devia retornar None (método é mutador), retornou: <class 'list'>
AVISO: Pymagem(5, 5, 0).pinte_disco(-1, -1, 2, 1) devia retornar None (método é mutador), retornou: <class 'list'>
AVISO: Pymagem(5, 5, 0).pinte_disco(-1, 5, 2, 1) devia retornar None (método é mutador), retornou: <class 'list'>
AVISO: Pymagem(5, 5, 0).pinte_disco(5, -1, 2, 1) devia retornar None (método é mutador), retornou: <class 'list'>
AVISO: Pymagem(5, 5, 0).pinte_disco(5, 5, 2, 1) devia retornar None (método é mutador), retornou: <class 'list'>
AVISO: Pymagem(1, 5, 0).pinte_disco(-1, 2, 3, 1) devia retornar None (método é mutador), retornou: <class 'list'>
AVISO: Pymagem(5, 1, 0).pinte_disco(2, 1, 3, 1) devia retornar None (método é mutador), retornou: <class 'list'>
pinte_disco() passou em todos os testes :-)
pinte_disco(): avaliação encerrada... (nota 1.5)

pinte_retangulo(): iniciando avaliação dos testes (vale 1.5 ponto(s))
AVISO: Pymagem(5, 5, 0).pinte_retangulo(1, 1, 3, 3, 1) devia retornar None (método é mutador), retornou: <class 'list'>
AVISO: Pymagem(5, 5, 0).pinte_retangulo(0, 0, 4, 4, 1) devia retornar None (método é mutador), retornou: <class 'list'>
AVISO: Pymagem(5, 5, 0).pinte_retangulo(0, 0, 5, 5, 1) devia retornar None (método é mutador), retornou: <class 'list'>
AVISO: Pymagem(5, 5, 0).pinte_retangulo(-1, -1, 5, 5, 1) devia retornar None (método é mutador), retornou: <class 'list'>
AVISO: Pymagem(5, 5, 0).pinte_retangulo(4, 0, 5, 4, 1) devia retornar None (método é mutador), retornou: <class 'list'>
AVISO: Pymagem(5, 5, 0).pinte_retangulo(4, 4, 5, 5, 1) devia retornar None (método é mutador), retornou: <class 'list'>
AVISO: Pymagem(5, 5, 0).pinte_retangulo(0, 4, 1, 5, 1) devia retornar None (método é mutador), retornou: <class 'list'>
AVISO: Pymagem(1, 5, 0).pinte_retangulo(0, 0, 1, 5, 1) devia retornar None (método é mutador), retornou: <class 'list'>
AVISO: Pymagem(5, 1, 0).pinte_retangulo(0, 0, 5, 1, 1) devia retornar None (método é mutador), retornou: <class 'list'>
pinte_retangulo() passou em todos os testes :-)
pinte_retangulo(): avaliação encerrada... (nota 1.5)

Seu programa não passou no(s) teste(s) acima. :-(

Fim da avaliação.
'''
    


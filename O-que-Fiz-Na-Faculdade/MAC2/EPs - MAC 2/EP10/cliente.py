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

        A monitora me explicou que eu devia utilizar a função 
        split(), strip(), map() e filter() para leitura dos dados
        no arquivo.

    Descrição de ajuda ou indicação de fonte:

'''

class Cliente:
    '''
        Siga as especificações do enunciado para 
        construir a classe Cliente.

        Coloque o seu código a seguir.
    '''
    def __init__(self,nome):
        self.nome = nome
        self.classificacao = {}
        self.lista = []
    
    def put_classificacao(self,filmes):
        for i in range(len(filmes)):
            self.classificacao[i] = filmes[i]
    
    def __str__(self):
        x = self.nome+'\n'
        for i in range(len(self.classificacao)):
            x = x + '%d: %s\n' %(i,self.classificacao[i])
        return x
    
    def get_nome(self):
        return self.nome
    
    def get_classificacao(self):
        for i in range(len(self.classificacao)):
            self.lista.append(self.classificacao[i])
        return self.lista
    
    def distancia(self,other):
        if self.lista == other.lista:
            return 0
        else:
            lista_modelo = {}
            lista_compara = []
            ordem = 0
            for i in range(len(self.lista)):
                if self.lista[i] in other.lista:
                    lista_modelo[self.lista[i]] = ordem
                    ordem += 1
            for j in range(len(other.lista)):
                if other.lista[j] in lista_modelo:
                    lista_compara.append(lista_modelo[other.lista[j]])
            if len(lista_modelo) == 1 or len(lista_modelo) == 2:
                return 0
            else:
                transposicao = 0
                for i in range(0,len(lista_compara)):
                    for j in range(0,len(lista_compara)-1):
                        if lista_compara[j] > lista_compara[j+1]:
                            x = lista_compara[j+1]
                            lista_compara[j+1] = lista_compara[j]
                            lista_compara[j] = x
                            transposicao += 1
                return transposicao
    
    


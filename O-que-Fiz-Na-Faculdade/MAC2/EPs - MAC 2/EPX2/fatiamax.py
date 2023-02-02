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
    monitores e colegas). Com exceção de material de MAC0122, 
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

#--------------------------------------------------------
def fatia_max(p, r, v):
    '''(int, int, list) -> int, int, int

    RECEBE uma lista v[p:r] de números inteiros e RETORNA
    valores inteiros soma_max, e, d tais que

        soma_max == sum(v[e,d]) é a maior soma de uma fatia 
        v[i:j] com p <= i <= j <= r.
    '''
    soma_parcial = [0]
    for i in range(p,r):
        soma_parcial.append(soma_parcial[i-p]+v[i])
    soma_max = soma_parcial[-1]-soma_parcial[0]
    nlin, ncol = p, r
    for i in range(p,r+1):
        for j in range(p,i+1):
            soma = soma_parcial[i-p] - soma_parcial[j-p]
            if soma_max < soma:
                soma_max = soma
                nlin, ncol = j, i
    return soma_max, nlin, ncol
#--------------------------------------------------------
def fatia_max_meio(p, q, r, v):
    '''(int, int, int, list) -> int, int, int

    RECEBE números inteiros p < q < r e uma lista v[p:r] de 
    números inteiros e RETORNA valores inteiros 
    soma_max, e, d tais que 

        soma_max==sum(v[e:d]) é a maior soma de uma fatia 
        v[i:j] com p <= i < q < j <= r.
    '''
    soma_parcial = {0:0}
    for i in range(len(v)):
        soma_parcial[i+1] = soma_parcial[i] + v[i]
    soma_max1 = soma_parcial[q] - soma_parcial[p]
    soma_max2 = soma_parcial[r] - soma_parcial[q]
    nlin1 = p
    ncol2 = r
    for j in range(p,q):
        soma = soma_parcial[q] - soma_parcial[j]
        if soma_max1 < soma:
            soma_max1 = soma
            nlin1 = j
    for l in range(q+1,r+1):
        soma = soma_parcial[l] - soma_parcial[q]
        if soma_max2 < soma:
            soma_max2 = soma
            ncol2 = l
    soma_max = soma_max1 + soma_max2
    return soma_max, nlin1, ncol2

#--------------------------------------------------------
def fatia_max_div_conq(p, r, v):
    '''(int, int, list) -> int, int, int

    RECEBE uma lista lista v[p:r] de números inteiros e RETORNA
    valores inteiros soma_max, e, d tais que

        soma_max == sum(v[e,d]) é a maior soma de uma fatia 
        v[i:j] com p <= i <= j <= r.
    '''
    soma_parcial = [0]
    for i in range(p,r):
        soma_parcial.append(soma_parcial[i-p]+v[i])
    soma_max = soma_parcial[-1]-soma_parcial[0]
    nlin, ncol = p, r
    for i in range(p,r+1):
        for j in range(p,i+1):
            soma = soma_parcial[i-p] - soma_parcial[j-p]
            if soma_max < soma:
                soma_max = soma
                nlin, ncol = j, i
    return soma_max, nlin, ncol


'''
Nota
Revisado em quarta, 6 nov 2019, 16:15 por Atribuição automática de nota
grade: 9,5 / 10,0
Final reduction: 0 [1 / 15 -0.5] Ajuda com Final reduction
Relatório de avaliação[-]
avaliador: criando lista auxiliar com 32768 inteiros...
avaliador: lista criada...
fatia_max(): iniciando avaliação dos testes (vale 4 ponto(s))
consumo de tempo:
n fatia_max T(2n)/T(n)
256 0.01s -
512 0.03s 3.58
1024 0.13s 4.41
2048 0.51s 4.04
4096 2.30s 4.52
8192 8.55s 3.72
16384 34.66s 4.05
consumo de tempo observado de fatia_max() foi O(n^{2})
fatia_max() passou em todos os testes :-)
fatia_max(): avaliação encerrada... (nota 4)

fatia_max_meio(): iniciando avaliação dos testes (vale 3 ponto(s))
consumo de tempo:
n fatia_max_meio T(2n)/T(n)
256 0.02s -
512 0.01s 0.80
1024 0.01s 0.82
2048 0.01s 1.04
4096 0.01s 1.28
8192 0.01s 0.88
16384 0.02s 1.23
32768 0.02s 1.18
consumo de tempo observado de fatia_max_meio() foi O(n^{0.045})
fatia_max_meio() passou em todos os testes :-)
fatia_max_meio(): avaliação encerrada... (nota 3)

fatia_max_div_conq(): iniciando avaliação dos testes (vale 3 ponto(s))
consumo de tempo:
n fatia_max_div_conq T(2n)/T(n)
256 0.01s -
512 0.03s 3.83
1024 0.14s 4.53
2048 0.53s 3.82
4096 2.34s 4.45
fatia_max_div_conq(0,8192,v) entrou em loop ou não tem consumo de tempo O(n lg n).
fatia_max_div_conq() não passou no(s) teste(s) acima
fatia_max_div_conq(): avaliação encerrada... (nota 2.5)

Seu programa não passou no(s) teste(s) acima. :-(

Fim da avaliação.
'''







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

class MarkovModel:
    def __init__(self,k,corpus):
        self.k = k
        self.corpus = corpus
        self.anagrama = {}
        self.simbolos = {}
    
    def __str__(self):
        self.simbolos = {}
        cobaia = []
        for i in range(len(self.corpus)):
            if self.corpus[i] not in cobaia:
                cobaia.append(self.corpus[i])
        cobaia.sort()
        for i in range(len(cobaia)):
            self.simbolos[cobaia[i]] = i
        d = {}
        for j in range(self.k,self.k+2):
            word = self.corpus+self.corpus[:j]
            for l in range(0,len(word)-j):
                p = word[l:l+j]
                if p not in d:
                    d[p] = 1
                else:
                    d[p] += 1
        for i in range(self.k,self.k+2):
            ordem = []
            for j in d:
                if len(j) == i:
                    ordem.append(j)
            ordem.sort()
            for l in ordem:
                self.anagrama[l] = d[l]
        x = 'alfabeto tem %d simbolos\n' %(len(self.simbolos))
        for r in self.anagrama:
            x = x+'"%s"' %(r) + '  %d\n' %(self.anagrama[r])
        return x
    
    def alphabet(self):
        x = str()
        for i in self.simbolos:
            x = x + i
        return x
    
    def N(self,t):
        if t not in self.anagrama:
            return
        return self.anagrama[t]
    
    def laplace(self,t):
        if t not in self.anagrama:
            if t[:len(t)-1] not in self.anagrama:
                return 1/len(self.simbolos)
            return 1/(self.anagrama[t[:len(t)-1]]+len(self.simbolos))
        elif t[:len(t)-1] not in self.anagrama:
            return (self.anagrama[t]+1)/len(self.simbolos)
        return (self.anagrama[t]+1)/(self.anagrama[t[:len(t)-1]]+len(self.simbolos))
    
'''
Nota
Revisado em quarta, 6 nov 2019, 16:10 por Atribuição automática de nota
grade: 9,5 / 10,0

Relatório de avaliação[-]
MarkovMode(2, 'aabcabaacaac'): iniciando avaliação (vale 2 ponto(s))
__str__() não retornou string esperada: 'alfabeto tem 3 simbolos\n"aa" 3\n"ab" 2\n"ac" 2\n"ba" 1\n"bc" 1\n"ca" 3\n"aab" 1\n"aac" 2\n"aba" 1\n"abc" 1\n"aca" 2\n"baa" 1\n"bca" 1\n"caa" 2\n"cab" 1'
não passou no(s) teste(s) acima
MarkovMode(2, 'aabcabaacaac'): avaliação encerrada... (nota 1.9)

MarkovMode(4, 'babababaabababaabaabaaaaaababaaaab'): iniciando avaliação (vale 2 ponto(s))
__str__() não retornou string esperada: 'alfabeto tem 2 simbolos\n"aaaa" 4\n"aaab" 2\n"aaba" 4\n"aabb" 1\n"abaa" 5\n"abab" 5\n"abba" 1\n"baaa" 2\n"baab" 3\n"baba" 6\n"bbab" 1\n"aaaaa" 2\n"aaaab" 2\n"aaaba" 1\n"aaabb" 1\n"aabaa" 2\n"aabab" 2\n"aabba" 1\n"abaaa" 2\n"abaab" 3\n"ababa" 5\n"abbab" 1\n"baaaa" 2\n"baaba" 3\n"babaa" 3\n"babab" 3\n"bbaba" 1'
não passou no(s) teste(s) acima
MarkovMode(4, 'babababaabababaabaabaaaaaababaaaab'): avaliação encerrada... (nota 1.9)

MarkovMode(0, 'Como é bom estudar MAC0122!'): iniciando avaliação (vale 2 ponto(s))
__str__() não retornou string esperada: 'alfabeto tem 19 simbolos\n"" 27\n" " 4\n"!" 1\n"0" 1\n"1" 1\n"2" 2\n"A" 1\n"C" 2\n"M" 1\n"a" 1\n"b" 1\n"d" 1\n"e" 1\n"m" 2\n"o" 3\n"r" 1\n"s" 1\n"t" 1\n"u" 1\n"é" 1'
não passou no(s) teste(s) acima
MarkovMode(0, 'Como é bom estudar MAC0122!'): avaliação encerrada... (nota 1.9)

MarkovMode(1, 'abcdefghijklmnopqrstuvwxyz'): iniciando avaliação (vale 2 ponto(s))
__str__() não retornou string esperada: 'alfabeto tem 26 simbolos\n"a" 1\n"b" 1\n"c" 1\n"d" 1\n"e" 1\n"f" 1\n"g" 1\n"h" 1\n"i" 1\n"j" 1\n"k" 1\n"l" 1\n"m" 1\n"n" 1\n"o" 1\n"p" 1\n"q" 1\n"r" 1\n"s" 1\n"t" 1\n"u" 1\n"v" 1\n"w" 1\n"x" 1\n"y" 1\n"z" 1\n"ab" 1\n"bc" 1\n"cd" 1\n"de" 1\n"ef" 1\n"fg" 1\n"gh" 1\n"hi" 1\n"ij" 1\n"jk" 1\n"kl" 1\n"lm" 1\n"mn" 1\n"no" 1\n"op" 1\n"pq" 1\n"qr" 1\n"rs" 1\n"st" 1\n"tu" 1\n"uv" 1\n"vw" 1\n"wx" 1\n"xy" 1\n"yz" 1\n"za" 1'
não passou no(s) teste(s) acima
MarkovMode(1, 'abcdefghijklmnopqrstuvwxyz'): avaliação encerrada... (nota 1.9)

MarkovMode(5, 'xxxxxxxxxxxxxxxxxxx'): iniciando avaliação (vale 2 ponto(s))
__str__() não retornou string esperada: 'alfabeto tem 1 simbolos\n"xxxxx" 19\n"xxxxxx" 19'
não passou no(s) teste(s) acima
MarkovMode(5, 'xxxxxxxxxxxxxxxxxxx'): avaliação encerrada... (nota 1.9)

Seu programa não passou no(s) teste(s) acima. :-(

Fim da avaliação.
'''
    
    
    

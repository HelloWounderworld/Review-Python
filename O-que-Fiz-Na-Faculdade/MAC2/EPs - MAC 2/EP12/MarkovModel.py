


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
            x = x+'"%s"' %(r) + '%d\n' %(self.anagrama[r])
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
            return 1/(self.anagrama[t[:len(t)-1]]+len(self.simbolos))
        return (self.anagrama[t]+1)/(self.anagrama[t[:len(t)-1]]+len(self.simbolos))
    
def main():
    print('Testando __init__()')
    corpus1 = "aabcabaacaac"
    corpus2 = "babababaabababaabaabaaaaaababaaaab"
    corpus3 = "Como é bom estudar MAC0122!"
    modelo1 = MarkovModel(2, corpus1)
    modelo2 = MarkovModel(4, corpus2)
    modelo3 = MarkovModel(0, corpus3)
    print()
    print('Testando __str__()')
    '''
    esses três primeiros e para testar no compilador
    '''
    str1 = str(modelo1)
    str2 = str(modelo2)
    str3 = str(modelo3)
    print(str1)
    print()
    print(str2)
    print()
    print(str3)
    print()
    print('Testando alphabet')
    alfabeto1 = modelo1.alphabet()
    alfabeto2 = modelo2.alphabet()
    alfabeto3 = modelo3.alphabet()
    print(alfabeto1)
    print()
    print(alfabeto2)
    print()
    print(alfabeto3)
    print()
    print('Testando N')
    print()
    print(modelo1.N("aa"))
    print()
    print(modelo1.N("aab"))
    print()
    print(modelo1.N("aac"))
    print()
    print(modelo1.N("aaa"))
    print()
    print(modelo1.N("aaaa"))
    print()
    print(modelo1.N("a"))
    print()
    print('Teste laplace')
    print()
    print(modelo1.laplace("aaa"))
    print()
    print(modelo1.laplace("aab"))
    print()
    print(modelo1.laplace("aac"))
    print()
    p = 0
    for c in modelo1.alphabet():
        p += modelo1.laplace("aa"+c)
    print(p)
    print()
    p = 0
    for c in modelo1.alphabet():
        p += modelo1.laplace("ab"+c)
    print(p)
    print()
    p = 0
    for c in modelo2.alphabet():
        p += modelo2.laplace("aaaa"+c)
    print(p)
    print()
    p = 0
    for c in modelo3.alphabet():
        p += modelo3.laplace(c)
    print(p)
main()
    
'''
__init__()

Python 3.6.3 |Anaconda, Inc.| (default, Oct 13 2017, 12:02:49) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from markov_model import MarkovModel
>>> corpus1 = "aabcabaacaac"
>>> corpus2 = "babababaabababaabaabaaaaaababaaaab"
>>> corpus3 = "Como é bom estudar MAC0122!"
>>> modelo1 = MarkovModel(2, corpus1)
>>> modelo2 = MarkovModel(4, corpus2)
>>> modelo3 = MarkovModel(0, corpus3)

__str__()

>>> str1 = str(modelo1)
>>> str2 = str(modelo2)
>>> str3 = str(modelo3)
>>> str1
'alfabeto tem 3 símbolos\n"aa"   3\n"ab"   2\n"ac"   2\n"ba"   1\n"bc"   1\n"ca"   3\n"aab"  1\n"aac"  2\n"aba"  1\n"abc"  1\n"aca"  2\n"baa"  1\n"bca"  1\n"caa"  2\n"cab"  1\n'
>>> print(str1)
alfabeto tem 3 símbolos
"aa"   3
"ab"   2
"ac"   2
"ba"   1
"bc"   1
"ca"   3
"aab"  1
"aac"  2
"aba"  1
"abc"  1
"aca"  2
"baa"  1
"bca"  1
"caa"  2
"cab"  1

>>> print(str2)
alfabeto tem 2 símbolos
"aaaa"   4
"aaab"   2
"aaba"   4
"aabb"   1
"abaa"   5
"abab"   5
"abba"   1
"baaa"   2
"baab"   3
"baba"   6
"bbab"   1
"aaaaa"  2
"aaaab"  2
"aaaba"  1
"aaabb"  1
"aabaa"  2
"aabab"  2
"aabba"  1
"abaaa"  2
"abaab"  3
"ababa"  5
"abbab"  1
"baaaa"  2
"baaba"  3
"babaa"  3
"babab"  3
"bbaba"  1

>>> print(str3)
alfabeto tem 19 símbolos
""   27
" "  4
"!"  1
"0"  1
"1"  1
"2"  2
"A"  1
"C"  2
"M"  1
"a"  1
"b"  1
"d"  1
"e"  1
"m"  2
"o"  3
"r"  1
"s"  1
"t"  1
"u"  1
"é"  1

alphabet()

>>> alfabeto1 = modelo1.alphabet()
>>> alfabeto2 = modelo2.alphabet()
>>> alfabeto3 = modelo3.alphabet()
>>> alfabeto1
'abc'
>>> alfabeto2
'ab'
>>> alfabeto3
' !012ACMabdemorstué'
>>>

N()

>>> modelo1.N("aa")
3
>>> modelo1.N("aab")
1
>>> modelo1.N("aac")
2
>>> modelo1.N("aaa")
>>> modelo1.N("aaaa")
>>> modelo1.N("a")
>>>

laplace()

>>> modelo1.laplace("aaa")
0.16666666666666666
>>> modelo1.laplace("aab")
0.3333333333333333
>>> modelo1.laplace("aac")
0.5
>>> p = 0
>>> for c in modelo1.alphabet():
...     p += modelo1.laplace("aa"+c)
... 
>>> p
1.0
>>> p = 0
>>> for c in modelo1.alphabet():
...     p += modelo1.laplace("ab"+c)
... 
>>> p
1.0
>>> p = 0
>>> for c in modelo2.alphabet():
...     p += modelo2.laplace("aaaa"+c)
... 
>>> p
1.0
>>> p = 0
>>> for c in modelo3.alphabet():
...     p += modelo3.laplace(c) # o mesmo que modelo3.laplace(""+c)
... 
>>> p
0.9999999999999998
>>> 
'''






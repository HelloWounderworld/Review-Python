from markov_model import MarkovModel
import math
import time

class TopModel:
    def __init__(self,k,dict_corpora):
        self.k = k
        self.dict_corpora = dict_corpora
        self.Markov = {}
        self.verossimilhanca = {}
        self.verossimilhanca_average = {}
        self.verossimilhanca_reverse = {}
        self.set = {}
        self.conjunto = set()
        for j in  self.dict_corpora:
            self.Markov[j] = MarkovModel(self.k,self.dict_corpora[j])
            
    
    def __str__(self):
        '''
        Falta alinhar todos os numeros que aparecem enfrente as sequencias de
        palavras que sao computadas dentro das strings
        '''
        n = len(self.dict_corpora)
        x = 'TopModel possui %d modelos:' %(n)
        modelo = list(self.dict_corpora)
        Model = {}
        for i in range(n):  
            Model[i] = modelo[i]
        for j in range(n):
            if j == n-1:
                x = x + '%s\n' %(Model[j])
            else:
                x = x + '%s,' %(Model[j])
        print(self.Markov)
        for l in self.dict_corpora:
            x = x + 'Modelo %s:\n' %(l)
            x = x+str(self.Markov[l])
        return x
    
    def modelo(self,nome_modelo):
        if nome_modelo not in self.dict_corpora:
            '''
            falta exibir uma msg de erro
            '''
            print('modelo(): {} nao foi definido'. format(nome_modelo))
            return 
        p = self.Markov[nome_modelo]
        print(p)
        return p
    
    def verossimilhanca_total(self,nome_modelo,citacao):
        if nome_modelo not in self.dict_corpora:
            print('modelo(): {} nao definido'. format(nome_modelo))
            return 
        conta = 0
        self.conjunto.add(nome_modelo)
        ditado = MarkovModel(self.k,citacao)
        str(ditado)
        self.verossimilhanca_average['media'] = 0
        for j in ditado.anagrama:
            if len(j) == self.k+1:
                conta = conta + math.log(self.Markov[nome_modelo].laplace(j))
                self.verossimilhanca_average['media'] += 1
        self.set[citacao] = self.conjunto
        self.verossimilhanca[nome_modelo] = conta
        return conta
    
    def media_verossimilhanca(self,nome_modelo,citacao):
        if nome_modelo not in self.dict_corpora:
            print('modelo(): {} nao definido'. format(nome_modelo))
            return
        p = self.verossimilhanca[nome_modelo]/self.verossimilhanca_average['media']
        self.verossimilhanca_average[nome_modelo] = p
        self.verossimilhanca_reverse[p] = nome_modelo
        return p
    
    def top_model(self,citacao):
        maior = []
        for i in self.set[citacao]:
            maior.append(self.verossimilhanca_average[i])
        p = max(maior)
        t = self.verossimilhanca_reverse[p]
        return t, p
    
def main():
    print('Teste __init__')
    corpus1  = "aabcabaacaac"
    corpus2  = "babababaabababaabaabaaaaaababaaaab"
    corpus3  = "Como é bom estudar MAC0122!"
    corpus4  = "aaabaaabaaabaaabaaab"
    dicio_corp1 = {"aab...": corpus1, "bab...": corpus2, "mac": corpus3}
    dicio_corp2 = {"aaab...": corpus4}
    auditor1 = TopModel(2, dicio_corp1)
    auditor2 = TopModel(3, dicio_corp2)
    print()
    print('Teste str')
    str_auditor1 = str(auditor1)
    str_auditor2 = str(auditor2)
    print(str_auditor1)
    print()
    print(str_auditor2)
    print()
    print('Teste modelo')
    print()
    
    modelo_aaab = auditor2.modelo("aaab")
    modelo_aaab = auditor2.modelo("aaab.")
    modelo_aaab = auditor2.modelo("aaab...")
    print(modelo_aaab)
    print()
    print('modelo_aaab.laplace("aaab")')
    print(modelo_aaab.laplace("aaab"))
    print()
    print('modelo_aaab.laplace("xxxx")')
    print(modelo_aaab.laplace("xxxx"))
    print()
    print('modelo_aaab.laplace("xxxa")')
    print(modelo_aaab.laplace("xxxa"))
    print()
    p = 0
    print(p)
    for c in modelo_aaab.alphabet():
        p += modelo_aaab.laplace("aaa" + c)
    print(p)
    print()
    print('Teste verossimilhanca_total')
    print()
    citacao = "aabca"
    print(auditor1.verossimilhanca_total("aab...", citacao))
    print()
    print(auditor1.verossimilhanca_total("bba...", citacao))
    print()
    print(auditor1.verossimilhanca_total("bab...", citacao))
    print()
    print(auditor1.verossimilhanca_total("mac", citacao))
    print()
    print(auditor2.verossimilhanca_total("aaab...", citacao))
    print()
    print('Teste media_verossimilhanca')
    print()
    print(auditor1.media_verossimilhanca("aab...", citacao))
    print()
    print(auditor1.media_verossimilhanca("bba...", citacao))
    print()
    print(auditor1.media_verossimilhanca("bab...", citacao))
    print()
    print(auditor1.media_verossimilhanca("mac", citacao))
    print()
    print(auditor2.media_verossimilhanca("mac", citacao))
    print()
    print(auditor2.media_verossimilhanca("aaab...", citacao))
    print()
    print('Teste Top Model')
    print()
    melhor_modelo, media_verossimilhanca = auditor1.top_model(citacao)
    print(melhor_modelo)
    print(media_verossimilhanca)
    print()
    melhor_modelo, media_verossimilhanca = auditor2.top_model(citacao)
    print(melhor_modelo)
    print(media_verossimilhanca)
    print()
    
main()
'''
def main():
    (None) -> None
    print("Programa classificador de autoria")      
    str_arquivos = input("Digite nomes de arquivos com corpus: ")
    lista_nomes_arquivos = str_arquivos.strip().split()
    k = int(input("Digite a ordem do modelo: "))

    #-----------------------------------------------
    # crie o dicionario de corpora
    dicio_corpora = {}
    for nome_arquivo in lista_nomes_arquivos:
        try:
            with open(nome_arquivo, "r", encoding="utf-8") as arq:
                corpus = arq.read()
        except:
            print("main(): arquivo '%s' não encontrado"%nome_arquivo)
            return None
        dicio_corpora[nome_arquivo] = corpus

    #------------------------------------------------
    # crie o objeto TopModel
    print("main(): criando o objeto TopModel...")
    inicio  = time.time()
    auditor = TopModel(k, dicio_corpora)
    fim = time.time()
    print("main(): TopModel criado...")
    print("main(): elapsed time = %.3fs"%(fim-inicio))
    
    #--------------------------------------------------
    # deixa o coletor de lixo trabalhar
    # corpora não é mais necessária e a memória pode ser liberada
    # só precisamos do nome dos modelos
    modelos = dicio_corpora.keys()
    dicio_corpora = None 
    
    #------------------------------------------------
    # leia a citacao
    nome_arquivo = input("Digite o nome arquivo com a citacao: ")
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arq:
            citacao = arq.read()
    except:
        print("main(): arquivo '%s' não encontrado"%nome_arquivo)
        return None

    print('Citação:"' + citacao + '"\n')
    for modelo in modelos:
        s  = "Modelo: " + modelo + " - "
        s += "media verossimilhança (log): " + str(auditor.media_verossimilhanca(modelo, citacao))
        print(s)
    melhor_modelo, media_verossimilhanca = auditor.top_model(citacao)      
    s = "Melhor modelo: " + melhor_modelo + \
        " - media verossimilhança (log): " + str(media_verossimilhanca) + "\n"\
        "Provavel autor: " + melhor_modelo  
    print(s)
 

#--------------------------------------------------
if __name__ == '__main__':
    main()
'''  
    
    
    

'''
    Programa classificador de autoria
    Digite nomes de arquivos com corpus: bush1+2.txt kerry1+2.txt
    Digite a ordem do modelo: 2
    main(): criando o objeto TopModel...
    main(): TopModel criado...
    main(): elapsed time = 0.237s
    Digite o nome arquivo com a citacao: bush3-00.txt
    Citação:"Thank you very much. 

    I want to thank Arizona State as well. 

    Yes, we can be safe and secure, if we stay on the offense against the terrorists and if we spread freedom and liberty around the world. 

    I have got a comprehensive strategy to not only chase down the Al Qaida, wherever it exists -- and we're making progress; three-quarters of Al Qaida leaders have been brought to justice -- but to make sure that countries that harbor terrorists are held to account. 

    As a result of securing ourselves and ridding the Taliban out of Afghanistan, the Afghan people had elections this weekend. And the first voter was a 19-year-old woman. Think about that. Freedom is on the march. 

    We held to account a terrorist regime in Saddam Hussein. 

    In other words, in order to make sure we're secure, there must be a comprehensive plan. My opponent just this weekend talked about how terrorism could be reduced to a nuisance, comparing it to prostitution, illegal gambling. I think that attitude and that point of view is dangerous. I don't think you can secure America for the long run if you don't have a comprehensive view as to how to defeat these people. 

    At home, we'll do everything we can to protect the homeland. I signed the homeland security bill to better align our assets and resources. My opponent voted against it. 

    We're doing everything we can to protect our borders and ports. 

    But absolutely we can be secure in the long run. It just takes good, strong leadership.

    "

    Modelo: bush1+2.txt - media verossimilhança (log): -2.1131202326469376
    Modelo: kerry1+2.txt - media verossimilhança (log): -2.189529829154229
    Melhor modelo: bush1+2.txt - media verossimilhança (log): -2.1131202326469376
    Provavel autor: bush1+2.txt

    Programa classificador de autoria
    Digite nomes de arquivos com corpus: kerry1+2.txt bush1+2.txt
    Digite a ordem do modelo: 2
    main(): criando o objeto TopModel...
    main(): TopModel criado...
    main(): elapsed time = 0.229s
    Digite o nome arquivo com a citacao: bush3-01.txt
    Citação:"Gosh, I just don't think I ever said I'm not worried about Osama bin Laden. It's kind of one of those exaggerations. 

    Of course we're worried about Osama bin Laden. We're on the hunt after Osama bin Laden. We're using every asset at our disposal to get Osama bin Laden. 

    My opponent said this war is a matter of intelligence and law enforcement. No, this war is a matter of using every asset at our disposal to keep the American people protected.

    "

    Modelo: kerry1+2.txt - media verossimilhança (log): -2.160704169368655
    Modelo: bush1+2.txt - media verossimilhança (log): -2.146690068943393
    Melhor modelo: bush1+2.txt - media verossimilhança (log): -2.146690068943393
    Provavel autor: bush1+2.txt
        
'''


'''
__init__()

    Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
    [GCC 7.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from top_model import TopModel
    >>> corpus1  = "aabcabaacaac"
    >>> corpus2  = "babababaabababaabaabaaaaaababaaaab"
    >>> corpus3  = "Como é bom estudar MAC0122!"
    >>> corpus4  = "aaabaaabaaabaaabaaab"
    >>> dicio_corp1 = {"aab...": corpus1, "bab...": corpus2, "mac": corpus3}
    >>> dicio_corp2 = {"aaab...": corpus4}
    >>> auditor1 = TopModel(2, dicio_corp1)
    >>> auditor2 = TopModel(3, dicio_corp2)
    >>> 

__str__()

    >>> str_auditor1 = str(auditor1)
    >>> str_auditor1
    'TopModel possui 3 modelos: aab...,bab...,mac\nModelo aab...:\nalfabeto tem 3 símbolos\n"aa"   3\n"ab"   2\n"ac"   2\n"ba"   1\n"bc"   1\n"ca"   3\n"aab"  1\n"aac"  2\n"aba"  1\n"abc"  1\n"aca"  2\n"baa"  1\n"bca"  1\n"caa"  2\n"cab"  1\nModelo bab...:\nalfabeto tem 2 símbolos\n"aa"   11\n"ab"   11\n"ba"   11\n"bb"   1\n"aaa"  6\n"aab"  5\n"aba"  10\n"abb"  1\n"baa"  5\n"bab"  6\n"bba"  1\nModelo mac:\nalfabeto tem 19 símbolos\n" M"   1\n" b"   1\n" e"   1\n" é"   1\n"!C"   1\n"01"   1\n"12"   1\n"2!"   1\n"22"   1\n"AC"   1\n"C0"   1\n"Co"   1\n"MA"   1\n"ar"   1\n"bo"   1\n"da"   1\n"es"   1\n"m "   1\n"mo"   1\n"o "   1\n"om"   2\n"r "   1\n"st"   1\n"tu"   1\n"ud"   1\n"é "   1\n" MA"  1\n" bo"  1\n" es"  1\n" é "  1\n"!Co"  1\n"012"  1\n"122"  1\n"2!C"  1\n"22!"  1\n"AC0"  1\n"C01"  1\n"Com"  1\n"MAC"  1\n"ar "  1\n"bom"  1\n"dar"  1\n"est"  1\n"m e"  1\n"mo "  1\n"o é"  1\n"om "  1\n"omo"  1\n"r M"  1\n"stu"  1\n"tud"  1\n"uda"  1\n"é b"  1\n'
    >>> str_auditor2 = str(auditor2)
    >>> str_auditor2
    'TopModel possui 1 modelos: aaab...\nModelo aaab...:\nalfabeto tem 2 símbolos\n"aaa"   5\n"aab"   5\n"aba"   5\n"baa"   5\n"aaab"  5\n"aaba"  5\n"abaa"  5\n"baaa"  5\n'
    >>> print(str_auditor1)
    TopModel possui 3 modelos: aab...,bab...,mac
    Modelo aab...:
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
    Modelo bab...:
    alfabeto tem 2 símbolos
    "aa"   11
    "ab"   11
    "ba"   11
    "bb"   1
    "aaa"  6
    "aab"  5
    "aba"  10
    "abb"  1
    "baa"  5
    "bab"  6
    "bba"  1
    Modelo mac:
    alfabeto tem 19 símbolos
    " M"   1
    " b"   1
    " e"   1
    " é"   1
    "!C"   1
    "01"   1
    "12"   1
    "2!"   1
    "22"   1
    "AC"   1
    "C0"   1
    "Co"   1
    "MA"   1
    "ar"   1
    "bo"   1
    "da"   1
    "es"   1
    "m "   1
    "mo"   1
    "o "   1
    "om"   2
    "r "   1
    "st"   1
    "tu"   1
    "ud"   1
    "é "   1
    " MA"  1
    " bo"  1
    " es"  1
    " é "  1
    "!Co"  1
    "012"  1
    "122"  1
    "2!C"  1
    "22!"  1
    "AC0"  1
    "C01"  1
    "Com"  1
    "MAC"  1
    "ar "  1
    "bom"  1
    "dar"  1
    "est"  1
    "m e"  1
    "mo "  1
    "o é"  1
    "om "  1
    "omo"  1
    "r M"  1
    "stu"  1
    "tud"  1
    "uda"  1
    "é b"  1

    >>> print(str_auditor2)
    TopModel possui 1 modelos: aaab...
    Modelo aaab...:
    alfabeto tem 2 símbolos
    "aaa"   5
    "aab"   5
    "aba"   5
    "baa"   5
    "aaab"  5
    "aaba"  5
    "abaa"  5
    "baaa"  5

    >>> 

modelo()

    >>> modelo_aaab = auditor2.modelo("aaab")
    modelo(): modelo 'aaab' não foi definido
    >>> modelo_aaab = auditor2.modelo("aaab.")
    modelo(): modelo 'aaab.' não foi definido
    >>> modelo_aaab = auditor2.modelo("aaab...")
    >>> print(modelo_aaab)
    alfabeto tem 2 símbolos
    "aaa"   5
    "aab"   5
    "aba"   5
    "baa"   5
    "aaab"  5
    "aaba"  5
    "abaa"  5
    "baaa"  5

    >>> modelo_aaab.laplace("aaab")
    0.8571428571428571
    >>> modelo_aaab.laplace("xxxx")
    0.5
    >>> modelo_aaab.laplace("xxxa")
    0.5
    >>> p = 0
    >>> for c in modelo_aaab.alphabet():
    ...      p += modelo_aaab.laplace("aaa" + c)
    ... 
    >>> p
    1.0
    >>> 

verossimilhanca_total():

    >>> citacao = "aabca"
    >>> auditor1.verossimilhanca_total("aab...", citacao)
    -5.19295685089021
    >>> auditor1.verossimilhanca_total("bba...", citacao)
    verossimilhanca_total(): modelo 'bba...' não foi definido
    >>> auditor1.verossimilhanca_total("bab...", citacao)
    -5.343472815221133
    >>> auditor1.verossimilhanca_total("mac", citacao)
    -14.722194895832203
    >>> auditor2.verossimilhanca_total("aaab...", citacao)
    -4.179502370562408
    >>> 

media_verossimilhanca():

    >>> auditor1.media_verossimilhanca("aab...", citacao)
    -1.038591370178042
    >>> auditor1.media_verossimilhanca("bba...", citacao)
    media_verossimilhanca(): modelo 'bba...' não foi definido
    >>> auditor1.media_verossimilhanca("bab...", citacao)
    -1.0686945630442266
    >>> auditor1.media_verossimilhanca("mac", citacao)
    -2.9444389791664407
    >>> auditor2.media_verossimilhanca("mac", citacao)
    media_verossimilhanca(): modelo 'mac' não foi definido
    >>> auditor2.media_verossimilhanca("aaab...", citacao)
    -0.8359004741124816
    >>> 

top_model()

    >>> melhor_modelo, media_verossimilhanca = auditor1.top_model(citacao)
    >>> melhor_modelo
    'aab...'
    >>> media_verossimilhanca
    -1.038591370178042
    >>> melhor_modelo, media_verossimilhanca = auditor2.top_model(citacao)
    >>> melhor_modelo
    'aaab...'
    >>> media_verossimilhanca
    -0.8359004741124816
    >>> 
'''







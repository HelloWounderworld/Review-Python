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
    monitores e colegas). Com exceção de material de MAC0122, caso
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
# MarkovModel(), MarkovModel.laplace(), __str__()
from markov_model import MarkovModel

# math.log()
import math

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
  
'''
Nota
Revisado em quarta, 4 dez 2019, 16:46 por Atribuição automática de nota
grade: 2,1 / 10,0

Relatório de avaliação[-]
Somente foi mostrado as chaves do corpora, para deixar os erros mais legíveis.
Desconsidere se seu programa não teve erros.

O retorno do método __str__ é diferente do esperado para o seguinte teste: (-0.06)
str(TopModel(2, dict_keys(['aab...', 'bab...', 'mac'])))

O retorno do método verossimilhanca_total não funciona para o seguinte teste: (-0.12)
TopModel(2, dict_keys(['aab...', 'bab...', 'mac'])).verossimilhanca_total("aab...", "aabca")
ERRO: 'MarkovModel' object has no attribute 'anagrama'

O retorno do método verossimilhanca_total não funciona para o seguinte teste: (-0.12)
TopModel(2, dict_keys(['aab...', 'bab...', 'mac'])).verossimilhanca_total("bab...", "aabca")
ERRO: 'MarkovModel' object has no attribute 'anagrama'

O retorno do método verossimilhanca_total não funciona para o seguinte teste: (-0.12)
TopModel(2, dict_keys(['aab...', 'bab...', 'mac'])).verossimilhanca_total("mac", "aabca")
ERRO: 'MarkovModel' object has no attribute 'anagrama'

O retorno do método media_verossimilhanca não funciona para o seguinte teste: (-0.12)
TopModel(2, dict_keys(['aab...', 'bab...', 'mac'])).media_verossimilhanca("aab...", "aabca")
ERRO: 'aab...'

O retorno do método media_verossimilhanca não funciona para o seguinte teste: (-0.12)
TopModel(2, dict_keys(['aab...', 'bab...', 'mac'])).media_verossimilhanca("bab...", "aabca")
ERRO: 'bab...'

O retorno do método media_verossimilhanca não funciona para o seguinte teste: (-0.12)
TopModel(2, dict_keys(['aab...', 'bab...', 'mac'])).media_verossimilhanca("mac", "aabca")
ERRO: 'mac'

O retorno do método top_model não funciona para o seguinte teste: (-0.36)
TopModel(2, dict_keys(['aab...', 'bab...', 'mac'])).top_model("aabca")
ERRO: 'aabca'

O retorno do método __str__ é diferente do esperado para o seguinte teste: (-0.06)
str(TopModel(3, dict_keys(['aaab...'])))

O retorno do método verossimilhanca_total não funciona para o seguinte teste: (-0.36)
TopModel(3, dict_keys(['aaab...'])).verossimilhanca_total("aaab...", "aabca")
ERRO: 'MarkovModel' object has no attribute 'anagrama'

O retorno do método media_verossimilhanca não funciona para o seguinte teste: (-0.36)
TopModel(3, dict_keys(['aaab...'])).media_verossimilhanca("aaab...", "aabca")
ERRO: 'aaab...'

O retorno do método top_model não funciona para o seguinte teste: (-0.36)
TopModel(3, dict_keys(['aaab...'])).top_model("aabca")
ERRO: 'aabca'

O retorno do método __str__ é diferente do esperado para o seguinte teste: (-0.06)
str(TopModel(3, dict_keys(['bush', 'kerry'])))

O retorno do método verossimilhanca_total não funciona para o seguinte teste: (-0.18)
TopModel(3, dict_keys(['bush', 'kerry'])).verossimilhanca_total("bush", "Thank you ...")
ERRO: 'MarkovModel' object has no attribute 'anagrama'

O retorno do método verossimilhanca_total não funciona para o seguinte teste: (-0.18)
TopModel(3, dict_keys(['bush', 'kerry'])).verossimilhanca_total("kerry", "Thank you ...")
ERRO: 'MarkovModel' object has no attribute 'anagrama'

O retorno do método media_verossimilhanca não funciona para o seguinte teste: (-0.18)
TopModel(3, dict_keys(['bush', 'kerry'])).media_verossimilhanca("bush", "Thank you ...")
ERRO: 'bush'

O retorno do método media_verossimilhanca não funciona para o seguinte teste: (-0.18)
TopModel(3, dict_keys(['bush', 'kerry'])).media_verossimilhanca("kerry", "Thank you ...")
ERRO: 'kerry'

O retorno do método top_model não funciona para o seguinte teste: (-0.36)
TopModel(3, dict_keys(['bush', 'kerry'])).top_model("Thank you ...")
ERRO: "Thank you very much. \n\nI want to thank Arizona State as well. \n\nYes, we can be safe and secure, if we stay on the offense against the terrorists and if we spread freedom and liberty around the world. \n\nI have got a comprehensive strategy to not only chase down the Al Qaida, wherever it exists -- and we're making progress; three-quarters of Al Qaida leaders have been brought to justice -- but to make sure that countries that harbor terrorists are held to account. \n\nAs a result of securing ourselves and ridding the Taliban out of Afghanistan, the Afghan people had elections this weekend. And the first voter was a 19-year-old woman. Think about that. Freedom is on the march. \n\nWe held to account a terrorist regime in Saddam Hussein. \n\nIn other words, in order to make sure we're secure, there must be a comprehensive plan. My opponent just this weekend talked about how terrorism could be reduced to a nuisance, comparing it to prostitution, illegal gambling. I think that attitude and that point of view is dangerous. I don't think you can secure America for the long run if you don't have a comprehensive view as to how to defeat these people. \n\nAt home, we'll do everything we can to protect the homeland. I signed the homeland security bill to better align our assets and resources. My opponent voted against it. \n\nWe're doing everything we can to protect our borders and ports. \n\nBut absolutely we can be secure in the long run. It just takes good, strong leadership.\n\n"

O retorno do método __str__ é diferente do esperado para o seguinte teste: (-0.06)
str(TopModel(3, dict_keys(['dilma', 'aecio'])))

O retorno do método verossimilhanca_total não funciona para o seguinte teste: (-0.18)
TopModel(3, dict_keys(['dilma', 'aecio'])).verossimilhanca_total("dilma", "O que nós ...")
ERRO: 'MarkovModel' object has no attribute 'anagrama'

O retorno do método verossimilhanca_total não funciona para o seguinte teste: (-0.18)
TopModel(3, dict_keys(['dilma', 'aecio'])).verossimilhanca_total("aecio", "O que nós ...")
ERRO: 'MarkovModel' object has no attribute 'anagrama'

O retorno do método media_verossimilhanca não funciona para o seguinte teste: (-0.18)
TopModel(3, dict_keys(['dilma', 'aecio'])).media_verossimilhanca("dilma", "O que nós ...")
ERRO: 'dilma'

O retorno do método media_verossimilhanca não funciona para o seguinte teste: (-0.18)
TopModel(3, dict_keys(['dilma', 'aecio'])).media_verossimilhanca("aecio", "O que nós ...")
ERRO: 'aecio'

O retorno do método top_model não funciona para o seguinte teste: (-0.36)
TopModel(3, dict_keys(['dilma', 'aecio'])).top_model("O que nós ...")
ERRO: 'O que nós precisamos é que a mesma eficiência que tive em Minas Gerais chegue ao governo federal.\n\nAs boas ideias, aquelas que melhoram a vida das pessoas, têm que avançar. Nós não temos que ter essa preocupação de sermos donos de determinado programa. Os programas são das pessoas. São dos brasileiros.\n\nMeu amigo, minha amiga que nos ouve, para a presidente da República a inflação não é problema. Ela não tem nenhuma proposta, nenhuma solução para enfrentar essa questão. Eu pergunto a quem nos ouve agora: você compra com o mesmo dinheiro de hoje o que comprava há seis meses? Se compra, deve votar na candidata Dilma Rousseff.\n\nNão adianta você mascarar a realidade, candidata, hoje infelizmente a inflação voltou a atormentar a vida dos brasileiros e das brasileiras, porque o seu governo foi leniente com ela.\n\nCandidata, tenha coragem de fazer a pergunta direta. É claro que essa é uma iniciativa extraordinária, e não é sua, é do Congresso Nacional. A senhora traz nesse debate, talvez pelo desespero, e tenta deturpar um tema que tem que ser colocado com absoluta clareza. Eu tive um episódio sim, que parei numa Lei Seca porque minha carteira estava vencida e ali naquele momento inadvertidamente não fiz o exame e me arrependi disso. Não como a senhora, que não se arrepende de nada no seu governo.\n\nNão consigo entender a sua dificuldade em entender o mérito dos outros. O Bolsa Família é um avanço. Mas se fizermos um DNA do Bolsa Família, o pai será Fernando Henrique Cardoso e a mãe a senhora Ruth Cardoso. Vocês aproveitaram o início do cadastro único e avançaram.\n\nA sua propaganda é só mentira. Não pode ser esse vale-tudo que a senhora transformou essa campanha. Eleve o nível desse debate. O seu governo virou um mar de lama, a grande verdade é essa. Brasileiros têm me pedido libertação: nos liberte desse governo do PT.\n\nNão sou o presidente Fernando Henrique, lamentavelmente. É importante que reconheçamos o caminho que chegamos até aqui. O Brasil de hoje é melhor que o de 15 anos atrás. Se não tivesse havido o governo do Fernando Henrique, outros avanços não teriam vindo.\n\nAcredito que a legislação atual (sobre o aborto) deve ser mantida. É uma posição pessoal que tenho.\n\nDefendo também o fim da reeleição e o cargo de cinco anos para o Executivo.\n\nEu acredito e confio nas nossas instituições. Todos esses casos foram investigados, se as pessoas estão soltas é porque as provas não existiram.\n\nOnde estão as pessoas do seu partido? Presos. O tesoureiro do seu partido? Está preso. O ex-presidente do seu partido? Preso. O Ministro mais importante do seu governo foi preso.\n\nO Pronatec foi inspirado nas Etecs de São Paulo. O Prouni foi uma inspiração em Goiás, no governo do PSDB que permitiu que se ampliasse vagas nas universidade. A senhora acha que é dona dos programas, ninguém é dona desse Brasil.\n\nA senhora permitiu ser sucedida na Casa Civil, o cargo que a senhora gosta de dizer que é o mais importante depois da presidência, pela sua amiga e braço direito que foi ali fazer negócios, e por isso foi demitida. Candidata, não me meça com sua régua.\n\nNão importa de qual partido, tem que investigar, a investigação tem que ir a fundo. Pela primeira vez a senhora dá credibilidade às denúncias do senhor Paulo Roberto Costa. Ele que disse que 2% das obras sob sua responsabilidade iam para o seu partido.\n\nO que me surpreende na senhora é o diagnóstico. Agora há pouco a senhora disse que a inflação não é um problema do governo, é problema sazonal. Comigo é tolerância zero com a inflação. A senhora terceiriza de novo as responsabilidades dizendo que é dos Estados essa responsabilidade constitucional (da segurança pública). Meu amigo, minha amiga, se for eleito presidente da República eu assumo aqui esse compromisso, vou liderar pessoalmente uma política nacional de segurança, que começa com a proibição do contingenciamento dos recursos.\n\nCandidata, a senhora tem ofendido Minas Gerais todos os instantes e em todos os debates. A senhora não tem conhecimento do que aconteceu no nosso Estado. Minas Gerais, pela força dos seus servidores, da sua gente, é um Estado respeitado no Brasil, respeitado internacionalmente.\n\nEu fico me perguntando quando vou à sua cidade, quando vou à Porto Alegre, onde é que está o metrô anunciado pelo seu programa de governo? Quando vou à minha Belo Horizonte, onde está o metrô que aparece lá como obra do seu governo? Quando vou, a Cuiabá, quando vamos a Curitiba, onde estão essas obras? A senhora tem um conjunto de boas intenções que a ineficiência do governo lamentavelmente não permitiu que ainda saíssem do papel.\n\nCandidata, tenha coragem de fazer a pergunta direto. É claro que essa é uma iniciativa extraordinária, e não é sua, é do Congresso Nacional. A senhora traz nesse debate, talvez pelo desespero, e tenta deturpar um tema que tem que ser colocado com absoluta clareza. Eu tive um episódio sim, que parei numa Lei Seca porque minha carteira estava vencida e ali naquele momento inadvertidamente não fiz o exame e me arrependi disso. Não como a senhora, que não se arrepende de nada no seu governo.\n\nMeu amigo, minha amiga que nos ouve, para a presidente da República a inflação não é problema, ela não tem nenhuma proposta, nenhuma solução para enfrentar essa questão. Eu pergunto a quem nos ouve agora: você compra com o mesmo dinheiro de hoje o que comprava há seis meses atrás? Se compra, deve votar na candidata Dilma Rousseff. Mas não adianta você mascarar a realidade, candidata, hoje infelizmente a inflação voltou a atormentar a vida dos brasileiros e das brasileiras, porque o seu governo foi leniente com ela.\n\nEu quero ser o grande presidente da integração nacional, o presidente da generosidade para com os brasileiros que mais precisam. Da integração do Nordeste ao nosso projeto de desenvolvimento.\n\nA senhora deturpa aqui palavras do Arminio Fraga. O que vamos dar aos bancos públicos é transparência.\n\n'

O retorno do método __str__ é diferente do esperado para o seguinte teste: (-0.06)
str(TopModel(5, dict_keys(['dilma', 'aecio'])))

O retorno do método verossimilhanca_total não funciona para o seguinte teste: (-0.18)
TopModel(5, dict_keys(['dilma', 'aecio'])).verossimilhanca_total("dilma", "O que nós ...")
ERRO: 'MarkovModel' object has no attribute 'anagrama'

O retorno do método verossimilhanca_total não funciona para o seguinte teste: (-0.18)
TopModel(5, dict_keys(['dilma', 'aecio'])).verossimilhanca_total("aecio", "O que nós ...")
ERRO: 'MarkovModel' object has no attribute 'anagrama'

O retorno do método media_verossimilhanca não funciona para o seguinte teste: (-0.18)
TopModel(5, dict_keys(['dilma', 'aecio'])).media_verossimilhanca("dilma", "O que nós ...")
ERRO: 'dilma'

O retorno do método media_verossimilhanca não funciona para o seguinte teste: (-0.18)
TopModel(5, dict_keys(['dilma', 'aecio'])).media_verossimilhanca("aecio", "O que nós ...")
ERRO: 'aecio'

O retorno do método top_model não funciona para o seguinte teste: (-0.36)
TopModel(5, dict_keys(['dilma', 'aecio'])).top_model("O que nós ...")
ERRO: 'O que nós precisamos é que a mesma eficiência que tive em Minas Gerais chegue ao governo federal.\n\nAs boas ideias, aquelas que melhoram a vida das pessoas, têm que avançar. Nós não temos que ter essa preocupação de sermos donos de determinado programa. Os programas são das pessoas. São dos brasileiros.\n\nMeu amigo, minha amiga que nos ouve, para a presidente da República a inflação não é problema. Ela não tem nenhuma proposta, nenhuma solução para enfrentar essa questão. Eu pergunto a quem nos ouve agora: você compra com o mesmo dinheiro de hoje o que comprava há seis meses? Se compra, deve votar na candidata Dilma Rousseff.\n\nNão adianta você mascarar a realidade, candidata, hoje infelizmente a inflação voltou a atormentar a vida dos brasileiros e das brasileiras, porque o seu governo foi leniente com ela.\n\nCandidata, tenha coragem de fazer a pergunta direta. É claro que essa é uma iniciativa extraordinária, e não é sua, é do Congresso Nacional. A senhora traz nesse debate, talvez pelo desespero, e tenta deturpar um tema que tem que ser colocado com absoluta clareza. Eu tive um episódio sim, que parei numa Lei Seca porque minha carteira estava vencida e ali naquele momento inadvertidamente não fiz o exame e me arrependi disso. Não como a senhora, que não se arrepende de nada no seu governo.\n\nNão consigo entender a sua dificuldade em entender o mérito dos outros. O Bolsa Família é um avanço. Mas se fizermos um DNA do Bolsa Família, o pai será Fernando Henrique Cardoso e a mãe a senhora Ruth Cardoso. Vocês aproveitaram o início do cadastro único e avançaram.\n\nA sua propaganda é só mentira. Não pode ser esse vale-tudo que a senhora transformou essa campanha. Eleve o nível desse debate. O seu governo virou um mar de lama, a grande verdade é essa. Brasileiros têm me pedido libertação: nos liberte desse governo do PT.\n\nNão sou o presidente Fernando Henrique, lamentavelmente. É importante que reconheçamos o caminho que chegamos até aqui. O Brasil de hoje é melhor que o de 15 anos atrás. Se não tivesse havido o governo do Fernando Henrique, outros avanços não teriam vindo.\n\nAcredito que a legislação atual (sobre o aborto) deve ser mantida. É uma posição pessoal que tenho.\n\nDefendo também o fim da reeleição e o cargo de cinco anos para o Executivo.\n\nEu acredito e confio nas nossas instituições. Todos esses casos foram investigados, se as pessoas estão soltas é porque as provas não existiram.\n\nOnde estão as pessoas do seu partido? Presos. O tesoureiro do seu partido? Está preso. O ex-presidente do seu partido? Preso. O Ministro mais importante do seu governo foi preso.\n\nO Pronatec foi inspirado nas Etecs de São Paulo. O Prouni foi uma inspiração em Goiás, no governo do PSDB que permitiu que se ampliasse vagas nas universidade. A senhora acha que é dona dos programas, ninguém é dona desse Brasil.\n\nA senhora permitiu ser sucedida na Casa Civil, o cargo que a senhora gosta de dizer que é o mais importante depois da presidência, pela sua amiga e braço direito que foi ali fazer negócios, e por isso foi demitida. Candidata, não me meça com sua régua.\n\nNão importa de qual partido, tem que investigar, a investigação tem que ir a fundo. Pela primeira vez a senhora dá credibilidade às denúncias do senhor Paulo Roberto Costa. Ele que disse que 2% das obras sob sua responsabilidade iam para o seu partido.\n\nO que me surpreende na senhora é o diagnóstico. Agora há pouco a senhora disse que a inflação não é um problema do governo, é problema sazonal. Comigo é tolerância zero com a inflação. A senhora terceiriza de novo as responsabilidades dizendo que é dos Estados essa responsabilidade constitucional (da segurança pública). Meu amigo, minha amiga, se for eleito presidente da República eu assumo aqui esse compromisso, vou liderar pessoalmente uma política nacional de segurança, que começa com a proibição do contingenciamento dos recursos.\n\nCandidata, a senhora tem ofendido Minas Gerais todos os instantes e em todos os debates. A senhora não tem conhecimento do que aconteceu no nosso Estado. Minas Gerais, pela força dos seus servidores, da sua gente, é um Estado respeitado no Brasil, respeitado internacionalmente.\n\nEu fico me perguntando quando vou à sua cidade, quando vou à Porto Alegre, onde é que está o metrô anunciado pelo seu programa de governo? Quando vou à minha Belo Horizonte, onde está o metrô que aparece lá como obra do seu governo? Quando vou, a Cuiabá, quando vamos a Curitiba, onde estão essas obras? A senhora tem um conjunto de boas intenções que a ineficiência do governo lamentavelmente não permitiu que ainda saíssem do papel.\n\nCandidata, tenha coragem de fazer a pergunta direto. É claro que essa é uma iniciativa extraordinária, e não é sua, é do Congresso Nacional. A senhora traz nesse debate, talvez pelo desespero, e tenta deturpar um tema que tem que ser colocado com absoluta clareza. Eu tive um episódio sim, que parei numa Lei Seca porque minha carteira estava vencida e ali naquele momento inadvertidamente não fiz o exame e me arrependi disso. Não como a senhora, que não se arrepende de nada no seu governo.\n\nMeu amigo, minha amiga que nos ouve, para a presidente da República a inflação não é problema, ela não tem nenhuma proposta, nenhuma solução para enfrentar essa questão. Eu pergunto a quem nos ouve agora: você compra com o mesmo dinheiro de hoje o que comprava há seis meses atrás? Se compra, deve votar na candidata Dilma Rousseff. Mas não adianta você mascarar a realidade, candidata, hoje infelizmente a inflação voltou a atormentar a vida dos brasileiros e das brasileiras, porque o seu governo foi leniente com ela.\n\nEu quero ser o grande presidente da integração nacional, o presidente da generosidade para com os brasileiros que mais precisam. Da integração do Nordeste ao nosso projeto de desenvolvimento.\n\nA senhora deturpa aqui palavras do Arminio Fraga. O que vamos dar aos bancos públicos é transparência.\n\n'

O retorno do método __str__ é diferente do esperado para o seguinte teste: (-0.06)
str(TopModel(3, dict_keys(['dilma', 'bush'])))

O retorno do método verossimilhanca_total não funciona para o seguinte teste: (-0.18)
TopModel(3, dict_keys(['dilma', 'bush'])).verossimilhanca_total("dilma", "Gosh, I ju...")
ERRO: 'MarkovModel' object has no attribute 'anagrama'

O retorno do método verossimilhanca_total não funciona para o seguinte teste: (-0.18)
TopModel(3, dict_keys(['dilma', 'bush'])).verossimilhanca_total("bush", "Gosh, I ju...")
ERRO: 'MarkovModel' object has no attribute 'anagrama'

O retorno do método media_verossimilhanca não funciona para o seguinte teste: (-0.18)
TopModel(3, dict_keys(['dilma', 'bush'])).media_verossimilhanca("dilma", "Gosh, I ju...")
ERRO: 'dilma'

O retorno do método media_verossimilhanca não funciona para o seguinte teste: (-0.18)
TopModel(3, dict_keys(['dilma', 'bush'])).media_verossimilhanca("bush", "Gosh, I ju...")
ERRO: 'bush'

O retorno do método top_model não funciona para o seguinte teste: (-0.36)
TopModel(3, dict_keys(['dilma', 'bush'])).top_model("Gosh, I ju...")
ERRO: "Gosh, I just don't think I ever said I'm not worried about Osama bin Laden. It's kind of one of those exaggerations. \n\nOf course we're worried about Osama bin Laden. We're on the hunt after Osama bin Laden. We're using every asset at our disposal to get Osama bin Laden. \n\nMy opponent said this war is a matter of intelligence and law enforcement. No, this war is a matter of using every asset at our disposal to keep the American people protected.\n\n"

O retorno do método __str__ é diferente do esperado para o seguinte teste: (-0.06)
str(TopModel(200, dict_keys(['aab...', 'bab...', 'mac'])))

O retorno do método verossimilhanca_total não funciona para o seguinte teste: (-0.12)
TopModel(200, dict_keys(['aab...', 'bab...', 'mac'])).verossimilhanca_total("aab...", "aabca")
ERRO: 'MarkovModel' object has no attribute 'anagrama'

O retorno do método verossimilhanca_total não funciona para o seguinte teste: (-0.12)
TopModel(200, dict_keys(['aab...', 'bab...', 'mac'])).verossimilhanca_total("bab...", "aabca")
ERRO: 'MarkovModel' object has no attribute 'anagrama'

O retorno do método verossimilhanca_total não funciona para o seguinte teste: (-0.12)
TopModel(200, dict_keys(['aab...', 'bab...', 'mac'])).verossimilhanca_total("mac", "aabca")
ERRO: 'MarkovModel' object has no attribute 'anagrama'

O retorno do método media_verossimilhanca não funciona para o seguinte teste: (-0.12)
TopModel(200, dict_keys(['aab...', 'bab...', 'mac'])).media_verossimilhanca("aab...", "aabca")
ERRO: 'aab...'

O retorno do método media_verossimilhanca não funciona para o seguinte teste: (-0.12)
TopModel(200, dict_keys(['aab...', 'bab...', 'mac'])).media_verossimilhanca("bab...", "aabca")
ERRO: 'bab...'

O retorno do método media_verossimilhanca não funciona para o seguinte teste: (-0.12)
TopModel(200, dict_keys(['aab...', 'bab...', 'mac'])).media_verossimilhanca("mac", "aabca")
ERRO: 'mac'

O retorno do método top_model não funciona para o seguinte teste: (-0.36)
TopModel(200, dict_keys(['aab...', 'bab...', 'mac'])).top_model("aabca")
ERRO: 'aabca'


Enviado em quarta, 30 out 2019, 18:25 (Baixar)
top_model.py

'''
    
    
    
    

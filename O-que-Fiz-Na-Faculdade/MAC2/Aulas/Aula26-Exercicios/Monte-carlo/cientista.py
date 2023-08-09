import random

class Cientista:
    def __init__(self, no_questoes, limiar, t):
        self.no_questoes = no_questoes
        self.limiar = limiar
        # o gabarito poderia ser toda resposta True...
        self.gabarito = [random.choice([True,False]) for i in range(no_questoes)]
        # sucesso significa que chutando a/o estudante acertou
        # menos que limiar questoes
        sucesso = 0
        for i in range(t):
            sucesso += self.experimento()
        self.p = sucesso/t

    def mean(self):
        return self.p
    
    def experimento(self):
        n        = self.no_questoes
        limiar   = self.limiar
        gabarito = self.gabarito
        acertos = 0
        for i in range(n):
            chute = random.choice([True,False])  
            if chute == gabarito[i]:
                acertos += 1
        if acertos < limiar: return 1        
        return 0        
        

# módulo para geração de números aleatórios
import random

from config import *

class Votacao:
    def __init__(self, no_votos = NO_VOTOS, por_A = POR_A, por_erro = POR_ERRO, t = T):
        '''(Votacao, int, float, float, int) ->

        Recebe

             - no_votos: número de votos
             - por_A: porcentagem de votos para o candidato A
             - por_erro: porcentagem de votos errados
             - t: número de experimentos

        determina a probabilidade do resultado da eleição ser alterado
        '''
        self.no_votos = no_votos
        self.por_A = por_A
        self.por_erro = por_erro

        # realize os no_t experimentos
        alterou = 0
        for i in range(t):
           alterou += self.experimento()
            
        self.p = alterou/t

    #-----------------------------------------------------------            
    def mean(self):
        return self.p

    #-----------------------------------------------------------    
    def experimento(self):
        '''(Votacao) -> bool

        Recebe a porcentagem de votos que são contados de forma errada
        e retorna True se o resultado da eleição foi alterado e False
        em caso contrário.

        Supõe que a porcentagem PORCEN_A de eleitores de A é 
        maior que porcentagem PORCEN_B de eleitores de B.
        '''
        no_votos = self.no_votos
        por_erro = self.por_erro
        por_A    = self.por_A
        
        # calcule número de votos errados
        no_erros = (no_votos * por_erro) // 100
        
        # calcule número de votos em A e em B
        votos_A  = (no_votos * por_A) // 100
        
        # print(no_votos, no_erros, votos_A)
        # número líquido de votos de B para A
        muda = 0
        
        # supor que os votos de A estão em range(votos_A)
        # supor que os votos de B estão em range(votos_A, no_votos)
        for i in range(no_erros):
            # escolhe um voto para alterar o resultado
            voto = random.randrange(no_votos)
            if voto < votos_A:
                # transfere um voto de A para B
                muda -= 1
                # diminui os votos de A que podem ser transferidos
                votos_A -= 1
            else:
                # transfere um voto de B para A
                muda += 1
            no_votos -= 1

        votos_A = (self.no_votos * por_A) // 100 
        votos_B = (self.no_votos - votos_A) 

        # print(votos_A, votos_B, muda)
        
        return  votos_A + muda <= votos_B - muda
        

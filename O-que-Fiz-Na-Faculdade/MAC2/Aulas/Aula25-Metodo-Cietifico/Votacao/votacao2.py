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

        Supõe que a porcentagem POR_A de eleitores de A é 
        maior que porcentagem POR_B de eleitores de B.
        '''
        no_votos = self.no_votos
        por_erro = self.por_erro
        por_A    = self.por_A
        
        # calcule número de votos em A e B
        votos_A  = (no_votos * por_A) // 100
        votos_B  =  no_votos - votos_A
        p_erro = por_erro/100
        # print(">>>", votos_A, votos_B, p_erro)
        vA = 0
        for i in range(votos_A):
            vA += random.random() > p_erro
            
        for i in range(votos_B):
            vA += random.random() < p_erro
        
        vB = no_votos - vA
        # print(vA, vB)
        
        return  vA <= vB
        

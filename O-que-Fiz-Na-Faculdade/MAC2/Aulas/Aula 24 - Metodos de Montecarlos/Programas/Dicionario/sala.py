'''
   MAC0122 Princípios de Desenvolvimento de Algoritmos

'''
import numpy as np
import random

VAZIA   = False
OCUPADA = True

class Sala:
    #------------------------------------------
    def __init__(self, n, m):
        '''(Sala, int, float, int)
        É esperado que alfa esteja entre 0 e 1, mas não muito perto de 1.
        '''
        self.n    = n  # número de estudantes
        self.m    = m  # numero de carteiras
        self.sala = np.full(m, VAZIA) # sala de aula
        self.distribua_estudantes()
        self.estatisticas()

    #---------------------------------------------
    def __str__(self):
        s = ''
        for i in range(self.m):
            s += 'x' if self.sala[i] == OCUPADA else ' '
        return s+"|"

    #---------------------------------------------
    def no_grupos(self):
        return self.grupos
                
    #-----------------------------------------    
    def media_malsucedidas(self):
        return self.fracasso

    #-----------------------------------------    
    def media_bemsucedidas(self):
        return self.mean_sucesso
    
    #-----------------------------------------
    def estatisticas(self):
        sala = self.sala
        m    = self.m
        anterior = VAZIA
        grupos = 0
        fracasso  = 0
        for i in range(self.m):
            atual = sala[i]
            if anterior == VAZIA and atual == OCUPADA:
                grupos += 1
                k =  2 
            elif anterior == OCUPADA and atual == OCUPADA:
                k += 1
            else:
                k = 1
            fracasso += k
            anterior  = atual
            
        if sala[0] == OCUPADA and sala[-1] == OCUPADA:
            grupos -= 1    
        self.grupos = grupos
        self.fracasso = fracasso/m

    #----------------------------------------    
    def distribua_estudantes(self):
        n = self.n
        m = self.m
        sala = self.sala
        sucesso = 1
        for i in range(n):
            carteira = random.randrange(m)
            while sala[carteira] != VAZIA:
                carteira += 1
                sucesso  += 1
                if carteira == m: carteira = 0
            sucesso += 1    
            sala[carteira] = OCUPADA
        self.mean_sucesso = sucesso/n

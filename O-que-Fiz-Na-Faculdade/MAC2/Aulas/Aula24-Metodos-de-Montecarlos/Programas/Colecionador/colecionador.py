'''
   MAC0122 Princípios de Desenvolvimento de Algoritmos

'''
from config import *
import random

class Colecionador:
    #------------------------------------------
    def __init__(self, n = N, t = T):
        self.n = n
        self.t = t
        no_figurinhas = 0
        for i in range(t):
            no_figurinhas += self.experimento()
        self.n_medio = no_figurinhas/t    

    #------------------------------------------    
    def mean(self):
        return self.n_medio

    #-----------------------------------------
    def experimento(self):
        n = self.n
        album = set()
        no_compradas = 0
        while len(album) != n:
            fig = random.randrange(n)
            no_compradas += 1
            album |= {fig}
        return no_compradas

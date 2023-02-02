'''
   MAC0122 Princípios de Desenvolvimento de Algoritmos

'''
from config import *
import random

class Aniversario:
    #------------------------------------------
    def __init__(self, n, t = T):
        self.n = n
        self.t = t
        sucessos = 0
        for i in range(t):
            sucessos += self.experimento()
        self.p = sucessos/t    

    #------------------------------------------    
    def mean(self):
        return self.p

    #-----------------------------------------
    def experimento(self):
        n = self.n
        aniversarios = set()
        for i in range(n):
            data = random.randrange(DATAS)
            if data in aniversarios:
               return True
            aniversarios |= {data}
        return False

from config import *
import random

class Pi:
    #------------------------------------------
    def __init__(self, n, t = T):
        self.n = n   # number of points
        self.t = t   # number of trials
        sucessos = 0
        for i in range(t):
            sucessos += self.experimento()
        self.p = 4*sucessos/t    

    #------------------------------------------    
    def mean(self):
        return self.p

    #-----------------------------------------
    def experimento(self):
        ''' Sorteia um ponto dentro do círculo
        '''
        n = self.n
        if n == 0: return 0
        cont = 0
        for i in range(n):
            x = random.random()
            y = random.random()
            if x*x + y*y < 1.0:
               cont += 1
        return cont / n

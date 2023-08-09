from config import *
import random

class Pi:
    #------------------------------------------
    def __init__(self, n, t = T, r = 1):
        self.n = n      # number of points
        self.t = t      # number of trials
        self.raio = r   # raio do círculo
        area_semicirculo = 0
        for i in range(t):
            area_semicirculo += self.experimento()
        self.p = 4*area_semicirculo/t    

    #------------------------------------------    
    def mean(self):
        return self.p

    #-----------------------------------------
    def experimento(self):
        ''' Sorteia um ponto dentro do círculo
        '''
        n = self.n
        r = self.raio
        if n == 0: return 0
        cont = 0
        for i in range(n):
            x = random.random()*r
            y = random.random()*r
            if x*x + y*y < r*r:
               cont += 1
        return r*r*(cont/n) # probabilidade de cair no semicírculo.

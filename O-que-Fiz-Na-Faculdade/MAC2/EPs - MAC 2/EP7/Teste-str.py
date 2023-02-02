import numpy as np

BLOCKED = 0  # sítio bloqueado
OPEN    = 1  # sítio aberto
FULL    = 2  # sítio cheio

class Percolation:
    def __init__(self,shape):
        self.shape = shape
        self.data = np.full(self.shape,BLOCKED)
        
    def __str__(self):
        Set = {0:' ',1:'o',2:   'x'}
        x = '+---'
        abertos = 0
        for i in range(len(self.data)):
            if i != 0:
                x = x + '+---'
            for j in range(len(self.data[i])):
                if j == len(self.data[i])-1:
                    x = x + '+\n|'
                else:
                    x = x + '+---'
            for l in range(len(self.data[i])):
                if l == len(self.data[i])-1:
                    if self.data[i,l] == OPEN:
                        abertos+=1
                    x = x + ' %s |\n' %(Set[self.data[i,l]])
                else:
                    if self.data[i,l] == OPEN:
                        abertos+=1
                    x = x + ' %s |' %(Set[self.data[i,l]])
        x = x + '+---'
        for t in range(len(self.data[0])):
            if t == len(self.data[0]) - 1:
                x = x + 'x\n'
            else:
                x = x + '+---'
        lin,col = self.shape
        x = x +'\ngrade de dimensao: %dx%d' %(lin,col)
        x = x +'\nno. sitios abertos: %d' %(abertos)
        x = x +'\npercolou: '
        return x
    #def open(self,lin,col):
        
    def is_open(self,lin,col):
        if self.data[lin,col] == OPEN:
            return True
        return False
        
    def is_full(self,lin,col):
        if self.data[lin,col] == 2:
            return True
        return False
    
    def percolates(self):
        pass
    
    def no_open(self):
        aberto = 0
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i,j] == OPEN:
                    aberto+=1
        return aberto
    
    def get_grid(self):
        return self.data.copy()


from percolation import Percolation
import numpy as np
import random
import math

def Intervalos(lista,inferior,superior):
    contador = 0
    for i in lista:
        if inferior<i<superior:
            contador+= 1
    return contador


def ordenar(lista):
    if len(lista) == 1:
        return lista
    else:
        for i in range(0,len(lista)-1):
            for j in range(i+1,len(lista)):
                if lista[j] <= lista[i]:
                    x = lista[j]
                    lista[j] = lista[i]
                    lista[i] = x
        


class PercolationStats:
    
    def __init__(self,shape,T):
        self.shape = shape
        self.T = T
        self.fracoes = []
        self.media = []
        self.variancia = []
        
    def mean(self):
        x_t = 0
        for i in range(self.T):
            Cobaia = Percolation(self.shape)
            aleatorio = [0]*Cobaia.data.size
            for j in range(Cobaia.data.size):
                aleatorio[j] = random.random()
            tuplas = np.array(aleatorio).reshape(self.shape)
            dictionary = {}
            for l in range(len(tuplas)):
                for t in range(len(tuplas[l])):
                    dictionary[tuplas[l,t]] = (l,t)       
            ordenar(aleatorio)
            ordenado = aleatorio
            for r in range(len(ordenado)):
                x = ordenado[r]
                nlin,ncol = dictionary[x]
                Cobaia.open(nlin,ncol)
                if Cobaia.percolates() == True:
                    break
            self.fracoes.append(Cobaia.no_open()/Cobaia.data.size)
            x_t = x_t + (Cobaia.no_open()/Cobaia.data.size)
        self.media.append(x_t/self.T)
        return x_t / self.T
    
    def stddev(self):
        soma = 0
        for i in self.fracoes:
            soma = soma + (self.media[0]-i)**2
        self.variancia.append(soma / (self.T - 1))
        return soma / (self.T - 1)
    
    def confidenceLow(self):
        return self.media[0]-((1.96*math.sqrt(self.variancia[0]))/(math.sqrt(self.T)))
    
    def confidenceHigh(self):
        return self.media[0]+((1.96*math.sqrt(self.variancia[0]))/(math.sqrt(self.T)))
    
def main():
    '''
    Preciso pensar na possibilidade de ter somente em 1 repeticao do experimento ?
    Os valores do mean em exp20's estao dando um valor na casa de 0.55...
    ou 0.56... verificar, pois exemplo esta retornando as casas em torno de
    0.59... ou 0.58...
    '''
    exp1 = PercolationStats((1,1), 2)
    exp2 = PercolationStats((2,2), 2)
    exp20_1 = PercolationStats((20,20), 100)
    exp20_2 = PercolationStats((20,20), 100)
    '''
    print('Teste mean:')
    print()
    print('exp1.mean()')
    print(exp1.mean())
    print()
    print('exp2.mean()')
    print(exp2.mean())
    print()
    '''
    print('exp20_1.mean()')
    print(exp20_1.mean())
    print()
    print('exp20_2.mean()')
    print(exp20_2.mean())
    print()
    '''
    print('Teste stddev():')
    print()
    print('exp1.stddev()')
    print(exp1.stddev())
    print()
    print('exp2.stddev()')
    print(exp2.stddev())
    print()
    print('exp20_1.stddev()')
    print(exp20_1.stddev())
    print()
    print('exp20_2.stddev()')
    print(exp20_2.stddev())
    print()
    print('Teste ConfidenceLow():')
    print()
    print('exp1.confidenceLow()')
    print(exp1.confidenceLow())
    print()
    print('exp2.confidenceLow()')
    print(exp2.confidenceLow())
    print()
    print('exp20_1.confidenceLow()')
    print(exp20_1.confidenceLow())
    print()
    print('exp20_2.confidenceLow()')
    print(exp20_2.confidenceLow())
    print()
    print('Teste confidenceHigh():')
    print()
    print('exp1.confidenceHigh()')
    print(exp1.confidenceHigh())
    print()
    print('exp2.confidenceHigh()') 
    print(exp2.confidenceHigh()) 
    print()
    print('exp20_1.confidenceHigh()')
    print(exp20_1.confidenceHigh())
    print()
    print('exp20_2.confidenceHigh()')
    print(exp20_2.confidenceHigh())
    '''
main()


import numpy as np
def show(array):
    return print(array)
class NumPymagem:
    
    def __init__(self,nlins = 0,ncolns = 0,valor = 0):
        print("Entrei no init")
        if nlins == 0 and ncolns == 0 :
            self.array = np.arange(1).reshape(1,)
            return self.array
        self.nlins = nlins
        self.ncolns = ncolns
        self.size = self.nlins*self.ncolns
        self.NumPymagem = np.arange(self.size).reshape(self.nlins,self.ncolns)
        print("Este é o tipo: ", type(self.NumPymagem))
        elif type(valor) == type(self.NumPymagem):
            self.NumPymagem = valor
            return self.NumPymagem
        else:
            for i in range(self.nlins):
                for j in range(self.ncolns):
                    self.NumPymagem[i,j] = valor
        
    def __str__(self):
        return show(self.NumPymagem)
        
def main():
    img = NumPymagem(3,4,100)
    imgtest = NumPymagem()
    print(img)
main()

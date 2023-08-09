def boleano(lista):
    for i in lista:
        if 0<= i:
            return False
    return True
        
class Revendedora:
    
    def __init__(self,estoque):
        self.estoque = estoque
        self.lista = []
        self.dicionario = {}
        for i in range(len(self.estoque)):
            self.lista.append(i)
            self.dicionario[-len(self.estoque)+i] = i
    def __str__(self):
        rolos = len(self.estoque)
        x = 'Estoque possui %d rolos:\n' %(rolos)
        for i in range(len(self.estoque)):
            x = x +'   '+'rolo %d: %d m\n' %(i,self.estoque[i])
        return x
    
    def atenda_encomenda(self,encomenda):
        x = boleano(encomenda)
        if x == True:
            print('Entrei, deu tudo negativo')
            print(encomenda)
            print()
            print('Dicionario que usarei:')
            print(self.dicionario)
            print()
            for i in range(len(encomenda)):
                encomenda[i] = self.dicionario[encomenda[i]]
            return encomenda
        else:
            for i in range(len(self.estoque)):
                for j in range(len(encomenda)):
                    if 0<= self.estoque[-1-i] - encomenda[j] and 0<=encomenda[j]:
                        y = encomenda[j]
                        self.estoque[-1-i] = self.estoque[-1-i] - encomenda[j]
                        encomenda[j] = -1-i
                        x = Revendedora(self.estoque).atenda_encomenda(encomenda)
                        if type(x) == list:
                            return x
                        else:
                            encomenda[j] = y
                            self.estoque[-1-i] = self.estoque[-1-i]+encomenda[j]
            return
                        

def main():
    '''
    Mostrar que o rev5 ta dando diferente do que esta aparecendo no exemplo do EP
    '''
    rev1 = Revendedora([100])
    rev2 = Revendedora([100, 150])
    rev3 = Revendedora([150, 100])
    rev4 = Revendedora([60, 70, 50])
    rev5 = Revendedora([100, 150, 100])
    rev6 = Revendedora([100, 80])
    print()
    print('__str__()')
    print()
    print(rev1)
    print()
    print(rev2)
    print()
    print(rev5)
    print()
    print('atenda_encomenda()')
    print()
    print('rev1:')
    print(rev1)
    print('Encomenda solicitada:')
    print([50, 15, 30])
    print(rev1.atenda_encomenda([50, 15, 30]))
    print()
    print(rev1)
    print()
    print('rev2:')
    print(rev2)
    print()
    print('Encomenda solicitada:')
    print([70, 90, 70])
    print()
    print(rev2.atenda_encomenda([70, 90, 70]))
    print(rev2)
    print()
    print('rev3:')
    print(rev3)
    print()
    print('Encomenda solicitada:')
    print([80, 80, 80])
    print(rev3.atenda_encomenda([80, 80, 80]))
    print()
    print(rev3)
    print()
    print('rev4:')
    print(rev4)
    print()
    print('Encomenda solicitada:')
    print([40, 5, 25, 30, 25, 55])
    print(rev4.atenda_encomenda([40, 5, 25, 30, 25, 55]))
    print()
    print('Resultado do rev4:')
    print(rev4)
    print()
    print('rev5:')
    print(rev5)
    print()
    print('Encomenda solicitada:')
    print([80, 35, 79, 70, 35, 35])
    print(rev5.atenda_encomenda([80, 35, 79, 70, 35, 35]))
    print()
    print(rev5)
    print()
    print('Encomenda solicitada:')
    print([80, 35, 70, 70, 35])
    print(rev5.atenda_encomenda([80, 35, 70, 70, 35]))
    print()
    print(rev5)
    print()
    print('rev6:')
    print(rev6)
    print()
    print('Encomenda solicitada:')
    print([45,80,45])
    print(rev6.atenda_encomenda([45,80,45]))
    print()
    print(rev6)
    print()
    rev7 = Revendedora([100,80])
    print('rev7:')
    print(rev7)
    print('Encomenda solicitada:')
    print([30,80,30,30])
    print(rev7.atenda_encomenda([30,80,30,30]))
    print()
    print(rev7)
main()

'''
atenda_encomenda()

    In [14]: rev1.atenda_encomenda([50, 15, 30])
    Out[14]: [0, 0, 0]

    In [15]: print(rev1)
    Estoque possui 1 rolos:
        rolo 0: 5 m


    In [16]: rev2.atenda_encomenda([70, 90, 70])
    Out[16]: [1, 0, 1]

    In [17]: print(rev2)
    Estoque possui 2 rolos:
        rolo 0: 10 m
        rolo 1: 10 m


    In [18]: rev3.atenda_encomenda([80, 80, 80])

    In [19]: print(rev3.atenda_encomenda([80, 80, 80]))
    None

    In [20]: print(rev3)
    Estoque possui 2 rolos:
        rolo 0: 150 m
        rolo 1: 100 m


    In [21]: print(rev4)
    Estoque possui 3 rolos:
        rolo 0: 60 m
        rolo 1: 70 m
        rolo 2: 50 m


    In [22]: rev4.atenda_encomenda([40, 5, 25, 30, 25, 55])
    Out[22]: [1, 0, 2, 1, 2, 0]

    In [23]: print(rev4)
    Estoque possui 3 rolos:
        rolo 0: 0 m
        rolo 1: 0 m
        rolo 2: 0 m


    In [24]: print(rev5)
    Estoque possui 3 rolos:
        rolo 0: 100 m
        rolo 1: 150 m
        rolo 2: 100 m


    In [25]: rev5.atenda_encomenda([80, 35, 79, 70, 35, 35])

    In [26]: print(rev5)
    Estoque possui 3 rolos:
        rolo 0: 100 m
        rolo 1: 150 m
        rolo 2: 100 m


    In [27]: rev5.atenda_encomenda([80, 35, 70, 70, 35])
    Out[27]: [2, 0, 1, 1, 0]

    In [28]: print(rev5)
    Estoque possui 3 rolos:
        rolo 0: 30 m
        rolo 1: 10 m
        rolo 2: 20 m
'''
    
    
    

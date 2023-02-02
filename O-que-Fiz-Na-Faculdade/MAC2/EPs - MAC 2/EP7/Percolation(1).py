import numpy as np

BLOCKED = 0  # sítio bloqueado
OPEN    = 1  # sítio aberto
FULL    = 2  # sítio cheio
        
def coleta(array,lin,col,tupla):
    if col == 0:
        if lin == len(array)-1:
            vizinhos = [array[lin-1,col],array[lin,col+1]]
            if OPEN not in vizinhos:
                return tupla
            else:
                tuplas = [(lin-1,col),(lin,col+1)]
                for i in tuplas:
                    nlin,ncol = i
                    if i not in tupla:
                        tupla.append(i)
                        array[nlin,ncol] = FULL
                        coleta(array,nlin,ncol,tupla)
                return coleta(array,nlin,ncol,tupla)
        else:
            vizinhos = [array[lin-1,col],array[lin+1,col],array[lin,col+1]]
            if OPEN not in vizinhos:
                return tupla
            else:
                tuplas = [(lin-1,col),(lin+1,col),(lin,col+1)]
                for i in tuplas:
                    nlin,ncol = i
                    if array[nlin,ncol] == OPEN:
                        if i not in tupla:
                            tupla.append(i)
                            array[nlin,ncol] = FULL
                            coleta(array,nlin,ncol,tupla)
                return coleta(array,nlin,ncol,tupla)
    elif col == len(array[lin]) - 1:
        if lin == len(array)-1:
            vizinhos = [array[lin-1,col],array[lin,col-1]]
            if OPEN not in vizinhos:
                return tupla
            else:
                tuplas = [(lin-1,col),(lin,col-1)]
                for i in tuplas:
                    nlin,ncol = i
                    if array[nlin,ncol] == OPEN:
                        if i not in tupla:
                            tuplas.append(i)
                            array[nlin,ncol] = FULL
                            coleta(array,nlin,ncol,tupla)
                return coleta(array,nlin,ncol,tupla) 
        else:
            vizinhos = [array[lin-1,col],array[lin+1,col],array[lin,col-1]]
            if OPEN not in vizinhos:
                return tupla
            else:
                tuplas = [(lin-1,col),(lin+1,col),(lin,col-1)]
                for i in tuplas:
                    nlin,ncol = i
                    if array[nlin,ncol] == OPEN:
                        if  i not in tupla:
                            tupla.append(i)
                            array[nlin,ncol] = FULL
                            coleta(array,nlin,ncol,tupla)
                return coleta(array,nlin,ncol,tupla)
    else:
        if lin == len(array)-1:
            vizinhos = [array[lin-1,col],array[lin,col-1],array[lin,col+1]]
            if OPEN not in vizinhos:
                return tupla
            else:
                tuplas = [(lin-1,col),(lin,col-1),(lin,col+1)]
                for i in tuplas:
                    nlin,ncol = i
                    if array[nlin,ncol] == OPEN:
                        tupla.append(i)
                        array[nlin,ncol] = FULL
                        coleta(array,nlin,ncol,tupla)
                return coleta(array,nlin,ncol,tupla)
        else:
            vizinhos = [array[lin-1,col],array[lin+1,col],array[lin,col-1],array[lin,col+1]]
            if OPEN not in vizinhos:
                return tupla
            else:
                tuplas = [(lin-1,col),(lin+1,col),(lin,col-1),(lin,col+1)]
                for i in tuplas:
                    nlin,ncol = i
                    if array[nlin,ncol] == OPEN:
                        if i not in tupla:
                            tupla.append(i)
                            array[nlin,ncol] = FULL
                            coleta(array,nlin,ncol,tupla)
                return coleta(array,nlin,ncol,tupla)
                
    
    

class Percolation:
    def __init__(self,shape):
        self.shape = shape
        self.data = np.full(self.shape,BLOCKED)
        
    def __str__(self):
        Percola = False
        for j in range(len(self.data[0])):
                if self.data[len(self.data)-1,j] == FULL:
                    Percola = True
                    break      
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
                    if self.data[i,l] == OPEN or self.data[i,l] == FULL:
                        abertos+=1
                    x = x + ' %s |\n' %(Set[self.data[i,l]])
                else:
                    if self.data[i,l] == OPEN or self.data[i,l]==FULL:
                        abertos+=1
                    x = x + ' %s |' %(Set[self.data[i,l]])
        x = x + '+---'
        for t in range(len(self.data[0])):
            if t == len(self.data[0]) - 1:
                x = x + '+'
            else:
                x = x + '+---'
        lin,col = self.shape
        x = x +'\ngrade de dimensao: %dx%d' %(lin,col)
        x = x +'\nno. sitios abertos: %d' %(abertos)
        x = x +'\npercolou: %s' %(Percola)
        return x
    
    def open(self,lin,col):
        if lin == 0:
            self.data[lin,col] = 2
        elif lin == len(self.data)-1:
            if col == len(self.data[lin])-1:
                vizinhanca = [self.data[lin-1,col],self.data[lin,col-1]]
                if FULL in vizinhanca:
                    x = coleta(self.data,lin,col,[(lin,col)])
                    for i in x:
                        nlin,ncol = i
                        self.data[nlin,ncol] = FULL
                else:
                    self.data[lin,col] = OPEN
            elif col == 0:
                vizinhanca = [self.data[lin-1,col],self.data[lin,col+1]]
                if FULL in vizinhanca:
                    x = coleta(self.data,lin,col,[(lin,col)])
                    for i in x:
                        nlin,ncol = i
                        self.data[nlin,ncol] = FULL
                else:
                    self.data[lin,col] = OPEN
            else:
                vizinhanca = [self.data[lin-1,col],self.data[lin,col-1],self.data[lin,col+1]]
                if FULL in vizinhanca:
                    x = coleta(self.data,lin,col,[(lin,col)])
                    self.data[nlin,ncol] = FULL
                else:
                    self.data[lin,col] = OPEN
                
        else:
            if col == 0 and 0< lin < len(self.data)-1:
                vizinhanca = [self.data[lin-1,col],self.data[lin+1,col],self.data[lin,col+1]]
                if FULL in vizinhanca:
                    x = coleta(self.data,lin,col,[(lin,col)])
                    for i in x:
                        nlin,ncol = i
                        self.data[nlin,ncol] = FULL
                else:
                    self.data[lin,col] = OPEN
            elif col == len(self.data[lin]) - 1 and 0<lin < len(self.data)-1:
                vizinhanca = [self.data[lin-1,col],self.data[lin+1,col],self.data[lin,col-1]]
                if FULL in vizinhanca:
                    x = coleta(self.data,lin,col,[(lin,col)])
                    for i in x:
                        nlin,ncol = i
                        self.data[nlin,ncol] = FULL
                else:
                    self.data[lin,col] = OPEN    
            elif lin< len(self.data)-1:
                vizinhanca = [self.data[lin-1,col],self.data[lin+1,col],self.data[lin,col-1],self.data[lin,col+1]]
                if FULL in vizinhanca:
                    x = coleta(self.data,lin,col,[(lin,col)])
                    for i in x:
                        nlin,ncol = i
                        self.data[nlin,ncol] = FULL
                else:
                    self.data[lin,col] = OPEN
                
        
    def is_open(self,lin,col):
        if self.data[lin,col] == OPEN or self.data[lin,col]==FULL:
            return True
        return False
        
    def is_full(self,lin,col):
        if self.data[lin,col] == 2:
            return True
        return False
    
    def percolates(self):
        for j in range(len(self.data[0])):
            if self.data[len(self.data)-1,j] == FULL:
                return True
        return False
    
    def no_open(self):
        aberto = 0
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i,j] == OPEN or self.data[i,j] ==FULL:
                    aberto+=1
        return aberto
    
    def get_grid(self):
        return self.data.copy()
        
'''    
def main():
    sis1 = Percolation((1,1))
    sis2 = Percolation((2,2))
    sis3 = Percolation((3,2))
    sis4 = Percolation((3,4))
    print('Teste do shape')
    print(sis1.shape)
    print()
    print(sis2.shape)
    print()
    print(sis3.shape)
    print()
    print(sis4.shape)
    print()
    print('Teste do metodo str')
    print('sis1:')
    print('print:')
    print(sis1)
    print('sis3:')
    print('print:')
    print(sis3)
    print()
    print('Teste open:')
    print('sis1:')
    #print(sis1.open(1,1))
    print()
    print(sis1.open(0,0))
    print()
    print(sis1)
    print()
    print('sis2:')
    print(sis2.open(0,0))
    print()
    print(sis2)
    print()
    print('sis3:')
    print(sis3.open(1,1))
    print()
    print(sis3)
    print()
    print(sis3.open(0,0))
    print()
    print(sis3)
    print()
    print('aplica sis')
    print(sis3.open(1,0))
    print()
    print(sis3)
    print()
    print(sis3.open(2,1))
    print()
    print(sis3)
    print()
    print('Teste is_open:')
    print(sis3.is_open(0,0))
    print()
    print(sis3.is_open(0,1))
    print()
    print(sis1.is_open(0,0))
    print()
    print(sis2.is_open(0,0))
    print()
    print(sis2.is_open(0,1))
    print()
    print(sis2.is_open(1,1))
    print()
    print('Teste is_full:')
    print('sis3:')
    print(sis3.is_full(0,0))
    print()
    print(sis3.is_full(0,1))
    print()
    print('sis1:')
    print(sis1.is_full(0,0))
    print()
    print('sis2:')
    print(sis2.is_full(0,0))
    print()
    print(sis2.is_full(0,1))
    print() 
    print(sis2.open(1,1))
    print()
    print(sis2)
    print()
    print(sis2.is_full(1,1))
    print()
    print('Teste percolates():')
    print('sis1:')
    print(sis1.percolates())
    print()
    print('sis2:')
    print(sis2.percolates())
    print()
    print('sis3:')
    print(sis3.percolates())
    print()
    print('sis4:')
    print(sis4.percolates())
    print()
    print('Teste get_grid():')
    print('sis1:')
    print(sis1.get_grid())
    print()
    print('sis2:')
    print(sis2.get_grid())
    print()
    print('sis3:')
    print(sis3.get_grid())
    print()
    print('sis4:')
    print(sis4.get_grid())
    print()
main()
    
Classe Percolation

Nesse exercício você implementará uma classe Percolation. A sua classe 
Percolation é definida pela seguintes estruturas e operações. A seção Exemplos 
contém execuções dos métodos da classe.

    Percolation(shape): recebe uma tuple shape = (n, m) de inteiros e 
    representa um grade n × m através de um array de inteiros. Cada posição 
    desse array pode conter um dentre três valores:
        0 indica que o sítio está bloqueado (BLOCKED);
        1 indica que o sítio está aberto (OPEN);
        2 indica que o sítio está cheio (FULL). Inicialmente todos os n × m 
        sítios estão bloqueados.
    __str__(): retorna uma string que exibe o estado do sistema. Esse método é 
    usado pelas funções print() e str().
    shape: é o atributo de estado que mantém a tuple que é forma (shape) da 
    grade do sistema.
    is_open(lin,col): retorna True se a posição [lin,col] está aberta e False 
    caso contrário.
    is_full(lin,col): retorna True se a posição [lin,col] está cheia e False 
    caso contrário.
    percolates(): retorna True se o sistema percolou e False caso contrário.
    no_open(): retorna o número de sítios abertos do sistema.
    open(lin, col): abre uma dada posição [lin,col] caso ela esteja bloqueada, 
    caso contrário não faz nada. Esse método, que é o coração do EP, pode ser 
    feito adaptando-se a função distancias() das aulas 9 e 10. Na adaptação as 
    posições [lin,col] do sítios fazem o papel das cidades. Cada sítio está 
    ligado a até 4 sítios que são seus vizinhos.
    get_grid(): retorna um clone do array que representa a grade que modela o 
    sistema.

Os índices de linhas devem ser inteiros em range( n ) e os índices de colunas 
devem ser inteiros em range( m ). Se um dos métodos is_open(), is_full() ou 
open() receber uma posição [lin, col] em que lin ou col está fora do respectivo 
intervalo, o método deve exibir uma mensagem de erro (print()) e retornar None. 
Se Percolation() não receber um tuple com dois inteiros positivos como 
argumento, deve exibir uma mensagem de erro e retornar None.
'''





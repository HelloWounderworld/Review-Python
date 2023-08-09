import numpy as np
def main():
    a = np.array( [1,2,3,4,5,6,7,8,9,0] ).reshape(2,5)
    print(a)
    fliplr(a)
    print(a)

def fliplr( ar ):
    ''' (array) -> array 
    espelha as colunas.
    '''
    nlin, ncol = ar.shape
    meio = ncol // 2

    for i in range(meio):
        fim = ncol-1-i
        temp = ar[:,i].copy()  ## lembre-se que fatias são vistas!
        ar[:,i] = ar[:,fim]
        ar[:,fim] = temp
main()


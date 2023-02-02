#2-) Dada uma matriz real A mxn, verificar se existem elementos repetidos em A.

def repetido(A):
    unicos = []
    lins = len(A)
    cols = len(A[0])
    for i in range(lins):
        for j in range(cols):
            if A[i][j] in unicos:
                print("Essa matriz tem elementos repetidos")
                return True
            unicos.append(A[i][j])
    return False

#O mesmo processo sem criar uma lista auxiliar:

def repetidos(A):
    lins = len(A)
    cols = len(A[0])
    for i in range(lins):
        for j in range(cols):
            for k in range(lins): #Parte nova
                for l in range(cols):
                    if (A[i][j] == A[k][l] and (i != k or j != l)):
                        return True
    return False


    


            
                

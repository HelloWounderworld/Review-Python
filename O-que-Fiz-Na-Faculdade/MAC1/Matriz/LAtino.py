def inteiro(v):
    n = len(v)
    for i in range(n):
        j = i+1
        if j not in v:
            print("nao tem todos os inteiros")
            return False
    return True

def latino(A):
    for i in range(len(A)-1):
        avalia = inteiro(A[i])
        if(avalia == True):
            for j in range(len(A[0])):
                for l in range(i+1,len(A)):
                    for p in range(len(A[0])):
                        if(A[i][j] == A[l][p] and j == p):
                            print("Nao e quadrado latino")
                            return False
        else:
            print("Nao e latino")
            return False
    print("E latino")
    return True

def main():
    A = [[1,2,3,4],[2,3,4,1],[4,1,2,3],[3,4,1,2]]
    B = [[1,2,3,4],[1,3,4,2],[4,1,2,3],[3,4,1,2]]
    Avalia_A = latino(A)
    Avalaia_B = latino(B)
main()
    

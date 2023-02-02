def func_inteiro(A,B,M,N):
    print("Entrei na funçao")
    k = M -(N-1)
    for i in range(k):
        y = A[i:(i+4)]
        print("Mostre-me a lista que sera avaliado", y)
        if (y == B):
            return True
    return False

def main():
    A = [10,1,5,4,3,2,1,6,4,5]
    B = [4,3,2,1]
    M = 10
    N = 4
    Avalaia = print(func_inteiro(A,B,M,N))
main()

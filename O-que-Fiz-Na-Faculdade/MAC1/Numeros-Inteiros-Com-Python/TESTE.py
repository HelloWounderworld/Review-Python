def main():
    Lista_A = [-2,0,1,3]
    Lista = []
    C = int(input("Entre com um outro valor inteiro A: "))
    j = 0
    x = 0

    while(C not in Lista_A):
        if(Lista_A[j] < C):
            Lista.append(Lista_A[j])
            print(Lista)
            j = j + 1
        elif(Lista_A[j] > C):
            Lista.append(C)
            Lista.append(Lista_A[j])
            print(Lista)
            j = j + 1
                    
                
                
                
main()

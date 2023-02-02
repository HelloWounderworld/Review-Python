def main():
    Lista_A = []
    Lista = []
    j = 0
    B = str(input("Entre com um valor inteiro ou a palavra 'Fim': "))
    while(B != "Fim"):
        A = int(B)
        if A not in Lista_A:
            Lista_A.append(A)
            print("Mostre-me a Lista construida: ", Lista_A)
        B = str(input("Entre comum valor inteiro ou a palavra 'Fim': "))
        

    E = int(max(Lista_A[j:]))
    i = len(Lista_A)-1
    Lista_Dami = [int(max(Lista_A[j:]))]*len(Lista_A)
    while(i < len(Lista_A) or i == len(Lista_A)):
        D = int(min(Lista_A[j:]))
        if (D != int(Lista_A[i])):
            i = i - 1
        else:
            Lista_A[i] = E
            Lista.append(D)
            print("Mostre-me a lista ordenada: ", Lista)
            print("Mostre-me a lista_A modificada: ", Lista_A)

            if(Lista_A[:] == Lista_Dami):
                Lista.append(E)
                break
                
            else:
                i = len(Lista_A)-1
                     
    print("Mostre-me a lista ordenada: ", Lista)
            
            
     
                       
main()
        

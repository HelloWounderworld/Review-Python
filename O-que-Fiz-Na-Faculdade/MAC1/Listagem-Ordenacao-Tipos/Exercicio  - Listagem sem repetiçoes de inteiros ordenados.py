#Dados dois números naturais m e n e duas sequências ordenadas com m e n números inteiros,
#obter uma única sequência ordenada contendo todos os elementos das sequências originais sem repetição.
def main():
    Lista_A = []
    Lista_B = []
    Lista = []
    A = ""
    B = ""
    i = 0
    j = 0
    while(A != "fim" or B != "fim"):
        A = int(input("Entre com um valor inteiro A: "))
        B = int(input("Entre com um valor inteiro B: "))
        Lista_A.append(A)
        Lista_B.append(B)
        print("Mostre-me a lista no momento: ", Lista_A)
        print("Mostre-me a lista no momento: ", Lista_B)
            
        C = int(input("Entre com um outro valor inteiro A: "))
        D = int(input("Entre com um outro valor inteiro B: "))

        if(C not in Lista_A):
            if for any Lista_A[j] >= C:
                Lista_A[j] = Lista_A[j+1]
                Lista_A[j] = C
                
                
                  
                  
                
                print("Mostre-me a lista no momento: ", Lista_A)
            
            
            while(Lista_A[j] < Lista_B[i]):
                
                Lista.append(A)
                Lista.append(B)
                print("Mostre-me a lista no momento: ", Lista)

        elif((A not in Lista_A) and (B in Lista_B)):
            Lista_A.append(A)
            print("Mostre-me a lista no momento: ", Lista_A)
            print("Mostre-me a lista no momento: ", Lista_B)

        elif((A in Lista_A) and (B not in Lista_B)):
            Lista_B.append(B)
            print("Mostre-me a lista no momento: ", Lista_A)
            print("Mostre-me a lista no momento: ", Lista_B)

        else:
            print("Mostre-me a lista no momento: ", Lista_A)
            print("Mostre-me a lista no momento: ", Lista_B)

    

main()
            
            
    

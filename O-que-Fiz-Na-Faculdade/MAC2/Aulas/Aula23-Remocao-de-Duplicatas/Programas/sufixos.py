'''
    MAC0122 Princípios de Desenvolvimento de Algoritmos

'''
def main():
    s = input()
    n = len(s)
    sufixo = [s[i:] for i in range(n)]
    print("Sufixos: ")
    for i in range(n):
        print("%3s: %s"%(i, sufixo[i]))
        
    pause()
    
    sufixo.sort()
    print("Sufixos ordenados: ")
    for i in range(n):
        print("%3s: %s"%(i, sufixo[i]))


def pause():
    input("Tecle ENTER para continuar.")
        
if __name__ == "__main__":
    main()
        
              

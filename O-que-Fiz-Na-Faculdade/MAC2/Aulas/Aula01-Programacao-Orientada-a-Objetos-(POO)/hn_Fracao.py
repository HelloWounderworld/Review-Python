from fracao import Fracao

def main():
    n = int(input("Digite n: "))

    # calcule o número harmônico de ordem n
    hn = Fracao()
    for i in range(1, n+1):
        f = Fracao(1,i)
        hn = hn + f
    num, den = hn.get()    
    print("1 + ... + 1/%d + 1/%d = %s = %f" %(n-1, n, hn, num/den))

#---------------------------------------------------
# início da execução do programa
if __name__ == "__main__":
    main()

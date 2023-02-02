def main():
    n = int(input("Digite n: "))

    # calcule o número harmônico de ordem n
    hn = 0
    for i in range(1,n+1):
        f = 1/i
        hn = hn + f
        
    print("1 + ... + 1/%d + 1/%d = " %(n-1,n), hn)

#---------------------------------------------------
# início da execução do programa
if __name__ == "__main__":
    main()

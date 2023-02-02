def tabuada():
    n = int(input("Coloque a dimensao da Linha: "))
    m = int(input("Coloque a dimensao da Coluna: "))
    print(end="\t")
    for l in range(1,m+1):
        print(l, end= "\t")
    print()
    for i in range(1,n+1):
        print(i, end="\t")
        for j in range(1,m+1):
            print(i*j, end="\t")
        print()
tabuada()

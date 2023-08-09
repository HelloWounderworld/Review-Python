def contagemRegressiva(n):
    if n == 0 :
        print("BOOOOOOOMMMMMMMM!!!!!!")
    else:
        print("{}!". format(n))
        contagemRegressiva(n-1)

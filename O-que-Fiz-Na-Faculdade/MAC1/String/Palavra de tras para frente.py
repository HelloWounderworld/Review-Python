def letra_inversa(n):
    x = []
    for i in range(len(n)):
        print(n[-(i+1)], end="\t")
        x.append(n[-(i+1)])
    return x

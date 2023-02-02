def clone_imagem(imagem):
    y = []
    for i in range(len(imagem)):
        x = []
        for j in range(len(imagem[i])):
            x.append(imagem[i][j])
            print(x)
        y.append(x)
    return y
# opcional, discutir com o monitor
'''def clone_imagem_opcional(imagem):
    return imagem[:]''' # essa forma falha pois estaria considerando tt como tt = t, ou seja, tt e t estarao atrelados aos mesmos obejtos.
        

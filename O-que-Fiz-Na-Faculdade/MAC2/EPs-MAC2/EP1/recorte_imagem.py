def recorte_imagem(imagem,tlx,tly,brx,bry):
    y = []
    for i in range(tlx,brx):
        x = []
        for j in range(tly,bry):
            x.append(imagem[i][j])
        y.append(x)
    return y
        

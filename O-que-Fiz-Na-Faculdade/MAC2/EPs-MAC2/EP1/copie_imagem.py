def copie_imagem(dest,orig):
    for i in range(len(orig)):
        for j in range(len(orig[i])):
            dest[i][j]=orig[i][j]
    return dest

from numpymagem import NumPymagem
from numpymutil import mostre_video
from numpymutil import salve_video

def main():
    
    video = []
    '''Para cada iteração preciso estar instanciando um novo objeto, pois se ficar mudando
    somente o posicionamento para o mesmo objeto, como este conserva a mudança anterior,
    entao toda hora, junto com o novo posicionamento, o posicionamento anterior acaba
    aparecendo durante a exibiçao de imagem
    '''
    lin = 59
    col = 79
    Sol_dark = 5
    raio_mercurio = 14
    mercurio = 2
    raio_venus = 20
    venus = 3
    raio_terra = 27
    terra = 5
    raio_marte = 30
    marte = 5
    def Borda(lin,col,raio):
        lista = []
        lista1 = []
        lista2 = []
        lista3 = []
        for i in range(lin,lin+raio):
            lista1.append(i)
        for i in range(col,col+raio):
            lista2.append(i)
        for i in range(lin-raio,lin+1):
            lista3.append(i)
        for i in range(lin-raio+1,lin+1):
            for j in range(col-raio,col+1):
                    if (raio-1)**2<=((i-lin)**2+(j-col)**2)<raio**2:
                        lista.append((i,j))
        for i in range(lin+1,lin+raio+1):
            for j in range(col-raio,col+1):
                if (raio-1)**2<=((i-lin)**2+(j-col)**2)<raio**2:
                    lista.append((i,j))
        for j in range(col,col+raio+1):
            for i in range(len(lista1)):
                if (raio-1)**2<=((lista1[-i-1]-lin)**2+(j-col)**2)<raio**2:
                    lista.append((lista1[-i-1],j))
        for j in range(len(lista2)):
            for i in range(len(lista3)):
                if (raio-1)**2<=((lista3[-i-1]-lin)**2+(lista2[-j-1]-col)**2)<raio**2:
                    lista.append((lista3[-i-1],lista2[-j-1]))
        return lista
    
    print(len(Borda(lin,col,raio_mercurio)))
    print(len(Borda(lin,col,raio_venus)))
    print(len(Borda(lin,col,raio_terra)))
    print(len(Borda(lin,col,raio_marte)))
    for i in range(len(Borda(lin,col,raio_mercurio))):
        lins,cols = Borda(lin,col,raio_mercurio)[i]
        white = NumPymagem(120,160,250)
        white.pinte_disco(lin,col,raio_mercurio,0)#Aqui faz com que some o Sol
        white.pinte_disco(lin,col,raio_mercurio-1,250)
        white.pinte_disco(lins,cols,mercurio,150)
        white.pinte_disco(lin,col,Sol_dark,0)
        video.append(white)
    
    for i in range(len(Borda(lin,col,raio_venus))):
        lins,cols = Borda(lin,col,raio_venus)[i]
        white = NumPymagem(120,160,250)
        white.pinte_disco(lin,col,raio_venus,0)
        white.pinte_disco(lin,col,raio_venus-1,250)
        white.pinte_disco(lins,cols,venus,20)
        if i < len(Borda(lin,col,raio_mercurio)):
            lin_mercurio,col_mercurio = Borda(lin,col,raio_mercurio)[i]
            white.pinte_disco(lin,col,raio_mercurio,0)
            white.pinte_disco(lin,col,raio_mercurio-1,250)
            white.pinte_disco(lin_mercurio,col_mercurio,mercurio,150)
            white.pinte_disco(lin,col,Sol_dark,0)
            video.append(white)
        else:
            lin_mercurio,col_mercurio = Borda(lin,col,raio_mercurio)[i-len(Borda(lin,col,raio_mercurio))]
            white.pinte_disco(lin,col,raio_mercurio,0)
            white.pinte_disco(lin,col,raio_mercurio-1,250)
            white.pinte_disco(lin_mercurio,col_mercurio,mercurio,150)
            white.pinte_disco(lin,col,Sol_dark,0)
            video.append(white)
    for i in range(len(Borda(lin,col,raio_terra))):
        lins,cols = Borda(lin,col,raio_terra)[i]
        white = NumPymagem(120,160,250)
        white.pinte_disco(lin,col,raio_terra,0)
        white.pinte_disco(lin,col,raio_terra-1,250)
        white.pinte_disco(lins,cols,terra,200)
        if i < len(Borda(lin,col,raio_venus)):
            lin_venus,col_venus = Borda(lin,col,raio_venus)[i]
            white.pinte_disco(lin,col,raio_venus,0)
            white.pinte_disco(lin,col,raio_venus-1,250)
            white.pinte_disco(lin_venus,col_venus,venus,20)
            if i < len(Borda(lin,col,raio_mercurio)):
                lin_mercurio,col_mercurio = Borda(lin,col,raio_mercurio)[i]
                white.pinte_disco(lin,col,raio_mercurio,0)
                white.pinte_disco(lin,col,raio_mercurio-1,250)
                white.pinte_disco(lin_mercurio,col_mercurio,mercurio,150)
                white.pinte_disco(lin,col,Sol_dark,0)
                video.append(white)
            else:
                lin_mercurio,col_mercurio = Borda(lin,col,raio_mercurio)[i-len(Borda(lin,col,raio_mercurio))]
                white.pinte_disco(lin,col,raio_mercurio,0)
                white.pinte_disco(lin,col,raio_mercurio-1,250)
                white.pinte_disco(lin_mercurio,col_mercurio,mercurio,150)
                white.pinte_disco(lin,col,Sol_dark,0)
                video.append(white)
        else:
            lin_venus,col_venus = Borda(lin,col,raio_venus)[i-len(Borda(lin,col,raio_venus))]
            white.pinte_disco(lin,col,raio_venus,0)
            white.pinte_disco(lin,col,raio_venus-1,250)
            white.pinte_disco(lin_venus,col_venus,venus,20)
            if i < len(Borda(lin,col,raio_mercurio)):
                lin_mercurio,col_mercurio = Borda(lin,col,raio_mercurio)[i]
                white.pinte_disco(lin,col,raio_mercurio,0)
                white.pinte_disco(lin,col,raio_mercurio-1,250)
                white.pinte_disco(lin_mercurio,col_mercurio,mercurio,150)
                white.pinte_disco(lin,col,Sol_dark,0)
                video.append(white)
            else:
                lin_mercurio,col_mercurio = Borda(lin,col,raio_mercurio)[i-len(Borda(lin,col,raio_mercurio))]
                white.pinte_disco(lin,col,raio_mercurio,0)
                white.pinte_disco(lin,col,raio_mercurio-1,250)
                white.pinte_disco(lin_mercurio,col_mercurio,mercurio,150)
                white.pinte_disco(lin,col,Sol_dark,0)
                video.append(white)
    for i in range(len(Borda(lin,col,raio_marte))):
        lins,cols = Borda(lin,col,raio_marte)[i]
        white = NumPymagem(120,160,250)
        white.pinte_disco(lin,col,raio_marte,0)
        white.pinte_disco(lin,col,raio_marte-1,250)
        white.pinte_disco(lins,cols,marte,40)
        if i < len(Borda(lin,col,raio_terra)):
            lin_terra,col_terra = Borda(lin,col,raio_terra)[i]
            white.pinte_disco(lin,col,raio_terra,0)
            white.pinte_disco(lin,col,raio_terra-1,250)
            white.pinte_disco(lin_terra,col_terra,terra,200)
            if i < len(Borda(lin,col,raio_venus)):
                lin_venus,col_venus = Borda(lin,col,raio_venus)[i]
                white.pinte_disco(lin,col,raio_venus,0)
                white.pinte_disco(lin,col,raio_venus-1,250)
                white.pinte_disco(lin_venus,col_venus,venus,20)
                if i < len(Borda(lin,col,raio_mercurio)):
                    lin_mercurio,col_mercurio = Borda(lin,col,raio_mercurio)[i]
                    white.pinte_disco(lin,col,raio_mercurio,0)
                    white.pinte_disco(lin,col,raio_mercurio-1,250)
                    white.pinte_disco(lin_mercurio,col_mercurio,mercurio,150)
                    white.pinte_disco(lin,col,Sol_dark,0)
                    video.append(white)
                else:
                    lin_mercurio,col_mercurio = Borda(lin,col,raio_mercurio)[i-len(Borda(lin,col,raio_mercurio))]
                    white.pinte_disco(lin,col,raio_mercurio,0)
                    white.pinte_disco(lin,col,raio_mercurio-1,250)
                    white.pinte_disco(lin_mercurio,col_mercurio,mercurio,150)
                    white.pinte_disco(lin,col,Sol_dark,0)
                    video.append(white)
            else:
                lin_venus,col_venus = Borda(lin,col,raio_venus)[i-len(Borda(lin,col,raio_venus))]
                white.pinte_disco(lin,col,raio_venus,0)
                white.pinte_disco(lin,col,raio_venus-1,250)
                white.pinte_disco(lin_venus,col_venus,venus,20)
                if i < len(Borda(lin,col,raio_mercurio)):
                    lin_mercurio,col_mercurio = Borda(lin,col,raio_mercurio)[i]
                    white.pinte_disco(lin,col,raio_mercurio,0)
                    white.pinte_disco(lin,col,raio_mercurio-1,250)
                    white.pinte_disco(lin_mercurio,col_mercurio,mercurio,150)
                    white.pinte_disco(lin,col,Sol_dark,0)
                    video.append(white)
                else:
                    lin_mercurio,col_mercurio = Borda(lin,col,raio_mercurio)[i-len(Borda(lin,col,raio_mercurio))]
                    white.pinte_disco(lin,col,raio_mercurio,0)
                    white.pinte_disco(lin,col,raio_mercurio-1,250)
                    white.pinte_disco(lin_mercurio,col_mercurio,mercurio,150)
                    white.pinte_disco(lin,col,Sol_dark,0)
                    video.append(white)
        else:
            lin_terra,col_terra = Borda(lin,col,raio_terra)[i-len(Borda(lin,col,raio_terra))]
            white.pinte_disco(lin,col,raio_terra,0)
            white.pinte_disco(lin,col,raio_terra-1,250)
            white.pinte_disco(lin_terra,col_terra,terra,200)
            if i < len(Borda(lin,col,raio_venus)):
                lin_venus,col_venus = Borda(lin,col,raio_venus)[i]
                white.pinte_disco(lin,col,raio_venus,0)
                white.pinte_disco(lin,col,raio_venus-1,250)
                white.pinte_disco(lin_venus,col_venus,venus,20)
                if i < len(Borda(lin,col,raio_mercurio)):
                    lin_mercurio,col_mercurio = Borda(lin,col,raio_mercurio)[i]
                    white.pinte_disco(lin,col,raio_mercurio,0)
                    white.pinte_disco(lin,col,raio_mercurio-1,250)
                    white.pinte_disco(lin_mercurio,col_mercurio,mercurio,150)
                    white.pinte_disco(lin,col,Sol_dark,0)
                    video.append(white)
                else:
                    lin_mercurio,col_mercurio = Borda(lin,col,raio_mercurio)[i-len(Borda(lin,col,raio_mercurio))]
                    white.pinte_disco(lin,col,raio_mercurio,0)
                    white.pinte_disco(lin,col,raio_mercurio-1,250)
                    white.pinte_disco(lin_mercurio,col_mercurio,mercurio,150)
                    white.pinte_disco(lin,col,Sol_dark,0)
                    video.append(white)
            else:
                lin_venus,col_venus = Borda(lin,col,raio_venus)[i-len(Borda(lin,col,raio_venus))]
                white.pinte_disco(lin,col,raio_venus,0)
                white.pinte_disco(lin,col,raio_venus-1,250)
                white.pinte_disco(lin_venus,col_venus,venus,20)
                if i < len(Borda(lin,col,raio_mercurio)):
                    lin_mercurio,col_mercurio = Borda(lin,col,raio_mercurio)[i]
                    white.pinte_disco(lin,col,raio_mercurio,0)
                    white.pinte_disco(lin,col,raio_mercurio-1,250)
                    white.pinte_disco(lin_mercurio,col_mercurio,mercurio,150)
                    white.pinte_disco(lin,col,Sol_dark,0)
                    video.append(white)
                else:
                    lin_mercurio,col_mercurio = Borda(lin,col,raio_mercurio)[i-len(Borda(lin,col,raio_mercurio))]
                    white.pinte_disco(lin,col,raio_mercurio,0)
                    white.pinte_disco(lin,col,raio_mercurio-1,250)
                    white.pinte_disco(lin_mercurio,col_mercurio,mercurio,150)
                    white.pinte_disco(lin,col,Sol_dark,0)
                    video.append(white)
        
    
    print("Quantidade de Frames:", len(video))
    

    mostre = True
    if mostre:
        mostre_video(video)

    salve = False
    if salve:
        print("Salvando vídeo")
        salve_video(video)

#-------------------------------------------------------------------------- 
#
# ESCREVA OUTRAS FUNÇÕES E CLASSES QUE DESEJAR
#-------------------------------------------------------------------------- 


#-------------------------------------------------------------------------- 
if __name__ == '__main__':
    main()

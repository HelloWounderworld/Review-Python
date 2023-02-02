from numpymagem import NumPymagem
from numpymutil import mostre_video
from numpymutil import salve_video

def Borda(lin,col,raio):
        lista = []
        lista1 = []
        lista2 = []
        lista3 = []
        for i in range(lin-1,lin+raio+1):
            lista1.append(i)
        for i in range(col-1,col+raio+1):
            lista2.append(i)
        for i in range(lin-raio+1,lin+1):
            lista3.append(i)
        for i in range(lin-raio,lin+1):
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

def main():
    video = []
    video_venus = []
    video_terra = []
    lin = 59
    col = 79
    Sol_dark = 5
    raio_mercurio = 9
    mercurio = 2
    raio_venus = 18
    venus = 3
    raio_terra = 33
    terra = 5
    raio_marte = 58
    marte = 5
    
    for i in range(len(Borda(lin,col,raio_mercurio))):
        lins,cols = Borda(lin,col,raio_mercurio)[i]
        white = NumPymagem(120,160,250)
        white.pinte_disco(lin,col,raio_mercurio,0)#Aqui faz com que some o Sol
        white.pinte_disco(lin,col,raio_mercurio-1,250)
        white.pinte_disco(lins,cols,mercurio,100)
        white.pinte_disco(lin,col,Sol_dark,0)
        video.append(white)
        
    for i in range(len(Borda(lin,col,raio_venus))):
        lins,cols = Borda(lin,col,raio_venus)[i]
        white = NumPymagem(120,160,250)
        white.pinte_disco(lin,col,raio_venus,0)
        white.pinte_disco(lin,col,raio_venus-1,250)
        white.pinte_disco(lins,cols,venus,20)
        recorte = video[i].crop(lin-raio_mercurio,col-raio_mercurio,lin+raio_mercurio,col+raio_mercurio)
        white.paste(recorte,lin-raio_mercurio,col-raio_mercurio)
        video.append(white)
        video_venus.append(white)
    
    for i in range(len(Borda(lin,col,raio_terra))):
        lins,cols = Borda(lin,col,raio_terra)[i]
        white = NumPymagem(120,160,250)
        white.pinte_disco(lin,col,raio_terra,0)
        white.pinte_disco(lin,col,raio_terra-1,250)
        white.pinte_disco(lins,cols,terra,120)
        recorte = video_venus[i].crop(lin-raio_venus-venus,col-raio_venus-venus,lin+raio_venus+venus,col+raio_venus+venus)
        white.paste(recorte,lin-raio_venus-venus,col-raio_venus-venus)
        video.append(white)
        video_venus.append(white)
        video_terra.append(white)
    
    for i in range(len(Borda(lin,col,raio_marte))):
        lins,cols = Borda(lin,col,raio_marte)[i]
        white = NumPymagem(120,160,250)
        white.pinte_disco(lin,col,raio_marte,0)
        white.pinte_disco(lin,col,raio_marte-1,250)
        white.pinte_disco(lins,cols,marte,200)
        recorte = video_terra[i].crop(lin-raio_terra-terra,col-raio_terra-terra,lin+raio_terra+terra,col+raio_terra+terra)
        white.paste(recorte,lin-raio_terra-terra,col-raio_terra-terra)
        video.append(white)
        video_terra.append(white)
    
    branco = NumPymagem(120,160,0)
    for i in range(0,100):
        video.append(branco)
    conta = 0
    cor = [100,150,200,250]
    for i in range(0,250,5):
        quadro = NumPymagem(120,160,250)        
        for j in range(len(cor)):
            anterior = video[-1]
            quadro.paste(anterior,0,0)
            if conta != 57:
                color = NumPymagem(120,160,cor[j])
                recorte = color.crop(conta+3,conta+4,120-(conta+3),160-(conta+4))
                quadro.paste(recorte,conta+3,conta+4)
                conta+=1
                for l in range(0,10):
                    video.append(quadro)
            else:
                break
    count = []
    for h in range(56):
        count.append(h)
    for p in range(len(count)):
        for t in range(len(Borda(count[-p-1]+3,count[-p-1]+4,3))):
            quadro = NumPymagem(120,160,250)
            anterior = video[-1]
            quadro.paste(anterior,0,0)
            line,colum = Borda(count[-p-1]+3,count[-p-1]+4,3)[t]
            recorte = anterior.crop(count[-p-1]+3,count[-p-1]+4,120-(count[-p-1]+3),160-(count[-p-1]+4))
            quadro.paste(recorte,line,colum)
            video.append(quadro)
    
    #print("Quantidade de Frames:", len(video))
        
    mostre = True
    if mostre:
        mostre_video(video)

    salve = False
    if salve:
        print("Salvando vídeo")
        salve_video(video)
        
if __name__ == '__main__':
    main()

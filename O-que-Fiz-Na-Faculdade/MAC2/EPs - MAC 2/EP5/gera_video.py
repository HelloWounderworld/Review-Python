# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome:Leonardo Takashi Teramatsu
    NUSP:9797083

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''

from numpymagem import NumPymagem
from numpymutil import mostre_video
from numpymutil import salve_video

# Escreva aqui outras constantes que desejar
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

ALTURA  = 120
LARGURA = 160
BLACK = 0
WHITE = 250

#-------------------------------------------------------------------------- 

def main():
    ''' (None) -> None
    Escreva o seu programa que cria o vídeo como descrito no enunciado.
    
    O código abaixo serve para ilustrar como usar a função mostre_video()
    que recebe uma lista com NumPymagens e as mostra em um vídeo na tela
    do seu computador usando PyGame. Por isso lembre-se de seguir as 
    instruções para instalar PyGame no seu computador.

    Remova ou altere o código para gerar o seu próprio vídeo. Não se esqueça
    de criar funções para facilitar o entendimento do seu vídeo.

    Você pode (mas não precisa!) salvar o seu vídeo em um formato mp4, para
    mostrar sua obra no fórum da disciplina. Para isso, antes de salvar, 
    você deve instalar o software ffmpeg que você pode baixar de 
    https://ffmpeg.org/download.html. 
    '''
    
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
        white = NumPymagem(ALTURA,LARGURA,WHITE)
        white.pinte_disco(lin,col,raio_mercurio,0)#Aqui faz com que some o Sol
        white.pinte_disco(lin,col,raio_mercurio-1,250)
        white.pinte_disco(lins,cols,mercurio,100)
        white.pinte_disco(lin,col,Sol_dark,0)
        video.append(white)
        
    for i in range(len(Borda(lin,col,raio_venus))):
        lins,cols = Borda(lin,col,raio_venus)[i]
        white = NumPymagem(ALTURA,LARGURA,WHITE)
        white.pinte_disco(lin,col,raio_venus,0)
        white.pinte_disco(lin,col,raio_venus-1,250)
        white.pinte_disco(lins,cols,venus,20)
        recorte = video[i].crop(lin-raio_mercurio,col-raio_mercurio,lin+raio_mercurio,col+raio_mercurio)
        white.paste(recorte,lin-raio_mercurio,col-raio_mercurio)
        video.append(white)
        video_venus.append(white)
    
    for i in range(len(Borda(lin,col,raio_terra))):
        lins,cols = Borda(lin,col,raio_terra)[i]
        white = NumPymagem(ALTURA,LARGURA,WHITE)
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
        white = NumPymagem(ALTURA,LARGURA,WHITE)
        white.pinte_disco(lin,col,raio_marte,0)
        white.pinte_disco(lin,col,raio_marte-1,250)
        white.pinte_disco(lins,cols,marte,200)
        recorte = video_terra[i].crop(lin-raio_terra-terra,col-raio_terra-terra,lin+raio_terra+terra,col+raio_terra+terra)
        white.paste(recorte,lin-raio_terra-terra,col-raio_terra-terra)
        video.append(white)
        video_terra.append(white)
    
    branco = NumPymagem(ALTURA,LARGURA,BLACK)
    for i in range(0,100):
        video.append(branco)
    conta = 0
    cor = [100,150,200,250]
    for i in range(0,250,5):
        quadro = NumPymagem(ALTURA,LARGURA,WHITE)        
        for j in range(len(cor)):
            anterior = video[-1]
            quadro.paste(anterior,0,0)
            if conta != 57:
                color = NumPymagem(ALTURA,LARGURA,cor[j])
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
            quadro = NumPymagem(ALTURA,LARGURA,WHITE)
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
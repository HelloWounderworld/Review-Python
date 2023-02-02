from numpymagem import NumPymagem
from numpymutil import mostre_video
from numpymutil import salve_video

# Escreva aqui outras constantes que desejar
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
    preto = NumPymagem(ALTURA, LARGURA, BLACK)    
    branco = NumPymagem(ALTURA, LARGURA, WHITE)
    cor = BLACK

    for i in range(60): # gera 2s de fundo preto
        video.append(preto)
    for i in range(60): # muda fundo para branco, gradualmente
        cor = (cor+3)%WHITE
        cinza = NumPymagem(ALTURA, LARGURA, cor)
        video.append(cinza)
    for i in range(60): # mostra 2s de fundo branco
        branco = NumPymagem(ALTURA, LARGURA, cor)
        video.append(branco)
    for i in range(60): # volta para preto
        cor = (cor-3)%WHITE
        cinza = NumPymagem(ALTURA, LARGURA, cor)
        video.append(cinza)

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
#
#-------------------------------------------------------------------------- 


#-------------------------------------------------------------------------- 
if __name__ == '__main__':
    main()


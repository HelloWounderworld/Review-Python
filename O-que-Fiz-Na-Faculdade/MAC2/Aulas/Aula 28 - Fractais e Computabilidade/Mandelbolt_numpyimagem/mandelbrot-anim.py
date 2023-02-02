# EP04
from numpymagem import NumPymagem    

# EP05
from numpymutil import mostre_video
from numpymutil import salve_video

import sys

# N, COLOR_MAP, FRAMES, WHITE, ZOOM
from config import *

def main(argv=None):
    if argv == None:
        argv = sys.argv
    nome_programa = argv[0]
    argc = len(argv)    
    if argc < 4:
        mostre_uso(nome_programa)
        return
    try:
        # centro da imagem
        xc   = float(argv[1]);
        yc   = float(argv[2]);
        # largura da imegam
        size = float(argv[3]);
    except:
        mostre_uso(nome_programa)
        return

    color_map = COLOR_MAP
    if argc == 5: color_map = argv[4]

    n    = N    # create N-by-N image
    maxi = MAX  # maximum number of iterations
    video = [None]*FRAMES
    for k in range(FRAMES):
        print("gerando imagem:", k, "de", FRAMES)
        img = NumPymagem(N, N, WHITE)
        for lin in range(n):
            for col in range(n):
                x = xc - size/2 + size*col/n
                y = yc + size/2 - size*lin/n
                c = complex(x, y)
                cor = maxi - mandel(c, maxi)
                img.put(lin, col, cor)
        video[k] = img
        size /= ZOOM # ZOOM e levemente maior que 1 
        
    # crie e mostre animação
    salve_video(video)
    mostre_video(video)

#----------------------------------------------------    
def mandel(c, maxi):
    '''(complex, int) -> int

    Retorna o número t < maxi de iterações até a sequência iterada
    começando em 0 deixar o interior do círculo de raio 2.
    Se a sequência não deixar o interior do círculo de
    raio 2 em maxi iterações a função retorna maxi.
    '''
    z = 0;
    for t in range(maxi):
        if abs(z) > 2: return t
        z = z*z + c
    return maxi    

#----------------------------------------------------
def mostre_uso(nome_programa):
    msg =   "prompt > python3 %s xc yx size\n"%nome_programa \
          + "        (xc,yc) = coordenadas do centro da imagem\n" \
          + "        size    = tamanho do lado da janela\n"
    print(msg)
    
#-------------------------------------------------------
if __name__ == "__main__":
    main()


import numpy as np
import matplotlib
# This function must be called before importing pyplot for the first
# time; or, if you are not using pyplot, it must be called before
# importing matplotlib.backends. If warn is True, a warning is issued if
# you try and call this after pylab or pyplot have been loaded. In
# certain black magic use cases, e.g. pyplot.switch_backend(), we are
# doing the reloading necessary to make the backend switch work (in some
# cases, e.g., pure image backends) so one can set warn=False to
# suppress the warnings.
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

# N, COLOR_MAP
from config import *

import sys

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
        xc   = float(argv[1])
        yc   = float(argv[2])
        # largura da imagem
        size = float(argv[3])
    except:
        mostre_uso(nome_programa)
        return

    color_map = COLOR_MAP
    if argc == 5: color_map = argv[4]
    
    n    = N    # create n-by-n image
    maxi = MAX  # maximum number of iterations
    img  = [[0 for col in range(n)] for lin in range(n)]    
    for lin in range(n):
        for col in range(n):
            x0 = xc - size/2 + size*col/n
            y0 = yc + size/2 - size*lin/n
            c = complex(x0, y0)
            cor = maxi-mandel(c, maxi)
            img[lin][col] = cor

    # crie e mostre a imagem
    fig = plt.figure(figsize=(10,10)) 
    pcolor = plt.pcolor(img, cmap = color_map)
    fig.canvas.draw()
    plt.show()


#----------------------------------------------------    
def mandel(c, maxi):
    '''(complex, int) -> int

    Retorna o número t < maxi de iterações até a sequência iterada
    começando em 0 deixar o interior do círculo de raio 2.
    Se a sequência não deixar o interior do círculo de
    raio 2 em maxi iterações a função retorna maxi.
    '''
    z = 0
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


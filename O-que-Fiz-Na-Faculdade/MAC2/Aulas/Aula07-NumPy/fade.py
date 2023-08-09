#----------------------------------------------------------------
#   Execução: python3 fade.py n imagem1.jpg imagem2.jpg
#
#  Produce animated effect, fading from image1.jpg to image2.jpg,
#  using n-1 intermediate frames.
#----------------------------------------------------------------
import sys
from PIL import Image
import numpy as np
from pilutil import mostre_animacao

def main(args=None):
    n = int(input("Digite o numero de frames: "))

    # leia imagem origem
    nome_im1 = input("Digite o nome do arquivo com a imagem1: ")
    im1 = Image.open(nome_im1)

    # leia imagem destino
    nome_im2 = input("Digite o nome do arquivo com a imagem2: ")
    im2 = Image.open(nome_im2)
    
    # transforma as imagens para ndarray
    pix1 = np.array(im1)
    pix2 = np.array(im2)
    ims = [None]*(n+1)
    for k in range(n+1):
        alpha = k/n
        pix = (1-alpha)*pix1 + alpha*pix2
        pix = pix.astype('uint8')
        ims[k]=pix
        
    # exibe a animação
    mostre_animacao(ims)

#---------------------------------------------    
if __name__ == "__main__":
    main()

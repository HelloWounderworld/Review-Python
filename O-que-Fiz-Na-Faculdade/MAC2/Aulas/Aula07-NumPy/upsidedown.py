#----------------------------------------------------------------
#   Execução: python3 upsidedown.py imagem.[jpg|...]
#   
#   Lê de um arquivo uma imagem e a exibe a imagem de ponta-cabeça
#----------------------------------------------------------------

from PIL import Image
import numpy as np

def main():
    nome_arq = input("Digite o nome do arquivo com a imagem: ")
    im = Image.open(nome_arq)
    
    # exiba imagem
    print(im.format, im.size, im.mode)
    im.show()
    
    # transform2 a imagem em ndarray 
    pix    = np.array(im)
    
    # reflita o array segundo o eixo horizontal
    pix_ud = np.flipud(im)
    
    # crie uma nova imagem a partir do array
    im_ud = Image.fromarray(pix_ud)
    
    # exiba a nova imagem
    im_ud.show()

#--------------------------------------------------------    
if __name__ == "__main__":
    main()

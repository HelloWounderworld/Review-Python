#----------------------------------------------------------------
#   Execução: python3 rotate.py imagem.jpg
#   
#   Lê de um arquivo uma imagem e a exibe a rotacionada de 90º
#----------------------------------------------------------------

from PIL import Image
import numpy as np

def main():
    nome_arq = input("Digite o nome do arquivo com a imagem: ")
    im = Image.open(nome_arq)
    
    # exiba imagem
    print(im.format, im.size, im.mode)
    # im.show()
    
    # transforme imagem em array 
    pix    = np.array(im)
    
    # rotacione a imagem de 90 graus
    pix_rt = np.rot90(pix, 1)
    
    # crie um nova imagem a partir do array
    im_rt = Image.fromarray(pix_rt)
    
    # exiba a novae imagem
    im_rt.show()

#---------------------------------------------------------    
if __name__ == "__main__":
    main()

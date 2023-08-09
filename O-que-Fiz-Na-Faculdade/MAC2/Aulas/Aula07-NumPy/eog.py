#----------------------------------------------------------------
#   Execução: python3 eog.py
#  
#   Lê de um arquivo uma imagem (jpg, png) e a exibe na tela.
#----------------------------------------------------------------

import sys
from PIL import Image

#----------------------------------------------------------    
def main():
    nome_arq = input("Digite o nome do arquivo: ")
    im = Image.open(nome_arq)
    print(im.format, im.size, im.mode)
    im.show()
    
#----------------------------------------------------------    
if __name__ == "__main__":
    main()

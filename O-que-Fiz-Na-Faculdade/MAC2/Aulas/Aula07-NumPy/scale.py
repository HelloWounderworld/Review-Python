#----------------------------------------------------------------
#   Execução: python3 scale.py imagem.jpg w h
#   
#   Lê de um arquivo uma imagem e a exibe com largura w e altura h
#----------------------------------------------------------------
from PIL import Image
import numpy as np

def main():
    nome_arq  = input("Digite o nome do arquivo com a imagem: ")
    w_novo  = int(input("Digite a nova largura: "))
    h_novo  = int(input("Digite a nova altura: "))
    
    # exiba imagem
    print(im.format, im.size, im.mode)
    im.show()
    
    # transforme imagem em array 
    orig    = np.array(im)

    # mude as dimesões da imagem
    h, w, dim = orig.shape
    dest  = np.zeros( (h_novo, w_novo, dim), 'uint8')
    lin_escala = h/h_novo
    col_escala = w/w_novo
    for lin_dest in range(h_novo):
        for col_dest in range(w_novo):
            lin_orig = int(lin_dest * lin_escala)
            col_orig = int(col_dest * col_escala)
            dest[lin_dest, col_dest] = orig[lin_orig, col_orig]
            
    # crie nova imagem a partir do do array dest
    im_dest = Image.fromarray(dest)
    
    # exiba a imagem
    im_dest.show()

#---------------------------------------------------------    
if __name__ == "__main__":
    main()

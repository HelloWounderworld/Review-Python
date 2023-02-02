from labirinto import *

#------------------------------------------------------
def main():
    arq_lab = input("Digite o nome do arquivo com o labirinto: ")
    try:
        lab = Labirinto(arq_lab)
    except:
        print("Erro ao criar o labirinto do arquivo '%s'"%arq_lab)
        return None
    
    lab.desenhe_lab()
    lab.atualize_posicao(lab.lin_ini,lab.col_ini)
    pause()
    procure_saida(lab, lab.lin_ini, lab.col_ini)
    lab.exitonclick()
    
#-------------------------------------------------------------------
def procure_saida(lab, lin, col):
    '''(Labirinto, int, int) -> bool
    '''
    # tente cada uma das quatro direções a partir da [lin][col] até encontrar a saida.
    # BASE
    # 1. batemos em uma parede
    lab.atualize_posicao(lin, col)
    if lab[lin][col] == PAREDE:
        return False
    # 2. chegamos em um posição que já foi examinada
    if lab[lin][col] == TENTOU or lab[lin][col] == BECO:
        return False
    # 3. encontramos We have found an outside edge not occupied by an obstacle
    if lab.encontrou_saida(lin,col):
        lab.atualize_posicao(lin, col, CAMINHO)
        return True
    lab.atualize_posicao(lin, col, TENTOU)
    # use "short circuiting" para tentar cada uma das 4 direções
    # se necessário
    encontrou = procure_saida(lab, lin-1, col) or \
                procure_saida(lab, lin+1, col) or \
                procure_saida(lab, lin,   col-1) or \
                procure_saida(lab, lin,   col+1)
    if encontrou:
        lab.atualize_posicao(lin, col, CAMINHO)
    else:
        lab.atualize_posicao(lin, col, BECO)
    return encontrou

#--------------------------------------------------------
def pause():
    input("Tecle enter para continuar.")

#-------------------------------------------------------------------
if __name__ == "__main__":
    main()

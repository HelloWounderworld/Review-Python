###############################################################################
 #  Execução:     python3 visualizador.py
 #  Dependencias: percolation.py, pygame
 #
 #  Esse programa ao ser excutado pede ao usuário que selecione uma
 #  dentre duas opções:
 #    - 'i': para ser executado em modo interativo
 #    - 'f': para ler o nome de uma arquivo e o seu conteúdo.
 #
 #  No modo interativo o usuário deve fornecer dois inteiros positivos n e m. 
 #  Esses inteiros são o shape (n, m) de uma grade onde o processo de
 #  percolação será excutado interativamente em uma grade n x m.
 #  O usuário deve clicar em um sítio para que ele seja aberto.
 #
 #  No modo arquivo o programa le de um arquivo a dimensão da grade
 #  e uma sequência de posições de sítios que devem ser abertos um após
 #  o outro. O arquivo percolation_testes.zip tem vários desses arquivos
 #  (extensão .txt) e as imgens que devem ser obtidas (extensão .png).
 #
##############################################################################  

import pygame
from percolation import Percolation # classe da aluna/aluno

#----------------------------------------------------------------------
# valores default
SCREEN_SIZE  = 600  # dimensão janela em pixels -- puro chute
GRID_BORDER  = 2    # margem em pixels da grade
SITIO_SIZE   = None # dimensão do sítio em pixels
SITIO_BORDER = None # margem em pixels de cada sítio
DELAY        = None # em ms?

#-----------------------------------------------------------------------
# Cores
BLUE  = [ 25, 120, 215]
WHITE = [255, 255, 255]
BLACK = [  0,   0,   0]
GRAY  = [100, 100, 100]

#-----------------------------------------------------------------------
def main() :
    pygame.init()
    mode = input("Digite 'i' para modo iterativo e 'f' para ler de arquivo: ")
    if mode == 'i':
        percolateIt()
    else: # digamos que mode == 'f'
        file_name = input("Nome do arquivo: ")
        percolateFromFile(file_name)
    pygame.quit()    

#---------------------------------------------------------------------------
def setScreen(shape):
    '''(tuple) -> "janela"

    Recebe a forma (nlins, ncols) da grade da percolação e de 
    define os dimensões dos atributos da janela baseados nesses
    valores.
    '''
    global SCREEN_SIZE  # dimensão da tela 
    global SITIO_SIZE   # dimensão dos sítios
    global SITIO_BORDER # borda dos sítios
    global DELAY  
    nlins, ncols = shape

    # quantos pixels podem ter cada linha da grade
    lin_size = (SCREEN_SIZE - 2*GRID_BORDER) // nlins

    # quantos pixels podem ter cada coluna da grade
    col_size = (SCREEN_SIZE - 2*GRID_BORDER) // ncols

    # dimensão dos sítios
    SITIO_SIZE = min(lin_size, col_size)

    # dimensão da margem do sítio
    SITIO_BORDER = SITIO_SIZE // 40 # valor chutado
        
    # corrige o tamanho da tela
    H_SIZE = 2*GRID_BORDER + ncols*SITIO_SIZE
    W_SIZE = 2*GRID_BORDER + nlins*SITIO_SIZE

    no_sitios = nlins * ncols
    if no_sitios > 2500:  # outro valor chutado
        DELAY = 1000 // no_sitios
    else:
        DELAY = 6000 // no_sitios

    if SITIO_SIZE > 40:    # mais um valor chutado    
        SITIO_SIZE   = 40  # mais outro
        SITIO_BORDER =  2  # e outro 
        H_SIZE = 2*GRID_BORDER + ncols*SITIO_SIZE
        W_SIZE = 2*GRID_BORDER + nlins*SITIO_SIZE
        
    pygame.display.set_caption("MAC0122 Visualizador de Percolação")
    sc = pygame.display.set_mode((H_SIZE, W_SIZE))

    # desenhe janela inicial
    pygame.draw.rect(sc, WHITE, pygame.Rect(0, 0, H_SIZE, W_SIZE), GRID_BORDER)
 
    return sc 

#-------------------------------------------------------------
def drawPercolation(perc, sc, border_color=BLACK):
    n, m = perc.shape
    for i in range(n):
        for j in range(m):
            rec = pygame.Rect(
                GRID_BORDER+SITIO_SIZE*j,
                GRID_BORDER+SITIO_SIZE*i,
                SITIO_SIZE,
                SITIO_SIZE
            )
            if   perc.is_full(i,j):
                pygame.draw.rect(sc, BLUE, rec)    
            elif perc.is_open(i,j):
                pygame.draw.rect(sc, WHITE, rec)
            pygame.draw.rect(sc, border_color, rec, GRID_BORDER)
    pygame.display.update()

#-------------------------------------------------------------     
def findRec(pos):
    col = (pos[0]-GRID_BORDER) // SITIO_SIZE
    lin = (pos[1]-GRID_BORDER) // SITIO_SIZE
    return col, lin

# --------------------------------------------------------------
def percolateFromFile(file_name):
    '''(str) -> None '''
    try:
        f = open(file_name)
    except:
        print("ERRO: arquivo '%s' não foi encontrado"%file_name)
        return
    
    # leia a dimensão da grade: nos arquivos é apenas um inteiro
    # já que neles as grades são quadradas
    line = f.readline()
    n = int(line)
    
    # crie um objeto Percolation
    perc = Percolation((n, n))
    
    # crie a janela
    screen = setScreen((n, n))
        
    # desenhe a grade
    drawPercolation(perc, screen)

    # leia posições a serem abertas
    line = f.readline()
    running = True 

    while line and running:
        # Limpa a string e Le as coordenadas
        pos = line.split()
        lin = int(pos[0])
        col = int(pos[1])
        
        # abra o sítio
        perc.open(lin, col)

        # desenhe a nova grade na janela
        drawPercolation(perc, screen)
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # espere um pouco        
        pygame.time.delay(DELAY)

        # pegue a nova posição 
        line = f.readline()

    # espere o usuário fechar a janela
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    print("Percolates: ",perc.percolates())
    print("Open sites: ",perc.no_open())
    f.close()

#---------------------------------------------------------    
# Versão Iterativa 
def percolateIt():
    # pegue a dimensão da grade
    dim_str = input("Digite a dimensão da grade (nlins e ncols): ")
    dim_lst = dim_str.split()
    try:
        nlins = int(dim_lst[0])
        ncols = int(dim_lst[1])
    except:
        print("ERRO: dimensão devem ser dois inteiros positivos")
        return
    
    # crie o objeto Percolation
    perc = Percolation((nlins,ncols))
    
    # crie a janela
    screen = setScreen((nlins, ncols))

    # desenhe a grade inicial
    drawPercolation(perc, screen)

    # comece a abrir sítios
    running = True 
    while running:
        # examine a fila de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: # usuário clicou
                # localize o sítio clicado
                col, lin = findRec(event.pos)
                # abra o sítio [lin][col]
                perc.open(lin, col)
                # desenhe a nova grade
                drawPercolation(perc, screen)

    # relatório            
    print("Percolates: ", perc.percolates())
    print("Open sites: ", perc.no_open())
     
if __name__ == "__main__":
    main()

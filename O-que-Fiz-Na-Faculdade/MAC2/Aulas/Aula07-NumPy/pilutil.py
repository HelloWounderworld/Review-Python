import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ========================================================================
def converta(imagens, color_map="gray"):
    ''' (list, str) -> list
    recebe uma lista de pimagens e um string representando um color map 
    (ver https://matplotlib.org/tutorials/colors/colormaps.html) e retorna uma lista de 
    imagens (arrays de Numpy) prontas para serem animadas.
    '''
    npimgs = []
    for img in imagens:
        npimgs.append([plt.imshow( np.array(img), cmap=color_map, vmin=0, vmax=255, animated=True)] )
    return npimgs

# ========================================================================
def mostre_animacao(imagens = [], color_map="gray", interval=50, blit=True, repeat_delay=1000,  ):
    ''' (list) -> None
    Recebe uma lista de Imagens em imagens
    e cria e mostra uma animação dessas Imagens.
    '''
    fig = plt.figure()
    npimgs = converta(imagens, color_map)
    ani = animation.ArtistAnimation(fig, npimgs, interval, blit, repeat_delay)
    plt.show()

# ========================================================================

def salve_animacao(imagens=[], color_map="gray", interval=50, blit=True, repeat_delay=1000 ):
    ''' (list) -> None
    Recebe uma lista de Imagens em imagens
    e cria e mostra uma animação dessas Imagens.
    '''
    fig = plt.figure()
    npimgs = converta(imagens, color_map)
    ani = animation.ArtistAnimation(fig, npimgs, interval, blit, repeat_delay)
    
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps = 15, metadata=dict(artist='mac0122-Mandelbrot'), bitrate=1800)
    ani.save('mandelbrot-'+ color_map + '.mp4', writer=writer)

# ========================================================================

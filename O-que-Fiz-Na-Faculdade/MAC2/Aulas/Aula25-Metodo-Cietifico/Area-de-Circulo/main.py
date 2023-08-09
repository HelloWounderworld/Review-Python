from pi import Pi

# sys.argv
import sys

# math
import math

import matplotlib.pyplot as plt

# parâmetros
from config import *

#------------------------------------------------------
def main(argv=None):
    # pegue argumentos da linha de comando
    if argv == None:
       argv = sys.argv

    # nome programa    
    nome_programa = argv[0]

    # argc = número de experimentos 
    argc = len(argv)
    if argc < 2:
        help(nome_programa)
        return 

    if argv[1] == "-b":
        bilog_plot()
        return
    
    # default
    t = T
    r = 1
    try:
        n = int(argv[1])
        # número de experimentos
        if argc == 3:
            r = float(argv[2])
    except:
        help(nome_programa)

    # print(n, r)    
    # realize os no_exp experimentos
    vpi = Pi(n, t, r)

    # média aritmética
    print("area =", vpi.mean(), "(%f)"%(math.pi*r*r))

#-------------------------------------------------------------
def bilog_plot():
    '''
    Referência: 
    https://panda.ime.usp.br/algoritmos/static/algoritmos/10-matplotlib.html
    '''
    plt.title("MAC0122 Valor de Pi")
    plt.xlabel("log(raio)")
    plt.ylabel("log(area)")
    x = []
    y = []
    n = 10 # pontos sortedados
    r = 1
    x0, y0 = 0, 0
    while r < 33:
        # realize os no_exp experimentos
        area = Pi(n, T, r)
        x1 = math.log(r)
        y1 = math.log(area.mean())
        x.append(x1)
        y.append(y1)
        plt.plot([x0,x1],[y0,y1], 'b-') #mlines.Line2D([x0,y0], [x1,y1])
        x0, y0 = x1, y1
        r *= 2
        
    plt.plot(x, y, 'go') # green bolinha
    plt.show()
    
#-------------------------------------------------------------
def help(nome_prog):
   """ Erro message explvping how to run the program
   """
   print("Uso: python3",nome_prog,"-b | n [r]]")
   print("   -b = gera gráfico bilog")
   print("    n = número de pontos")
   print("    r = raio do círculo")
   print("    t = número de experimentos (default %d)"%T)
        

#--------------------------------------------------------------
if __name__ == "__main__":
    main()

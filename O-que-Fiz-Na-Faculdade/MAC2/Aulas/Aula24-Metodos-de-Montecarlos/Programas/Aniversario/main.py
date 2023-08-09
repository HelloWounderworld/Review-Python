'''
   MAC0122 Princípios de Desenvolvimento de Algoritmos

'''
from aniversario import Aniversario

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

    if argv[1] == "-g":
        grafico()
        return

    if argv[1] == "-a":
        adaptative_plot()
        return
    
    # default
    t = T
    try:
        n = int(argv[1])
        # número de experimentos
        if argv == 3:
            no_exp = int(argv[2])
    except:
        help(nome_programa)

    # realize os no_exp experimentos
    ani = Aniversario(n, t)

    # média aritmética
    print("probabilidade =", ani.mean(), "(%f)"%prob(n))
    
#-------------------------------------------------------------
def adaptative_plot():
    '''
    Referência: 
    https://panda.ime.usp.br/algoritmos/static/algoritmos/10-matplotlib.html
    '''
    # import matplotlib.lines as mlines
    plt.title("MAC0122 Paradoxo do Aniversário")
    plt.xlabel("número de pessoas")
    plt.ylabel("probabilidade")
    # desenhe o ponto inicial e final
    plt.plot([X0, X1], [Y0, Y1], 'go') # green bolinha
    # desenhe a curva entre eles
    curva(X0, Y0, X1, Y1)
    # mostre o gráfico
    plt.show()

#--------------------------------------------------------   
def curva(x0, y0, x1, y1):
    xm = (x0 + x1) // 2;
    ym = (y0 + y1) /  2; # float
    
    # realiza o experimento
    ani = Aniversario(xm,T)
    fxm = ani.mean()
    ani = None # evita 'loitering': essencial quando o espaço é importante
    
    # base da recursão
    if x1 - x0 < GAP or abs(ym - fxm) < ERR:
        # desenha a linha entre [x0,y0] e [x1, y1]
        plt.plot([x0,x1],[y0,y1], 'b-') 
        return None
    
    # desenhe recursivamente a curva entre [x0,y0] e [xm,fm]
    curva(x0, y0, xm, fxm);
    
    # desenhe o ponto [xm,fm]
    plt.plot(xm, fxm, 'go') # green bolinha
    
    # desenhe recursivamente a curva entre [xm,fxm] e [x1,y1]
    curva(xm, fxm, x1, y1);

    
#-------------------------------------------------------------
def grafico():
    '''
    Referência: 
    https://panda.ime.usp.br/algoritmos/static/algoritmos/10-matplotlib.html
    '''
    plt.title("MAC0122 Paradoxo do Aniversário")
    plt.xlabel("número de pessoas")
    plt.ylabel("probabilidade")
    x = []
    y = []
    x0, y0 = X0, Y0
    for n in range(X0, X1, GAP):
        # realize os no_exp experimentos
        ani = Aniversario(n, T)
        x1 = n
        y1 = ani.mean()
        x.append(x1)
        y.append(y1)
        plt.plot([x0,x1],[y0,y1], 'b-') #mlines.Line2D([x0,y0], [x1,y1])
        x0, y0 = x1, y1
    plt.plot(x, y, 'go') # green bolinha
    plt.show()


#----------------------------------------
def prob(n):
    '''
    Retorna a probabilidade teorica.

    import math
    num = math.factorial(DATAS)
    den = math.factorial(DATAS-n)
    prob_c = num/(DATAS**n * den)
    '''
    prob_c = 1
    for i in range(n):
        prob_c *= (1 - i/DATAS)
    return 1 - prob_c
    
#-------------------------------------------------------------
def help(nome_prog):
   """ Erro message explaning how to run the program
   """
   print("Uso: python3",nome_prog,"-g | -a | n [t]]")
   print("   -g = gera gráfico")
   print("   -a = gera gráfico adaptativamente")
   print("    n = número de pessoas")
   print("    t = número de experimentos (default %d)"%T)
        

#--------------------------------------------------------------
if __name__ == "__main__":
    main()

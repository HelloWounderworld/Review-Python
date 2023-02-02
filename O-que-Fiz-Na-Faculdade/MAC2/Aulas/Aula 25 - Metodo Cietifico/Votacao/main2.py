# sys.argv
import sys

from votacao2 import Votacao

from config import *

import matplotlib.pyplot as plt

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
        return None

    if argv[1] == "-g":
        grafico()
        return

    if argv[1] == "-a":
        adaptative_plot()
        return
    
    # default
    t = T
    try:
        # probabilidade de erro
        p_erro = int(argv[1])
        # número de experimentos
        if argc == 3:
            t = int(argv[2])
    except:
        help(nome_programa)

    # realize os t experimentos
    votacao = Votacao(NO_VOTOS, POR_A, p_erro, t)
    
    # média aritmética
    print("probabilidade de alterar resultado= %.3f"%votacao.mean())


#-------------------------------------------------------------
def adaptative_plot():
    '''
    Referência: 
    https://panda.ime.usp.br/algoritmos/static/algoritmos/10-matplotlib.html
    '''
    # import matplotlib.lines as mlines
    plt.title("MAC0122 Voting Machine")
    plt.xlabel("porcentagem de erro")
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
    vot = Votacao(NO_VOTOS, POR_A, xm, T)
    fxm = vot.mean()
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
    plt.title("MAC0122 Voting Machine")
    plt.xlabel("porcentagem de erro")
    plt.ylabel("probabilidade")
    x = []
    y = []
    for p_erro in range(2, 100, 2):
        # realize os no_exp experimentos
        votacao = Votacao(NO_VOTOS, POR_A, p_erro, T)
        x.append(p_erro)
        y.append(votacao.mean())
    plt.plot(x, y, 'go') # green bolinha
    plt.show()
    
#-------------------------------------------------------------
def help(nome_prog):
   """ Erro message explaning how to run the program
   """
   print("Uso: python3",nome_prog,"-g |-a | p_erro [e]")
   print("   -g = gera gráfico")
   print("   -a = gera gráfico adaptativamente")
   print("    p_erro = porcentagem de erro")
   print("    e  = número de experimentos (default %d)"%T)

#--------------------------------------------------------------
if __name__ == "__main__":
    main()

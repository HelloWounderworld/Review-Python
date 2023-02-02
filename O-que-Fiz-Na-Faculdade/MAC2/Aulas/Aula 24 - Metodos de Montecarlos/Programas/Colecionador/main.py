'''
   MAC0122 Princípios de Desenvolvimento de Algoritmos

'''
#
from colecionador import Colecionador

# valores default: N e T
from config import *

# sys.argv
import sys

#------------------------------------------------------
def main(argv=None):
    # pegue argumentos da linha de comando
    if argv == None:
       argv = sys.argv

    # nome programa    
    nome_programa = argv[0]

    # argc = número de parametros
    argc = len(argv)
    if argc < 2:
        help(nome_programa)
        return None
    
    # grafico
    if argv[1] == "-g":
        grafico()
        return None

    # número de exeprimentos
    t = T
    n = N
    try:
        # número de figurinhas
        n = int(argv[1])
        if argv == 3:
            # número de experimentos
            t = int(argv[2])
    except:
        help(nome_programa)

    # realize os t experimentos
    exp = Colecionador(n, t)

    # média aritmética
    print("número de figurinhas compradas = %g (%g)"%(exp.mean(), n*H(n)))
    

#-----------------------------------------------------------
def H(n):
    hn = 0
    for i in range(n,0,-1):
        hn += 1/i
    return hn

#-------------------------------------------------------------
def grafico():
    import matplotlib.pyplot as plt
    plt.title("MAC0122 Coupon collector's")
    plt.xlabel("tamanho do álbum")
    plt.ylabel("no. figurinhas a comprar")
    x = []
    y = []
    x0, y0 = 0, 0
    for n in range(X0, X1, GAP):
        # realize os T experimentos
        exp = Colecionador(n, T)
        x1 = n
        y1 = exp.mean()
        x.append(n)
        y.append(exp.mean())
        plt.plot([x0,x1],[y0,y1], "b-")
        x0, y0 = x1, y1
    plt.plot(x, y, 'go') # green bolinha
    plt.show()
    
#-------------------------------------------------------------
def help(nome_prog):
   """ Erro message explaning how to run the program
   """
   print("Uso: python3",nome_prog,"[n [t] | -g]")
   print("    n = número de figurinhas")
   print("    t = número de experimentos")
   print("   -g = para gerar gráfico")
        

#--------------------------------------------------------------
if __name__ == "__main__":
    main()
    

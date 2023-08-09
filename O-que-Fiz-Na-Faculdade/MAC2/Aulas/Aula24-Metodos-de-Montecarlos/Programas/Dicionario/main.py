'''
   MAC0122 Princípios de Desenvolvimento de Algoritmos

'''
#
from sala import Sala

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
    try:
        n = int(argv[1])
        m = int(argv[2])
    except:
        help(nome_programa)
        return None

    # realize os t experimentos
    sala = Sala(n, m)

    print(sala)
    print()
    print("no. grupos: %s"%sala.no_grupos())
    print("média sondagens em busca bem-sucedida: %.2f"%sala.media_bemsucedidas())
    print("média sondagens em bascu  malsucedida: %.2f"%sala.media_malsucedidas())
    

#-------------------------------------------------------------
def help(nome_prog):
   """ Erro message explaning how to run the program
   """
   print("Uso: python3",nome_prog,"n m")
   print("    n = número de alunos")
   print("    m = número de carteiras")
        

#--------------------------------------------------------------
if __name__ == "__main__":
    main()
    

'''
  MAC0122 Principios de Desenvolvimento de Algoritmos
  
  Torres de Hanoi: versão recursiva
'''

# sys.argv
import sys

#------------------------------------------------------
def main(argv=None):

    # pegue argumentos da linha de comando
    if argv == None:
       argv = sys.argv

    # nome programa    
    nome_programa = "hanoi.py" # argv[0]

    # argc = número de argumentos 
    argc = len(argv)
    if argc < 2:
        help(nome_programa)
        return None

    try:
        # número de discos
        no_discos = int(argv[1])
    except:
        help(nome_programa)
        return None
    
    hanoi (no_discos,'A','B','C')

#----------------------------------------------------------
def hanoi(no_discos, origem, auxiliar, destino):
    '''(int,str,str,str) -> None

    Recebe o numero de discos 'no_discos', o pinos
    origem, auxiliar e destino e o número do proximo
    movimento e imprime as mesagens que resolvem o
    problema das torres de Hanoi.

    Exemplo:
    >>> hanoi(3,'A','B','C')
    1: mova o disco 1 da torre A para a torre C.
    2: mova o disco 2 da torre A para a torre B.
    3: mova o disco 1 da torre C para a torre B. 
    4: mova o disco 3 da torre A para a torre C.
    5: mova o disco 1 da torre B para a torre A.
    6: mova o disco 2 da torre B para a torre C.
    7: mova o disco 1 da torre A para a torre C.
    '''

    if no_discos > 0:
        hanoi(no_discos-1, origem, destino, auxiliar)
        mova_disco(no_discos, origem, destino)
        hanoi(no_discos-1, auxiliar, origem, destino)
        

#----------------------------------------------------------
def mova_disco(n, origem, destino):
    '''(int,str,str) -> None

    Recebe o número de um disco e o nomes dos pinos origem e
    destino e imprime a mensagem de movimento do disco 
    da origem para o destino.

    Na mensagem, mova_disco.mov é o número do movimento.
    '''
    # contador de movimentos
    try:
        mova_disco.mov += 1
    except:
        # para a primeira vez
        mova_disco.mov = 1
    
    print("%d: mova o disco %d da torre %s para a torre %c." 
          %(mova_disco.mov, n, origem, destino))
    

#-------------------------------------------------------------
def help(nome_prog):
   """ Erro message explaning how to run the program
   """
   print("Uso: python3",nome_prog,"n") 
   print("   n = número de discos")
        

#--------------------------------------------------------------
if __name__ == "__main__":
    main()

'''
  MAC0122 Principios de Desenvolvimento de Algoritmos
  
  Torres de Hanoi: versão recursiva
'''
#------------------------------------------------------
def main(argv=None):
    no_discos = int(input("hanoi: digite o no. de discos: "))
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
    mova o disco 1 da torre A para a torre C.
    mova o disco 2 da torre A para a torre B.
    mova o disco 1 da torre C para a torre B. 
    mova o disco 3 da torre A para a torre C.
    mova o disco 1 da torre B para a torre A.
    mova o disco 2 da torre B para a torre C.
    mova o disco 1 da torre A para a torre C.
    '''
    if no_discos == 0: return
    hanoi(no_discos-1, origem, destino, auxiliar)
    print("mova o disco %d da torre %s para a torre %c." 
          %(no_discos, origem, destino))
    hanoi(no_discos-1, auxiliar, origem, destino)
        
#--------------------------------------------------------------
if __name__ == "__main__":
    main()

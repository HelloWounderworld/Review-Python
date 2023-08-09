'''
  MAC0122 Principios de Desenvolvimento de Algoritmos
  
  Torres de Hanoi: versão recursiva
'''

#----------------------------------------------------------
def hanoi(no_discos, origem, auxiliar, destino):
    '''(int,str,str,str) -> None

    Recebe o numero de discos 'no_discos', o pinos
    origem, auxiliar e destino e o número do proximo
    movimento e imprime as mesagens que resolvem o
    problema das torres de Hanoi.
    '''

    if no_discos > 0:
        hanoi(no_discos-1, origem, destino, auxiliar)
        mova_disco(no_discos, origem, destino)
        hanoi(no_discos-1, auxiliar, origem, destino)
        
#----------------------------------------------------------
def mova_disco(n, origem, destino):
    '''(int,str,str) -> None

    Recebe o número de um disco e os nomes dos origem e
    destino e imprime a mensagem de movimento do disco 
    da origem para o destino. 
    '''

    print("mova o disco %d da torre %s para a torre %c." 
          %(n, origem, destino))
    

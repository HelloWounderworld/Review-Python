#-----------------------------------------------------------------------------
#
# MAC0122 Princípio de Desenvolvimento de Algoritmos
#
# Programa que lê uma lista de palavras e imprime as palavras removendo
# repetições
#
# python dedup_list.py < tinyTale.txt
#
# main(): lendo o texto ...
# main(): texto lido ...
# main(): removendo pontuação ...
# main(): pontuação removida ...
# main(): criando lista de palavras ...
# main(): lista com 60 palavras criada ...
# main(): criando lista de palavras ...
# main(): lista com 20 palavras criado
# elapsed time     = 0.000
# main(): mostra dom 20 palavras no texto:
# it
# was
# the
# best
# of
# times
# worst
# age
# wisdom
# foolishness
# epoch
# belief
# incredulity
# season
# light
# darkness
# spring
# hope
# winter
# despair
#
#----------------------------------------------------------------------------

# para cronometrar o tempo gasto
import time

# constantes
import string
# >>> string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# para substituir pontuação por " "
import re

#------------------------------------------------------------------------
def main():
    # leia o texto
    nome_arq = input("Digite o nome do arquivo com o texto: ")
    print("main(): lendo o texto ...")
    with open(nome_arq, "r", encoding="utf-8") as arq:
        texto = arq.read()
    print("main(): texto lido ...")
    # print(texto)

    # substitui pontuação por " "
    print("main(): removendo pontuação ...")
    texto = re.sub("["+string.punctuation+"]", " ", texto) 
    print("main(): pontuação removida ...")
    # print(texto)

    # crie lista de palavras
    print("main(): criando lista de palavras ...")
    lista_pals = texto.split()
    print("main(): lista com %s palavras criada ..."%len(lista_pals))

    # cria lista com palavras sem repetições    
    print("main(): criando lista de palavras sem repeticoes ...")
    inicio = time.time()
    pals = sem_repetidos(lista_pals)
    print("main(): lista com %s palavras criado"%(len(lst_pals)))
    fim = time.time()
    print("elapsed time     = %.3f"%(fim-inicio))
    
    print("main(): mostra dom 20 palavras no texto:")
    i = 0
    for pal in pals:
        print(pal)
        i += 1
        if i == 20: break

#----------------------------------------------------------------        
def sem_repetidos(lst):
    '''(lst) -> lst 
    Retorna uma lista com o itens em lst sem repetições
    '''
    lst_pals = []
    for pal in lst:
        if pal not in lst_pals: # O(n) no pior caso, onde n é o número de palavras em lst_pals
            lst_pals.append(pal) # O(1)
    return lst_pals
            
#------------------------------------------------------------------------
if __name__ == "__main__":
    main()

        
        

#-----------------------------------------------------------------------------
#
# MAC0122 Princípio de Desenvolvimento de Algoritmos
#
# Programa que lê uma lista de palavras e imprime os grupos de palavras 
# que são anagramas umas das outras.
#
#----------------------------------------------------------------------------

# para cronometrar o tempo gasto
import time

#------------------------------------------------------------------------
def main():
    # leia o texto
    nome_arq = input("Digite o nome do arquivo com as palavras: ")
    print("main(): lendo as palavras ...")
    with open(nome_arq, "r", encoding="utf-8") as arq:
        pals = arq.read()
    print("main(): palavras lidas ...")
    # print(pals)

    print("main(): criando lista de palavras ...")
    lst_pals = pals.split()
    print("main(): lista com %s palavras criada ..."%len(lst_pals))

    print("main(): criando dicionário de anagramas ...")
    inicio = time.time()
    dicio_anagramas = anagramas(lst_pals)
    fim = time.time()
    print("main(): dicionário com %s anagramas criado"%(len(dicio_anagramas)))
    print("elapsed time     = %.3f"%(fim-inicio))

    print("main(): mostra os anagramas:")
    for chave in dicio_anagramas:
        if len(dicio_anagramas[chave]) > 1:
            print("%s: "%chave, end="")
            for pal in dicio_anagramas[chave]:
                print(pal, end=' ')
            print() # muda de linha

def anagramas(lst_pals):
    ''' (list) -> dict
    Retorna um dicionário em que cada chave é uma string
    e o correspondente valor é o conjunto de anagramas da 
    string.
    '''
    dicio_anagramas = {}
    for pal in lst_pals:
        # letras na palavra
        pal_aux = list(pal)

        # letras ordenadas
        pal_aux.sort()

        # cria a chave do dicionário
        chave = ''.join(pal_aux)

        # se a chave não está no dicionário insira
        if chave not in dicio_anagramas: # O(1) esperado
            dicio_anagramas[chave] = set()

        # coloque o anagrama no cojunto da chave    
        dicio_anagramas[chave].add(pal)

    return dicio_anagramas        
        
#------------------------------------------------------------------------
if __name__ == "__main__":
    main()

        
        

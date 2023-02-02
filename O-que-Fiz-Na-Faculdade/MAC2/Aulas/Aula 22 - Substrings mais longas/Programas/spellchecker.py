#-----------------------------------------------------------------------------
#
# MAC0122 Princípio de Desenvolvimento de Algoritmos
#
# Lê um arquivo com um as palavras de um dicionário e um texto e imprime as
# palavras do texto que não estão no dicionário.
#
# python spellchecker.py < texto.txt
#
#----------------------------------------------------------------------------

# para cronometrar o tempo gasto
import time

# para substituir pontuação por " "
import re

# constantes
import string
# >>> string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

#------------------------------------------------------------------------
def main():
    
    print("main(): lendo palavras no dicionário ...")
    set_pals = set()
    with open("../txt/words.utf-8.txt", "r", encoding="utf-8") as arq:
        for line in arq:
            pal = line.strip().lower()
            set_pals.add(pal)
    print("main(): dicionário criado com %s palavras"%len(set_pals))            


    nome_arq = input("Digite o nome do arquivo com o texto: ")
    print("main(): lendo texto...")
    inicio = time.time()
    with open(nome_arq, "r", encoding="utf-8") as arq:
        texto = arq.read()
    print("main(): texto lido")

    linhas_texto = texto.split("\n")
    no_lin = 0
    conta  = 0
    for linha in linhas_texto:
        linha = re.sub("["+string.punctuation+"]", " ", linha) # substitui pontuação por " "
        lista_pals = linha.split()
        for pal in lista_pals:
            pal = pal.lower()
            if pal != "" and pal not in set_pals:
                print("%s: %s"%(no_lin, pal))
                conta += 1           
        no_lin += 1
    fim = time.time()                  
    print("main(): verificação encerrada.")
    print("main(): foram encontradas %s palavras desconhecidas"%conta)
    print("elapsed time     = %.3f"%(fim-inicio))
            
#------------------------------------------------------------------------
if __name__ == "__main__":
    main()

        
        

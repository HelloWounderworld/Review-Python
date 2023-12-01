# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
#Fazer!
import os

def listar(lista):
    print()
    if not lista:
        print('Não há nada a ser listado!')
        return

    print('Tarefas:')
    for tarefa in lista:
        print(f'{tarefa}')
    print()

def desfazer(lista, listaRefaz):
    print()
    if not lista:
        print('Não há nada a ser desfeito!')
        return

    listaRefaz.append(lista.pop())
    print()

def refazer(listaRefaz, lista):
    print()
    if not listaRefaz:
        print('ListaRefaz vazio')
        return

    lista.append(listaRefaz.pop())
    print()

def adicionar(argumento, lista):
    print()
    argumento = argumento.strip()
    if not argumento:
        print('Você precisa digitar algo!')
        return
    lista.append(argumento)
    print()

guardando_sigla = {'listar': 0, 'desfazer': 1, 'refazer': 2, 'clear': 3}
# print(tuple(guardando_sigla.keys())[0])
# print(tuple(guardando_sigla.keys())[1])
# print(tuple(guardando_sigla.keys())[2])
# print(tuple(guardando_sigla.keys())[3])

lista = []
listaRefaz = []

# Motivo de ter usado o continue:
# É mais para garantir que nada depois dela será executado!
while (True):
    print('Comandos: listar, desfazer e refazer')
    entrada = input('Digite uma tarefa ou comando: ')
    
    if entrada == 'listar':
        listar(lista)
        continue

    elif entrada == 'desfazer':
        desfazer(lista, listaRefaz)
        listar(lista)
        continue

    elif entrada == 'refazer':
        refazer(listaRefaz, lista)
        listar(lista)
        continue

    elif entrada == 'clear':
        # aqui serve para dar o comando "clear" para limpar o terminal
        os.system('clear')
        continue

    else:
        adicionar(entrada, lista)
        listar(lista)
        continue

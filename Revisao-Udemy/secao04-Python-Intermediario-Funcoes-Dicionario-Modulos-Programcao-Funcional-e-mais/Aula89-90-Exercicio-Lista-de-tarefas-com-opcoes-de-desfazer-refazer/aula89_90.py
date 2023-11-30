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

def desfazer(lista):
    if not lista:
        print('Não há nada a ser desfeito!')
        return

    lista.pop()
    return lista

def refazer(listaRefaz, lista):
    if not listaRefaz:
        print('ListaRefaz vazio')
        return
    
    if not lista:
        print('Não há nada para refazer!')
        return

    lista.append(listaRefaz[0])
    listaRefaz.pop(0)
    return lista

def adicionar(argumento, lista):
    lista.append(argumento)

guardando_sigla = {'listar': 0, 'desfazer': 1, 'refazer': 2, 'clear': 3}
# print(tuple(guardando_sigla.keys())[0])
# print(tuple(guardando_sigla.keys())[1])
# print(tuple(guardando_sigla.keys())[2])
# print(tuple(guardando_sigla.keys())[3])

lista = []
listaRefaz = []

while (True):
    print('Comandos: listar, desfazer e refazer')
    entrada = input('Digite uma tarefa ou comando: ')
    print('Entrada: ', entrada)
    
    if entrada == 'listar':
        print(tuple(guardando_sigla.keys())[0])
        listar(lista)
        ...
    elif entrada == 'desfazer':
        print(tuple(guardando_sigla.keys())[1])
        desfazer(lista)

    elif entrada == 'refazer':
        print(tuple(guardando_sigla.keys())[2])
        refazer(listaRefaz, lista)
        ...
    elif entrada == 'clear':
        # aqui serve para dar o comando "clear" para limpar o terminal
        os.system(tuple(guardando_sigla.keys())[3])
        ...
    else:
        print('Entrei para add')
        adicionar(entrada, lista)
        listar(lista)

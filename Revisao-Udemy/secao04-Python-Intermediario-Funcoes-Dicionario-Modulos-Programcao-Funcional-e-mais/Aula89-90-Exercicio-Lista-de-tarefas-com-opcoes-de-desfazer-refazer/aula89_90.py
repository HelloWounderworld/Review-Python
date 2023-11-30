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
import os

def listar(argumento, lista=None):
    if lista is None:
        lista = []

    lista.append(argumento)
    return lista

def desfazer(lista=None):
    if lista is None:
        lista = []

    lista.pop()
    return lista

def refazer(listaRefaz=None, lista=None):
    if lista is None:
        lista = []

    lista.append(listaRefaz[0])
    listaRefaz.pop(0)
    return lista

guardando_sigla = {'listar': 0, 'desfazer': 1, 'refazer': 2}

lista = []
listaRefaz = []

while (True):
    entrada = input("Comnados: listar, desfazer, refazer\n Digite uma tarefa ou comando: ")
    if guardando_sigla[entrada] == 0:
        ...
    elif guardando_sigla[entrada] == 1:
        ...
    elif guardando_sigla[entrada] == 2:
        ...
    else:
        print(listar(entrada, lista))

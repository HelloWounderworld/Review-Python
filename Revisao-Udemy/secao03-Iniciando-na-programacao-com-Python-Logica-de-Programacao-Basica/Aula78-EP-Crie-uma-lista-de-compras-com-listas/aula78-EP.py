"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
# Tente deixar o meu código mais enxuto e possível!!!
import os
lista_de_compras = []
confere_opcao = 'ial'

while True:
    opcao = input('Selecione uma opção\n[i]nserir [a]pagar [l]istar: ')
    opcao = opcao.lower()
    
    if opcao in confere_opcao:
        if opcao == confere_opcao[0]:
            lista = input('Valor: ')
            if lista not in lista_de_compras:
                lista_de_compras.append(lista)
            else:
                print('Item já listado. Por favor, escolher um outro item.')
                continue
        elif opcao == confere_opcao[1]:
            indice = input('Coloque o índice: ')
            try:
                indice = int(indice)
                if indice < len(lista_de_compras):
                    del lista_de_compras[indice]
                else:
                    if len(lista_de_compras) == 0:
                        print('Não há nada para apagar, lista vazia.')
                        continue
                    else:
                        print('Coloque um índice existente para apagar.')
                        continue
            except:
                print('Coloque um valor inteiro.')
                continue
        elif opcao == confere_opcao[2]:
            os.system('clear')
            if len(lista_de_compras) > 0:
                for item in enumerate(lista_de_compras):
                    indice, conteudo = item
                    print(indice, conteudo)
            else:
                print('Não há nada para ser exibido. Por favor, insira um item!')
                continue
    else:
        print('Por favor, selecione apenas as opções i, a ou l.')
        continue

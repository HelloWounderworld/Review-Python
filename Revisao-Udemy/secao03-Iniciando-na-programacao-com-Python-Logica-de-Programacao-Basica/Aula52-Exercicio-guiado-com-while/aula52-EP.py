"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
nome_letra = 0
nova_string = ''
while nome_letra < tamanho_nome:
    nova_string = nova_string + f'*{nome[nome_letra]}'
    nome_letra += 1
nova_string += '*'
print(nova_string)
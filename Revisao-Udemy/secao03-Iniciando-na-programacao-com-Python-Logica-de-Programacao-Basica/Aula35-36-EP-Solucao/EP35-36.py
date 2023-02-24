"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
name = input('Digite o seu nome: ')
age  = input('Digite a sua idade: ')
espaco = ''

if name != '' and age != '':
    age = int(age)
    contem_espaco = ' ' in name
    if contem_espaco == True:
        espaco = 'contém'
    else:
        espaco = 'NÃO contém'
    print(f'Seu nome é {name}')
    print(f'Seu nome invertido é {name[::-1]}')
    print(f'Seu nome {espaco} espaços.')
    print(f'Seu nome tem {len(name)} letras.')
    print(f'A primeira letra do seu nome é {name[0]}')
    print(f'A última letra do seu nome é {name[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')

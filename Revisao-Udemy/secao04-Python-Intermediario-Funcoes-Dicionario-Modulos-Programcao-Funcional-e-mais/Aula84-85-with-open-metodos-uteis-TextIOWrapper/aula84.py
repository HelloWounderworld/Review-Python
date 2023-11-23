# Aprendendo a manipular arquivos que nem PHP, usando o python.
caminho_arquivo = 'aula84.txt'

# Linux ou MacOS
# caminho_arquivo_path = '/home/leonardo/Documentos/estudos-programacao/Review-Python/Revisao-Udemy/secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais/Aula84-85-with-open-metodos-uteis-TextIOWrapper/aula84_path.txt'

# Windows
caminho_arquivo_path = 'C:\\Users\\ltakashi\\Documents\\Review-Python\\Revisao-Udemy\\secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais\\Aula84-85-with-open-metodos-uteis-TextIOWrapper\\aula84_path.txt'

print(caminho_arquivo)
print(caminho_arquivo_path)

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

# arquivo_path = open(caminho_arquivo_path, 'w')
# arquivo_path.close()

# with open(caminho_arquivo, 'w') as arquivo:
#     arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!\n')
#     arquivo.write('Hello WounderWorld!\n')
#     print(arquivo.read())

# with open(caminho_arquivo, 'w') as arquivo:
#     arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!\n')
#     arquivo.write('Hello WounderWorld!\n')

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

with open(caminho_arquivo, 'w+') as arquivo:
    print(type(arquivo))
    arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!\n')
    arquivo.write('Hello WounderWorld!\n')
    arquivo.writelines(
        ('Lupin III\n', 'Italian Game\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print()
    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())

# with open(caminho_arquivo_path, 'w') as arquivo:
#     arquivo.write('Foi criado dentro da pasta dessa aula 84!! Hello WounderWorld!\n')
#     arquivo.write('Hello WounderWorld!\n')

# with open(caminho_arquivo_path, 'r') as arquivo:
#     print(arquivo.read())

print()
print('#'*40)
print()

with open(caminho_arquivo_path, 'w+') as arquivo:
    arquivo.write('Foi criado dentro da pasta dessa aula 84!! Hello WounderWorld!\n')
    arquivo.write('Hello WounderWorld!\n')
    arquivo.writelines(
        ('Lupin III\n', 'Italian Game\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print(arquivo.readline(), end='')
    print()
    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())

with open(caminho_arquivo_path, 'a', encoding='utf-8') as arquivo:
    arquivo.write('Foi criado dentro da pasta dessa aula 84!! Hello WounderWorld!\n')
    arquivo.write('Hello WounderWorld!\n')
    arquivo.writelines(
        ('Lupin III\n', 'Italian Game\n')
    )
    arquivo.write('Atenção!! Isso é uma organização')
# with open(caminho_arquivo_path, 'w') as arquivo:
#     ...

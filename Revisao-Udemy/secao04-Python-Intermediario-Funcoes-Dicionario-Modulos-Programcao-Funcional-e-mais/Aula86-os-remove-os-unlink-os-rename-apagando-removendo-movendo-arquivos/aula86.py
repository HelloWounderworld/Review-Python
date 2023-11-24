import os

# Aprendendo a manipular arquivos que nem PHP, usando o python.
caminho_arquivo = 'aula86.txt'

# Linux ou MacOS
# caminho_arquivo_path = '/home/leonardo/Documentos/estudos-programacao/Review-Python/Revisao-Udemy/secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais/Aula86-os-remove-os-unlink-os-rename-apagando-removendo-movendo-arquivos/aula86_path.txt'

# Windows
caminho_arquivo_path = 'C:\\Users\\ltakashi\\Documents\\Review-Python\\Revisao-Udemy\\secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais\\Aula86-os-remove-os-unlink-os-rename-apagando-removendo-movendo-arquivos\\aula86_path.txt'

print(caminho_arquivo)
print(caminho_arquivo_path)

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

os.rename(caminho_arquivo_path, 'aula86_path_renomeado_e_movido.txt')
os.rename(caminho_arquivo, 'C:\\Users\\ltakashi\\Documents\\Review-Python\\Revisao-Udemy\\secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais\\Aula86-os-remove-os-unlink-os-rename-apagando-removendo-movendo-arquivos\\aula86_renomeado_movido_da_raiz.txt')

# os.unlink(caminho_arquivo)
# os.remove(caminho_arquivo_path)

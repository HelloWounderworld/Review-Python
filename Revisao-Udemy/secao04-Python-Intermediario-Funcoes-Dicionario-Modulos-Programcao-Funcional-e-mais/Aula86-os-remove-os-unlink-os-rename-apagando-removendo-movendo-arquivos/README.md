# Aula 86 - os.remove, os.unlink e os.rename - apagando, renomeando e movendo arquivos:
Mais algumas coisas que queremos mostrar sobre manipulações de arquivos, mas de modo superficial, pois isso remete ao uso de módulos e, mais pela frente, teremos uma aula desse tipo.

No caso, vamos aprender a usar o módulo chamado "os" que é um módulo nativo do Python que importado ela já conseguimos utilizar.

Dentro desse módulo vamos aprender sobre "remove", "unlink" e "rename", para conseguirmos manipular os arquivos.

Primeiro, vamos criar um arquivo. Para isso, segue o seguinte código (claro, o estudante terá que colocar a própria path de acordo como está está organizando o repositório)

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

Rodado o código acima, agora, vamos importar o módulo e vamos usar da seguinte forma

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

    os.unlink(caminho_arquivo)
    os.remove(caminho_arquivo_path)

Bom, acima, tanto o método "unlink" quanto o "remove", ambos removem o arquivo criado. Mas, então, qual a diferença entre ambos?

Basicamente, não há uma diferença tão significativa, pois ambos são focados para deletar arquivos. Porém, o "unlink" é um método que foi implementada quando foi lançado a versão do Python 3 que aumenta o número de sistemas operacionais suportados.

Agora, temos o método "rename", que, basicamente, assim como o nome já diz, serve para renomear o nome de um arquivo. Porém, ela serve tbm para podermos mover o arquivo.

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

Como podemos ver acima, não só renomeamos o nome dos arquivos, mas conseguimos tbm mover o arquivo de lugar trocando. O arquivo "aula86_path.txt" que estava dentro da pasta da aula, mudou de nome e foi movido para a pasta raiz desse repositório e "aula86.txt" mudou o nome e foi movido para a pasta dentro dessa aula.

Para melhor compreensão, seguir o link:

    https://stackoverflow.com/questions/42636018/python-difference-between-os-remove-and-os-unlink-and-which-one-to-use

    https://www.sarthaks.com/3476480/what-is-the-difference-between-os-remove-and-os-unlink

# Aula 84 e 85 - with open (context manager) e métodos úteis do TextIOWrapper e Modos de abertura de arquivo e encoding com with open:
Vamos, agora, tentar escrever algo nos arquivos dentro do processo de criação.

Vamos começar com o seguinte código, que foi feito na última aula

    # Aprendendo a manipular arquivos que nem PHP, usando o python.
    caminho_arquivo = 'aula84.txt'

    caminho_arquivo_path = 'caminho_arquivo_path = '/home/leonardo/Documentos/estudos-programacao/Review-Python/Revisao-Udemy/secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais/Aula84-85-with-open-metodos-uteis-TextIOWrapper/aula84_path.txt''

    print(caminho_arquivo)
    print(caminho_arquivo_path)

    # arquivo = open(caminho_arquivo, 'w')
    # arquivo.close()

    # arquivo_path = open(caminho_arquivo_path, 'w')
    # arquivo_path.close()

    with open(caminho_arquivo, 'w') as arquivo:
        print('Hello WounderWorld')
        print('Arquivo vai ser fechado')

    with open(caminho_arquivo_path, 'w') as arquivo:
        print('Hello WounderWorld')
        print('Arquivo vai ser fechado')

Obs: Os prints dentro do "with open" não é necessário. Bastaria dar "..." dentro dela que iria funcionar.

Levando, então, como no seguinte caso

    # Aprendendo a manipular arquivos que nem PHP, usando o python.
    caminho_arquivo = 'aula84.txt'

    caminho_arquivo_path = 'caminho_arquivo_path = '/home/leonardo/Documentos/estudos-programacao/Review-Python/Revisao-Udemy/secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais/Aula84-85-with-open-metodos-uteis-TextIOWrapper/aula84_path.txt''

    print(caminho_arquivo)
    print(caminho_arquivo_path)

    # arquivo = open(caminho_arquivo, 'w')
    # arquivo.close()

    # arquivo_path = open(caminho_arquivo_path, 'w')
    # arquivo_path.close()

    with open(caminho_arquivo, 'w') as arquivo:
        ...

    with open(caminho_arquivo_path, 'w') as arquivo:
        ...

Se executarmos o código na forma como está acima, conseguimos ter o mesmo resultado. Ou seja, o arquivo "aula84_path.txt" criado dentro da pasta desse aula e o arquivo "aula84.txt" criado na raiz desse repositório.

Agora, finalmente, vamos escrever algo dentro do arquivo que vamos criar! Para isso, usaremos o ".write()" para conseguirmos escrever algo dentro do arquivo

    # Aprendendo a manipular arquivos que nem PHP, usando o python.
    caminho_arquivo = 'aula84.txt'

    caminho_arquivo_path = 'caminho_arquivo_path = '/home/leonardo/Documentos/estudos-programacao/Review-Python/Revisao-Udemy/secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais/Aula84-85-with-open-metodos-uteis-TextIOWrapper/aula84_path.txt''

    print(caminho_arquivo)
    print(caminho_arquivo_path)

    # arquivo = open(caminho_arquivo, 'w')
    # arquivo.close()

    # arquivo_path = open(caminho_arquivo_path, 'w')
    # arquivo_path.close()

    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!')

    with open(caminho_arquivo_path, 'w') as arquivo:
        arquivo.write('Foi criado dentro da pasta dessa aula 84!! Hello WounderWorld!')

Agora, se colocarmos uma outra linha? O que vai acontecer?

    # Aprendendo a manipular arquivos que nem PHP, usando o python.
    caminho_arquivo = 'aula84.txt'

    caminho_arquivo_path = 'caminho_arquivo_path = '/home/leonardo/Documentos/estudos-programacao/Review-Python/Revisao-Udemy/secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais/Aula84-85-with-open-metodos-uteis-TextIOWrapper/aula84_path.txt''

    print(caminho_arquivo)
    print(caminho_arquivo_path)

    # arquivo = open(caminho_arquivo, 'w')
    # arquivo.close()

    # arquivo_path = open(caminho_arquivo_path, 'w')
    # arquivo_path.close()

    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!')
        arquivo.write('Hello WounderWorld!')

    with open(caminho_arquivo_path, 'w') as arquivo:
        arquivo.write('Foi criado dentro da pasta dessa aula 84!! Hello WounderWorld!')
        arquivo.write('Hello WounderWorld!')

Podemos ver que foi colado em seguida! Bom, se quisermos que seja feito uma quebra de linha, a parte boa, é que esse método "write" aceita os mesmos parâmetros do que é utilizado em print para conseguirmos manipular a forma de visualização dos textos.

    # Aprendendo a manipular arquivos que nem PHP, usando o python.
    caminho_arquivo = 'aula84.txt'

    caminho_arquivo_path = 'caminho_arquivo_path = '/home/leonardo/Documentos/estudos-programacao/Review-Python/Revisao-Udemy/secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais/Aula84-85-with-open-metodos-uteis-TextIOWrapper/aula84_path.txt''

    print(caminho_arquivo)
    print(caminho_arquivo_path)

    # arquivo = open(caminho_arquivo, 'w')
    # arquivo.close()

    # arquivo_path = open(caminho_arquivo_path, 'w')
    # arquivo_path.close()

    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!\n')
        arquivo.write('Hello WounderWorld!\n')

    with open(caminho_arquivo_path, 'w') as arquivo:
        arquivo.write('Foi criado dentro da pasta dessa aula 84!! Hello WounderWorld!\n')
        arquivo.write('Hello WounderWorld!\n')

Agora, visto que o arquivo foi criado, podemos mudar o "'w'" dentro do "with open" para "'r'" para conseguirmos realizar apenas a leitura do arquivo já existente

    # Aprendendo a manipular arquivos que nem PHP, usando o python.
    caminho_arquivo = 'aula84.txt'

    caminho_arquivo_path = 'caminho_arquivo_path = '/home/leonardo/Documentos/estudos-programacao/Review-Python/Revisao-Udemy/secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais/Aula84-85-with-open-metodos-uteis-TextIOWrapper/aula84_path.txt''

    print(caminho_arquivo)
    print(caminho_arquivo_path)

    # arquivo = open(caminho_arquivo, 'w')
    # arquivo.close()

    # arquivo_path = open(caminho_arquivo_path, 'w')
    # arquivo_path.close()

    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!\n')
        arquivo.write('Hello WounderWorld!\n')

    with open(caminho_arquivo, 'r') as arquivo:
        print(arquivo.read())

    with open(caminho_arquivo_path, 'w') as arquivo:
        arquivo.write('Foi criado dentro da pasta dessa aula 84!! Hello WounderWorld!\n')
        arquivo.write('Hello WounderWorld!\n')

    with open(caminho_arquivo_path, 'r') as arquivo:
        print(arquivo.read())

O que não irá funcionar é se tentarmos realizar o seguinte

    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!\n')
        arquivo.write('Hello WounderWorld!\n')
        print(arquivo.read())

Se tentarmos rodar o código na forma como está acima, irá causar um erro, UnsuporttedOperation.

E nem como seguinte

    with open(caminho_arquivo, 'r') as arquivo:
        arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!\n')
        arquivo.write('Hello WounderWorld!\n')
        print(arquivo.read())

Pois o arquivo não estará "writable".

Caso, a pessoa queira continuar podendo colocar o "print(arquivo.read())" dentro do "with open" na forma "'w'", será necessário colocarmos um "+" dentro dela

    with open(caminho_arquivo, 'w+') as arquivo:
        arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!\n')
        arquivo.write('Hello WounderWorld!\n')
        print(arquivo.read())

Quando abrimos o arquivo que foi escrito com as strings configurado dentro do "with open" acima, conseguimos ver que o cursor "|" ele fica no final do texto. Haverá casos em que o desejável é que esse cursor fique no início, até porque os passo a passo que foi colocado no "write" acima ele simula, literalmente, o processo de escrita manual de uma pessoa digitando. Para isso, utilizamos o "seek" para conseguirmos definir em qual parte o cursor ficará localizado

    with open(caminho_arquivo, 'w+') as arquivo:
        arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!\n')
        arquivo.write('Hello WounderWorld!\n')
        arquivo.seek(0, 0)
        print(arquivo.read())

Em vez de ter que escrever linha por linha chamando "write" uma de cada vez, temos uma forma de conseguirmos escrever várias linhas de cada vez, que é usando o "writelines" da seguinte forma

    with open(caminho_arquivo, 'w+') as arquivo:
        arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!\n')
        arquivo.write('Hello WounderWorld!\n')
        arquivo.writelines(
            ('Lupin III\n', 'Italian Game\n')
        )
        arquivo.seek(0, 0)
        print(arquivo.read())

Da mesma forma que escrevemos um conjunto de linha de uma vez só, podemos, também, ler linha por linha, usando a sintaxe "readline()"

    with open(caminho_arquivo, 'w+') as arquivo:
        arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!\n')
        arquivo.write('Hello WounderWorld!\n')
        arquivo.writelines(
            ('Lupin III\n', 'Italian Game\n')
        )
        arquivo.seek(0, 0)
        print(arquivo.read())
        print('Lendo')
        arquivo.seek(0, 0)
        print(arquivo.readline())

O método "readline" é como se fosse um "next", é pelo número de vezes que ele é chamado que será lido as linhas sucessoras.

Porém, como podemos ver, se chamarmos várias vezes o "readline" ocorrerá uma quebra de linha automática, que é configurado como algo padrão desse método. Para evitarmos que isso aconteça as alternativas para isso seriam

    with open(caminho_arquivo, 'w+') as arquivo:
        arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!\n')
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

Ou, usamos o método "strip"

    with open(caminho_arquivo, 'w+') as arquivo:
        arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!\n')
        arquivo.write('Hello WounderWorld!\n')
        arquivo.writelines(
            ('Lupin III\n', 'Italian Game\n')
        )
        arquivo.seek(0, 0)
        print(arquivo.read())
        print('Lendo')
        arquivo.seek(0, 0)
        print(arquivo.readline(), end='')
        print(arquivo.readline().strip())

Bom, além do método, "readline" temos tbm o seu plural "readlines"

    with open(caminho_arquivo, 'w+') as arquivo:
        arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!\n')
        arquivo.write('Hello WounderWorld!\n')
        arquivo.writelines(
            ('Lupin III\n', 'Italian Game\n')
        )
        arquivo.seek(0, 0)
        print(arquivo.read())
        print('Lendo')
        arquivo.seek(0, 0)
        print(arquivo.readline(), end='')
        print(arquivo.readline().strip())
        print()
        print('READLINES')
        arquivo.seek(0, 0)
        for linha in arquivo.realines():
            print(linha.strip())

Ou seja, "readlines" está criando uma lista de linhas e iterando elas.

Bom, continuando aqui, vamos falar, agora, sobre Modos.

Se analisarmos o tipo que o "arquivo" está exibindo, como no seguinte, print(type(arquivo))

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
        print(arquivo.readline(), end='')
        print(arquivo.readline().strip())
        print()
        print('READLINES')
        arquivo.seek(0, 0)
        for linha in arquivo.realines():
            print(linha.strip())

Veremos que ela retorna "TextIOWrapper". No caso, o "open" ele é um contextManager que abre e fecha um arquivo e que retorna um TextIOWrapper para esse aquivo aqui.

Vamos falar mais a respeito dos modos de abertura. Segundo a instrução abaixo

    # Modos:
    # r (leitura), w (escrita), x (para criação)
    # a (escreve ao final), b (binário)
    # t (modo texto), + (leitura e escrita)

Vamos dar a atenção para "w" e "a", focando nas suas diferenças.

- w: Ele abre o arquivo apaga tudo o que está nele e escreve tudo de novo.

    Isso quer dizer o seguinte. Primeiro vamos rodar o seguinte código

        with open(caminho_arquivo, 'w') as arquivo:
            print(type(arquivo))
            arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!\n')
            arquivo.write('Hello WounderWorld!\n')
            arquivo.writelines(
                ('Lupin III\n', 'Italian Game\n')
            )

    Em seguida, vamos rodar o seguinte código

         with open(caminho_arquivo, 'w') as arquivo:
            ...

    Note que, na primeira, foi criado, na pasta raiz do repositório, o arquivo "aula84.txt". Porém, em seguida, ao rodarmos o último código acima, no mesmo arquivo, antes, o que havía sido escrito nela está tudo apagado.

    Isso deixa claro que, com o que foi definido a ser colocado de texto pelo "w" num determinado arquivo já existente ou não, o processo que ela faz é apagar tudo primeiro e, em seguida, colocar o que foi solicitado.

- a: De um arquivo existênte com algum conteúdo, não apaga nada e só complementa. (append mode)

    Isso significa o seguinte

        with open(caminho_arquivo, 'a') as arquivo:
            print(type(arquivo))
            arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!\n')
            arquivo.write('Hello WounderWorld!\n')
            arquivo.writelines(
                ('Lupin III\n', 'Italian Game\n')
            )

    Visto que o arquivo "aula84.txt" já foi criado, se rodarmos o código acima, vamos ver que os conteúdos são complementados.

    Claro, que se vc quiser colocar algo do tipo "arquivo.read()" dentro do "a", vamos precisar da sintaxe "+" também.

Agora, vamos falar de algo bem, mas bem, importante, que é o Encoding.

Vamos supor o seguinte exemplo. No contexto acima, usamos o inglês que não tem caracteres especiais que nem na língua portuguesa. Mas suponhamos que colocamos o seguinte texto

    with open(caminho_arquivo, 'w') as arquivo:
        print(type(arquivo))
        arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!\n')
        arquivo.write('Hello WounderWorld!\n')
        arquivo.writelines(
            ('Lupin III\n', 'Italian Game\n')
        )
        arquivo.write('Atenção!! Isso é uma organização')

Vimos que aqui, está sendo colocado, na última linha caracteres especiais da língua portuguesa.

Obs: Esse problema de caracteres especiais, apenas, acontece no Windows. Em Linux e MacOS não haverá problema. É que eu estou alternando os estudos entre Linux e Windows de Python, pois hora preciso estar usando Linux e hora preciso estar usando Windows. O motivo dessa diferença está no uso padrão da UTF-8 que já tem no Linux e no MacOS, mas não tem no Windows. (https://www.otaviomiranda.com.br/ - Procure pelo curso Normalização Unicode em Python para entender melhor esse assunto)

Ao olharmos o arquivo "aula84.txt" esse texto não estará recohecendo tais caracteres especiais. O Encoding vai nos ajudar em tais reconhecimentos. No caso, com o arquivo "aula84.txt" aberto na sua frente, no VSCode, haverá, na tela direito de baixo, um lugar escrito UTF-8. Clicamos nela e, na aba da pesquisa, aparecerá "Reabrir com codificação" ou "Reopen with Encoding", daí mostrará vários formas de encoding. Nela vamos escolher "Western windows 1252". Fazendo isso, vamos ver que no arquivo "aula84.txt", onde havía caracteres especiais, que não estava sendo reconhecido, passará a ser reconhecido.

Mas, como corrigirmos isso no código? Bom, basta realizar o seguinte

    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo: # utf-8 ou utf8, tanto faz
        print(type(arquivo))
        arquivo.write('Foi criado na raiz desse repositorio! Hello WounderWorld!\n')
        arquivo.write('Hello WounderWorld!\n')
        arquivo.writelines(
            ('Lupin III\n', 'Italian Game\n')
        )
        arquivo.write('Atenção!! Isso é uma organização')

Claro, antes de compilar o código acima, no arquivo "aula84.txt" volta de "Western windows 1252" para "UTF-8". Daí, vamos ver que o problema foi corrigido.

Link para leitura:

    https://www.w3schools.com/python/python_file_open.asp
    https://pt.stackoverflow.com/questions/535114/o-que-%C3%A9-um-context-manager-em-python
    https://www.otaviomiranda.com.br/

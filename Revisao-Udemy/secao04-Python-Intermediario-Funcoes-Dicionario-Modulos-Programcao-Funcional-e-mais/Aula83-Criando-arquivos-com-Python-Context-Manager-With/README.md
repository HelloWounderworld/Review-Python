# Aula 83 - Criando arquivos com Python + Context Manager with:
Vamos aprender a criar arquivos com o Python.

Existe uma linguagem de programação chamado PHP que nela podemos realizar o mesmo.

Por começo, vamos realizar o seguinte, criamos um arquivo "aula83.py" e nela vamos colocar o seguinte

    caminho_arquivo = 'aula83.txt'

    caminho_arquivo_path = '/home/leonardo/Documentos/estudos-programacao/Review-Python/Revisao-Udemy/secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais/Aula83-Criando-arquivos-com-Python-Context-Manager-With/aula83_path.txt'

    print(caminho_arquivo)
    print(caminho_arquivo_path)

No caso, a variável acima, estamos pensando no mesmo nível em que irei executar o arquivo "aula83.py". Claro, podemos expecificar, definindo path, onde vamos criar o arquivo, como foi feito na segunda variável. Lembrando, que a forma como foi colocado a path acima é válido para MacOS e Linux. Para o windows, muda a sua forma de enviar o caminho, a barra é invertida de "/", como está acima, para "\\", usando duas barras, pois, se fosse uma "\", o python entende como uma outra sintaxe.

Agora, vamos entrar nos modos de conseguirmos manipular os arquivos que seria o seguinte

    # Modos:
    # r (leitura), w (escrita), x (para criação)
    # a (escreve ao final), b (binário)
    # t (modo texto), + (leitura e escrita)

Vamos por partes. Primeiro, vamos criar um arquivo, então coloquemos o seguinte

    caminho_arquivo = 'aula83.txt'

    caminho_arquivo_path = '/home/leonardo/Documentos/estudos-programacao/Review-Python/Revisao-Udemy/secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais/Aula83-Criando-arquivos-com-Python-Context-Manager-With/aula83_path.txt'

    print(caminho_arquivo)
    print(caminho_arquivo_path)

    arquivo = open(caminho_arquivo, 'r')
    arquivo_path = open(caminho_arquivo_path, 'r')

    arquivo.close()
    arquivo_path.close()

É de boa prática, sempre que vc abrir algum arquivo, no final fechar ela, como foi feito acima. Exatamente para te evitar vários problemas, umas delas, vazamento de dados.

Se vc executar o código acima, irá gerar um erro, porque eu só pedi para abrir um arquivo no modo leitura... de um arquivo inexistente.

Logo, para resolvermos esse tipo de problema, a lógica é o mesmo que realizamos no linux shell quando queremos criar um arquivo usando o echo.

    caminho_arquivo = 'aula83.txt'

    caminho_arquivo_path = '/home/leonardo/Documentos/estudos-programacao/Review-Python/Revisao-Udemy/secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais/Aula83-Criando-arquivos-com-Python-Context-Manager-With/aula83_path.txt'

    print(caminho_arquivo)
    print(caminho_arquivo_path)

    arquivo = open(caminho_arquivo, 'w')
    arquivo_path = open(caminho_arquivo_path, 'w')

    arquivo.close()
    arquivo_path.close()

Note que, acima, da variável "caminho_arquivo" o arquivo foi criado na pasta raíz desse curso, mas a variável "caminho_arquivo_path" que foi especificado a path foi criado exatamente dentro da pasta Aula83.

A lógica que temos aqui para manipular os arquivos, é igual quando usamos o try/catch/except/finally, pois para que não ocorra nenhum problema de vazamento de dados ou tela travada, independente do que ocorra, sempre, finally, no final realizamos a ação de fechar ou voltar para a tela inicial.

No caso, é de boa prática usarmos try/catch/except/finally sempre que formos manipular arquivos em python tbm.

Podemos usar tbm, a palavra "with" para que um arquivo seja aberto e fechado, custe o que custar. Como seguinte

    caminho_arquivo = 'aula83.txt'

    caminho_arquivo_path = '/home/leonardo/Documentos/estudos-programacao/Review-Python/Revisao-Udemy/secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais/Aula83-Criando-arquivos-com-Python-Context-Manager-With/aula83_path.txt'

    print(caminho_arquivo)
    print(caminho_arquivo_path)

    with open(caminho_arquivo, 'w') as arquivo:
        print('Hello WounderWorld')
        print('Arquivo vai ser fechado')

No caso, o que difere de usar apenas o "open" e o "with" é que, no final, o arquivo será fechado.

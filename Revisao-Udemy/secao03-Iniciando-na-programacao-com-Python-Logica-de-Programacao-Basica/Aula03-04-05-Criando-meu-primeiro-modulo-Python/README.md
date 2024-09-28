# Aula 03 - Criando meu primeiro módulo Python (*.py):
O formato da extensão python é .py

# Aula 04 - O interpretador do Python + comentários de código:
Vamos aprender a fazer comentário no arquivo python!

No caso, no arquivo aula03-04-05.py, a forma para realizarmos um comentário seria por três tipos

    # - Permite fazer comentário em uma linha, apenas

    """ """ - Permite fazer comentário em um conjunto de linhas

    ''' ''' - Permite fazer comentário em um conjunto de linha

Donde, a sua aplicação ficaria

    """
    DocString
    E escrever o que eu
    quiser
    asdfasdfd
    """

    ''' Usar para escrever suas notas '''
    print(123)  # Na frente

Agora, a forma para conseguirmos exibir alguma msg pelo terminal, usaremos o print, como podemos ver no código acima. Ao rodarmos o arquivo, vamos conseguir exibir a msg acima no terminal. Mas, lembre-se, o print ele funciona para ser exibido as coisas na tela.

# Aula 05 - Docstrings como comentários:
Mais sobre comentário, a forma de utilizar o """ """ e ''' '''.

No caso, as aspas, ", ele se comporta como comentário, mas temos que deixar claro que ele não é um comentário, pois o interpretador do python ele irá ler isso. No caso, a forma de comentar usando as aspas, é conhecido como DocString.

Agora, o aspas simples, tbm, serve para comentar, que também é uma DocString.

No caso, o DocString, ele pode ser usado como uma forma de anotar e, como será lido pelo interpretador python, ele ficará guardado na memória, diferente de comentar por # que será ignorado.

## O que raios e o interpretador do Python?
O interpretador trabalha de forma semelhante a uma shell de Unix: quando chamado com a saída padrão conectada a um console de terminal, ele lê e executa comandos interativamente; quando chamado com um nome de arquivo como argumento, ou com redirecionamento da entrada padrão para ler um arquivo, o interpretador lê e executa o script contido no arquivo.

Fonte de link para leitura:

    https://docs.python.org/pt-br/3/tutorial/interpreter.html

# Aula 34 - Fatiamento de strings e a função len:
Vamos ver fatiamento de strings e função len.

No caso, o fatiamento de strings é tratar elas como um array para conseguirmos realizar algumas manipulações

    """
    Fatiamento de strings
    012345678
    Olá mundo
    -987654321
    Fatiamento [i:f:p] [::]
    Obs.: a função len retorna a qtd 
    de caracteres da str
    """
    variavel = 'Olá mundo'
    print(variavel[5])

Acessando a leta "u" dessa string.

Podemos acessar o mesmo elemento usando o número negativo tbm

    print(variavel[-4])

Além disso, podemos fazer o fatiamento

    print(variavel[4:])

No caso, aqui ele indica que quero pegar o pedaço da string que começa do "m" e vai até o fim.

Assim, podemos tbm colocar o final onde queremos que seja pego

    print(variavel[4:7])

No caso, colocamos o pedaço até onde queremos pegar, mas nesse caso aqui será omitido o índice 7. Ou seja, será pego até o índice 6.

O mesmo podemos fazer de trás para frente. No caso, se quisermos pegar uma fatia a partir de um ponto e tudo o que vier antes dele podemos fazer o seguinte

    print(variavel[:5])

Percebe-se que aqui, o índice 5 foi omitido e foi pego do índice 4 para trás. Da mesma forma, podemos fazer para os números tbm

    print(variavel[-8:-2])

No caso, note que, aqui mesmo sendo número negativo a regra de range continua funcionando. No caso, o "-2" ele indica o caractere "d", mas ela foi omitido ao pegar o pedaço da fatia.

Podemos, tbm, saber a quantidade de caractere que está presente numa string usando o len

    print(len('aaaaaaaaa'))
    print(len(variavel))

No caso, aqui fica evidente que de fato é contado idependente se um dado caractere apareceu mais de uma vez, ela é contado mesmo assim indexando um novo índice nela. Seria uma função em que vai dos naturais e algumas quantidades de índices de naturais vão até um mesmo caractere de palavras.

Ainda faltou falar de passos no fatiamento

    print(variavel[0:len(variavel):1])

Aqui o terceiro parâmetro, onde está o '1', indica os passos em que ele vai pulando os caractéres para ser exibido no final. No caso, o '1' aqui não vai mudar nada porque ele não estará pulando nada. Creio que com o próximo exemplo ficaria mais evidente

    print(variavel[0:len(variavel):2])

No caso, o print acima retorna o seguinte

    Oámno

Visto que a string original é 'Olá mundo'.

Podemos usar, nessa bricadeira, o número negativo tbm

    print(variavel[0:len(variavel):-1])
    print(variavel[0:len(variavel):-2])

Nisso, o que irá acontecer é que em vez de contar os passos de esquerda para direita, é contado de direita para à esquerda. Entretanto, ao usarmos o número negativo, os outros números tbm precisam ser negativos. Como prova disso, os dois prints acima não será retornado nada. O certo teria que ser

    print(variavel[-1:-10:-1])
    print(variavel[-1:-10:-2])

Agora, sim, será retornado as strings invertidas

    odnum álO
    onmáO

Podemos fazer o mesmo para o print(variavel[-1:-10:-1]) da seguinte forma abaixo

    print(variavel[::-1])

Como nesse caso aqui que foi invertido a string.

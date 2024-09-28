# Aula 21 - Usando a função input para coletar dados do usuário:
Vamos ver um pouco mais sobre a função input.

O input ele é uma função do python donde vc pode coletar dados do usuário que estiver usando o seu programa.

No caso, no arquivo aula21.py temos o seguinte código

    nome = input('Qual o seu nome? ')
    print(f'O seu nome é {nome}')
    print(f'O seu nome é {nome=}')

Basicamente, quando vc rodar o código acima, pelo terminal será exibido a msg de pergunta "Qual o seu nome?", como definido dentro da função input e em seguinte, com o f-strings, conseguimos exibir essa msg.

Além disso, no código acima, temos um truque de conseguirmos exibir não somente o conteúdo que foi colocado dentro input mas o seu tipo tbm, donde é exibido "{nome=}".

O mesmo podemos fazer os inputs para números tbm. Só que com um detalhe é que o input ele envia uma string. Logo, seria necessário alterar o input para um tipo número

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')

    int_numero_1 = int(numero_1)
    int_numero_2 = int(numero_2)

    print(f'A soma dos números é: {int_numero_1 + int_numero_2}')

Obs: Como uma boa prática, recomendamos que o programador não faça a seguinte forma de conversão achando que isso seria um corta caminho

    numero_1 = int(input('Digite um número: '))

Pode parecer que de fato é um corta caminho, mas o problema é que isso pode gerar uma confusão de quando seria necessário procurar onde está dando erro no código. Pois muitas vezes dificulta o que o usuário colocou dentro do input para checar a validade ou não.

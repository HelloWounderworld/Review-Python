# Aula 30 - Introdução à função lambda + list.sort e sorted:
Vamos aprender sobre função lambda em Python.

No caso, a função lambda é uma função anônima de uma linha. No caso, sempre que montamos uma função lambda, toda a relação deverá estar contida em uma única linha.

    lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
    lista.sort(reverse=True)
    sorted(lista)

No caso, a funçã, usado acima, é uma função de ordenação, mas não é um função lambda. No caso, acima, é um exemplo simples de ordenação, visto que temos os números inteiros sendo usado nela. Agora, imagina se quisermos realizar uma espécie de ordenação numa lista de bibliotecas como seguite

    lista = [
        {'nome': 'Luiz', 'sobrenome': 'miranda'},
        {'nome': 'Maria', 'sobrenome': 'Oliveira'},
        {'nome': 'Daniel', 'sobrenome': 'Silva'},
        {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
        {'nome': 'Aline', 'sobrenome': 'Souza'},
    ]

No caso, não iremos conseguir usar o sort() como acima, pois aqui temos dicionarios entre dicionários, donde não há uma ordem entre objetos para conseguirmos realizar a tal ordenação que tanto queremos. Uma das maneiras, que podemos usar o sort() para conseguirmos realizar alguma ordenação de forma mais flexível, no sentido de definirmos os parâmetros que queremos considerar para realizar a ordenação seria usando o "key" dentro do sorte e nela passar alguma função que considera algum indice dentro da ordenação.

    def ordena(item):
        print('Objeto a ser ordenado: ', item)
        return item['nome']

    lista.sort(key=ordena)
    print(lista)

No caso, o que está acontecendo acima, seria que usamos a função ordena dentro do sort(). Ou seja, conseguimos definir por qual parâmetro consideramos paramos realizarmos a tal ordenação, 'nome'.

Lembrando que o Python, ele utiliza a tabela unicode para considerar a ordenação de qualquer caracteres. No nosso caso, o unicode é o utf8.

Entretanto, até agora, não abordamos função lambda. Vamos, agora, finalmente, usar uma função lambda para mostrarmos como isso ficaria mais flexivel do que o formato acima para conseguirmos realizar a devida ordenacação

    lista.sort(key=lambda item: item['nome'])

No caso, acima é definitivamente a função lambda. Note que, a versão da função lambda acima, é o último exemplo que mostramos de ordenação usando "key" de forma enxuta.

Podemos realizar a mesma ordenação aplicando a função lambda dentro da função sorted tbm, como segue

    sorted(lista, key=lambda item: item['nome'])

No caso, a ordenação acima é reversa.
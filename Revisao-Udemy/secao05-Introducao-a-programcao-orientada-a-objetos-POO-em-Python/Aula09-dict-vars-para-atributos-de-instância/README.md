# Aula 09 - __dict__ e vars para atributos de instância:
Em Python, __dict__ e a função vars() são usados para acessar o dicionário de atributos de um objeto. Eles são úteis para inspeção, serialização e manipulação dinâmica de atributos de objetos.

O __dict__ mantem um objeto do tipo mapping.

## Uso de __dict__:
Como podemos ver abaixo, conseguimos manipular os atributos que foram instanciados, desde mudar o seu valor e, ate mesmo, deletar

    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

    p1.nome = 'Eita'
    print(p1.nome)

    del p1.nome
    print(p1.nome)

Porem, esses atributos elas estao armazenados em algum lugar antes, quando tinha algum valor. Entoa, onde esses valores estavam salvos?

Re: dentro do __dict__.

O __dict__ é um atributo especial que armazena todos os atributos de um objeto em forma de dicionário. Cada chave do dicionário é o nome de um atributo e cada valor é o valor correspondente do atributo.

    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

    p1.nome = 'Eita'
    print(p1.nome)

    del p1.nome
    print(p1.nome)

    p = Pessoa("João", 30)
    print(p.__dict__)

Tome cuidado que o __dict__ ele e editavel. Ou seja, podemos fazer algo do seguinte tipo

    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

    p1.nome = 'Eita'
    print(p1.nome)

    del p1.nome
    print(p1.nome)

    p = Pessoa("João", 30)
    print(p.__dict__)

    p.__dict__['outra'] = 'coisa'
    print(p.__dict__)

Bom, o legal disso seria que usando o __dict__ conseguimos salvar tais dados armazenados numa classe instanciada em forma de JSON. E tbm, recuperar esse JSON e criar novamente os objetos das classes, como por exemplo

    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

    p1.nome = 'Eita'
    print(p1.nome)

    del p1.nome
    print(p1.nome)

    p = Pessoa("João", 30)
    print(p.__dict__)

    p.__dict__['outra'] = 'coisa'
    print(p.__dict__)

    dados = {'nome': 'Helena', 'idade': 12}
    p1 = Pessoa(**dados)
    print(p1.__dict__)

Ou seja, desenpacotamento do dicionario.

Ou seja, podemos usar esse __dict__ para salvar dados ou retorna-los, via banco de dados que sera feito mais pela frente em MySQL. Claro, podemos realizar a mesma coisa para qualquer outro banco de dados nao relacional tbm.

## Uso de vars():
vars() é uma função integrada que retorna o __dict__ de um objeto. Se nenhum argumento for fornecido, vars() atuará como locals().

print(vars(p))

## Utilidades:
- 1. Inspeção de Objeto: __dict__ e vars() podem ser usados para inspecionar os atributos de um objeto em tempo de execução, o que é útil para debugging e logging.

- 2. Serialização: Facilitam a serialização de objetos para formatos como JSON, permitindo converter facilmente os atributos de um objeto em um dicionário antes de serializar.

- 3. Manipulação Dinâmica: Permitem a manipulação dinâmica de atributos. Por exemplo, você pode adicionar, modificar ou remover atributos de um objeto em tempo de execução.

- 4. Cópia de Atributos: Podem ser usados para copiar atributos de um objeto para outro dinamicamente.

- 5. Reflexão e Metaprogramação: São úteis em técnicas avançadas de programação onde o código precisa manipular informações sobre si mesmo.

## Considerações:
- __dict__ só está disponível em objetos que têm um dicionário de atributos, o que não inclui objetos criados a partir de classes definidas com __slots__ ou alguns tipos embutidos como listas e tuplas.

- vars() pode ser usado em qualquer objeto que suporte __dict__. Se o objeto não suportar __dict__, vars() lançará um TypeError.

Essas ferramentas são poderosas para manipulação dinâmica de objetos e introspecção em Python, facilitando a programação reflexiva e dinâmica.
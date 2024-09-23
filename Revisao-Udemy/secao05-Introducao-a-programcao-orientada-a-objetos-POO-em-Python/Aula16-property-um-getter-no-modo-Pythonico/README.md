# Aula 16 - @property - um getter no modo Pythônico:
Quem conhece Java, provavelmente, ira sacar rapidamente que tem haver com o getter e o setter.

Sim, os conceitos fundamentais de getters e setters em Python usando @property e em Java são os mesmos. Ambos são utilizados para encapsular o acesso aos dados de uma classe, permitindo que a classe controle como esses dados são acessados e modificados, e para incluir lógica de validação ou transformação dos dados quando necessário.

O decorador @property em Python é usado para criar propriedades em uma classe, permitindo que você controle o acesso aos atributos de uma classe de maneira mais sofisticada. Ele transforma um método de uma classe em um atributo "getter", que pode ser acessado como se fosse um atributo normal, mas na verdade é um método sendo executado.

Suponhamos o seguinte cenario da seguinte classe

    class Caneta:
        def __init__(self, cor):
            self.cor = cor

    caneta = Caneta('Azul')
    print(caneta.cor)
    print(caneta.cor)
    print(caneta.cor)
    print(caneta.cor)
    print(caneta.cor)

Bom, se, por acaso, o nome do atributo, self.cor, tiver que ser mudado, da forma que o atributo esta sendo requisitado acima, tornaria extremamente trabalhoso para mudar todos os nomes.

    self.cor -> self.tinta # agora tu vai ter que mudar todos os prints, caneta.cor para caneta.tinta

Basicamente, para evitarmos que isso ocorra, podemos utilizar @property para encapsularmos e, com isso, criar o um getter que devolve o atributo. Dai, a vantagem disso seria que se, por acaso, tiver a necessidade de mudar o nome de um atributo, self.cor, sera necessario que vc mude somente dentro das classes e tudo continuara normal.

Como uma regra pratica e sempre recomendavel que vc encapsule aquelas linguagens de programacao mais enraizado, de modo que torne as alteracoes e melhorias mais faceis. As linguagens de programacao de infra, classe, banco de dados, etc... sera sempre de boa pratica que elas estejam todas encapsuladas assim separando os codigos de regra de negocio com codigo de nivel raiz.

Como uma aplicacao do @property, seguimos com o seguinte melhoria abaixo na classe, Caneta

    class Caneta:
        def __init__(self, cor):
            self.cor = cor

        def get_cor(self):
            return self.cor

    caneta = Caneta('Azul')
    print(caneta.get_cor())
    print(caneta.get_cor())
    print(caneta.get_cor())
    print(caneta.get_cor())
    print(caneta.get_cor())

Com a forma acima, conseguimos proteger o atributo "self.cor", podemos controlar a sua transparencia tbm usando private, protected, public, etc... Porem, so com o encapsulamento acima, conseguimos adicionar uma camada na protecao. Se bem que, em Python, a ideia de proteger um atributo nao e muito relevante.

Agora, sem o uso do @property, a forma de encapsulamento mostrada acima e um getter.

Vamos utilizar, agora, o @property para implementar o getter de uma forma mais sofisticada

    class Caneta:
        def __init__(self, cor):
            self.tinta = cor

        @property
        def cor(self):
            return 'QUALQUER COISA'

    caneta = Caneta('Azul')
    print(caneta.cor)
    print(caneta.cor)
    print(caneta.cor)
    print(caneta.cor)
    print(caneta.cor)

Note que, utilizando o @property, conseguimos criar um getter, sem a necessidade de, ao chamarmos o metodo, cor, da forma como se fosse um metodo, como foi feito antes, print(caneta.get_cor()). Ou seja, print(caneta.cor), estamos chamando o ".cor" como se fosse um atributo, mas, na verdade, ela e um metodo. No caso, o @property, nos permite que consigamos chamar tal metodo como se fosse um atributo.

No caso, isso cabe no mesmo cenario de se mudarmos o nome do atributo raiz que esta dentro da classe

    class Caneta:
        def __init__(self, cor):
            self.tinta = cor

        @property
        def cor(self):
            return self.tinta

    caneta = Caneta('Azul')
    print(caneta.cor)
    print(caneta.cor)
    print(caneta.cor)
    print(caneta.cor)
    print(caneta.cor)

## Funcionalidades do @property:
- 1. Encapsulamento: Permite esconder a implementação interna de um atributo, expondo apenas uma interface através de getters e setters.

- 2. Validação de Dados: Permite adicionar lógica de validação ao definir um valor.

- 3. Cálculo Dinâmico: Permite que o valor de um atributo seja calculado dinamicamente, em vez de ser armazenado.

Seguir o seguinte exemplo

    class Circulo:
        def __init__(self, raio):
            self._raio = raio

        @property
        def raio(self):
            return self._raio

        @raio.setter
        def raio(self, valor):
            if valor < 0:
                raise ValueError("O raio não pode ser negativo")
            self._raio = valor

        @property
        def area(self):
            return 3.14159 * self._raio ** 2

    # Uso da classe
    circulo = Circulo(5)
    print(circulo.raio)  # Saída: 5
    print(circulo.area)  # Saída: 78.53975

    circulo.raio = 10
    print(circulo.raio)  # Saída: 10
    print(circulo.area)  # Saída: 314.159

    # Tentativa de definir um raio negativo
    try:
        circulo.raio = -5
    except ValueError as e:
        print(e)  # Saída: O raio não pode ser negativo

- @property é usado para definir o método raio como um getter para o atributo _raio.

- @raio.setter define um método para definir o valor do _raio, incluindo uma verificação para garantir que o raio não seja negativo.

- A propriedade area é um exemplo de cálculo dinâmico, onde a área do círculo é calculada sempre que é acessada, usando o valor atual do raio.

Este exemplo ilustra como @property pode ser usado para adicionar validação e cálculo dinâmico, melhorando a segurança e a flexibilidade do código.

## O que seria um codigo Pythonico?
O termo "Pythonic" refere-se a uma filosofia de programação em Python que enfatiza a legibilidade, a simplicidade e a clareza do código. Ser "Pythonic" não é apenas sobre escrever código que funcione, mas sobre escrever código que se alinha com os princípios de design da linguagem Python, tornando-o fácil de entender e manter. Aqui estão alguns aspectos centrais do que torna um código Pythonic:

### Seguir o Zen de Python
O Zen de Python, acessível através do comando import this no interpretador Python, é uma coleção de 19 "afirmações" que capturam a filosofia da linguagem. Algumas das mais destacadas incluem:

- "Bonito é melhor que feio."

- "Explícito é melhor que implícito."

- "Simples é melhor que complexo."

- "Deve haver uma — e preferencialmente só uma — maneira óbvia de fazer algo."

### Utilizar recursos específicos da linguagem
Python oferece várias construções e recursos que não são encontrados em outras linguagens, ou que são mais elegantes em Python. Usar esses recursos de maneira eficaz é considerado Pythonic. Exemplos incluem:

- Compreensões de lista, dicionário e conjunto.

- Geradores e iteradores.

- Decoradores.

- Uso de with para gerenciamento de contexto.

### Escrever código legível e conciso
Python valoriza a legibilidade do código. Isso significa evitar linhas excessivamente longas, usar nomes de variáveis e funções descritivos, e evitar construções complicadas quando uma solução simples e direta está disponível.

### Seguir as convenções de estilo PEP 8
PEP 8 é o guia de estilo para Python que oferece convenções sobre como formatar código Python. Isso inclui diretrizes sobre nomes de variáveis, tamanho de linha, uso de espaços em branco e muito mais. Seguir o PEP 8 ajuda a manter o código Python uniforme e legível.

### Aproveitar as funcionalidades de alto nível
Python é uma linguagem de alto nível com muitas abstrações embutidas, como manipulação automática de memória (garbage collection), tipos de dados dinâmicos e uma extensa biblioteca padrão. Usar essas funcionalidades plenamente é parte de escrever código Pythonic.

### Preferir a simplicidade e a elegância
Pythonic code often involves finding the most straightforward solution to a problem, which not only works but also minimizes future code maintenance.

### Exemplo de código não Pythonic vs Pythonic
Não Pythonic:

    result = []
    for i in range(len(some_list)):
        if some_list[i] > 0:
            result.append(some_list[i] * 2)

Pythonic:

    result = [x * 2 for x in some_list if x > 0]

O exemplo Pythonic usa uma compreensão de lista, que é mais concisa, mais fácil de ler e mais "Pythonic".

Em resumo, escrever de maneira Pythonic significa adotar as convenções e filosofias da linguagem Python para produzir código que não apenas funcione bem, mas que também seja limpo, legível e eficiente.
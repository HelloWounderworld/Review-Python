# Aula 13 - Métodos de classe (@classmethod) + factories methods (métodos fábrica):
Lembra quando discutimos sobre atributo de classe?

    class Pessoa:
        ano = 2024 # atributo de classe

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def metodo_de_classe(self):
            print('Howdy!')

Para acessarmos esse atributo de classe, nao precisamos instanciar a classe Pessoa, bastaria acessar como se fosse um metodo

    print(Pessoa.ano)

Agora, para o metodo, metodo_de_classe, que criamos, nao funciona da mesma coisa. Ou seja, usando o seguinte

    Pessoa.metodo_de_classe()

Isso ira nos fornecer um erro... Pois, precisariamos passar algum argumento como self, que nesse caso, seria uma classe que foi instanciado

    Pessoa.metodo_de_classe(p1)

Porem, ao usarmos @classmethod, conseguimos criar um metodo dentro da classe, Pessoa, sem a necessidade de passarmos o 'self' como parametro, mas, sim, a propria classe, 'cls', e conseguimos chamar o metodo sem a necessidade de instanciarmos a classe

    class Pessoa:
        ano = 2024 # atributo de classe

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def metodo_de_classe(self):
            print('Howdy!')

        @classmethod
        def metodo_de_classe_sem_self(cls):
            print('Hello!')

    Pessoa.metodo_de_classe(p1)
    Pessoa.metodo_de_classe_sem_self()

Mas, ai, qual a utilidade desse @classmethod??? Seria para fabricar metodos, factories methods. Ou seja, um metodo que cria um outro objeto de pessoa. Como podemos ver no exemplo seguinte

    class Pessoa:
        ano = 2024 # atributo de classe

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def metodo_de_classe(self):
            print('Howdy!')

        @classmethod
        def metodo_de_classe_sem_self(cls):
            print('Hello!')

        @classmethod
        def criar_com_50_anos(cls, nome):
            return cls(nome, 50)

No exemplo acima, suponhamos que tenhamos um conjunto de pessoas que toda elas tenham 50 anos. Entao, o metodo, criar_com_50_anos, funciona para conseguirmos instanciar uma nova classe, mas com esse valor hard coder, 50. Nesse metodo, criar_com_50_anos, conseguimos ver que esta sendo retornado o cls, que e a propria classe, Pessoa, de forma oculta.

    class Pessoa:
        ano = 2024 # atributo de classe

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def metodo_de_classe(self):
            print('Howdy!')

        @classmethod
        def metodo_de_classe_sem_self(cls):
            print('Hello!')

        @classmethod
        def criar_com_50_anos(cls, nome):
            return cls(nome, 50)

    p2 = Pessoa.criar_com_50_anos('Miyami')
    print(p2.nome)
    print(p2.idade)

Ou seja, isso que e o factories methods, que e um metodo que cria novos objetos com alguma logica.

Lembrando que nao temos o self dentro desses @classmethod. Entao, vc nao conseguiria dizer 'self.nome' ou 'self.idade' em si. Ou seja, pensa @classmethod e como se fosse um molde ou uma extensao de molde de uma classe.

## @classmethod:
Em Python, o decorador @classmethod é usado para definir um método da classe que pode ser chamado diretamente na classe, sem a necessidade de criar uma instância dela. Este método recebe o primeiro parâmetro como cls, que representa a própria classe, ao invés de self, que representa uma instância da classe.

### Utilidades de @classmethod:

- Acesso a Atributos de Classe: Permite modificar ou acessar variáveis que são específicas da classe, não de instâncias individuais.

- Fábrica de Instâncias (Factory Methods): Frequentemente usado para criar métodos de fábrica. Um método de fábrica é um método que retorna objetos da classe, mas não necessariamente usando o construtor diretamente.

Exemplo de Uso de @classmethod

    class Pessoa:
        especie = "Homo sapiens"

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        @classmethod
        def criar_bebe(cls, nome):
            return cls(nome, 0)

        @classmethod
        def mudar_especie(cls, nova_especie):
            cls.especie = nova_especie

No exemplo acima:

- criar_bebe é um método de fábrica que cria uma nova instância da classe Pessoa com idade 0.

- mudar_especie é um método que altera o atributo de classe especie.

### Utilidades dos Factory Methods:
- 1. Simplificação da Criação de Instâncias: Podem oferecer uma maneira mais intuitiva ou simplificada de criar instâncias, especialmente quando a criação envolve lógica complexa.

- 2. Nomeação de Construtores Alternativos: Permitem que você tenha múltiplos "construtores" com nomes claros que podem inicializar a classe de maneiras diferentes.

- 3. Encapsulamento de Lógica de Instanciação: Encapsula a lógica de criação de instâncias dentro da classe, mantendo o código externo mais limpo e simples.

Exemplo de Factory Method

    class Carro:
        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo

        @classmethod
        def com_ano_modelo(cls, marca, modelo, ano):
            carro = cls(marca, modelo)
            carro.ano = ano
            return carro

No exemplo acima, com_ano_modelo é um factory method que não só cria uma instância de Carro, mas também adiciona um atributo adicional ano à instância.

Em resumo, @classmethod e factory methods são ferramentas poderosas em Python para gerenciar como as instâncias são criadas e como a lógica relacionada à classe é manipulada.

## O que nao tem em @classmethod que tem na forma comum de instanciar uma classe?
Suponha que temos uma classe Empregado que precisa de um método para criar um empregado a partir de uma string que contém o nome e o salário separados por hífen. Isso é um exemplo clássico de um factory method, onde a lógica de criação da instância é um pouco mais complexa do que apenas passar argumentos diretamente para o construtor.

    class Empregado:
        def __init__(self, nome, salario):
            self.nome = nome
            self.salario = salario

        @classmethod
        def de_string(cls, dados_str):
            nome, salario = dados_str.split('-')
            return cls(nome, float(salario))

    # Instanciação comum
    emp1 = Empregado("João", 5000.00)

    # Instanciação usando @classmethod
    emp2 = Empregado.de_string("Maria-7000.00")

    print(emp1.nome, emp1.salario)  # Saída: João 5000.0
    print(emp2.nome, emp2.salario)  # Saída: Maria 7000.0

A instanciação comum de uma classe é mais vantajosa quando a criação do objeto é direta e não requer lógica adicional para configurar o objeto. Isso é particularmente útil quando os valores necessários para criar um objeto são simples e podem ser passados diretamente para o construtor sem necessidade de pré-processamento ou configuração complexa.

### Exemplo Prático: Classe Ponto
Considere uma classe Ponto que representa um ponto em um sistema de coordenadas bidimensional. A criação de um ponto é direta, onde apenas as coordenadas x e y são necessárias.

    class Ponto:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f"Ponto({self.x}, {self.y})"

    # Instanciação comum
    p1 = Ponto(3, 4)
    p2 = Ponto(5, 6)

    print(p1)  # Saída: Ponto(3, 4)
    print(p2)  # Saída: Ponto(5, 6)

#### Vantagens da Instanciação Comum Neste Caso
- 1. Simplicidade: A criação de um objeto Ponto é muito simples e direta. Os valores de x e y são passados diretamente ao construtor sem necessidade de manipulação adicional.

- 2. Clareza: A instanciação comum torna o código fácil de entender. Quando você vê Ponto(3, 4), é imediatamente claro que um ponto está sendo criado com coordenadas x=3 e y=4.

- 3. Performance: Embora a diferença seja geralmente mínima, a instanciação comum evita o overhead adicional de processamento que pode acompanhar um método de classe que manipula dados antes de criar uma instância.

- 4. Menos Código: Não há necessidade de definir um método de classe adicional se a lógica de criação do objeto não exigir isso. Menos código significa menos manutenção e menor chance de bugs.

#### Contexto onde @classmethod seria menos útil
No caso da classe Ponto, um @classmethod seria menos útil a menos que houvesse uma necessidade específica de criar pontos de uma maneira não convencional que exigisse algum tipo de cálculo ou configuração especial antes da criação do objeto. Por exemplo, se precisássemos de um método para criar um ponto que sempre esteja a uma certa distância de outro ponto, poderíamos considerar um @classmethod. No entanto, para a criação básica de pontos, a instanciação comum é mais direta e adequada.

Este exemplo mostra como a instanciação comum pode ser a escolha ideal para situações em que a criação de objetos é direta e não envolve lógica complexa.

### Diferenças entre @classmethod e Instanciação Comum
- 1. Flexibilidade na Criação: O método de_string permite uma forma alternativa de criar uma instância da classe Empregado, processando uma string para extrair os dados necessários. Isso não é possível com a instanciação comum, a menos que essa lógica seja colocada fora da classe.

- 2. Encapsulamento de Lógica Específica: O @classmethod encapsula a lógica de conversão de uma string para uma instância dentro da classe. Isso mantém o código que usa a classe Empregado mais limpo e focado, sem se preocupar com os detalhes de como os dados são processados.

- 3. Uso de cls em vez de self: O @classmethod usa cls para acessar a classe e criar uma instância. Isso significa que ele opera com a classe em si, não com uma instância da classe. Em contraste, métodos regulares que usam self operam em instâncias específicas da classe.

- 4. Herança e Polimorfismo: Se Empregado fosse uma classe base para outras classes, de_string ainda retornaria uma instância da classe que foi chamada, graças ao uso de cls. Isso é útil em situações de herança, onde subclasses podem querer herdar ou modificar o comportamento do factory method.

Este exemplo ilustra como @classmethod pode ser usado para adicionar métodos de criação alternativos que encapsulam lógica específica, proporcionando flexibilidade e mantendo o código organizado.
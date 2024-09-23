# Aula 24 - Tipos Heranças - Python Orientado a Objetos - Herança Simples:
Na teoria das categorias, a ideia de "herança" como conhecida na programação orientada a objetos (POO) não é um conceito diretamente aplicável, pois a teoria das categorias lida com objetos e morfismos em um contexto matemático muito mais abstrato. No entanto, podemos traçar paralelos entre alguns conceitos de teoria das categorias e tipos de herança em POO.

Em Python ja existe, naturalmente, uma superclasse de todas as classes que e o object. Que e simplesmente uma classe que nao tem nada. E tupo um subconjunto de todos os conjuntos... Vazio.

## Tipos de Herança em Programação Orientada a Objetos:
1. Herança Simples: Uma classe herda diretamente de uma única superclasse. Este é o tipo mais comum de herança, amplamente suportado em muitas linguagens de programação como Java, C#, e Python.

2. Herança Múltipla: Uma classe pode herdar de mais de uma classe base. Isso permite que uma subclasse combine comportamentos e atributos de múltiplas superclasses. Python é um exemplo de uma linguagem que suporta herança múltipla.

3. Herança Multinível: Uma forma de herança onde uma classe é derivada de uma classe que é ela mesma derivada de outra classe. Por exemplo, se temos uma classe Animal, uma classe Mamífero que herda de Animal, e uma classe Cão que herda de Mamífero.

4. Herança Hierárquica: Ocorre quando uma classe base é herdada por múltiplas subclasses. Por exemplo, uma classe Veículo pode ser herdada por classes Carro, Bicicleta e Caminhão.

## Conceitos Relacionados na Teoria das Categorias:
Embora a teoria das categorias não trate diretamente de herança como em POO, alguns conceitos relacionados podem ser considerados:

- Objetos e Morfismos: Em teoria das categorias, objetos podem ser vistos como "tipos" ou "classes", e morfismos como "funções" ou "métodos" entre esses objetos. Isso se assemelha à forma como métodos operam sobre instâncias de classes em POO.

- Funtores: Representam mapeamentos entre categorias que preservam a estrutura de objetos e morfismos. Funtores podem ser pensados como uma forma de transformação ou mapeamento entre diferentes estruturas, o que pode ser comparado à forma como subclasses transformam ou estendem o comportamento das superclasses.

- Limites e Colimites: Estes conceitos tratam da combinação de objetos e morfismos de maneira a construir novos objetos que preservam certas propriedades. Isso pode ser vagamente relacionado à herança múltipla, onde uma classe combina características de múltiplas superclasses.

## Conclusão:
Na prática da programação orientada a objetos, os tipos de herança mais comumente usados são a herança simples e a herança múltipla. A teoria das categorias, embora forneça uma estrutura matemática rica para pensar sobre estruturas e transformações, não se aplica diretamente aos conceitos de herança em POO, mas oferece uma linguagem para descrever abstrações de alto nível que podem ser úteis em design de software complexo e teoria de tipos.

## Exemplos para cada tipo de Herança listado acima:
Aqui estão exemplos de código em Python para ilustrar os diferentes tipos de herança mencionados:

### Herança Simples
Herança simples ocorre quando uma subclasse herda diretamente de uma única superclasse.

    class Animal:
        def __init__(self, nome):
            self.nome = nome

        def falar(self):
            return "Som genérico de animal"

    class Cachorro(Animal):
        def falar(self):
            return "Au au!"

    # Uso
    animal = Animal("Bicho")
    cachorro = Cachorro("Rex")
    print(animal.falar())  # Saída: Som genérico de animal
    print(cachorro.falar())  # Saída: Au au!

### Herança Múltipla
Herança múltipla ocorre quando uma subclasse herda de mais de uma superclasse.

    class Terrestre:
        def caminhar(self):
            return "Caminhando..."

    class Aquatico:
        def nadar(self):
            return "Nadando..."

    class Anfibio(Terrestre, Aquatico):
        pass

    # Uso
    sapo = Anfibio()
    print(sapo.caminhar())  # Saída: Caminhando...
    print(sapo.nadar())  # Saída: Nadando...

### Herança Multinível
Herança multinível ocorre quando uma subclasse herda de uma superclasse, que por sua vez também é uma subclasse de outra superclasse.

    class Veiculo:
        def descricao(self):
            return "Veículo genérico"

    class Carro(Veiculo):
        def descricao(self):
            return "Carro"

    class Sedan(Carro):
        def descricao(self):
            return "Sedan"

    # Uso
    veiculo = Veiculo()
    carro = Carro()
    sedan = Sedan()
    print(veiculo.descricao())  # Saída: Veículo genérico
    print(carro.descricao())  # Saída: Carro
    print(sedan.descricao())  # Saída: Sedan

### Herança Hierárquica
Herança hierárquica ocorre quando várias subclasses herdam de uma única superclasse.

    class Veiculo:
        def descricao(self):
            return "Veículo genérico"

    class Carro(Veiculo):
        def descricao(self):
            return "Carro"

    class Motocicleta(Veiculo):
        def descricao(self):
            return "Motocicleta"

    # Uso
    veiculo = Veiculo()
    carro = Carro()
    motocicleta = Motocicleta()
    print(veiculo.descricao())  # Saída: Veículo genérico
    print(carro.descricao())  # Saída: Carro
    print(motocicleta.descricao())  # Saída: Motocicleta

## Herança Simples
A herança simples é um dos conceitos fundamentais da programação orientada a objetos (POO). Ela permite que uma classe derive ou herde propriedades (atributos) e comportamentos (métodos) de outra classe. Na herança simples, uma classe herda diretamente de apenas uma superclasse.

### Conceitos Básicos
- Superclasse (Classe Base ou Classe Pai): É a classe cujas propriedades e métodos são herdados por outra classe.

- Subclasse (Classe Derivada ou Classe Filha): É a classe que herda propriedades e métodos de outra classe.

### Vantagens da Herança Simples
1. Reutilização de Código: Permite que novas classes reutilizem código de classes já existentes sem reescrevê-lo.

2. Organização do Código: Facilita a organização e manutenção do código ao agrupar comportamentos comuns em uma classe base.

3. Extensibilidade: Novas funcionalidades podem ser adicionadas facilmente através de subclasses.

4. Hierarquia de Classes: Estabelece uma relação natural entre classes mais gerais (superclasses) e classes mais específicas (subclasses).

### Como Funciona
Quando uma classe herda de outra, ela automaticamente incorpora todos os atributos e métodos da classe base. A subclasse pode então:

- Utilizar os métodos herdados diretamente.

- Modificar (sobrescrever) os métodos herdados.

- Adicionar novos métodos e atributos próprios.

### Detalhes Importantes
- Construtor da Superclasse: Subclasses em Python não herdam o construtor da superclasse automaticamente. Se você definir um construtor na subclasse (__init__), você precisa chamar explicitamente o construtor da superclasse usando super().__init__() se necessário.

- Sobrescrita de Métodos: A subclasse pode modificar o comportamento de um método herdado. Isso é conhecido como sobrescrita de método (method overriding).

- Polimorfismo: A herança permite o polimorfismo, onde o mesmo método pode ter várias implementações diferentes em diferentes subclasses.

### Conclusão
A herança simples é uma ferramenta poderosa em POO que facilita a reutilização de código, a extensibilidade e a manutenção do software. Ao entender e aplicar corretamente a herança, os desenvolvedores podem criar sistemas mais robustos e flexíveis, mantendo o código organizado e eficiente.
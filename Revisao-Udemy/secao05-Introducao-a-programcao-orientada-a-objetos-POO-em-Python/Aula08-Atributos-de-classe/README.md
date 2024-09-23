# Aula 08 - Atributos de classe:
Vamos abordar mais ainda sobre o conceito de atributo de classe.

Atributos de classe em Python são variáveis que são definidas dentro de uma classe, mas fora de qualquer método. Esses atributos são compartilhados por todas as instâncias da classe, o que significa que eles têm o mesmo valor para cada instância, a menos que explicitamente alterados. Atributos de classe são úteis para armazenar propriedades que devem ser as mesmas para todas as instâncias de uma classe.

Bom, como podemos ver no nosso exemplo que criamos

    class Pessoa:
        atributo = 'valor'

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def get_ano_nascimento(self):
            return 2024 - self.idade
        
    p1 = Pessoa('Joao', 35)
    p2 = Pessoa('Helena', 12)

    print(p1.get_ano_nascimento())
    print(p2.get_ano_nascimento())

A classe, Pessoa, que foi criado, nela, conseguimos definir o atributo chamado 'atributo'. E no metodo, get_ano_nascimento, temos um hard coder, 2024. Para esse hard coder, podemos criar uma constante fora da classe como seguinte

    # Atributos e classe
    ANO_ATUAL = 2024

    class Pessoa:
        atributo = 'valor'

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def get_ano_nascimento(self):
            return ANO_ATUAL - self.idade
        
    p1 = Pessoa('Joao', 35)
    p2 = Pessoa('Helena', 12)

    print(p1.get_ano_nascimento())
    print(p2.get_ano_nascimento())

Mas, tambem, como uma alternativa pratica, podemos criar um atributo desse tipo dentro da classe tbm

    # Atributos e classe
    # ANO_ATUAL = 2024

    class Pessoa:
        # atributo = 'valor'
        ano_atual = 2024

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def get_ano_nascimento(self):
            return Pessoa.ano_atual - self.idade
        
    p1 = Pessoa('Joao', 35)
    p2 = Pessoa('Helena', 12)

    print(p1.get_ano_nascimento())
    print(p2.get_ano_nascimento())

Para acessarmos esse atributo, que esta valendo para todas as classes, existem duas formas:

- Primeira: Pessoa.ano_atual

- Segunda: self.ano_atual - Pode existir uma instancia, ano_atual, no init. Entao, para separarmos entre o que e atributo e instancia, melhor adotarmos a pratica acima para atributos, quando for acessar o seu valor.

A primeira forma de acessarmos o atributo, ano_atual, dentro da classe, esta entre as boas praticas. Ja a segunda ela e um pouco perigosa, pois, dependendo do caso, fica sujeito a alteracao no processo de instanciacao externo.

Como vimos na aula anterior, conseguimos acessar esse atributo dentro dessa classe sem a necessidade de instanciarmos a classe, Pessoa

    # Atributos e classe
    # ANO_ATUAL = 2024

    class Pessoa:
        # atributo = 'valor'
        ano_atual = 2024

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def get_ano_nascimento(self):
            return Pessoa.ano_atual - self.idade
        
    p1 = Pessoa('Joao', 35)
    p2 = Pessoa('Helena', 12)

    print(Pessoa.ano_atual)
    print(p1.get_ano_nascimento())
    print(p2.get_ano_nascimento())

Porem, esse atributo que definimos dentro dessa classe, ela esta sujeita a alteracao, como seguinte

    # Atributos e classe
    # ANO_ATUAL = 2024

    class Pessoa:
        # atributo = 'valor'
        ano_atual = 2024

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def get_ano_nascimento(self):
            return Pessoa.ano_atual - self.idade
        
    p1 = Pessoa('Joao', 35)
    p2 = Pessoa('Helena', 12)

    print(Pessoa.ano_atual)
    Pessoa.ano_atual = 1

    print(p1.get_ano_nascimento())
    print(p2.get_ano_nascimento())

Mas qual o motivo disso ter ocorrido? Bom, o motivo disso e porque ela e o atributo da classe. Ou seja, um atributo que esta atrelado ao molde em si. Entao, quando vc mudar o valor dela, essa mudanca surtira para todas as instancias efetudadas.

## Utilidades dos Atributos de Classe
1. Valores Constantes: Atributos de classe são frequentemente usados para definir constantes que são relevantes para todas as instâncias da classe.

2. Contadores ou Estatísticas: Eles podem ser usados para contar o número de instâncias de uma classe ou acumular valores que são relevantes em um nível de classe, como o total de todas as transações feitas em todas as instâncias de uma classe de conta bancária.

3. Configurações Padrão: Atributos de classe podem ser usados para definir valores padrão que são compartilhados por todas as instâncias, como configurações padrão em aplicativos.

4. Métodos de Fábrica: Eles podem ser usados em conjunto com métodos de classe para criar instâncias de uma maneira particular, baseada em parâmetros que são comuns a todas as instâncias.

5. Dados Compartilhados: Eles permitem que dados sejam compartilhados entre todas as instâncias de uma classe, o que pode ser útil para implementar certos padrões de design como Singleton.

## Exemplo de Atributo de Classe

    class Carro:
        numero_de_rodas = 4  # Atributo de classe

        def __init__(self, marca, modelo):
            self.marca = marca  # Atributo de instância
            self.modelo = modelo  # Atributo de instância

        def detalhes(self):
            return f"{self.marca} {self.modelo} tem {Carro.numero_de_rodas} rodas."

    # Acessando o atributo de classe diretamente pela classe
    print(Carro.numero_de_rodas)  # Saída: 4

    # Modificando o atributo de classe afeta todas as instâncias
    Carro.numero_de_rodas = 6
    carro1 = Carro("Toyota", "Corolla")
    carro2 = Carro("Honda", "Civic")

    print(carro1.detalhes())  # Saída: Toyota Corolla tem 6 rodas.
    print(carro2.detalhes())  # Saída: Honda Civic tem 6 rodas.

## Considerações
Alterar um atributo de classe afeta todas as instâncias que acessam esse atributo através da classe. No entanto, se uma instância sobrescreve esse atributo (por exemplo, self.numero_de_rodas = 5), essa mudança será local para a instância.

Atributos de classe são uma ferramenta poderosa para compartilhar dados e comportamentos entre todas as instâncias de uma classe, mas devem ser usados com cuidado para evitar comportamentos inesperados devido ao compartilhamento de estado.
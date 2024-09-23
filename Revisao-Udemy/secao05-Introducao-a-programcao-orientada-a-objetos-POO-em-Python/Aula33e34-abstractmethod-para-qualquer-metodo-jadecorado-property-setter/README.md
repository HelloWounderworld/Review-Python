# Aula 33 e 34 - Classes abstratas - Abstract Base Class (abc) - Python Orientado a Objetos - abstractmethod para qualquer método já decorado (property e setter):

## Classes abstratas
Classes abstratas em Python são uma ferramenta fundamental na programação orientada a objetos, especialmente quando se deseja criar uma base de classe que defina um modelo para outras classes, mas que por si só não deve ser instanciada. Em Python, classes abstratas são implementadas com a ajuda do módulo abc (Abstract Base Classes).

### O que são Classes Abstratas?
Uma classe abstrata é uma classe que não pode ser instanciada por conta própria e é destinada apenas a servir como uma classe base para outras classes. Classes abstratas são usadas para definir interfaces quando há um grupo de métodos relacionados que as subclasses devem implementar. Elas promovem um design limpo e permitem a reutilização de código.

### Por que usar Classes Abstratas?
- Definir um Contrato para Subclasses: Classes abstratas permitem que você defina métodos que devem ser criados pelas subclasses, garantindo assim uma interface consistente.

- Prevenir a Instanciação: Evitam a criação de objetos de classes que são concebidas apenas para serem base de outras classes.

- Organização do Código: Facilitam a organização do código e a manutenção, pois centralizam e padronizam comportamentos comuns.

### Como Implementar Classes Abstratas em Python
Para criar uma classe abstrata em Python, você precisa importar ABC e abstractmethod do módulo abc.

    from abc import ABC, abstractmethod

    class Animal(ABC):
        @abstractmethod
        def falar(self):
            pass

Neste exemplo, Animal é uma classe abstrata porque herda de ABC, uma classe auxiliar do módulo abc que facilita a criação de classes abstratas. O método falar é decorado com @abstractmethod, o que significa que qualquer subclasse de Animal deve implementar o método falar.

### Exemplo Completo

    from abc import ABC, abstractmethod

    class Animal(ABC):
        def __init__(self, nome):
            self.nome = nome

        @abstractmethod
        def falar(self):
            pass

    class Cachorro(Animal):
        def falar(self):
            return f"{self.nome} diz: Au au!"

    class Gato(Animal):
        def falar(self):
            return f"{self.nome} diz: Miau!"

    # Instanciando objetos
    # animal = Animal("Bicho")  # Isso resultará em erro, pois Animal é abstrato
    dog = Cachorro("Rex")
    cat = Gato("Whiskers")

    print(dog.falar())  # Saída: Rex diz: Au au!
    print(cat.falar())  # Saída: Whiskers diz: Miau!

Neste exemplo, tentar instanciar Animal diretamente resultará em um erro, pois é uma classe abstrata. As subclasses Cachorro e Gato implementam o método falar, conforme exigido pela classe base abstrata.

### Considerações Importantes
- Métodos Abstratos: Podem ter uma implementação na classe abstrata, mas ainda assim, as subclasses são obrigadas a sobrescrever esses métodos.

- Múltiplos Métodos Abstratos: Uma classe abstrata pode ter vários métodos abstratos.

- Subclasses de Subclasses: Se uma subclasse não implementar todos os métodos abstratos, ela também será considerada uma classe abstrata.

### Conclusão
Classes abstratas são uma parte essencial da programação orientada a objetos em Python, proporcionando uma estrutura robusta para o código. Elas forçam um contrato nas subclasses, garantindo que certos métodos sejam implementados, o que é crucial para manter a integridade e a previsibilidade do comportamento das classes em projetos complexos.

## Classes abstratas no sentido da Teoria de Tipos:
Na teoria dos tipos, uma classe abstrata pode ser entendida como um tipo abstrato. Um tipo abstrato é um tipo que não pode ser instanciado diretamente, mas serve como um modelo ou contrato para os tipos derivados (subtipos). Esses subtipos devem implementar ou concretizar as especificações definidas pelo tipo abstrato.

### Definição Formal em Teoria dos Tipos
1. Tipo Abstrato 1: Um tipo que define uma coleção de operações (métodos) sem implementá-las. Este tipo não pode ser instanciado por si só. Ele apenas especifica um conjunto de operações que todos os subtipos concretos devem implementar.

2. Subtipos (S1, S2, ...): Tipos que herdam do tipo abstrato T e fornecem implementações específicas para as operações definidas por T. Esses são os tipos que podem ser instanciados e usados em programas.

### Exemplo
Suponha que temos um tipo abstrato Animal que define a operação emitirSom. Animal por si só não pode ser instanciado porque não sabemos como um animal genérico emite som. No entanto, podemos ter subtipos como Cachorro e Gato que são concretizações de Animal:

- Animal (Tipo Abstrato):

    - Operações: emitirSom()

- Cachorro (Subtipo de Animal):

    - Implementa emitirSom() para retornar "Au au!"

- Gato (Subtipo de Animal):

    - Implementa emitirSom() para retornar "Miau!"

### Propriedades Importantes
- Encapsulamento: O tipo abstrato encapsula o comportamento esperado dos seus subtipos, definindo uma interface comum sem detalhar a implementação.

- Polimorfismo: Objetos de diferentes subtipos do mesmo tipo abstrato podem ser usados de forma intercambiável em um programa, desde que o programa interaja com eles através da interface definida pelo tipo abstrato.

- Reutilização e Extensibilidade: Novos subtipos podem ser criados a partir do tipo abstrato sem alterar o código existente que usa o tipo abstrato, facilitando a extensão e a manutenção do sistema.

### Conclusão
Essa abordagem na teoria dos tipos ajuda a garantir que os sistemas sejam construídos de forma modular e extensível, com partes do sistema dependendo apenas de interfaces bem definidas, e não de implementações específicas.

Seguir link para leitura:

    https://docs.python.org/3/library/abc.html
# Aula 35 e 36 - Teoria e Pratica: polimorfismo, assinatura de métodos e Liskov Substitution Principle:

## Polimorfismo
Polimorfismo é um conceito fundamental em programação orientada a objetos (POO) que permite que objetos de diferentes classes sejam tratados através da mesma interface. Em Python, isso é alcançado principalmente através de métodos que podem ser definidos em várias classes, mas com implementações específicas para cada uma delas. O termo "polimorfismo" vem do grego e significa "muitas formas".

### Conceitos Básicos
1. Polimorfismo de Métodos: Refere-se à capacidade de diferentes objetos responderem, de maneira específica, a uma mesma chamada de método. Isso é possível através da sobrescrita de métodos em subclasses.

2. Polimorfismo com Funções: Em Python, funções que podem aceitar diferentes tipos de parâmetros são também uma forma de polimorfismo. Por exemplo, a função len() pode aceitar qualquer objeto que defina o método especial __len__().

### Como Funciona
- Sobrescrita de Métodos: Subclasses podem fornecer uma implementação específica de um método que já é definido em sua superclasse. Isso é conhecido como sobrescrita de método (method overriding).

- Métodos Especiais: Python utiliza métodos especiais (como __str__, __repr__, __add__) que permitem a implementação de operações que podem ser "polimórficas" dependendo do tipo de objeto. Por exemplo, o método __add__ pode ser definido de maneira diferente em classes para representar soma de números, concatenação de strings, ou união de conjuntos.

### Exemplos Práticos

    class Animal:
        def falar(self):
            pass

    class Cachorro(Animal):
        def falar(self):
            return "Au au!"

    class Gato(Animal):
        def falar(self):
            return "Miau!"

    def animal_som(animal):
        print(animal.falar())

    # Uso
    dog = Cachorro()
    cat = Gato()
    animal_som(dog)  # Saída: Au au!
    animal_som(cat)  # Saída: Miau!

Neste exemplo, a função animal_som é polimórfica porque pode aceitar um objeto de qualquer classe que seja um Animal e chamar o método falar, que é implementado de forma específica para cada classe.

### Vantagens do Polimorfismo
1. Flexibilidade e Reutilização: Código que pode operar com objetos de diferentes tipos é mais flexível e pode ser reutilizado em diferentes contextos.

2. Simplicidade: Polimorfismo permite que complexidades sejam encapsuladas, tornando o código externo mais simples e limpo.

3. Extensibilidade: Novos tipos de objetos que seguem a mesma interface podem ser adicionados sem alterar muito o código existente que usa a interface.

### Considerações Importantes
- Interface Consistente: É crucial que métodos polimórficos em diferentes classes mantenham uma interface consistente em termos de parâmetros de entrada e tipo de retorno.

- Documentação: Devido à sua natureza flexível, é importante que o comportamento esperado de métodos polimórficos seja bem documentado.

- Uso de isinstance e issubclass: Embora geralmente seja melhor evitar verificações explícitas de tipo em Python (em favor de "duck typing"), em alguns casos complexos, pode ser necessário verificar tipos para implementar comportamento condicional.

### Conclusão
Polimorfismo é uma poderosa ferramenta em Python que permite a construção de interfaces flexíveis e reutilizáveis, facilitando a manutenção e expansão de sistemas. Ele é central para a implementação de muitos padrões de design e práticas recomendadas em programação orientada a objetos.

## Polimorfismo em termos matematicos
Polimorfismo, no contexto da matemática e ciência da computação teórica, não possui uma definição "matemática" específica como você encontraria para conceitos puramente matemáticos como integrais ou derivadas. No entanto, pode ser descrito em termos de teoria dos tipos e sistemas de tipos, que são fundamentais na matemática da computação.

### Definição em Teoria dos Tipos
Em teoria dos tipos, que é uma área da matemática e lógica que lida com sistemas que podem categorizar, ou tipificar, entidades, o polimorfismo refere-se à capacidade de uma função ou um tipo de operar em diferentes tipos de dados. Em sistemas de tipos, isso é frequentemente expresso através de:

- Polimorfismo Paramétrico: Funções ou tipos que podem ser escritos genericamente para operar em qualquer tipo de dados, que são especificados como parâmetros de tipo. Isso é semelhante a funções genéricas em linguagens de programação como Java (com Generics) ou C++ (com templates).

- Polimorfismo Ad-hoc: Funções que podem ser aplicadas a argumentos de diferentes tipos em maneiras que não são intercambiáveis, o que pode ser implementado através de sobrecarga de funções ou métodos.

### Exemplo Matemático de Polimorfismo Paramétrico
Considere uma função identidade em teoria dos tipos, que é uma função que retorna exatamente o que é dado a ela. Matematicamente, pode ser expressa como:

$f:\mathcal{A}\longrightarrow\mathcal{A}$

onde $\mathcal{A}$ é um tipo de parâmetro. Esta função é polimórfica porque pode operar sobre qualquer tipo $\mathcal{A}$, seja ele um número, uma string, ou uma estrutura de dados mais complexa.

### Exemplo Matemático de Polimorfismo Ad-hoc
Considere a operação de "soma" que pode ser definida para números inteiros, números reais, e vetores. Cada uma dessas implementações da "soma" pode comportar-se de maneira diferente dependendo do tipo de seus operandos, mas todas compartilham o mesmo nome de operação. Matematicamente, isso pode ser representado por diferentes funções:

$sum:\mathbb{Z}\times\mathbb{Z}\longrightarrow\mathbb{Z}$

$sum:\mathbb{R}\times\mathbb{R}\longrightarrow\mathbb{R}$

$sum:\mathbb{R}^{n}\times\mathbb{R}^{n}\longrightarrow\mathbb{R}^{n}$

Cada uma dessas funções "sum" é específica para seu tipo de entrada, mas todas realizam a operação conceitual de "adição".

### Conclusão
Embora o polimorfismo seja um conceito amplamente discutido e utilizado em ciência da computação, especialmente em linguagens de programação e design de software, sua aplicação em matemática pura é mais indireta, relacionando-se principalmente com a teoria dos tipos e a formalização de sistemas de tipos em lógica matemática.

## Assinatura de Método
A assinatura de um método em Python refere-se à definição de como o método é declarado, incluindo o nome do método, os parâmetros que ele aceita e, em alguns casos, o tipo de valor que ele retorna. A assinatura é crucial para entender como os métodos podem ser usados e como eles interagem com outras partes do código, especialmente em contextos de herança e polimorfismo.

### Componentes de uma Assinatura de Método
1. Nome do Método: Identifica o método de forma única dentro de sua classe.

2. Parâmetros: Lista de variáveis que o método aceita. Em Python, os parâmetros podem ser obrigatórios, opcionais (com valores padrão), ou variáveis (usando args para listas e kwargs para dicionários).

3. Tipo de Retorno: Em Python, com a adição de type hints (sugestões de tipo), a assinatura de um método também pode incluir o tipo de dado que o método deve retornar.

### Exemplo de Assinatura de Método com Type Hints

    def soma(a: int, b: int) -> int:
        return a + b

## Liskov Substitution Principle (LSP)
O Princípio de Substituição de Liskov, um dos cinco princípios SOLID de design orientado a objetos, afirma que se uma classe S é um subtipo de uma classe T, então objetos do tipo T em um programa podem ser substituídos por objetos do tipo S sem alterar as propriedades desejáveis desse programa (correção, tarefa realizada, etc.).

### Implicações do LSP
- Preservação de Comportamento: Subclasses não devem alterar o comportamento esperado da superclasse. Isso significa que métodos sobrescritos na subclasse devem aderir à "promessa" feita pela superclasse.

- Compatibilidade de Assinaturas: As assinaturas dos métodos sobrescritos devem ser compatíveis. Em Python, isso geralmente significa que os parâmetros e os tipos de retorno devem corresponder, embora Python seja dinâmico e permita certa flexibilidade.

### Relação com Polimorfismo
O polimorfismo e o LSP estão intrinsecamente ligados. O polimorfismo permite que diferentes classes derivadas sejam tratadas através de uma interface comum (por exemplo, chamando o mesmo método). O LSP garante que essa substituição seja segura e que os objetos derivados possam ser usados no lugar de objetos da classe base sem causar erros ou comportamentos inesperados.

### Exemplo Demonstrativo

    class Bird:
        def fly(self):
            print("This bird can fly.")

    class Penguin(Bird):
        def fly(self):
            raise Exception("Penguins do not fly.")

    def make_it_fly(bird: Bird):
        bird.fly()

    # Usando o princípio de substituição de Liskov corretamente
    sparrow = Bird()
    make_it_fly(sparrow)  # Funciona bem

    # Quebra o princípio de substituição de Liskov
    penguin = Penguin()
    make_it_fly(penguin)  # Levanta uma exceção

Neste exemplo, a classe Penguin quebra o LSP porque altera o comportamento esperado do método fly() herdado de Bird, levando a uma exceção inesperada. Isso demonstra a importância de manter a compatibilidade de comportamento ao aplicar polimorfismo e herança.

### Conclusão
A assinatura do método e o Liskov Substitution Principle são fundamentais para implementar polimorfismo eficaz e seguro em Python. Eles garantem que o código seja modular, reutilizável e, acima de tudo, confiável, ao permitir que subclasses sejam substituídas por suas superclasses sem efeitos colaterais indesejados.
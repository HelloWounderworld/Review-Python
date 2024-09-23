# Aula 23 - TEORIA: Herança, generalização e especialização:
Herança é um dos pilares fundamentais da programação orientada a objetos (POO). Ela permite que uma classe herde atributos e métodos de outra classe. A classe que herda é chamada de classe derivada ou subclasse, enquanto a classe da qual os atributos e métodos são herdados é chamada de classe base ou superclasse.

## Vantagens da Herança:
1. Reutilização de Código: Permite reutilizar código da classe base, reduzindo a redundância.

2. Organização do Código: Facilita a organização e manutenção do código ao agrupar comportamentos comuns em uma classe base.

3. Extensibilidade: Novas funcionalidades podem ser adicionadas facilmente através de subclasses.

4. Hierarquia de Classes: Estabelece uma relação natural entre classes mais gerais (superclasses) e classes mais específicas (subclasses).

## Tipos de Herança:
- Herança Simples: Uma classe herda de apenas uma classe base.

- Herança Múltipla: Uma classe pode herdar comportamentos e atributos de mais de uma classe base.

## Exemplo em Python:
Vamos considerar um exemplo simples onde temos uma classe base chamada Veiculo e duas subclasses chamadas Carro e Bicicleta.

    class Veiculo:
        def __init__(self, marca, ano):
            self.marca = marca
            self.ano = ano

        def mostrar_detalhes(self):
            print(f"Marca: {self.marca}, Ano: {self.ano}")

    class Carro(Veiculo):
        def __init__(self, marca, ano, hp):
            super().__init__(marca, ano)
            self.hp = hp

        def mostrar_detalhes(self):
            super().mostrar_detalhes()
            print(f"Potência: {self.hp} HP")

    class Bicicleta(Veiculo):
        def __init__(self, marca, ano, tipo):
            super().__init__(marca, ano)
            self.tipo = tipo

        def mostrar_detalhes(self):
            super().mostrar_detalhes()
            print(f"Tipo: {self.tipo}")

    # Criando instâncias
    carro = Carro("Toyota", 2021, 150)
    bicicleta = Bicicleta("Trek", 2020, "Mountain")

    # Mostrando detalhes
    carro.mostrar_detalhes()
    bicicleta.mostrar_detalhes()

- A classe Veiculo é a classe base com atributos comuns marca e ano.

- A classe Carro é uma subclasse de Veiculo e adiciona um novo atributo hp (cavalos de potência).

- A classe Bicicleta é outra subclasse de Veiculo e adiciona um atributo tipo para especificar o tipo de bicicleta.

- O método mostrar_detalhes() é definido na classe base e sobreescrito nas subclasses para adicionar informações adicionais.

- super().__init__(marca, ano) é usado para chamar o construtor da classe base, garantindo que os atributos da classe base sejam inicializados corretamente.

- super().mostrar_detalhes() é usado nas subclasses para chamar a implementação do método na classe base e então adicionar detalhes específicos da subclasse.

## Definição Matemática de Herança
Matematicamente, a herança em programação orientada a objetos pode ser modelada usando a teoria dos conjuntos. Vamos considerar que cada classe é um conjunto que contém métodos e atributos como seus elementos.

### Conjuntos e Relações de Subconjunto
Seja $\mathcal{C}$ o conjunto de todas as classes possíveis em um sistema de programação orientada a objetos. Para duas classes $\mathcal{A}$ e $\mathcal{B}$ em $\mathcal{C}$, dizemos que $\mathcal{A}$ é uma subclasse de $\mathcal{B}$ se todos os elementos (métodos e atributos) de $\mathcal{B}$ estão contidos em $\mathcal{A}$. Matematicamente, isso é expresso como:

$\mathcal{B}\subseteq\mathcal{A}$

Aqui, $\mathcal{B}$ é a superclasse e $\mathcal{A}$ é a subclasse. Esta relação de subconjunto indica que $\mathcal{A}$ herda todos os elementos de $\mathcal{B}$, e pode adicionar ou modificar elementos adicionais.

Isso significa que a herenca e um conjunto minimo, ou seja, um conjunto onde possui todos os elementos necessarios e suficientes para as suas subclasses.

Obs: conjunto minimal $\neq$ conjunto minimo. Ou seja, no conjunto minimal, que seria a intersecao nao vazia de todas as possiveis subclasses que possuem caracteristicas em comum, mas que tal processo de refinamento, os elementos resultantes dentro do conjunto minimal, por mais que sejam necessarios, nao necessariamente sao o suficientes. Entao, pelo menos, conseguimos dizer que conjunto minimal $\subseteq$ conjunto minimo.

### Conjunto Minimal
Em matemática, um conjunto minimal em um contexto de interseção é o conjunto que contém exatamente os elementos comuns a todos os conjuntos em um determinado sistema de conjuntos. Este é o menor conjunto possível que ainda retém os elementos comuns a todos os conjuntos considerados. Em termos de herança em POO, isso seria análogo a identificar os atributos e métodos que são absolutamente comuns a todas as subclasses derivadas de uma superclasse, assumindo que estamos considerando todas as subclasses possíveis.

### Conjunto Mínimo
Um conjunto mínimo pode ser entendido como o conjunto que contém os elementos necessários e suficientes para definir uma certa propriedade ou condição. No contexto da herança em POO, a superclasse pode ser vista como um conjunto mínimo para as subclasses, pois fornece os elementos essenciais (atributos e métodos) que as subclasses herdam e podem estender. Não necessariamente é o conjunto mais pequeno em termos de interseção de todos os conjuntos possíveis, mas é o conjunto base necessário para a funcionalidade das subclasses.

### Aplicação em POO
Quando modelamos herança em POO:

- A superclasse fornece um conjunto de características (atributos e métodos) que são essenciais e comuns para as subclasses. Este conjunto pode ser considerado "mínimo" no sentido de que fornece a base necessária sobre a qual as subclasses são construídas.

- As subclasses podem adicionar mais características além das fornecidas pela superclasse. Portanto, cada subclasse pode ser vista como um conjunto que inclui o conjunto da superclasse (conjunto mínimo) mais quaisquer elementos adicionais específicos da subclasse.

### Diferença Chave
A diferença chave entre "conjunto minimal" e "conjunto mínimo" no contexto de herança em POO é que:

- Conjunto minimal implicaria a interseção de todos os conjuntos de características de todas as subclasses possíveis, resultando nos elementos absolutamente comuns a todas.

- Conjunto mínimo na superclasse refere-se ao conjunto de características necessárias e suficientes que todas as subclasses herdarão e sobre as quais podem construir.

### Função de Herança
Podemos também definir uma função de herança $f$ que mapeia cada classe para sua superclasse direta, se houver:

$f:\mathcal{C}\longrightarrow\mathcal{C}$

onde $f\left(\mathcal{A}\right)=\mathcal{B}$ que signfica que $\mathcal{A}$ herda diretamente de $\mathcal{B}$. Se $\mathcal{A}$ não herda de nenhuma classe, então $f\left(\mathcal{A}\right)$ pode ser indefinido para essa classe, ou mapear para um elemento nulo que representa "nenhuma classe".

### Cadeias de Herança
Em sistemas mais complexos, uma classe pode herdar de outra que por sua vez herda de outra, formando uma cadeia de herança. Se $\mathcal{A}$ herda de $\mathcal{B}$, e $\mathcal{B}$ harda de $\mathcal{C}$, então indiret4famente $\mathcal{A}$ também herda de $\mathcal{C}$. Isso pode ser representado como uma sequência de aplicações da função $f$

$f\left(f\left(\mathcal{A}\right)\right)=\mathcal{C}$

### Exemplo Prático
Considere um sistema onde temos uma classe base Veiculo e duas subclasses Carro e Bicicleta. Matematicamente, podemos representar isso como:

- Veiculo $\subseteq$ Carro

- Veiculo $\subseteq$ Bicicleta

Isso indica que tanto Carro quanto Bicicleta herdam as propriedades e métodos de Veiculo.

Bom, apesar que nao serviu de exemplo...

## Conclusão
A herança, portanto, cria uma estrutura hierárquica de classes que permite a reutilização e extensão de código de maneira organizada e sistemática, facilitando a manutenção e expansão de sistemas de software. A modelagem matemática da herança ajuda a entender e formalizar essas relações em termos de teoria dos conjuntos e funções.

## Importante: Herança vs Composição

### Herança
Herança é um mecanismo pelo qual uma nova classe, chamada subclasse, pode herdar atributos e métodos de uma classe existente, chamada superclasse. A herança promove a reutilização de código e estabelece uma relação "é-um". Por exemplo, se considerarmos uma classe Pássaro e uma classe Pinguim, Pinguim é um tipo de Pássaro, então Pinguim pode herdar características e comportamentos da classe Pássaro.

#### Vantagens da Herança:
- Promove a reutilização de código.

- Estabelece relações naturais e hierárquicas entre classes.

- Facilita a manutenção e atualizações, pois as mudanças na superclasse podem beneficiar todas as subclasses.

#### Desvantagens da Herança:
- Pode levar a uma estrutura de classes rígida e frágil.

- As subclasses são fortemente acopladas à superclasse, o que pode ser problemático se a superclasse mudar.

- Pode levar a uma hierarquia de classes confusa se não for bem planejada.  

### Composição
Composição é um princípio de design onde uma classe inclui instâncias de outras classes como parte de seus campos, estabelecendo uma relação "tem-um". Por exemplo, uma classe Carro pode ter um Motor, Rodas, e assim por diante. A composição é geralmente preferida sobre a herança porque promove maior flexibilidade e menor acoplamento entre as classes.

#### Vantagens da Composição:
- Flexibilidade: objetos compostos podem facilmente trocar componentes em tempo de execução.

- Menor acoplamento: as classes não dependem das implementações umas das outras, apenas de suas interfaces.

- Encapsulamento: os detalhes internos de cada componente podem ser ocultados dos outros.

#### Desvantagens da Composição:
- Pode exigir mais esforço de design para definir interfaces adequadas entre componentes.

- Pode levar a um sistema com muitos pequenos objetos, o que pode ser mais difícil de entender e gerenciar.

### Conclusão
A escolha entre herança e composição depende do problema específico que você está tentando resolver. A herança é útil para estabelecer uma relação taxonômica (hierárquica) entre classes, enquanto a composição é útil para construir classes que são feitas de componentes intercambiáveis. Em muitos casos, a composição é considerada mais flexível e é recomendada como a abordagem de design preferida para a maioria das situações na POO.
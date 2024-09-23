# Aula 19 - Relações entre classes: associação, agregação e composição:
Na programação orientada a objetos (POO), as relações entre classes descrevem como objetos de diferentes classes interagem e dependem uns dos outros. Existem três tipos principais de relações: associação, agregação e composição. Cada tipo define um nível diferente de dependência entre as classes.

Neste topico iremos abordar sobre a relacao de Associacao.

## Associação
A associação é uma relação entre duas classes onde os objetos de uma classe se relacionam com os objetos de outra, mas ambos podem existir independentemente. É a forma mais básica de relação que simplesmente indica que uma classe conhece a outra.

### Definição Matemática:
Associação pode ser vista como uma relação binária $\mathcal{R}$ entre dois conjuntos $\mathcal{A}$ e $\mathcal{B}$, onde $\mathcal{A}$ e $\mathcal{B}$ representam diferentes tipos de objetos (classes). Matematicamente, isso é expresso como:

$\mathcal{R}\subseteq\mathcal{A}\times\mathcal{B}$

Cada par ordenado $\left(a,b\right)\in\mathcal{R}$ indica o objeto $\mathcal{a}$ da classe $\mathcal{A}$ está associado ao objeto $\mathcal{b}$ da classe $\mathcal{B}$.

### Exemplo:
Se $\mathcal{A}$ é um conjunto de professores e $\mathcal{B}$ é um conjunto de departamentos, uma relação de associação $\mathcal{R}$ pode representar quais professores trabalham em quais departamentos.

### Exemplos de Associação Simples
Vamos considerar um exemplo simples de uma biblioteca e seus livros:

    class Livro:
        def __init__(self, titulo):
            self.titulo = titulo

    class Bibliotecario:
        def __init__(self, nome):
            self.nome = nome

        def empresta_livro(self, livro):
            print(f"{self.nome} emprestou o livro {livro.titulo}")

    # Instâncias
    livro1 = Livro("1984")
    bibliotecario = Bibliotecario("João")

    # Associação sendo utilizada
    bibliotecario.empresta_livro(livro1)

Neste exemplo, a classe Bibliotecario está associada à classe Livro através do método empresta_livro. O bibliotecário conhece o livro, mas ambos podem existir independentemente.

### Exemplos de Associação com Múltiplas Formas
Vamos expandir o exemplo para incluir alunos que podem alugar livros da biblioteca:

    class Livro:
        def __init__(self, titulo):
            self.titulo = titulo

    class Bibliotecario:
        def __init__(self, nome):
            self.nome = nome

        def empresta_livro(self, livro):
            print(f"{self.nome} emprestou o livro {livro.titulo}")

    class Aluno:
        def __init__(self, nome):
            self.nome = nome
            self.livros_alugados = []

        def aluga_livro(self, livro):
            self.livros_alugados.append(livro)
            print(f"{self.nome} alugou o livro {livro.titulo}")

    # Instâncias
    livro1 = Livro("1984")
    bibliotecario = Bibliotecario("João")

    # Associação sendo utilizada
    bibliotecario.empresta_livro(livro1)

    # Instâncias
    aluno1 = Aluno("Maria")

    # Associação sendo utilizada
    aluno1.aluga_livro(livro1)

Aqui, a classe Aluno também está associada à classe Livro. A associação permite que o aluno alugue livros, adicionando-os à sua lista de livros alugados. Cada aluno mantém uma lista de livros que alugou, demonstrando uma associação onde o aluno "conhece" os livros.

### Exemplo de Associação Bidirecional
Em alguns casos, pode ser útil que ambos os objetos associados conheçam um ao outro. Por exemplo, um livro pode saber quem o alugou:

    class Livro:
        def __init__(self, titulo):
            self.titulo = titulo
            self.alugado_por = None

        def alugar(self, pessoa):
            self.alugado_por = pessoa
            pessoa.livros_alugados.append(self)
            print(f"{self.titulo} foi alugado por {pessoa.nome}")

    # Atualizando a classe Aluno para suportar a associação bidirecional
    class Aluno:
        def __init__(self, nome):
            self.nome = nome
            self.livros_alugados = []

        def aluga_livro(self, livro):
            livro.alugar(self)

    # Associação bidirecional sendo utilizada
    aluno1.aluga_livro(livro1)
    print(f"O livro {livro1.titulo} está alugado por {livro1.alugado_por.nome}")

## Conclusao
Essas relações ajudam a modelar a realidade no design de software, permitindo que os desenvolvedores criem sistemas mais organizados e compreensíveis, onde as dependências e interações entre objetos são claramente definidas.

Composicao $\subseteq$ Agregacao $\subseteq$ Associacao

Seguir link para leitura - Unified Modeling Language

    https://en.wikipedia.org/wiki/Unified_Modeling_Language
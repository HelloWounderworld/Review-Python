# Aula 21 - Composição - Python Orientado a Objetos:
Na programação orientada a objetos (POO), as relações entre classes descrevem como objetos de diferentes classes interagem e dependem uns dos outros. Existem três tipos principais de relações: associação, agregação e composição. Cada tipo define um nível diferente de dependência entre as classes.

Neste topico iremos abordar sobre a relacao de Composicao.

## Composição
A composição é uma forma forte de agregação que indica uma relação "parte-todo" onde as partes não podem existir sem o todo. Se o objeto "todo" for destruído, então os objetos "parte" também serão destruídos. Isso significa que a composição é uma relação de dependência onde a vida útil das partes está intrinsecamente ligada à vida útil do todo.

### Definição Matemática:
A composição é uma forma mais restritiva de agregação onde a existência das partes está condicionada à existência do todo. Isso pode ser representado por uma função total:

$f:\mathcal{B}\longrightarrow\mathcal{A}$

onde cada elemento em $\mathcal{B}$ está associado a exatamente um elemento em $\mathcal{A}$, e se um elemento de $\mathcal{A}$ é removido, todos os elementos de $\mathcal{B}$ associados a ele também são removidos.

### Exemplo:
Se $\mathcal{A}$ é um conjunto de carros e $\mathcal{B}$ é um conjunto de motores, $f(b)=a$ indica que o motor $b$ está no carro $a$. Se o carro $a$ é destruído, o motor $b$ também é.

### Exemplo de Composição
Considere um exemplo de um Carro e um Motor. Um motor é uma parte essencial de um carro e não existe sem o carro.

    class Motor:
        def __init__(self, potencia):
            self.potencia = potencia

    class Carro:
        def __init__(self, modelo):
            self.modelo = modelo
            self.motor = Motor(potencia=120)  # Motor é criado junto com o Carro

        def __del__(self):
            print("O carro e o motor foram destruídos.")

Neste exemplo, o Motor é criado e gerenciado pelo Carro. Se o objeto Carro for destruído, o Motor associado também será destruído, refletindo a natureza da composição.

### Diversos Usos da Composição
1. Sistemas de Gerenciamento de Software: Em um sistema de gerenciamento de software, você pode ter componentes como SistemaOperacional, Driver e Programa, onde cada Driver e Programa não pode existir sem um SistemaOperacional.

        class SistemaOperacional:
            def __init__(self, nome):
                self.nome = nome
                self.programas = []

            def instalar_programa(self, programa):
                self.programas.append(programa)

        class Programa:
            def __init__(self, nome):
                self.nome = nome

        windows = SistemaOperacional("Windows")
        word = Programa("Word")
        windows.instalar_programa(word)

2. Sistemas de Gerenciamento de Conteúdo: Em um CMS, uma Página pode conter Elementos como Texto, Imagem, e Vídeo. Se a página é deletada, todos os seus elementos também são.

        class Elemento:
            def __init__(self, tipo):
                self.tipo = tipo

        class Pagina:
            def __init__(self, titulo):
                self.titulo = titulo
                self.elementos = []

            def adicionar_elemento(self, elemento):
                self.elementos.append(elemento)

        pagina = Pagina("Página Inicial")
        texto = Elemento("Texto")
        imagem = Elemento("Imagem")
        pagina.adicionar_elemento(texto)
        pagina.adicionar_elemento(imagem)

3. Sistemas de Gerenciamento de Recursos Humanos: Em um sistema de RH, um Departamento pode ter Funcionários, onde os funcionários não existem sem um departamento.

        class Funcionario:
            def __init__(self, nome):
                self.nome = nome

        class Departamento:
            def __init__(self, nome):
                self.nome = nome
                self.funcionarios = []

            def adicionar_funcionario(self, funcionario):
                self.funcionarios.append(funcionario)

        desenvolvimento = Departamento("Desenvolvimento")
        empregado = Funcionario("João")
        desenvolvimento.adicionar_funcionario(empregado)

### Conclusão
A composição é uma ferramenta poderosa na programação orientada a objetos que ajuda a modelar relações fortes e dependentes entre objetos. Ela é crucial para garantir a integridade e o gerenciamento correto do ciclo de vida dos objetos em sistemas complexos, facilitando a manutenção e a escalabilidade do software.

### Representação Gráfica
Essas relações também podem ser visualizadas usando diagramas de Venn ou grafos:

- Associação: Linhas conectando elementos de dois conjuntos.

- Agregação: Linhas com uma ponta de seta indicando a direção da parte para o todo, mas com a possibilidade de elementos sem conexões.

- Composição: Linhas com uma ponta de seta sólida indicando uma conexão obrigatória entre a parte e o todo.

Essas representações ajudam a visualizar e entender as dependências e conexões entre diferentes objetos em sistemas de software, facilitando a modelagem e a análise de sistemas complexos.
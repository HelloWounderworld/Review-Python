# Aula 20 - Agregação - Python Orientado a Objetos:
A agregação é um tipo de associação que representa uma relação "tem-um" ou "parte-de" entre duas classes, onde as partes podem existir separadamente do todo. Isso significa que se o objeto contêiner (o todo) for destruído, os objetos contidos (as partes) podem continuar a existir.

Na programação orientada a objetos (POO), as relações entre classes descrevem como objetos de diferentes classes interagem e dependem uns dos outros. Existem três tipos principais de relações: associação, agregação e composição. Cada tipo define um nível diferente de dependência entre as classes.

Neste topico iremos abordar sobre a relacao de Agregacao.

## Definição Matemática:
A agregação é um tipo especial de associação que também pode ser representada como uma relação binária, mas com a característica adicional de que os elementos de um conjunto (partes) podem existir independentemente do conjunto agregador (todo). Isso pode ser representado por uma função parcial:

$f:\mathcal{B}\longrightarrow\mathcal{A}$

onde $\mathcal{B}$ é o conjunto de partes e $\mathcal{A}$ é o conjunto de todos. A função $f$ não é necessariamente total, significando que nem todos os elementos de $\mathcal{B}$ precisam estar mapeados para elementos em $\mathcal{A}$.

## Exemplo:
Se $\mathcal{A}$ é um conjunto de bibliotecas e $\mathcal{B}$ é um conjunto de livros, $f(b)=a$ indica que o livro $b$ esta na biblioteca $a$, mas livros podem existir fora de qualquer biblioteca.

## Caracteristicas da Agregacao
- Independência: As partes (objetos contidos) podem existir independentemente do todo (objeto contêiner).

- Relação não exclusiva: Uma parte pode pertencer a mais de um todo sem que isso implique exclusividade.

- Transitividade: Se um objeto contêiner contém outro objeto, e este por sua vez contém um terceiro objeto, a relação de agregação pode ser transitiva.

### Exemplo de Agregação
Consideremos um exemplo de uma biblioteca que contém livros. A biblioteca pode fechar, mas os livros ainda existirão.

    class Livro:
        def __init__(self, titulo):
            self.titulo = titulo

    class Biblioteca:
        def __init__(self, nome):
            self.nome = nome
            self.livros = []

        def adicionar_livro(self, livro):
            self.livros.append(livro)

    # Criando objetos
    biblioteca = Biblioteca("Biblioteca Central")
    livro1 = Livro("1984")
    livro2 = Livro("Brave New World")

    # Agregando livros à biblioteca
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    # Listando livros na biblioteca
    for livro in biblioteca.livros:
        print(f"{livro.titulo} está na {biblioteca.nome}")

### Diversos Usos da Agregação
1. Sistemas de Gerenciamento de Recursos: Em um sistema de gerenciamento de recursos humanos, uma empresa pode ter diversos departamentos. Cada departamento pode existir sem a empresa, e a empresa pode existir sem um departamento específico.

        class Departamento:
            def __init__(self, nome):
                self.nome = nome
                self.funcionarios = []

            def adicionar_funcionario(self, funcionario):
                self.funcionarios.append(funcionario)

        class Empresa:
            def __init__(self, nome):
                self.nome = nome
                self.departamentos = []

            def adicionar_departamento(self, departamento):
                self.departamentos.append(departamento)

        # Uso
        empresa = Empresa("TechCorp")
        departamento = Departamento("Desenvolvimento")
        empresa.adicionar_departamento(departamento)

2. Sistemas de Gerenciamento de Conteúdo: Em um sistema de gerenciamento de conteúdo, uma página pode conter vários elementos, como textos, imagens e vídeos. A página pode ser deletada, mas os elementos podem ser reutilizados em outras páginas.

        class Elemento:
            def __init__(self, tipo):
                self.tipo = tipo

        class Pagina:
            def __init__(self, titulo):
                self.titulo = titulo
                self.elementos = []

            def adicionar_elemento(self, elemento):
                self.elementos.append(elemento)

        # Uso
        pagina = Pagina("Página Inicial")
        texto = Elemento("Texto")
        imagem = Elemento("Imagem")
        pagina.adicionar_elemento(texto)
        pagina.adicionar_elemento(imagem)

## Conclusão
A agregação é uma forma de associação que permite uma flexibilidade maior na modelagem de sistemas, representando relações onde as partes podem existir sem o todo. Isso é útil em muitos contextos de desenvolvimento de software, especialmente em sistemas complexos onde a independência entre os componentes é crucial para a manutenção e escalabilidade do sistema.
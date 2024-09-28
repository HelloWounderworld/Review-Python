# Aula 76 - Funções recursivas, recursividade e Stack Overflow:
Função recursiva = É um conceito matemático que se estuda em teoria dos conjuntos.

No livro Set Theory, Thomas Jech, Springer Editor, procurar pelo Teorema da Recursão, apenas as suas aplicações, não precisa tentar entender a demonstração, se o aluno não entender o que é demonstração matemática e não tem o mínimo de background matemático. Assim, como outras sequências ou conjuntos que obedece um certo tipo de padrão. Lembrei dos meus estudos em Teoria dos Conjuntos que foi ministrado pelo professor Artur Hideyuki Tomita.

A função recursiva ela tem uma motivação matemática muito forte e o uso em programação é muito recorrente.

Basicamente, a ideia de recursividade em funções é uma função que chama ela mesma de volta de modo que isso acaba gerando um loop.

O bom é que as funções recursivas servem para partir os problemas grandes em menores, contanto que tenha uma uniformidade, esse detalhe é importante. A uniformidade aqui eu me refiro à padrões que se repetem da mesma forma independente da escala. Um exemplo de uma função recursiva que conseguimos criar aqui é o fatorial que temos em matemática

    n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1

Vamos criar uma função recursiva bem simples para entendermos a ideia

    def recursiva(inicio=0, fim=10):
        # Caso recursivo
        # contar até chegar ao final
        inicio += 1
        return recursiva(inicio, fim)

Claro, se rodarmos o código do jeito que está acima, dará um loop infinito, pois não colocamos uma condicional que simplesmente pare o loop. Isso implicará em um problema chamado "Stack Overflow". Claro, não é o site em que conseguimos encontrar vários problemas comentadas, resolvidas ou até mesmo problemas em abertos que estão sendo investigados. O erro, Stack Overflow, que me refiro aqui é o próprio problema que a frase fala "Muito cheio" ao ponto de transbordar. No caso, o Python está dizendo que tem um limite que podemos colocar na memória, visto que a cada loop o valor "+1" que é feito na função cima é mais um dado criado na memória.

Vamos colocar uma condicional que faz o loop parar

    def recursiva(inicio=0, fim=10):
        # Caso base
        if inicio >= fim:
            return fim
        # Caso recursivo
        # contar até chegar ao final
        inicio += 1
        return recursiva(inicio, fim)

    print(recursiva())

Estudei muito isso na faculdade. Qualquer coisa o leitor poderá visitar a outra pasta minha, O-que-Fiz-Na-Faculdade, que está nesse mesmo repositório.

Seguir link para leitura

    https://pt.wikipedia.org/wiki/Recursividade

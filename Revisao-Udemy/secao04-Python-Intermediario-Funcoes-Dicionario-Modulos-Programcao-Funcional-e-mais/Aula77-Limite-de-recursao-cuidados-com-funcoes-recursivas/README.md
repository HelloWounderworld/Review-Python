# Aula 77 - Limite de recursão e cuidados com funções recursivas:
Vimos na seção anterior que ao executarmos a função recursiva sem que coloquemos alguma condição que faça o loop infinito dela parar, iremos ter um erro chamado Stack Overflow, donde no erro o Python informa que só conseguimos suportar até 1000.

O tipo de erro acima podemos reproduzir até colocando valores tbm com condições que faria o Python parar

    def recursiva(inicio=0, fim=10):
        print(inicio, fim)
        # Caso base
        if inicio >= fim:
            return fim
        # Caso recursivo
        # contar até chegar ao final
        inicio += 1
        return recursiva(inicio, fim)

    print(recursiva(0, 1000))

Entretanto, temos uma forma de conseguirmos alterar o limite disso, algo que não recomendo, usando o módulo sys que tem o método "setrecursionlimit($`n`$)", com $`n\in\mathbbo{N}`$.

    import sys

    sys.setrecursionlimit(1004)

    def recursiva(inicio=0, fim=10):
        print(inicio, fim)
        # Caso base
        if inicio >= fim:
            return fim
        # Caso recursivo
        # contar até chegar ao final
        inicio += 1
        return recursiva(inicio, fim)

    print(recursiva(0, 1000))

Não recomendo usar acima e procurar mais em respeitar o limite que o python estabelece.

Agora, vamos, finalmente, partir para definir recursivamente o fatorial e vamos tentar entender a lógica disso

    def fatorial(n):
        if n <= 1:
            return 1
        return n * fatorial(n-1)

    print(fatorial(5))

Foi intuitivo a recursão acima para ti?

Bom, o momento em que definimos o fatorial recursivamente, de início, pode confundir bastante pessoas, pois tirando o caso base que é compreensível, estamos retornando "n * fatorial(n-1)". Faz sentido isso?

Resposta, sim, faz, pois o que está ocorrendo no retorno é exatamente a seguinte condição. Dado $`n\in\mathbb{N}`$ estritamente maior do que 1, temos que o fatorial de $`n`$ pode ser expressa da forma

    n! = n * (n-1)! = n * (n-1) * (n-2)! = ... = n * (n-1) * (n-2) * ... * 3 * 2 * 1

No caso, ao retornarmos o "n * fatorial(n-1)" estamos, indutivamente, realizando a relação de igualdade acima passo a passo, pois se destrincharmos com a função que definimos da mesma forma acima ficaria

    fatorial(n) = n * fatorial(n-1) = n * (n-1) * fatorial(n-2) = ... = n * (n-1) * (n-2) * ... * 3 * 2 * fatorial(1)

onde o caso fatorial(1) cai no caso base do valor 1.

Bom, entendido como se aplica a recursividade nos fatoriais acima, quero dar a seguinte observação. A forma como foi codado acima ela é didática para entender como funciona o fatorial, porém não serve para conseguirmos realizar contas gigantescas. Já me ferrei num exercício de programa onde tive que computar a série de Taylor trigonométrica para conseguir obter resultados precisos esquecendo desse fator e, consequentemente, otimizar o código...

No caso, se vc quiser utilizar fatorial em escalas de contas enormes, será necessário melhorar a qualidade do código no sentido de antes mesmo de atingir o valor limite, sempre parar a contagem para guardar o valor de múltiplicação feita até então em um dado imutável e conseguir esvaziar a memória deixando apenas a memória do valor que foi feito a multiplicação e conseguir processeguir a partir do ponto que parou adiante. Isso precisa de um pouco mais de esforço para otimizar e realizar isso.

A não ser que vc se ateie à uma prática que considero duvidosa que é usando o setrecursionlimit do módulo sys.

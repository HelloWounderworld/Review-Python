# Aula 06 - (Parte 2) Escopo de funções e módulos em Python + global:
Vamos abordar mais sobre escopo.

Bom, existem dois tipos de escopo, global e local:

- Escopo global: É o escopo onde todo o código é alcançavel.

- Escopo local: É o escopo onde apenas nomes do mesmo local podem ser alcançados.

Bom, um exemplo legal, que mostra a ideia de que as ordem de priorização vai de escopo local em direção ao escopo externo está na seguinte função

    x = 1

    def escopo():
        x = 10
        def outra_funcao():
            x = 11
            y = 2
            print(x,y)
        outra_funcao()
    
    escopo()

Ao executarmos a função acima, será printado, pelo print(x,y), o valor "11 2". Mas, agora, se comentarmos o "x = 11", qual valor de "x" será considerado?

    x = 1

    def escopo():
        x = 10
        def outra_funcao():
            #x = 11
            y = 2
            print(x,y)
        outra_funcao()
    
    escopo()

Será considerado o valor do "x" mais próximo que temos, que é o "x = 10", então será printado "10 2". O mesmo, vale se comentarmos "x = 10" com "x = 11" comentado, será considerado "x" mais próximo que temos que é o "x = 1". Esse comportamento se parece muito com a teoria de categoria quando vc consegue concluir as propriedades de uma categoria considerando apenas a sua sub-categoria. No caso, visto essa ideia em questão, se fizermos um experimento análogo com "y", no sentido de em vez de definirmos os "y"'s externamento, executamos print(y) fora do escopo onde o "y" está definido?

    x = 1

    def escopo():
        x = 10
        def outra_funcao():
            #x = 11
            y = 2
            print(x,y)
        outra_funcao()
        print(y)
    
    print(y)
    escopo()

No caso, como a prioridade da ordem é de dentro para fora, então o print(y) executado fora do escopo de onde o "y" está definido nos retornará um erro dizendo que não temos a variável "y" definido.

Leitura:

    https://phylos.net/2021-06-01/python-escopos-e-namespaces
    https://www.interviewcake.com/concept/java/call-stack#:~:text=The%20call%20stack%20is%20what,dice%20and%20printed%20the%20sum.
# Aula 13 - Closure e funções que retornam outras funções:
O Closure, no caso, ela é a definição do que vimos de funções de primeira classe nas aulas anteriores, quando definimos a função "executa". Ou seja, é uma função que retorna outras funcções.

Vamos abordar o assunto com mais profundidade explorando o que mais de interessante podemos conseguir obter desse conceito

    def criar_saudacao(saudacao, nome):
        return f'{saudacao}, {nome}!'

    s1 = cria_saudacao('Bom dia', 'Leonardo')
    s2 = cria_saudacao('Boa noite', 'Leonardo')
    print(s1)
    print(s2)

Bom, o formato da função acima, ainda não é uma clousure. Mas, basicamente, já podemos ver que ela retorna a saudação que queremos fazer de forma correta. Agora, começando a implementar o clousure, que é criar uma funçõa que executa outra função, podemos realizar a seguinte modificação da função acima

    def criar_saudacao(saudacao, nome):
        def saudar():
            return f'{saudacao}, {nome}!'
        return saudar()

    s1 = cria_saudacao('Bom dia', 'Leonardo')
    s2 = cria_saudacao('Boa noite', 'Leonardo')
    print(s1)
    print(s2)

No caso, se executarmos o script acima, vamos ver que tudo continua ocorrendo de forma correta. Porém, mesmo assim, ainda não é definitivamente uma clousure, pois, lembrando novamente, clousure ela nos dá mais flexibilidade de executar as funções nos momentos que queremos que ela seja executada ou não. A função acima, uma vez acionada, ela será executada e feito o devido retorno, f'{saudacao}, {nome}!'. Porém, temos uma forma de conseguirmos evitar que isso ocorra e de conseguirmos atribuir às variáveis "s1" e "s2" somente as funções saudar() prontas para serem executadas, mas não executando-as

    def criar_saudacao(saudacao, nome):
        def saudar():
            return f'{saudacao}, {nome}!'
        return saudar

    s1 = cria_saudacao('Bom dia', 'Leonardo')
    s2 = cria_saudacao('Boa noite', 'Leonardo')
    print(s1)
    print(s2)

Ao rodarmos o script acima, vamos ver que os dois prints retornam a memória da função saudar (o que indica que as informações estão guardadas na memória), que são diferentes entre "s1" e "s2", mas não o que de fato essa função, saudar(), retorna que é a saudação. Ou seja, isso significa que as duas variáveis "s1" e "s2" passam a serem funções que vc tem a liberdade de definir o momento em que ela será executada

    def criar_saudacao(saudacao, nome):
        def saudar():
            return f'{saudacao}, {nome}!'
        return saudar

    s1 = cria_saudacao('Bom dia', 'Leonardo')
    s2 = cria_saudacao('Boa noite', 'Leonardo')
    print(s1)
    print(s1())

    print(s2)
    print(s2())

Basicamente, isso é o clousure. Ou seja, vc não executa a função, mas as informações dos argumentos que vc passou estão guardadas na memória, e vc terá acessao só no momento em que vc executa, fechando os parênteses (close, por issoclosure) para, aí sim, acessar as informações que ficam guaradadas na memória do computador.

Aciona o Breakpoint para verificar isso passo a passo e ver como funciona e ver se está de acordo com o que foi abordado acima!

Bom, a clousure, praticamente, é o que define o paradigma de uma programação funcional.

    https://www.programiz.com/python-programming/closure
    https://www.learnpython.org/en/Closures
# Aula 61 - Variáveis livres + nonlocal (locals, globals):
Vamos falar de variáveis livres e nonlocal.

- Variável livre:

    Vamos começar pela definição do que seria uma variável livre:

        Uma variável livre é uma variável referenciada em uma função, que não é nem uma variável local nem um argumento daquela função.

    Vamos pegar um exemplo padrão disso

        def fora():
            a = 1

            def dentro():
                return a
            return dentro
        
        print(fora())
        print(fora()())

    No caso, nma função "fora()" definido acima a variável livre é o "a" que está sendo definido dentro dessa função, pois ela não está sendo definido dentro do escopo da função "dentro()".

    Claro, podemos dinamizar essa variável livre

        def fora(x):
            a = x

            def dentro():
                return a
            return dentro
        
        dentro1 = fora(10)
        dentro2 = fora(20)

        print(dentro1())
        print(dentro2())

    No caso, agora, a variável livre "a" está dinamizada, pois podemos colocar o valor que quisermos.

    Para conferirmos isso, podemos usar as funções nativas do python o "locals" e "globals"

        def fora(x):
            a = x

            def dentro():
                print(locals())
                return a
            return dentro
        
        dentro1 = fora(10)
        dentro2 = fora(20)

        print(dentro1())
        print(dentro2())

    Donde, o "locals()" ela confere, quais variáveis são locais.

    Além disso, para definitivamente, sabermos se, de fato, "a" é ou não uma variável livre, podemos usar o "__code__.co_freevars"

        def fora(x):
            a = x

            def dentro():
                print(locals())
                print(dentro.__code__.co_freevars)
                return a
            return dentro
        
        dentro1 = fora(10)
        dentro2 = fora(20)

        print(dentro1())
        print(dentro2())

    Podemos usar o "globals" para verificarmos quais são as variáveis globais

        print(globals())

        def fora(x):
            a = x

            def dentro():
                print(locals())
                print(dentro.__code__.co_freevars)
                return a
            return dentro
        
        dentro1 = fora(10)
        dentro2 = fora(20)

        print(dentro1())
        print(dentro2())

    Seguir link de leitura:

        https://www.codesansar.com/python-programming/local-global-free-variables-example.htm#:~:text=In%20Python%2C%20there%20exist%20another,is%20known%20as%20free%20variable.

        https://dunossauro.github.io/python-funcional/roteiros/08_closures_1_escopo.html

- nonlocal:

    Agora, visto que aprendemos o conceito de variável livre acima, suponhamos que queiramos realizar um processo iterativo usando a variável livre como seguinte

        def concatenar(string_inicial):
            valor_final = string_inicial

            def interna(valor_a_concatenar):
                return valor_final
            return interna

        c = concatenar('a')
        print(c('b'))
        print(c('c'))
        print(c('d'))
    
    Bom, inicialmente, a função acima não tem nada de novidade, pois seja qual for o "valor_a_concatenar" que iremos colocar, vamos sempre retonar o valor final.

    Mas, agora, suponhamos que queremos realizar o seguinte

        def concatenar(string_inicial):
            valor_final = string_inicial

            def interna(valor_a_concatenar):
                valor_final += valor_a_concatenar
                return valor_final
            return interna

        c = concatenar('a')
        print(c('b'))
        print(c('c'))
        print(c('d'))

    No caso, a ideia é que ela irá retonar para cada print os respectivos strings concatenados. Porém, no formato como está acima, isso irá retornar um erro.

    O motivo disso, estaria por conta do escopo. Ou seja, a variável livre "valor_final" não é do escopo da função "interna". Podemos apenas ler o valor dessa variável livre, mas não podemos alterar ela. Por isso, para corrigirmos esse problema, precisamos falar para o Python de que essa variável livre, valor_final, não é do escopo da função "interna" e é aí que entra o uso da sintaxe "nonlocal"

        def concatenar(string_inicial):
            valor_final = string_inicial

            def interna(valor_a_concatenar):
                nonlocal valor_final
                valor_final += valor_a_concatenar
                return valor_final
            return interna

        c = concatenar('a')
        print(c('b'))
        print(c('c'))
        print(c('d'))

    O uso é muito parecido com a sintaxe "global" para dizer que uma variável é global.

    Link para leitura

        https://www.toppr.com/guides/python-guide/references/methods-and-functions/global-local-nonlocal-variables/python-global-local-and-nonlocal-variables-with-examples/#:~:text=In%20python%2C%20nonlocal%20variables%20refer,nor%20in%20the%20global%20scope.&text=Here%2C%20the%20inner()%20function%20is%20nested%20in%20nature.

        https://pt.stackoverflow.com/questions/250362/qual-a-diferen%C3%A7a-de-global-e-nonlocal-no-python

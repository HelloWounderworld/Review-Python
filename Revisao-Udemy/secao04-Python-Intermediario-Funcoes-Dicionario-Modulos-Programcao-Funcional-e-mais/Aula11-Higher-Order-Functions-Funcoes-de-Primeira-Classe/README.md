# Aula 11 - Higher Order Functions - Funções de primeira classe:
Vamos entender sobre funções de primeira classe. Basicamente, a definição de funções de primeira classe significa que, assim como outros dados em Python, as funções em Python, também, podem ser tratadas como um dado.

    def saudacao(msg):
        return msg

    print(saudacao('Bom dia!'))

No caso, como a definição acima se aplica, pegando a função, saudacao, como exemplo, podemos realizar a seguinte tratativa nela como se fosse um dado mesmo

    def saudacao(msg):
        return msg

    saudacao_2 = saudacao
    random = saudacao_2('Boa noite!!!')
    print(random)
    print(saudacao('Bom dia!'))

Ou seja, note que, na variável "saudacao_2" estou atribuindo à ela "saudacao" que é o nome da função e, em seguida, usando a variável "saudacao_2" como se fosse uma função colocando um argumento 'Boa notie!!!'.

Nessa brincadeira, podemos definir uma função que decide ou não executar alguma outra função, como segue

    def saudacao(msg):
        return msg

    def executa(funcao):
        return funcao()

    saudacao_2 = saudacao
    random = executa(saudacao_2)
    print(random)

Entretanto, do jeito como está acima dará erro, pois na função "saudacao" ela exige que tenha algum argumento e na chamada acima não considera nenhum tipo de argumento. Para resolvermos isso, seria necessário colocar "*arg" como mais um argumento da função "executa"

    def saudacao(msg):
        return msg

    def executa(funcao, *arg):
        return funcao(*arg)

    saudacao_2 = saudacao
    random = executa(saudacao_2, 'Boa tarde!')
    print(random)

Claro, no lugar de "*arg" poderia ser um parâmetro simples, mas o *arg ela serve mais para podemos conseguir flexibilizar mais a quantidade de argumentos, caso, por ventura, eu acabe colocando mais parâmetros dentro da função saudacao

    def saudacao(msg, nome):
        return f'{msg}, {nome}'

    def executa(funcao, *arg):
        return funcao(*arg)

    saudacao_3 = saudacao
    random = executa(saudacao_3, 'Boa tarde', 'Leonardo')
    print(random)

# Aula 12 - Termos técnicos: Higher Order Functions e First-Class Functions:
Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

- Higher Order Functions - Funções que podem receber e/ou retornar outras funções

- First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.
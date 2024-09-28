# Aula 41 - dir, hasattr e getattr em Python:
Uma das coisas mais corriqueiras que temos na programação tbm, seria em checar se existe algum determinado tipo de valor dentro de um objeto.

Bom, isso, muitas vezes, acaba sendo útil para conseguirmos debugar algum código. O que é frenquete de ser usado tbm, é o breakpoint onde a pessoa para o código bem no momento em que ela precisa e em seguida escolha a opção debbuger console e nela digitamos o nome da variável para mostrar o que seria exibido nela e tbm usar o dir(nome da variável) para mostrar que tipo de atributos existem para esse objeto. Ou seja, uma das formas de conseguirmos debugar o código é usando o "dir" e verificar se existe o método dentro dela tbm

    string = 'Leonardo'
    print(string)

Aciona o breakpoint e vai no consule debbuger e nela digita "dir(string)" para verificar se existe o método que vc quer dentro dela.

Ou podemos, também, usar o "hasattr" para verificar se um determinado tipo de atributo existe dentro de um objeto que estamos analisando

    string = 'Leonardo'

    if hasattr(string, 'upper'):
        print('Existe upper aqui')
        print(string.upper())

No caso, acima, estamos checando se o objeto "string" que está com o valor "Leonardo", nela tem um método chamado "upper" ou não.

Podemos, também, dinamizar isso. Ou seja, o nome do método poderia estar numa variável

    string = 'Leonardo'
    metodo = 'upper'

    if hasattr(string, metodo):
        print('Existe upper')
        print(string.upper())

Além disso, caso o nome do método esteja em forma de string numa variável e feito a checagem pelo hasattr, vc queira usar ela, aí temos o getattr para isso. Ou seja, vc poderá usar o método que está dinamizado sem precisar chamar ela via o próprio objeto

    tring = 'Leonardo'
    metodo = 'upper'

    if hasattr(string, metodo):
        print('Existe upper')
        print(getattr(string, metodo)())

    else:
        print('O método não existe', metodo)
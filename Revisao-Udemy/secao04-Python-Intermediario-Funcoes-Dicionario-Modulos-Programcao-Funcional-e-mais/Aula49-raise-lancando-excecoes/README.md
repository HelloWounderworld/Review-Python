# Aula 49 - raise - lançando exceções (erros):
Bom, agora que estamos em um nível intermediário para avançado, vamos verificar os tratamentos de erros.

Uma das características que compõe um bom programador é que eles gostam de erros, no ramo tecnológico, quanto mais erros vc sabe tratar melhor seria a qualidade de funcionamento do teu programa, donde essa qualidade é um grande diferencial no ramo da tecnologia.

Vamos, agora, simular um tipo de erro para melhorar. Muitas vezes, precisamos que um determinado erro seja lançado para melhorar e, por fim, encontrar algum meio de tratamento. Para isso, vamos aprender a usar a funcionalidade "raise" que serve, exatamente, para lançar algum erro. No caso, vamos verificar o seguinte

    def divide(x, y):
        return x / y

    print(divide(8, 0))

Claro que sabemos a divisão acima dará um erro. Mas a finalidade que queremos é que esse erro seja lançado.

Bom, para isso vamos realizar o uso do try/except dentro da função divide

    def divide(x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return x

    print(divide(8, 0))

Bom, no caso, o exemplo acima, ela serve para realizar alguma tratativa da divisão pelo zero, que foi retornar o número do numerador da divisão. Só que, queremos que tal erro seja lançado. Para isso que usamos o raise

    def divide(x, y):
        try:
            return x / y
        except ZeroDivisionError:
            raise

    print(divide(8, 0))

No caso, o raise ela relança o erro que ocorreu. Entretanto, a condição acima é redundante com o caso de simplesmente retornar na função "divisao" o valor "x / y" feito a tal divisão errônea. A nossa finalidade é que usemos o raise para realizar alguma tratativa util, como no caso seguinte

    def divide(x, y):
        if y == 0:
            raise ZeroDivisionError('Você está tentando dividir por zero!')

        return x / y

    print(divide(8, 0))

Note que, ao executarmos o código acima, agora, a msg de erro clássico "division by zero" mudou para pela msg que escrevi dentro da classe ZeroDivisionError. Basicamente, o que eu fiz acima é criar o meu próprio erro.

Agora, como uma via de uma boa prática, vamos precisar realizar o seguinte. Em uma função, sempre seria uma boa colocar de funcionalidade somente o que queremos que aquela função realize. Por exemplo, a função que criamos "divide" seria de boa prática colocar dentro dessa função a funcionalidade de divisão, somente. Entretanto, na forma como está a função "divide" no último exemplo, ela está sendo colocado a funcionalidade de tratativa do erro. O ideal é que essa tratativa esteja separado e que ela seja chamado dentro dessa função. No caso, algo do seguinte tipo

    def divisao_por_zero_indefinido(denominador):
        if denominador == 0:
            raise ZeroDivisionError('Não pode dividir pelo zero!')

    def divide(x, y):
        divisao_por_zero_indefinido(y)
        return x / y

    print(divide(8, 0))

Isso nos permite melhorar a qualidade da leitura do código, de forma que ela fica mais didática, e tbm na sua organização. De forma que cada função fique mais independente da outra, pois a forma acima facilita em considerar e desconsiderar algumas funcionalidades sem a necessidade de refatorar grandes quantidades de linha.

Da mesma forma serve para conseguirmos criar a tratativa para outros tipos de erros, pois imagina a pessoa passa, dentro do argumento da função, alguma String? No caso, para esse cenário segue o seguinte

    def divisao_por_zero_indefinido(denominador):
        if denominador == 0:
            raise ZeroDivisionError('Não pode dividir pelo zero!')

    def divide(x, y):
        if not isinstance(x, (float, int)):
            raise TypeError(
                f'{x} deve ser int ou float.'
            )

        if not isinstance(y, (float, int)):
            raise TypeError(
                f'{y} deve ser int ou float.'
            )
        
        divisao_por_zero_indefinido(y)
        return x / y

    print(divide(8, '0'))

Assim, passando o zero como uma string, na função "divide" acima ela irá retornar uma mensagem de erro dizendo que o "'0'" deveria ser um int ou float.

Claro, como uma boa prática do clean code, vamos colocar essa condicional que colocamos dentro da função divide para uma função fora

    def divisao_por_zero_indefinido(denominador):
        if denominador == 0:
            raise ZeroDivisionError('Não pode dividir pelo zero!')

    def deve_ser_int_ou_float(n):
        tipo_n = type(n)
        if not isinstance(n, (float, int)):
            raise TypeError(
                f'"{n}" deve ser int ou float. '
                f'"{tipo_n.__name__}" enviado.'
            )
        return True

    def divide(x, y):
        deve_ser_int_ou_float(x)
        deve_ser_int_ou_float(y)
        
        divisao_por_zero_indefinido(y)
        return x / y

    print(divide(8, '0'))

Bom, o legal do raise é que vc consegue criar as suas próprias excessões de erros para ter mais flexibilidade de tratamento. Isso computaria mais e mais possibilidades de erros para informar de forma didática ao usuário.

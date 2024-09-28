# Aula 48 - try, except, else e finally + Built-in Exceptions:
O que vc pode querer fazer com o try/except e que mesmo que tenha passado no try e expcet, que a aplicação ela não pare. No caso, que de alguma forma o sistema continue em funcionamento sem que ela pare. Para isso, seria necessário colocar uma outra funcionalidade junto com o try/except, que é o finally

    try:
        ...
    except:
        ...
    finally:
        ...

Acima, basicamente, está a estrutura padrão de uso. No caso, finally ela sempre será executado mesmo que tenha ocorrido algum erro ou que a aplicação tenha dado certo. No caso, o uso eficaz desse método é sempre colocar alguma conclusão do processo que, independente do que resultar, que tal processo ocorra no final.

    try:
        print('ABRIR ARQUIVO')
        8/0
    except ZeroDivisionError:
        print('DIVIDIU ZERO')
    finally:
        print('FECHAR ARQUIVO')

Uma outra alternativa de um uso conjunto com o finally, seria usando o else. Nesse caso, vc não irá precisar colocar alguma condicional dentro do finally de caso o processo tenha dado certo. No lugar disso, podemos usar o else

    try:
        print('ABRIR ARQUIVO')
        # 8/0 # Comenta e descomenta para verificar que quando dá certo ela entra no else e quando não dá, ela não entra no else.
    except ZeroDivisionError:
        print('DIVIDIU ZERO')
    else:
        print('NÃO DEU ERRO')
    finally:
        print('FECHAR ARQUIVO')

Claro, mesmo assim o finally ela é um passo que irá com toda certeza ser passado nela. Bom, nesse caso fica a dúvido do que o else ela tem de utilidade. No caso, o else ela serve mais para conseguir colocar algum processo posterior ao processo que deu certo, pois antes de o processo ser finalizado, vc queira colocar algum tipo de condição ou efetuar algo.

Seguir o link para leitura:

    https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

# Aula 28 - Operador Lógico "and":
Bom, vamos ver sobre uma das lógicas proposicional, o 'e/and'.

Quem conhece muito bem sobre teoria dos conjuntos a lógia aplicada nela é a mesma. Como é o meu caso irei usar essa aula só para ver quais são as sintaxes para eu poder aplicar a teoria

    # Operadores lógicos
    # and (e), or (ou) e not (não)
    # and - Todas as condições precisam ser verdadeiras.
    # Se qualquer valor for considerado falso, a expressão inteira avaliada naquele valor será considerada falso
    # São considerado falso:
    # 0 0.0 '' False
    # Também existe o tipo None que é usado para representar um não valor.
    entrada = input('[E]ntrar [S]air: ')
    senha_digitada = input('Senha: ')

    senha_permitida = '123456'

    if entrada == 'E' and senha_digitada == senha_permitida:
        print('Entrar')
    else:
        print('Sair')

No caso, a sintaxe usada para representarmos o operador and é o próprio nome "and".

No caso, assim como em JavaScript, em Python, também, temos a avaliação de curto circuito

    # Avaliação de curto circuito
    print(bool(0))
    print(bool(0.0))
    print(bool(''))
    print(True and False and True)
    print(True and 0 and True)
    print('' and True and True)
    print(True and True and 0.0)

No caso, a ideia do curto circuito em python é a mesma que no JavaScript.

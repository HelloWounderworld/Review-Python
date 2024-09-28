# Aula 27 - Exemplo de uso do tipo set:
Irei te mostrar um exemplo de uso de set que é uma forma de uso corriqueiro.

Quando você quer verificar a existência de algum elemento se ele já existiu ou não. No caso, verificamos a existência de uma pertinência como segue

    letras = set()
    while True:
        letra = input('Digite: ')
        letras.add(letra.lower())

        if 'l' in letras:
            print('Tu encontrou a letra')
            break

        print(letras)

Ou seja, o set em si ele costuma ser mais eficiente do que outros tipos de objetos por não ter algum índice nela fincado. No caso, ela acaba sendo mais rápido para procurar algo.
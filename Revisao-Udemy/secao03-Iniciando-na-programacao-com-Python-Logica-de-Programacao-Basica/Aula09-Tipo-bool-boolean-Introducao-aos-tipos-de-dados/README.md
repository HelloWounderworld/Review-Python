# Aula 09 - Tipo bool (boolean) - Introdução aos tipos de dados:
Vamos conhecer os booleanos.

Como foi visto na revisão do JavaScript, aqui não muda muita coisa tbm.

Os booleanos são tipos de dados que são usados para declarar alguma validade de uma sentença ou não se dividindo em True e False. Geralmente, usamos muito em operações condicionais, if, donde dentro do operador avaliamos alguma sentença ou em outros casos somente validamos alguma execução ou não. Ou seja, assim como em JavaScript, aqui em python, não precisamos muitas vezes usar diretamente true ou false, mas, de forma implícita, tais dados booleanos estarão trabalhando por baixo dos panos quando usamos os operadores lógicos tbm.

    # Tipo de dado bool (boolean)
    # Ao questionar algo em um programa,
    # só existem duas respostas possíveis:
    # sim (True) ou não (False).
    # Existem vários operadores para "questionar".
    # Dentre eles o ==, que é um operador lógico que
    # questiona se um valor é igual a outro
    print(10 == 10)  # Sim => True (Verdadeiro)
    print(10 == 11)  # Não => False (Falso)
    print(type(True))
    print(type(False))
    print(type(10 == 10))
    print(type(10 == 11))

Ficaria mais fácil para mim entender que o booleano é uma espécie que atua como álgebra. Ou seja, não existe mais ou menos ou aproximado, mas ou é sim ou é não. Daria para axiomatizar toda a álgebra de grupos, aneis e corpos e teoria de Galois dentro disso. Um dos projetos meus é criar esse axioma em forma de classe para depois verificar em que área no mundo teria a aplicabilidade. O mesmo vale para a álgebra linear!

# Aula 08 - Tipo int e float (números) - Introdução aos tipos de dados:
Vamos entender melhor sobre o dado number, em python.

No caso, temos dois tipos, int e float.

- int - Número inteiro: O tipo int representa qualquer número positivo ou negativo. int sem sinal é considerado positivo.

- float - Número com ponto flutuante: O tipo float representa qualquer número positivo ou negativo com ponto flutuante. O float sem sinal é considerado positivo.

Para conferirmos se um dado número é um tipo int ou float, usamos o type

- type - A classe type mostra o tipo que o Python inferiou ao valor.

Como prova disso, no arquivo aula08.py temos o seguinte

    # Tipo int
    print(11)
    print(-11)
    print(0)

    # Tipo float
    print(1.1)
    print(10.11)
    print(0.0)
    print(-1.5)

    # Função type
    print(type(1))
    print(type(1.0))
    print(type(0))
    print(type(0.0))

Obs: Tudo em python é um objeto, então quando rodamos a classe type, não é estranho, no terminal, ter retornado o valor <class bla bla>, pois as classes são os que manipulam os objetos.

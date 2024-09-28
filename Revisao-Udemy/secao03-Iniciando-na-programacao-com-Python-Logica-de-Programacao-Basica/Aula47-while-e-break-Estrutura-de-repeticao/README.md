# Aula 47 - while e break - Estrutura de repetição (Parte 1):
Vamos começar a ver sobre repetições que temos em python.

No caso, vamos começar a ver a repetição pelo while.

Bom, a estrutura de repetição, while, aqui ela tem a mesma funcionalidade que foi vista em JavaScript. A única diferença é que aqui em Python o while tem somente uma, visto que em JavaScript temos dois tipos o while e do while. Então, como foi avisado, devemos tomar cuidado com condições que colocamos no while que pode gerar um looping infinito

    """
    Repetições
    while (enquanto)
    Executa uma ação enquanto uma condição for verdadeira
    Loop infinito -> Quando um código não tem fim
    """
    condicao = True

    while condicao:
        nome = input('Qual o seu nome: ')
        print(f'Seu nome é {nome}')

        if nome == 'sair':
            break

    print('Acabou')

Importante lembrar que o break que estamos usando aqui, ela considera o laço mais próximo, nesse caso o único while que estamos usando. Assim, se tivermos um loop dentro de um outro loop, e usarmos o break para o loop dentro, ele irá sair apenas do loop dentro e o loop fora irá continuar ainda.

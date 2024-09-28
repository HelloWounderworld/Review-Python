# Aula 60 - Introdução ao for / in - estrutura de repetição para coisas finitas:
Vamos ver sobre for, que é uma das formas de iterações mais importantes que temos em Python.

O for ele é uma estrutura de repetição, assim como vimos em while. Entretanto, o que difere com o while é que, enquanto que no while vc tem mais controle sobre a forma como a estrutura de repete, em for vc não tem esse controle condicional. No caso, ele itera de forma finita o conteúdo na qual vc pediu para ele iterar

    senha_salva = '123456'
    senha_digitada = ''
    repeticoes = 0

    while senha_salva != senha_digitada:
        senha_digitada = input(f'Sua senha ({repeticoes}x): ')

        repeticoes += 1

    print(repeticoes)
    print('Aquele laço acima pode ter repetições infinitas')

Um exemplo de repetição pelo while acima

    texto = 'Python'

    novo_texto = ''
    for letra in texto:
        novo_texto += f'*{letra}'
        print(letra)
    print(novo_texto + '*')

Exemplo de repetição do for.

Bom, aí entra a pergunta. Qual das duas formas de iterações é boa?

A resposta, obviamente, é depende. Pois, por exemplo, existem situações em que o for ele acaba sendo incompatível para certas finalidades exigidas.

Um exemplo disso, seria para caso vc exigir uma repetição indeterminada, como no exemplo acima em que colocamos a senha e enquanto a senha não estiver certa o programa ela irá continuar a perguntar várias vezes até que vc forneça a senha correta. Percebe-se que nesse tipo de cenário, não há uma quantidade de repetições determinadas as serem realizadas. Assim como vimos outros tipo de exercícios que tivemos com o uso do while, onde vc coloca a condicional, literalmente, "True" e definimos uma função dentro de while que ela repita enquanto o programa não receber alguma resposta que indica em sair do laço pelo break, como no programa que te perguntava se deseja sair ou não do laço. Nessas situações, claramente, o laço for não é eficiente, pois o laço for ela é eficiente no uso de repetições com quantidade determinada e de forma bem direta sem muito trabalho que tínhamos para o while.

# Aula 50 - while + continue - pulando alguma repetição:
Bom, aqui o continue funciona da mesma forma como foi estudado em JavaScript, então não irei me aprofundar tanto.

No caso, o continue, em repetição, ela serve para vc pular alguns dados

    """
    Repetições
    while (enquanto)
    Executa uma ação enquanto uma condição for verdadeira
    Loop infinito -> Quando um código não tem fim
    """
    contador = 0

    while contador <= 100:
        contador += 1

        if contador == 6:
            print('Não vou mostrar o 6.')
            continue

        if contador >= 10 and contador <= 27:
            print('Não vou mostrar o', contador)
            continue

        print(contador)

        if contador == 40:
            break


    print('Acabou')

Além disso, da mesma forma para break, o continue, quando ele é ativado, os códigos de linhas posteriores não serão rodados. O que significa que em um loop, ela irá simplesmente, continuar a iterar adiante. Por isso, teria que tomar muito cuidado onde colocar o continue e o break, para que vc não crie algum laço infinito ou que vc acabe deixando de rodar alguns códigos que são sempre necessários rodar.

Mas a vantagem de usar break e o continue, está no fato de que eles te dão condições para tornar a sua compilação muito mais performáticos.

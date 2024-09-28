# Aula 81 - split, join e strip são métodos muito úteis da str:
Vamos aprender a usar o split e join para lidar com lista e string.

Seguir os links de leitura abaixo sobre tais métodos

    https://www.geeksforgeeks.org/python-program-split-join-string/
    https://www.freecodecamp.org/news/python-string-split-and-join-methods-explained-with-examples/

Bom, por começo, vamos tentar manipular o seguinte string

    frase = 'Olha só que, coisa interessante'

No caso, o split, ele é um método que ajuda a dividir uma string de acordo com um tipo de caractere que vc pede para ele separar

    frase = 'Olha só que, coisa interessante'
    # lista_palavras = frase.split()
    lista_palavras = frase.split(',')
    print(frase)
    print(lista_palavras)

Além disso, podemos usar o método strip, donde ela é o método que tira os espaços do início e o fim de uma frase

    frase = 'Olha só que, coisa interessante'
    # lista_palavras = frase.split()
    lista_palavras = frase.split(',')
    print(frase)

    for i, frase in enumerate(lista_palavras):
        print(lista_palavras[i].strip())
        
    print(lista_palavras)

O strip, podemos optar por qual lado do espaço das frases que queremos eliminar, usand "r", de right, ou "l", de left

    frase = 'Olha só que, coisa interessante'
    # lista_palavras = frase.split()
    lista_palavras = frase.split(',')
    print(frase)

    for i, frase in enumerate(lista_palavras):
        print(lista_palavras[i].strip())
        print(lista_palavras[i].rstrip())
        print(lista_palavras[i].lstrip())
        
    print(lista_palavras)

Podemos, nessa iteração, corrigir os elementos dentro da lista, tirado os espaços usando o strip

    frase = 'Olha só que, coisa interessante'
    # lista_palavras = frase.split()
    lista_palavras = frase.split(',')
    print(frase)

    for i, frase in enumerate(lista_palavras):
        # print(lista_palavras[i].strip())
        # print(lista_palavras[i].rstrip())
        # print(lista_palavras[i].lstrip())
        lista_palavras[i] = lista_palavras[i].strip()
        
    print(lista_palavras)

Claro, o formato acima é de forma enxuta, mas dificulta a leitura do código. Em seu formato de boa prática ficaria o seguinte

    frase = '     Olha só que    , coisa interessante    '
    # lista_palavras = frase.split()
    lista_palavras_cruas = frase.split(',')
    print(frase)
    lista_palavras = []

    for i, frase in enumerate(lista_palavras_cruas):
        # print(lista_palavras[i].strip())
        # print(lista_palavras[i].rstrip())
        # print(lista_palavras[i].lstrip())
        # lista_palavras[i] = lista_palavras[i].strip()
        lista_palavras.append(lista_palavras_cruas[i].strip())
        
    print(lista_palavras_cruas)
    print(lista_palavras)

Agora, o join, é um outro método de string e ela tem por finalidade unir as frases.

    frase = '     Olha só que    , coisa interessante    '
    # lista_palavras = frase.split()
    lista_palavras_cruas = frase.split(',')
    print(frase)
    lista_palavras = []

    for i, frase in enumerate(lista_palavras_cruas):
        # print(lista_palavras[i].strip())
        # print(lista_palavras[i].rstrip())
        # print(lista_palavras[i].lstrip())
        # lista_palavras[i] = lista_palavras[i].strip()
        lista_palavras.append(lista_palavras_cruas[i].strip())
        
    # print(lista_palavras_cruas)
    # print(lista_palavras)
    # frases_unidas = ''.join('abc')
    # frases_unidas = '-'.join('abc')
    # frases_unidas = '-'.join(lista_palavras)
    frases_unidas = ', '.join(lista_palavras)
    print(frases_unidas)

Nesse método, note que, precisamos passar algum parâmetro para ela para unir seja ela os caracteres de uma frase string ou seja ela os elementos de uma lista. Por exemplo, no join usado para 'frases_unidas = '-'.join('abc')', note que, ao rodarmos o códido printando-a, será retornado 'a-b-c'. Se for vazio, '', será retornado a mesma string que foi colocado no join. A mesma lógica vale para listas. Enquando que em uma string, cada caracteres que compõe uma string é vista como um elemento, na lista é a mesma coisa.

Obs: Até agora, somente a lista, string e tuples são iteráveis.

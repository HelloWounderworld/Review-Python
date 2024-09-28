# Aula 63 - O que aprendemos com while também funciona no for (continue, break, else, etc):
Vamos ver que os usos que fizemos de continue, break, else, etc... Para o while, funciona tudo para o for tbm.

No caso, segue um exemplo disso

    for i in range(10):
        if i == 2:
            print('i é 2, pulando...')
            continue

        if i == 8:
            print('i é 8, seu else não executará')
            break

        for j in range(1, 3):
            print(i, j)
    else:
        print('For completo com sucesso!')

Além disso, assim como foi visto o uso do break dentro do while que está de um outro while, o mesmo vale para o for

    for i in range(10):
        for j in range(10):
            if j == 2:
                print('Escopo interno', j)
                break
        print('Escopo externo', i)

Ou seja, ele funciona de uma forma de que o break ele quebra apenas o laço mais próximo dele.

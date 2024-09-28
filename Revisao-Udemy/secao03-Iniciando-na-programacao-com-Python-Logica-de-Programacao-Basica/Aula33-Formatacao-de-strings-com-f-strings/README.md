# Aula 33 - Formatação de strings com f-strings:
Vamos ver formatação de strings com f-strings.

Bom, o f-strings já foi visto antes o seu uso e já aplicamos algumas vezes nos estudos daqui. Porém vamos ver algo um pouco mais à fundo disso

    """
    Formatação básica de strings
    s - string
    d - int
    f - float
    .<número de dígitos>f
    x ou X - Hexadecimal
    (Caractere)(><^)(quantidade)
    > - Esquerda
    < - Direita
    ^ - Centro
    = - Força o número a aparecer antes dos zeros
    Sinal - + ou -
    Ex.: 0>-100,.1f
    Conversion flags - !r !s !a 
    """
    variavel = 'ABC'
    print(f'{variavel}')

Agora, suponhamos que queremos colocar mais caracteres de espaço para esquerda. No caso, o f-strings ele faz isso

    print(f'{variavel: >10}.')
    print(f'{variavel: <10}.')

Donde é análogo para espaço para direita.

           ABC.
    ABC       .

Basicamente, é o que está sendo devolvido. No caso, a contagem funciona assim

           3210  
           ABC.

e o restante de 4 até 9 para preencher o restante de 10 caractéres.

Mas, mais especificamente, isso que estamos fazendo é uma forma de colocarmos mais caractéres no lado esquerdo ou direito.

Temos uma forma de colocar o caractére no centro tbm

    print(f'{variavel: ^10}.')

No caso, será retornado o seguinte

       ABC    .

Temos tbm, para exibir alguns números, a forma seguinte

    print(f'{1000.4873648123746:.1f}')
    print(f'{1000.4873648123746:,.1f}')
    print(f'{-1000.4873648123746:,.1f}')
    print(f'{1000.4873648123746:-,.1f}')
    print(f'{1000.4873648123746:+,.1f}')
    print(f'{1000.4873648123746:0>+10,.1f}')
    print(f'{1000.4873648123746:0=+10,.1f}')

Donde, será o retornado o seguinte

    1000.5
    1,000.5
    -1,000.5
    1,000.5
    +1,000.5
    00+1,000.5
    +001,000.5

E temos tbm o hexadecimal como foi visto antes

    print(f'O hexadecimal de 1500 é {1500:08X}')

Além disso, temos a possibilidade tbm de usarmos para exibir os seus métodos

    print(f'{variavel!r}')

Para mais detalhes seguir a documentação

    https://realpython.com/python-f-strings/#:~:text=Also%20called%20%E2%80%9Cformatted%20string%20literals,the%20__format__%20protocol.

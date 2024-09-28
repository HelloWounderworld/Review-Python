# Aula 26 - Operadores importantes para o tipo set (conjuntos):
Bom, vamos aprender sobre os operadores existentes no "set".

Vale lembrar que tais operadores são, definitivamente, as operações usuais de conjuntos que temos na matemática.

São elas, as mais usuais

- Une | - União:

    Para união de conjuntos, usamos o caractere "|" como segue

        s11 = {1,2,3}
        s12 = {2,3,4}

        s13 = s11 | s12

- intersecção & (intersection):

    Para a intersecção de conjuntos, usamos o caractere "&" como segue

        s11 = {1,2,3}
        s12 = {2,3,4}

        s14 = s11 & s12

- diferença - complemento:

    Para o complemento de conjunto, usamos o caractere "-" como segue

        s11 = {1,2,3}
        s12 = {2,3,4}

        s15 = s11 - s12

- diferença simétrica ^ - Itens que não estão em ambos - Complemento da união:

    Esse aqui é uma espécie de complemento da intersecção. Em outras palavras, ao detalharmos o que é representado pelo "^" que é a diferença simétrica de conjuntos, considerando A e B, os conjuntos, seria "(A-B)|(B-A)". Como segue

        s11 = {1,2,3}
        s12 = {2,3,4}

        s17 = s11 ^ s12
        s18 = (s11 - s12) | (s12 - s11)
        
        print(s17)
        print(s18)
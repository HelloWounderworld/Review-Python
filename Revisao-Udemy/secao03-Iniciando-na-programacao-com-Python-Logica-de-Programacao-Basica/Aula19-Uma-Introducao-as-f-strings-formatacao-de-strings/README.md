# Aula 19 - Uma introdução às f-strings (formatação de strings):
Vamos aprender o básico sobre a formatação de strings.

No caso, suponhamos que tenhamos uma frase que queiramos jogar tudo em uma variável. Claro, o usual nessa hora seria usar uma string para tal finalidade. Mas podemos usar a formatação de strings que ela permite não somente manter o formato string, mas permite implementar algumas variáveis dentro dela

    linha_1 = f'{nome} tem {altura:.2f} de altura,'
    linha_2 = f'pesa {peso} quilos e seu imc é'
    linha_3 = f'{imc:.2f}'

    print(linha_1)
    print(linha_2)
    print(linha_3)

Ou seja, o f-strings ela é uma espécie de crase do JavaScript, onde podemos chamar  as outras variáveis que definimos dentro dela e retornar, pelo terminal, em uma forma de string.

Bom, isso foi uma brevíssima introdução sobre f-strings.

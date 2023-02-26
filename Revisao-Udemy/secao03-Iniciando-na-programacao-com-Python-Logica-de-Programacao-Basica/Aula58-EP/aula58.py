"""Qual letra apareceu mais vezes?"""

letra = input('Digite uma frase: ')

i = 0
letra_apareceu_mais_vezes = ''
qtd_apareceu_mais_vezes = 0
while i < len(letra):
    if letra[i] == ' ':
        i += 1
        continue
    j = 0
    letra_verifica = letra[i].lower()
    contador = 0
    while j < len(letra):
        if letra[j].lower() == letra_verifica:
            contador += 1
        j += 1
    if contador >= qtd_apareceu_mais_vezes:
        qtd_apareceu_mais_vezes = contador
        letra_apareceu_mais_vezes = letra_verifica
    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)
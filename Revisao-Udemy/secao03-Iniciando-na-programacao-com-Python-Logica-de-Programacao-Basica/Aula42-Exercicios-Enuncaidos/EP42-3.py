"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
entrada = input('Coloque o seu primeiro nome: ')

try:
    confere_string = entrada.isdigit()
    confere_float = float(entrada)
    print('Coloque um nome válido!')
except:
    confere_espaco = ' ' in entrada
    if confere_espaco is not True:
        print(len(entrada))
        menos_4_letra = len(entrada) <= 4
        entre_5_6_letras = len(entrada) >= 5 and len(entrada) <= 6
        maior_6_letras = len(entrada) > 6
        if menos_4_letra:
            print('Seu nome é curto')
        elif entre_5_6_letras:
            print('Seu nome é normal')
        elif maior_6_letras:
            print('Seu nome é muito grande')
    else:
        print('Coloque um nome sem espaço')

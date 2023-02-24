"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input('Que horas são: ')

try:
    entrada = int(entrada)
    confere_dentro_24 = entrada >=0 and entrada < 24
    if confere_dentro_24:
        if entrada >= 0 and entrada <= 11:
            print('Bom dia')
        if entrada >=12 and entrada <=17:
            print('Boa tarde')
        if entrada >= 18 and entrada <= 23:
            print('Boa noite')
    else:
        print('Esse número não pode ser lido como hora')
except:
    print('Digite um horário válido')

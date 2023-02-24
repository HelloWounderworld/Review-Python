"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada = int(entrada)
    par = entrada % 2 == 0
    if par:
        print('O número é par')
    else:
        print('O número é ímpar')
else:
    print('Isso não é um número inteiro')

try:
    entrada = int(entrada)
    par = entrada % 2 == 0
    if par:
        print('O número é par')
    else:
        print('O número é ímpar')
except:
    print('Isso não é um número inteiro')
    
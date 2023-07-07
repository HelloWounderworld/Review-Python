"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
11 10  9  8  7  6  5  4  3  2
7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
entrada = input('Digite o seu CPF com pontos e traços: ')
cpf_enviado = entrada.replace('.', '') \
    .replace('-', '') \
    .replace(' ', '')
cpf = cpf_enviado[:9]

soma = 0
for i in range(0,len(cpf)):
    soma = soma + ((10-i)*int(cpf[i]))

soma = (soma * 10) % 11
cpf = cpf + str((soma if soma <= 9 else 0))

soma = 0
for i in range(0,len(cpf)):
    soma = soma + ((11-i)*int(cpf[i]))

soma = (soma * 10) % 11
cpf = cpf + str((soma if soma <= 9 else 0))

if cpf == cpf_enviado:
    print(f'{cpf_enviado} é válido!')

else:
    print('CPF inválido!')

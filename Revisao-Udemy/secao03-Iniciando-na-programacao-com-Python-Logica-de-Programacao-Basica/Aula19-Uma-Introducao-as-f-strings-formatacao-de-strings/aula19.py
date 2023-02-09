nome = 'Leonardo Takashi Teramatsu'
altura = 1.83
peso = 78
imc = peso / altura ** 2

# f-strings
# O ":.2f" vc configura a quantidade de casas decimais que vc quer para um float.
# No caso acima está sendo até duas casas decimais. Se for três seria ":.3f".
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Existem casos em que queremos realizar as separações dos números inteiros por vírgula
numero = 100050.4

numero_personaliza = f'{numero:,.2f}'

print(numero_personaliza)
# Retorna: 100,050.40

"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

# print(1234)
# print(456)
# int('a')
# float('a')

numero_str = input('Vou dobrar o número que vc digitar: ')
# print(numero_str.isdigit())

try:
    # ...
    print('STR: ', numero_str)
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobre de {numero_str} é {numero_str * 2}')
    print(f'O dobre de {numero_str} é {numero_float * 2}')
    print(f'O dobre de {numero_str} é {numero_float * 2:.0f}')
    print(f'O dobre de {numero_str} é {numero_float * 2:.2f}')
except:
    # ...
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobre de {numero_str} é {numero_str * 2}')
#     print(f'O dobre de {numero_str} é {numero_float * 2}')
#     print(f'O dobre de {numero_str} é {numero_float * 2:.0f}')
#     print(f'O dobre de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')



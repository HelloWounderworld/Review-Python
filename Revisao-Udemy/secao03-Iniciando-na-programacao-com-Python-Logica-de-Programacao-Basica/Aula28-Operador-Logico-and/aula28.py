# Operadores lógicos
# and (e), or (ou) e not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira avaliada naquele valor será considerada falso
# São considerado falso:
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor.
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
print(bool(0))
print(bool(0.0))
print(bool(''))
print(True and True and True)
print(True and 1 and True)
print(True and 1 and False)
print(True and 1 and 0)
print(True and False and True)
print(True and 0 and True)
print('' and True and True)
print(True and True and 0.0)


# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
# senha = input('Senha: ') or 'Sem senha'
# print(senha)

print(bool(0))
print(bool(0.0))
print(bool(''))
print(False or False or False)
print(True or True or True)
print(True or 1 or True)
print(True or 1 or False)
print(True or 1 or 0)
print(True or False or True)
print(True or 0 or True)
print('' or True or True)
print(True or True or 0.0)
print(0 or 0.0 or '')
print('' or 0 or 0.0)
print(0.0 or '' or 0)
print(0.0 or False or 0)
print('' or 0.0 or False)

"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg, nome=None):
    return f'{msg}, {nome}'

def executa(funcao, *arg):
    return funcao(*arg)

saudacao_2 = saudacao
random = saudacao_2('Boa noite!!!')
print(random)

saudacao_3 = saudacao
variavel = executa(saudacao_3, 'Boa tarde!')
print(variavel)

saudacao_4 = saudacao
variavel2 = executa(saudacao_4, 'Boa tarde', 'Leonardo')
print(variavel2)

print(saudacao('Bom dia!'))

v = saudacao('Bom dia!')
print(v)

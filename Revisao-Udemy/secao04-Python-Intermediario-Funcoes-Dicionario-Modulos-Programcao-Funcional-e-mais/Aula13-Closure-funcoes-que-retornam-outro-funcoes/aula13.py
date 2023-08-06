"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('Bom dia', 'Leonardo')
s2 = criar_saudacao('Boa noite', 'Leonardo')
print(s1)
print(s1())

print(s2)
print(s2())

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('Bom dia')
s2 = criar_saudacao('Boa noite')
print(s1)
print(s1('Leonardo'))

print(s2)
print(s2('Leonardo'))

for i in ['Luiz', 'Maria', 'Bruno', 'Pedro']:
    print(s1(i))
    print(s2(i))
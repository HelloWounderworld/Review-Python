"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y):
    #Definicao 
    print(x+y)
    print(f'{x=} y={y}', '|', 'x+y= ', x+y)

print(soma)
# print(soma(1,2))
# Não nomeado
soma(1,2)
soma(2,1)

# Nomeado
soma(x=1, y=2)
soma(y=2, x=1)

def soma2(x, y, z):
    print(f'{x=} y={y} {z=}', '|', 'x+y+z= ', x+y+z)

soma2(1,2,z=3)
# soma2(1,y=2,3) # isso vai dar errado
soma2(1,y=2,z=3)
soma2(z=3,x=1,y=2)
print(1,2,3,sep='-')

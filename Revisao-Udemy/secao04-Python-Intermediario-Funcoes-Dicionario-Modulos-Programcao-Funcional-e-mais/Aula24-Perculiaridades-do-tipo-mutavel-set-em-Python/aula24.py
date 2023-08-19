# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
s1= set('Leonardo')
print(s1, type(s1))

s2 = {'Leonardo', 1, 2, 3}
print(s2, type(s2))

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
s3 = {1, 1, 1, 1, 2, 3, 3, 3, 3, 3}
print(s3)

l1 = [1, 1, 1, 1, 2, 3, 3, 3, 3, 3]
t1 = (1, 1, 1, 1, 2, 3, 3, 3, 3, 3)

s4 = set(l1)
s5 = set(t1)

print(s4)
print(s5)

l2 = list(s4)
t2 = tuple(s5)

print(l2)
print(t2)

# s6 = {1,2,3,[123]}
s7 = {1,2,3,(123,)}
# s8 = {1,2,3,{123}}

print(s7)
print(3 in s7)
print(4 in s7)
print(5 not in s7)
# print(s8)

for numero in s7:
    print(numero)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
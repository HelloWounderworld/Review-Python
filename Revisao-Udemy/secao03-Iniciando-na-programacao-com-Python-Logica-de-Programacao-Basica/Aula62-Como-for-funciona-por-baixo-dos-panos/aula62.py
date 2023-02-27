"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Leonardo'.__iter__()  # iterável
print(texto)
print('--------------')
iteratador = iter(texto)  # iterator
print(iteratador)
# print(iteratador.__next__())
# print(iteratador.__next__())
# print(iteratador.__next__())
# print(iteratador.__next__())
# print(iteratador.__next__())
# print(iteratador.__next__())
# print(iteratador.__next__())
# print(iteratador.__next__())
# print(iteratador.__next__())
print('--------------')
# while True:
#     print(next(iteratador))
    
while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

# for letra in texto:
#     print(letra)
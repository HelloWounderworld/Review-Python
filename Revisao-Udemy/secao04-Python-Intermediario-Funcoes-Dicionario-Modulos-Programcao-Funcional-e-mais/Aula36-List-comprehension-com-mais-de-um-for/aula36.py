import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

lista = []

for x in range(3):
    for y in range(3):
        lista.append((x,y))

p(lista)

lista2 = [
    (x, y) 
    for x in range(3) 
    for y in range(3)
]

p(lista2)

lista3 = [
    [x for y in range(3)]
    for x in range(3)
]

p(lista3)

lista4 = [
    [(x, y) for y in range(3)]
    for x in range(3)
]

p(lista4)

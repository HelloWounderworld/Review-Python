# isinstace - para saber se objeto é de determinado tipo

lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Leonardo'}]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        item = item.upper()
        print(item, isinstance(item, str))

    elif isinstance(item, (int, float)):
        item+=1
        print(item, isinstance(item, (int, float)))

    else:
        print('OUTRO')

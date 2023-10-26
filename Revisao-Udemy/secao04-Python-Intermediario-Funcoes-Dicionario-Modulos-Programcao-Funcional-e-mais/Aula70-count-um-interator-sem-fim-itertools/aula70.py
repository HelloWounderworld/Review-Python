# count é um iterador sem fim (itertools)
from itertools import count

c1 = count(10)
r1 = range(10, 100)
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print()
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))
print()
print('count')
for i in c1:
    if i >= 100:
        break

    print(i)
print()
print('range')
for j in r1:
    print(j)

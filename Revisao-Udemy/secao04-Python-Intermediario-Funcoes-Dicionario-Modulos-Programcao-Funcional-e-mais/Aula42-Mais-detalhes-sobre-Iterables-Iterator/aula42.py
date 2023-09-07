# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iterable.__iter__() # tem __iter__ e __next__
iterator = iter(iterable)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

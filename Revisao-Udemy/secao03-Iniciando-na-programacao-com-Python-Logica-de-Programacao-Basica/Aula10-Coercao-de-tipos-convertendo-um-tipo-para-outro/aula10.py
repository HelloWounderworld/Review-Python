# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(1 + 1)
print('a' + 'b')
# print('a' + 1)
print('1', type('1'))
print(int('1'), type(int('1')))

# print('a', type('a'))
# print(int('a'), type(int('a')))

print(1.0 + 1) # retorna um float

print(bool(''))
print(bool(' '))

print(bool({}))
print(bool({ 'Estado': 'SP'}))

print(bool([]))
print(bool([1]))

print(str(11) + 'b')
print(str({}))
print(str([]))
print(str(True))
print(str(False))

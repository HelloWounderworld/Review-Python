# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError('Você está dividindo por zero!')
    
    return x / y

print(divide(8, 0))

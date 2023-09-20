# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def divisao_por_zero_indefinido(denominador):
    if denominador == 0:
        raise ZeroDivisionError('Você está dividindo por zero!')

def divide(x, y):
    divisao_por_zero_indefinido(y)
    return x / y

print(divide(8, 0))

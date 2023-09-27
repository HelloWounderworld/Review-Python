# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def divisao_por_zero_indefinido(denominador):
    if denominador == 0:
        raise ZeroDivisionError('Não pode dividir pelo zero!')

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True

def divide(x, y):
    deve_ser_int_ou_float(x)
    deve_ser_int_ou_float(y)
    
    divisao_por_zero_indefinido(y)
    return x / y

print(divide(8, '0'))

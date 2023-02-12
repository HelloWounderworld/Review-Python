primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor < segundo_valor:
    valor_maior = 'segundo_valor='+'\''+segundo_valor+'\''
    valor_menor = 'primeiro_valor='+'\''+primeiro_valor+'\''
else:
    valor_maior = 'primeiro_valor='+'\''+primeiro_valor+'\''
    valor_menor = 'segundo_valor='+'\''+segundo_valor+'\''

resultado = '{valor1} é maior que o {valor2}'.format(valor1=valor_maior,valor2=valor_menor)
print(resultado)

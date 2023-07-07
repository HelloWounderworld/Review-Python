"""
Operação ternária (condicional de uma liniha)
<valor> if <condicao> else<outro valor>
"""

print('Valor' if True else 'Outro valor')
print('Valor' if False else 'Outro valor')

condicao = 10 == 10
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

print('Valor1' if True else 'Valor2' if True else 'Valor3' if True else 'FIM')
print('Valor1' if False else 'Valor2' if True else 'Valor3' if True else 'FIM')
print('Valor1' if False else 'Valor2' if False else 'Valor3' if True else 'FIM')
print('Valor1' if False else 'Valor2' if False else 'Valor3' if False else 'FIM')

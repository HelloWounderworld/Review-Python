# Aprendendo a importar módulos ou diretamente recursos existentes dentro desse módulo
import aula52_m
from aula52_m import soma, variavel_modulo
import aula52_m as aula
from aula52_m import soma as doublesum, variavel_modulo as nome

print('Este módulo, aula52.py, se chama: ', __name__)
#print(aula52_m)

print(aula52_m.variavel_modulo)
print(variavel_modulo)

print(aula52_m.soma(2, 3))
print(soma(3, 4))

print(aula.variavel_modulo)
print(aula.soma(4, 5))

print(doublesum(5, 6))
print(nome)

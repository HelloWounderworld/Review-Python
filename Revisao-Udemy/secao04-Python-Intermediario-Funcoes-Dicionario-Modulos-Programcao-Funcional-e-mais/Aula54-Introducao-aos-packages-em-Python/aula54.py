from sys import path

import aula54_p.modulo
from aula54_p import modulo
#from aula54_p.modulo import soma_do_modulo
from aula54_p.modulo import *

print(__name__)
print()
print("Path: ", path)
print()
print(*path, sep='\n')
print()
print(aula54_p.modulo.soma_do_modulo(2, 3))
print()
print(modulo.soma_do_modulo(4, 5))
print()
print(variavel)
print()
print(soma_do_modulo(3, 4))

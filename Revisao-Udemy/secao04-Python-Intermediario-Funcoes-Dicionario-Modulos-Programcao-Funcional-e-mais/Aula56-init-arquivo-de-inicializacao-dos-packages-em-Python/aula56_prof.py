# from sys import path
# https://stackoverflow.com/questions/2386714/why-is-import-bad

# import aula56_package.modulo
# from aula56_package import modulo
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)
# from aula56_package.modulo import fala_oi, soma_do_modulo
# print(__name__)
# fala_oi()

from aula56_package import falar_oi, soma_do_modulo

print(soma_do_modulo(2, 3))
falar_oi()
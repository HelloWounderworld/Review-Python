import importlib
import aula53_m

print(aula53_m.variavel)

for i in range(10):
    importlib.reload(aula53_m)

print('Fim')
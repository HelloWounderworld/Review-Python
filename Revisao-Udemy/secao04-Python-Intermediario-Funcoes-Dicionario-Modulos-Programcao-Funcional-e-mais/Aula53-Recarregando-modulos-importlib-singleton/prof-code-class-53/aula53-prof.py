import importlib

import aula53_prof_m

print(aula53_prof_m.variavel)

for i in range(10):
    importlib.reload(aula53_prof_m)
    print(i)

print('Fim')
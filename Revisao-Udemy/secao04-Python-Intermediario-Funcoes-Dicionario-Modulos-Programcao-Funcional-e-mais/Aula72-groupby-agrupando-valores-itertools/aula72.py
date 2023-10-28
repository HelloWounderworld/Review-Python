# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
print(*alunos_agrupados, sep='\n')
print()

# alunos = ['a', 'a', 'a', 'a', 'a', 'b', 'c']
grupos_sem_chave = groupby(alunos)
grupos = groupby(alunos_agrupados, key=ordena)

print(grupos_sem_chave)
print()
print(grupos)
print()

# print(*list(grupos), sep='\n')

for chave, grupo in grupos:
    print(chave)
    print(grupo)
    # print(*list(grupo), sep='\n')
    for aluno in grupo:
        print(aluno)
    print()
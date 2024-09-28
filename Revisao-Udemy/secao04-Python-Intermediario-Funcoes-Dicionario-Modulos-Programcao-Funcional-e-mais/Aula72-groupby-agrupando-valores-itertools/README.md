# Aula 72 - groupby - agrupando valores (itertools):
Vamos aprender e mexer na ferramente groupby, que é uma ferramenta de agrupamento de valores, e que é método do móulo itertools.

Para o começo, vamos definir a seguinte lista

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

Por começo, vamos aplicar o método groupby para algo simples

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

    alunos = ['a', 'a', 'a', 'a', 'a', 'b', 'c']
    grupos = groupby(alunos)
    print(grupos)
    print(list(grupos))

Ou, para melhor vizualizarmos, podemos ver o seguinte

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

    alunos = ['a', 'a', 'a', 'a', 'a', 'b', 'c']
    grupos = groupby(alunos)
    
    for chave, grupo in grupos:
        print(chave)
        print(grupo)
        print(list(grupo))

Note que, na forma acima, vimos que foi criado várias sub-listas, donde separa pelos elementos que se repetiram e a sua quantidade de repetições sendo mostrado pela quantidade de aparições do mesmo elemento.

No caso, queremos que a mesma coisa aconteça na lista alunos donde temos como elementos vários dicionários, mas, para isso, precisamos, primeiro, ordernar.

Já estudamos ordenação, no curso onde estávamos estudando sobre sort e sorted, que aplicado tais conhecimentos seria da seguinte forma

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

    alunos_agrupados = sorted(alunos, key=lambda a: a['nota'])
    print(*alunos_agrupados, sep='\n')

Agora, sim, vamos usar o group. Note que, na ordenação, precisamos especificar por qual chave iremos realizar a tal ordenação. Para o groupby, não muda nada tbm, pois iremos precisar especificar por qual chave iremos criar tais sub-listas

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

    alunos_agrupados = sorted(alunos, key=lambda a: a['nota'])
    print(*alunos_agrupados, sep='\n')

    grupos_sem_chave = groupby(alunos)
    grupos = groupby(alunos_agrupados, key=lambda a: a['nota'])


Vamos melhorar a qualidade do código, seguindo os princípios do clean code, para evitarmos em repetir o "lambda a: a['nota']"

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

    grupos_sem_chave = groupby(alunos)
    grupos = groupby(alunos_agrupados, key=ordena)

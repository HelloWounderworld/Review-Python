# Aula 40 - Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis:
Vamos ver mais sobre os valores Falsy e Truthy.

Bom, o falsy e thuthy, podemos usar sobre os valores mutáveis e imutáveis, donde temos como padrão os tipos de valores que são considerados falsos ou outros como verdadeiros. Já vimos sobre isso nas aulas anteriores sobre os valores mutáveis e imutáveis. Recomendamos que o leitor revise tais aulas caso ficou alguma dúvida.

    lista = []
    dicionario = {}
    conjunto = set()
    tupla = ()
    string = ''
    inteito = 0
    flutuante = 0.0
    nada = None
    falso = False
    intervalo = range(0)


    def falsy(valor):
        return 'falsy'if not valor else 'truthy'


    print(f'TESTE', falsy('TESTE'))
    print(f'{lista=}', falsy(lista))
    print(f'{dicionario=}', falsy(dicionario))
    print(f'{conjunto=}', falsy(conjunto))
    print(f'{tupla=}', falsy(tupla))
    print(f'{string=}', falsy(string))
    print(f'{inteito=}', falsy(inteito))
    print(f'{flutuante=}', falsy(flutuante))
    print(f'{nada=}', falsy(nada))
    print(f'{falso=}', falsy(falso))
    print(f'{intervalo=}', falsy(intervalo))
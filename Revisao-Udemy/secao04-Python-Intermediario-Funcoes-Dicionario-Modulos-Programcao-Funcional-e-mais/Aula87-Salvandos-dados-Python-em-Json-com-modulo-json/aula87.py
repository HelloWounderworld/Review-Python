import json

caminho_arquivo_path = '/home/leonardo/Documentos/estudos-programacao/Review-Python/Revisao-Udemy/secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais/Aula87-Salvandos-dados-Python-em-Json-com-modulo-json/aula87.json'

pessoa = {
    'nome': 'Leonardo T',
    'sobrenome': 'Teramatsu',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 123}
    ],
    'altura': 183,
    'numeros_preferidos': (2, 3, 13, 17, 19, 23),
    'dev': True,
    'nada': None
}

# with open(caminho_arquivo_path, 'w') as arquivo:
#     json.dump(pessoa, arquivo)

# with open(caminho_arquivo_path, 'w') as arquivo:
#     json.dump(pessoa, arquivo, ensure_ascii=False)

with open(caminho_arquivo_path, 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2
    )

with open(caminho_arquivo_path, 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))
    print(pessoa['nome'])

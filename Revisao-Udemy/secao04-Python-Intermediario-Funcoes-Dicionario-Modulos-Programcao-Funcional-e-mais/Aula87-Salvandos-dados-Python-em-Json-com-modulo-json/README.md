# Aula 87 - Salvando dados Python em JSON com módulo json:
Vamos aprender a salvar dados Python em Json com módulo json.

Para quem não sabe o que é json, seguir o seguinte link de vídeo:

    https://www.youtube.com/watch?v=XmCrArtfjaQ

Basicamente, o Json ele é uma estrutura de dados que é bom para ser salva e enviada para outros sistemas. Geralmente, as API's ou Endpoints, quando elas enviam algum dado de um sistema para o outro sistema em uma espécie de integração, os dados são mandados no formato Json. Essa estrutura Json é muito bem vista em JavaScript, por exemplo, package.json, onde nela se encontram pacotes e estruturas que precisam ser baixadas para poder rodar o projeto.

No python, isso não muda muito. Aqui, também, para podermos salvar algum dado ou até mesmo enviar, o tipo de estrutura boa para possibilitarmos isso é usando o Json.

Bom, vamos, por começo, criar um arquivo "aula87.py" e dentro dela vamos importar o seguinte módulo

    import json

    caminho_arquivo_path = '/home/leonardo/Documentos/estudos-programacao/Review-Python/Revisao-Udemy/secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais/Aula87-Salvandos-dados-Python-em-Json-com-modulo-json/aula87.json'

    pessoa = {
        'nome': 'Leonardo',
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

Em seguida, vamos colocar o seguinte

    with open(caminho_arquivo_path, 'w') as arquivo:
        json.dump(pessoa, arquivo)

Ao executarmos o código acima, vamos ver que será criado um arquivo "aula87.json" dentro da pasta dessa aula 87 e dentro dela foi feito um dump (Serializa o objeto formato Python para um arquivo Json) do dado pessoa. O que é diferente de simplesmente escrever a variável pessoa dentro do arquivo json. Como segue

    {"nome": "Leonardo", "sobrenome": "Teramatsu", "enderecos": [{"rua": "R1", "numero": 32}, {"rua": "R2", "numero": 123}], "altura": 183, "numeros_preferidos": [2, 3, 13, 17, 19, 23], "dev": true, "nada": null}

Existem caso de se vc colocar algum caractere especial, isso irá deixar salvo no arquivo "json" em um formato estranho os elementos que vc salvou dentro da variável pessoa. Eu recomendo deixar do jeito como está. Porém, caso a pessoa queira resolver esse problema, ela poderia fazer o seguinte

    with open(caminho_arquivo_path, 'w') as arquivo:
        json.dump(pessoa, arquivo, ensure_ascii=False)

Se quisermos que o nosso dicionário que foi salvo no arquivo json, aula87.json, seja salvo de forma bem identada, bastaria colocar a sintaxe "indent="

    with open(caminho_arquivo_path, 'w', encoding='utf8') as arquivo:
        json.dump(
            pessoa,
            arquivo,
            ensure_ascii=False,
            indent=2
        )

Assim, será salvo como podemos ver o seguinte

    {
        "nome": "Leonardo",
        "sobrenome": "Teramatsu",
        "enderecos": [
            {
                "rua": "R1",
                "numero": 32
            },
            {
                "rua": "R2",
                "numero": 123
            }
        ],
        "altura": 183,
        "numeros_preferidos": [
            2,
            3,
            13,
            17,
            19,
            23
        ],
        "dev": true,
        "nada": null
    }

Um detalhe importante!

Lembre-se que a estrutura de dados json, ele é bom para salvar estrutura de dados simples. Logo, não vamos poder salvar dentro dessa estrutura dados como funções, métodos, classes e sets. Caso, vc coloque algum desses tipos de dados, dará um erro na compilação.

Outro detalhe, é que, se olharmos o elemento "numeros_preferidos", antes, ela estava no formato de uma tupla. Porém, quando dizemos o dump dentro do arquivo json, ele virou uma lista, array. Logo, quando trazermos de volta o dado que está salvo no json, também, provavelmente, ela estará como lista tbm.

Vamos, agora, aprender a trazer de volta os dados que está no json. Primeiro, vamos comentar, fora o "import json" e "caminho_arquivo_path", todos os códigos que criamos até agora. Em seguida, vamos colocar o seguinte código

    with open(caminho_arquivo_path, 'r', encoding='utf8') as arquivo:
        pessoa = json.load(arquivo)
        print(pessoa)
        print(type(pessoa))
        print(pessoa['nome'])

Como podemos ver, conseguirmos puxar um dado do arquivo externo python.

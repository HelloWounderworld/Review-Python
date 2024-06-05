# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

caminho_arquivo_path = 'c:/Users/leona/Documents/study-programming/Review-Python/Revisao-Udemy/secao05-Introducao-a-programcao-orientada-a-objetos-POO-em-Python/Aula10e11-Exercicio-Solucao-Salve-sua-classe-em-JSON/aula1011.json'

class Pessoa:

    def __init__(self, nome, sobrenome, endereco, altura, numeros_preferidos, dev):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco
        self.altura = altura
        self.numeros_preferidos = numeros_preferidos
        self.dev = dev
    
pessoa1 = Pessoa(
    'Leonardo Takashi', 
    'Teramatsu', 
    [
        {'rua': 'Estou perdido', 'numero': 00},
        {'rua': 'Nesse mundo onde nao tenho lugar', 'numero': 234}
    ], 
    180.5, 
    (2, 3, 13, 17, 19, 23),
    True
)

pessoa2 = Pessoa(
    'Alan', 
    'Turing', 
    [
        {'rua': 'Estou perdido', 'numero': 00},
        {'rua': 'Nesse mundo onde nao tenho lugar', 'numero': 234}
    ], 
    180, 
    (2, 3, 13, 17, 19, 23),
    False
)

pessoa3 = Pessoa(
    'Albert', 
    'Einstein', 
    [
        {'rua': 'Estou perdido', 'numero': 00},
        {'rua': 'Nesse mundo onde nao tenho lugar', 'numero': 234}
    ], 
    170, 
    (2, 3, 13, 17, 19, 23),
    False
)

pessoa = [pessoa1.__dict__, vars(pessoa2), pessoa3.__dict__]

def dump(pessoa):
    with open(caminho_arquivo_path, 'w', encoding='utf8') as arquivo:
            json.dump(
                pessoa,
                arquivo,
                ensure_ascii=False,
                indent=4
            )

if __name__ == '__main__':
     dump(pessoa)

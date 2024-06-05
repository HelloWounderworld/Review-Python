# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

caminho_arquivo_path = 'c:/Users/leona/Documents/study-programming/Review-Python/Revisao-Udemy/secao05-Introducao-a-programcao-orientada-a-objetos-POO-em-Python/Aula10e11-Exercicio-Solucao-Salve-sua-classe-em-JSON/aula1011.json'

dados = {}

with open(caminho_arquivo_path, 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)

class Pessoa:

    def __init__(self, nome, sobrenome, endereco, altura, numeros_preferidos, dev):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco
        self.altura = altura
        self.numeros_preferidos = numeros_preferidos
        self.dev = dev

for i in range(0,len(dados)):
    p = Pessoa(**dados[i])
    # print(p.__dict__)
    print(p.nome)
    print(p.sobrenome)
    print(p.endereco[0])
    print(p.endereco[1])
    print(p.altura)
    print(p.numeros_preferidos)
    print(p.dev)
    print()

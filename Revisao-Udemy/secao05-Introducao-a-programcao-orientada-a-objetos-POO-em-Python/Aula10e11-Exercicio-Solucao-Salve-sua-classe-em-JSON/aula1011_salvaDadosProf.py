import json

CAMINHO_ARQUIVO = 'c:/Users/leona/Documents/study-programming/Review-Python/Revisao-Udemy/secao05-Introducao-a-programcao-orientada-a-objetos-POO-em-Python/Aula10e11-Exercicio-Solucao-Salve-sua-classe-em-JSON/aula1011Prof.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Joao', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), p2.__dict__, vars(p3)]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

print(__name__)
if __name__ == '__main__':
    print('ELE É O __main__')
    fazer_dump()
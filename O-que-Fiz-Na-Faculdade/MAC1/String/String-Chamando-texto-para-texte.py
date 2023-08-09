nome = input("Escreva o nome de um arquivo:")

with open(nome, 'r', encoding = 'utf-8') as arq_entrada:
    conteudo = arq_entrada.read()

print(conteudo)

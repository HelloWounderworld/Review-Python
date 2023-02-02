nome = "nome.txt" #poderia ser um input("Digite o nome do arquivo")

with open(nome, 'w', encoding = 'utf-8') as arq:
    #corpo do with
    arq.write(" O poeta e fingidor \n")
    arq.write(" Finge tao completamente \n")
    arq.write(" Que chega a fingir que e dor\n")
    arq.write(" A dor que deveras sente. \n")
    arq.write("            Fernando Pessoa.\n")

with open(nome, 'r', encoding = 'utf-8') as arq_entrada:
    conteudo = arq_entrada.read()

print(conteudo)

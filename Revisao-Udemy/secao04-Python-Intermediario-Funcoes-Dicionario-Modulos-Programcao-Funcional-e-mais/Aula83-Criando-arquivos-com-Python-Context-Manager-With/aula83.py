# Aprendendo a manipular arquivos que nem PHP, usando o python.
caminho_arquivo = 'aula83.txt'

caminho_arquivo_path = '/home/leonardo/Documentos/estudos-programacao/Review-Python/Revisao-Udemy/secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais/Aula83-Criando-arquivos-com-Python-Context-Manager-With/aula83_path.txt'

print(caminho_arquivo)
print(caminho_arquivo_path)

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

# arquivo_path = open(caminho_arquivo_path, 'w')
# arquivo_path.close()

with open(caminho_arquivo, 'w') as arquivo:
    print('Hello WounderWorld')
    print('Arquivo vai ser fechado')

with open(caminho_arquivo_path, 'w') as arquivo:
    print('Hello WounderWorld')
    print('Arquivo vai ser fechado')

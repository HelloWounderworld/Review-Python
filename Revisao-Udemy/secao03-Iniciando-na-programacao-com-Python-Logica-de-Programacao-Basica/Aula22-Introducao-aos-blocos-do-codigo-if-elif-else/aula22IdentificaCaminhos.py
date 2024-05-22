import os

# Determinar o Diretório de Trabalho Atual
current_working_directory = os.getcwd()
print(f"Diretório de trabalho atual: {current_working_directory}")

# Diretório de trabalho atual
cwd = os.getcwd()
print(f"Diretório de trabalho atual: {cwd}")

# Caminho relativo
relative_path = 'data/file.txt'
absolute_path = os.path.join(cwd, relative_path)
print(f"Caminho absoluto correspondente: {absolute_path}")

# Caminho absoluto
absolute_path = '/home/user/data/file.txt'
print(f"Caminho absoluto: {absolute_path}")

# Verifica se o caminho relativo existe
if os.path.exists(relative_path):
    print("O arquivo relativo existe.")
else:
    print("O arquivo relativo não existe.")

# Verifica se o caminho absoluto existe
if os.path.exists(absolute_path):
    print("O arquivo absoluto existe.")
else:
    print("O arquivo absoluto não existe.")


# O ponto de partida para a leitura de uma path é determinado pelo diretório de trabalho atual.
# Usando os.getcwd(), você pode descobrir o diretório atual e resolver caminhos relativos a partir dele. 
# Para trabalhar com caminhos absolutos, forneça o caminho completo que começa na raiz do sistema de arquivos.
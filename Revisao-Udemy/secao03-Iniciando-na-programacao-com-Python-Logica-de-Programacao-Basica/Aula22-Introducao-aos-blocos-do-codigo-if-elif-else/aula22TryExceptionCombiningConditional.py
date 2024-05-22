# Combinacao do Try\Exception e condicional

import os

# Verificar o nome do sistema operacional
# Na pratica aqui se usa tyr/Exception, colocando esse if dentro dele.
if os.name == 'nt':
    print("Sistema Operacional: Windows")
    # file_path = "c:\\Users\\leona\\Documents\\study-programming\\Review-Python\\Revisao-Udemy\\secao03-Iniciando-na-programacao-com-Python-Logica-de-Programacao-Basica\\Aula22-Introducao-aos-blocos-do-codigo-if-elif-else\\tryExceptionCombiningConditional.txt"
    file_path = 'C:\\Users\\leona\\Documents\\study-programming\\Review-Python\\Revisao-Udemy\\secao03-Iniciando-na-programacao-com-Python-Logica-de-Programacao-Basica\\Aula22-Introducao-aos-blocos-do-codigo-if-elif-else\\TryExceptionCombiningConditional.txt'
    # file_path = 'TryExceptionCombiningConditional.txt'
    # file_path = "c:/Users/leona/Documents/study-programming/Review-Python/Revisao-Udemy/secao03-Iniciando-na-programacao-com-Python-Logica-de-Programacao-Basica/Aula22-Introducao-aos-blocos-do-codigo-if-elif-else/tryExceptionCombiningConditional.txt"
    # file_path = "c:/Users/leona/Documents/study-programming/Review-Python/Revisao-Udemy/secao03-Iniciando-na-programacao-com-Python-Logica-de-Programacao-Basica/Aula22-Introducao-aos-blocos-do-codigo-if-elif-else/tryExceptionCombiningConditional.txt"

elif os.name == 'posix':
    print("Sistema Operacional: Unix/Linux/MacOS")
    file_path = ''
else:
    print(f"Sistema Operacional desconhecido: {os.name}")
    print('Que porra de sistema operacional e esse???')
    file_path = ''

def read_file(file_path):
    print(os.path)
    print(os.path.exists(file_path))
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError as e:
        print(f"File not found exception: {e}")
    except OSError as e:
        print(f"I\O exception: {e}")

# Example usage
# read_file('TryExceptionCombiningConditional.txt')
read_file(file_path)
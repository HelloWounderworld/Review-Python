# Combinacao do Try\Exception e condicional

import os

# file_path = "c:\\Users\\leona\\Documents\\study-programming\\Review-Python\\Revisao-Udemy\\secao03-Iniciando-na-programacao-com-Python-Logica-de-Programacao-Basica\\Aula22-Introducao-aos-blocos-do-codigo-if-elif-else\\tryExceptionCombiningConditional.txt"
file_path = os.path.normpath('Revisao-Udemy\\secao03-Iniciando-na-programacao-com-Python-Logica-de-Programacao-Basica\\Aula22-Introducao-aos-blocos-do-codigo-if-elif-else\\tryExceptionCombiningConditional.txt')
# file_path = "c:/Users/leona/Documents/study-programming/Review-Python/Revisao-Udemy/secao03-Iniciando-na-programacao-com-Python-Logica-de-Programacao-Basica/Aula22-Introducao-aos-blocos-do-codigo-if-elif-else/tryExceptionCombiningConditional.txt"
# file_path = "c:/Users/leona/Documents/study-programming/Review-Python/Revisao-Udemy/secao03-Iniciando-na-programacao-com-Python-Logica-de-Programacao-Basica/Aula22-Introducao-aos-blocos-do-codigo-if-elif-else/tryExceptionCombiningConditional.txt"

def read_file(file_path):
    print(os.path)
    print(os.path.exists(file_path))
    # if not os.path.exists(file_path):
    #     print("File does not exist.")
    #     return

    # try:
    #     with open(file_path, 'r') as file:
    #         for line in file:
    #             print(line.strip())
    # except FileNotFoundError as e:
    #     print(f"File not found exception: {e}")
    # except OSError as e:
    #     print(f"I\O exception: {e}")

# Example usage
read_file('tryExceptionCombiningConditional.txt')
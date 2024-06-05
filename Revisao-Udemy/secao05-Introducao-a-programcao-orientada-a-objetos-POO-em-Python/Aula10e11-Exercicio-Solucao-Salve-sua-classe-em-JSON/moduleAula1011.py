def print_message():
    print("Esta função foi chamada de module.py")

if __name__ == '__main__':
    print(__name__)
    print("module.py está sendo executado diretamente")
    print_message()
else:
    print(__name__)
    print("module.py foi importado")
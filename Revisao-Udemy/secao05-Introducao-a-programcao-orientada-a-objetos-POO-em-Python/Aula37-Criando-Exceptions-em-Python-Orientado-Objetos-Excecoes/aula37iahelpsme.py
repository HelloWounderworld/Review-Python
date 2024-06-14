class MyCustomError(Exception):
    def __init__(self, message, code):
        super().__init__(message)  # Chama o construtor da classe base com a mensagem
        self.code = code  # Um código de erro adicional

# Em algum lugar do seu código, você pode levantar essa exceção:
def do_something(param):
    if param < 0:
        raise MyCustomError("O parâmetro não pode ser negativo", code=400)

try:
    do_something(-1)
except MyCustomError as e:
    print(f"Erro capturado: {e}, Código: {e.code}")

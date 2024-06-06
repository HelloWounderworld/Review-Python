class Matematica:
    @staticmethod
    def area_circulo(raio):
        return 3.14159 * raio * raio

    @staticmethod
    def area_retangulo(largura, altura):
        return largura * altura
    
# Uso dos métodos estáticos
print("Área do Círculo:", Matematica.area_circulo(5))
print("Área do Retângulo:", Matematica.area_retangulo(4, 5))

class NumerosReais:
    @staticmethod
    def adicionar(x, y):
        return x + y

    @staticmethod
    def subtrair(x, y):
        return x - y

    @staticmethod
    def multiplicar(x, y):
        return x * y

    @staticmethod
    def dividir(x, y):
        if y == 0:
            raise ValueError("Não é possível dividir por zero.")
        return x / y

# Uso dos métodos estáticos
print("Adição:", NumerosReais.adicionar(5, 3))
print("Subtração:", NumerosReais.subtrair(5, 3))
print("Multiplicação:", NumerosReais.multiplicar(5, 3))
print("Divisão:", NumerosReais.dividir(5, 3))

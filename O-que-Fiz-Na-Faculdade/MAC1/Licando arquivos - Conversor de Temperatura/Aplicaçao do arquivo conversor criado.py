from conversor import Conversor
def main():
    '''c = Conversor() #Esse metodo somente armazena que a operaçao esta sendo feita dentro da classe Conversor
    f = c.celsiusParaFahrenheit(30.0) Essa forma serve somente para caso nao use @classmethod '''

    f = Conversor.celsiusParaFahrenheit(30.0)

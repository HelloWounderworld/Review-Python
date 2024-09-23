# Aula 15 - method vs @classmethod vs @staticmethod:
Bom, vamos resumir os tres conceitos que vimos ate agora.

- method: self, metodo de instancia - Qualquer metodo que eu definir dentro da classe que necessite utilizar o self sera um metodo de instancia.

- @classmethod: cls, metodo de classe - Eu nao tenho acesso ao self dentro desse metodo. Metodo de classe ele recebe a classe, cls. Note que, a forma como construimos a classe dentro desse metodo e o mesmo.

- @staticmethod: metodo (nao self, nao cls) - Nao tem acesso ao self e nem a classe, cls. E uma funcao, apenas.
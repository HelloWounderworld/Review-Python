# Objeto: instancia de uma "classe"
# Classe: entidade que reune caracteristicas especificas
# Classe = estado + comportamento, onde : estado = variaveis; comportamento = metodos que manipulam o estado

#class Carro:
    #pass
    #a = Carro()
    #b = Carro()
    #a == b

#fusca = Carro()
#brasilia = Carro()
#fusca.ano = 1968
#fusca.modelo = "Fusca"
#fusca.cor = "preto"
#brasilia.ano = 1981
#brasilia.modelo = "Brasilia"
#brasilia.cor = "amarela"
#novo_fusca = fusca
#fusca.ano = fusca.ano + 10
#print(fusca.ano)

class Carro:
    def __init__(self,ano,modelo,cor): # "init" = Construtor ,ou seja, ele cria o objeto
        print("Entre na funçao __init__")
        self.ano = ano
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0
        print("Mostre-me o processo ano: ", self.ano)
        print("Mostre-me o processo modelo: ", self.modelo)
        print("Mostre-me o processo cor: ", self.cor)
        print("Mostre-me o processo velocidade: ", self.velocidade)

    def acelera(self,velocidade):
        print("Entrei na funçao acelera")
        #print("Mostre-me a velocidade antes mesmo de ser acrescentada: ", self.velocidade)
        self.velocidade = self.velocidade + velocidade
        #print("Mostre-me a velocidade acrescentada: ", self.velocidade)

    def pare(self):
        print("Entrei na funçao pare")
        #print("Mostre-me a velocidade antes mesmo de parar: ", self.velocidade)
        self.velocidade = 0
        #print("Mostre-me a velocidade docarro parado: ", self.velocidade)

    def imprima(self):
        print("Entrei na funçao imprima")
        print("Carro: ")
        print("   Ano:{}". format(self.ano))
        print("   Modelo:{}". format(self.modelo))
        print("   Cor:{}". format(self.cor))

    def __str__(self):
        print("Entrei na funçao __str__")
        return "Carro: \n Ano:{} \n". format(self.ano)

fusca = Carro(1968,"Fusca","preto")
Carro.imprima(fusca)

Carro.acelera(fusca,30) # ou fusca.acelera(30)
print(fusca.velocidade)

Carro.pare(fusca)
print(fusca.velocidade)

#print(fusca.acelera(20)) # Erro
'''print(fusca.cor)
print(fusca.ano)
print(fusca.modelo)''' # opcional




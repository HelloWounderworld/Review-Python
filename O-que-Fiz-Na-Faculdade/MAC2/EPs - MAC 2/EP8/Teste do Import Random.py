import random

def noIntervalo(lista,inferior,superior):
    contador = 0
    for numero in lista:
        if inferior<numero<superior:
            contador = contador + 1
    return contador
def main():
    numerodeIntervalos = 8
    intervalos = [0]*numerodeIntervalos
    LarguraDoIntervalo = 1.0/numerodeIntervalos
    lista = []
    for j in range(1000):
        x = random.random()
        lista.append(x)
    print(lista)
    for i in range(numerodeIntervalos):
        inferior = i*LarguraDoIntervalo
        superior = inferior + LarguraDoIntervalo
        intervalos[i] = noIntervalo(lista,inferior,superior)
    print(intervalos)
        
main()


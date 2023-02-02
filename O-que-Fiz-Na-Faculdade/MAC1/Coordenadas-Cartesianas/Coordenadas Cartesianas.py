#Cria um programa em Python que receba as coordenadas x, y de um ponto R2 e imprima em qual quadrante o ponto está localizado.
#O primeiro quadrante corresponde à coordenadas x e y positivas, o segundo a x positivo e y negativo, e assim por diante.
while( True ):
    x = float(input("Entre com o valor de x:"))
    y = float(input("Entre com o valor de y:"))

    if ( x > 0 and y > 0 ):
        print("Esta no 1º quadrante")

    elif ( x < 0 and y > 0 ):
        print("Esta no 2º quadrante")

    elif ( x < 0 and y < 0 ):
        print("Esta no 3º quadrante")

    elif ( x > 0 and y < 0 ):
        print("Esta no 4º quadrante")

    elif ( x == 0 and y == 0 ):
        print("Esta no olho do teu cu")

    else:
        print("Esta em alguma das retas cartesianas")
        

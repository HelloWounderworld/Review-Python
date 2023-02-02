# Escreva um programa que receba via teclado os tamanhos de 3 lados de um triângulo, e imprima se o triângulo é retângulo ou não. (Dica: Teorema de Pitágoras).
while ( True ):
    a = float(input("Entre com o valor de a:"))
    b = float(input("Entre com o valor de b:"))
    c = float(input("Entre com o valor de c:"))

    if ( c**2 == b**2 + a**2 ):
        print("E um triangulo retangulo")

    elif ( a**2 == b**2 + c**2 ):
        print("E um triangulo retangulo")

    elif ( b**2 == c**2 + a**2 ):
        print("E um triangulo retangulo")

    else:
        print("Manda um outro numero ai")

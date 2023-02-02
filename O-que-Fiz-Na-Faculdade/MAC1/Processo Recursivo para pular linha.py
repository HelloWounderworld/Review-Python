def nLinhas(n):
    
    if n > 0 and not(n < 0):
        print()
        nLinhas(n-1)        

def Quantaslinhaspulam():
    x = int(input("Entre com um valor inteiro positivo: "))
    print("Inicio")
    nLinhas(x)
    print("Final")
Quantaslinhaspulam()

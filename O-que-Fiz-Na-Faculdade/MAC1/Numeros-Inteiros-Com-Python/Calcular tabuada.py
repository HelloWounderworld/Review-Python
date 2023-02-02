def main(): #Calcular Tabuada de um certo valor n
    n = int(input("Entre com o valor de n:"))
    x = 1
    while x <= 1: # Enquanto o x for enor ou igual ao n
        prod = n * x
        print(n, "x", x, "=", prod) #Se preferir poderia ter colocado diretamente no lugar de prod n * x
        x = x + 1 # Essa linguagem caso queira fazer uma tabuada de n * 1, ... , n * n = n²
main()
            

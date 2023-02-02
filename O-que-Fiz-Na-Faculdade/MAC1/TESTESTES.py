def main():
    sequencia = []
    contador = 0
    n = float(input("Entre com um valor real n: "))
    print("********************")
    while (n > 0):
        sequencia.append(n)
        m = float(input("Entre com um valor real m: "))
        print("********************")
        if (m < n and n != (for x in sequencia)):
            sequencia.append(m)
            n = m
        else:
           print("Os termos da sequencia no momento: {}". format(sequencia))
           print("********************")
           break

    for i in range(len(sequencia)):
                print("Termo e o valor real: {}". format(sequencia[-i]))
                print("********************")
main()
    
        
        

def main():
    sequencia = []
    n = float(input("Entre com um valor real n: "))
    print("********************")
    while (n > 0):
        
        if n not in sequencia:
            sequencia.append(n)
            print("Sequencia apos o termo incluido: {}". format(sequencia))
            m = float(input("Entre com um valor real m: "))
            print("********************")
            
            if(m > 0):
            
                if (m < n and m not in sequencia):
                    sequencia.append(m)
                    k = float(input("Entre com um outro valor real k: "))
                    print("********************")
                    
                    if (k > 0):
                        while(k >= n):
                            k = float(input("Entre com um outro valor real k: "))
                        n = k

                    else:
                        break
                    
                else:
                    print("Os termos da sequencia no momento: {}". format(sequencia))
                    l = float(input("Entre com um outro valor real l: "))
                    print("********************")
                    if (l <= 0):
                        break
                    
                    else:
                        while(l >= n):
                            l = float(input("Entre com um outro valor real l: "))
                            print("********************")
                        n = l
                        
            else:
                break
                
        else:
            n = float(input("Entre com um outro valor real n: "))
            print("Os termos da sequencia no moento: {}". format(sequencia))
            print("********************")
    
    for i in range(len(sequencia)):
                print("Termos na ordem crescente: {}". format(sequencia[-(1+i)]))
                print("********************")
    print("O conjunto da sequencia no final das contas: {}". format(sequencia))
main()
    
        
        

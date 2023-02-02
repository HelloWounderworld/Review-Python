def main():

    n_str=input("Entre com o vlaor de n:")
    n=int(n_str)#Esse processo de "n_str" caso tiver um argumento ou um processo muito complexo e longo, ajudaria a colocar em poucas palavras
    x=1
    while x<=n:
        if x % 2 == 0: #caso for ímpar teria q ser "if x % 2 != 0 
            print(x)
        x=x+1
    print("terminei")
main()

            
        
        
        

from polinomio import Polinomio

def main():
    # crie lista de coeficientes
    coefs = [5, 1, 2, 0, 3]

    # crie um objeto da classe polinomio
    p = Polinomio(coefs) # __init__() 
    print("Polinomio p:", p) # __str__()

    # crie um polinomio que represente a derivada de p
    dp = p.derive()  # derive()
    print("Polinomio dp:", dp)

    # crie um polinomio que represente a derivada de p
    ddp = dp.derive()
    print("Polinomio ddp:", ddp)

    # calcule o valor dos polinômio 
    valores = [0, 1, 3.2]
    for x in valores:
        print("p(%s) = %s" %(x, p(x))) # __call__() 
        print("dp(%s) = %s" %(x, dp(x)))
        print("ddp(%s) = %s" %(x, ddp(x)))


#-------------------------------------------------------------
if __name__ == "__main__":
    main()

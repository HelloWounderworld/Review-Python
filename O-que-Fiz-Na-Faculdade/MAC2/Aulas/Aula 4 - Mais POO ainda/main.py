from polinomio import Polinomio

def main():
    # leia polinomio
    s = input("digite os coefs do polinomio: ")

    lst_str = s.split()

    # crie lista de coeficientes
    coefs = [float(coef_str) for coef_str in lst_str]

    # crie um objeto da classe polinomio
    p = Polinomio(coefs)
    print("Polinomio p:", p)

    # crie um polinomio que represente a derivada de p
    dp = p.derive()
    print("Polinomio dp:", dp)

    # crie um polinomio que represente a derivada de p
    ddp = dp.derive()
    print("Polinomio ddp:", ddp)

    # leia os valores x_0,...,x_{n-1} e calcule os valores
    # dos polinomios
    n = int(input("Digite n: "))
    for i in range(n):
        x = float(input("Digite x%d: "%(i)))
        print("p(%f) = %f" %(x, p(x)))
        print("dp(%f) = %f" %(x, dp(x)))
        print("ddp(%f) = %f" %(x, ddp(x)))
    

if __name__ == "__main__":
    main()

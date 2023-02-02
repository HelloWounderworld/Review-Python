from cientista import Cientista

def main():
    n_questoes = int(input("Digite o no de questões: "))
    limiar     = int(input("Digite o limiar para chute: "))
    t          = int(input("Digite o no de experimentos: "))
    adilson = Cientista(n_questoes, limiar, t)
    print("Probabilidade da/do estudante estar chutando", adilson.mean())

#--------------------------------------------------
if __name__ == "__main__":
    main()

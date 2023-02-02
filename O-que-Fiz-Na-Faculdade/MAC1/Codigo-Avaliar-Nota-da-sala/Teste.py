def main():
    n = int(input("Numero de Alunos da Turma: "))
    Aluno = 1
    while (Aluno <= n):
        print("Aluno: ", Aluno)
        P1 = int(input("Nota da Prova 1: "))
        P2 = int(input("Nota da Prova 2: "))
        if (P1 != -1 and P2 != -1):
            P = (P1 + P2)//2
            Psub = -1
            print("Nota da Prova Substitutiva: ", Psub)
        elif ( P1 == -1 or P2 == -1):
            Psub = int(input("Nota da Prova Substitutiva: "))
            P = (Psub + max(P1,P2))//2
        else:
            Psub = int(input("Nota da Prova Substitutiva: "))
            P = Psub // 2
        EP1 = int(input("Nota do Exercicio de Programaçao 1: "))
        EP2 = int(input("Nota do Exercicio de Programaçao 2: "))
        EP3 = int(input("Nota do Exercicio de Programaçao 3: "))
        if (EP1 != -1 and EP2 != -1 and EP3 != -1):
            EP = (4*EP1 + 5*EP2 + 11*EP3)//20
        elif (EP1 == -1):
            if(EP2 != -1 and EP3 != -1):
                EP = (5*EP2 + 11*EP3)//20
            elif(EP2 == -1 and EP3 != -1):
                EP = (11*EP3)//20
            elif(EP2 != -1 and EP3 == -1):
                EP = (5*EP2)//20
            else:
                EP = 0
        elif (EP2 == -1):
            if(EP1 != -1 and EP3 != -1):
                EP = (4*EP1 + 11*EP3)//20
            elif(EP1 == -1 and EP3 != -1):
                EP = (11*EP3)//20
            elif(EP1 != -1 and EP3 == -1):
                EP = (4*EP1)//20
            else:
                EP = 0
        else:
            if(EP1 != -1 and EP2 != -1):
                EP = (4*EP1 + 5*EP2)//20
            elif(EP1 == -1 and EP2 != -1):
                EP = (5*EP2)//20
            elif(EP1 != -1 and EP2 == -1):
                EP = (4*EP1)//20
            else:
                EP = 0
        Frequencia = int(input("Frequencia do Aluno: "))
        MF = (3*P + EP)//4
        print("Media das Provas: ", P)
        print("Media das Notas dos Exercicios de Programaçao: ", EP)
        print("Media Final: ", MF)
        print("Voce esta Aprovado ! Good Job !")
        Aluno = Aluno + 1
main()
                

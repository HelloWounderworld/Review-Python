def main():
    n = int(input("Numero de Alunos da Turma: "))
    Aluno = 1
    Aprovado = 0

    while(Aluno <= n):
        print("Aluno: ", Aluno)
        Frequencia = int(input("Frequencia do Aluno: "))
        P1 = int(input("Nota da Prova 1: "))
        P2 = int(input("Nota da Prova 2: "))
        Psub = int(input("Nota da Prova Substitutiva: "))

        if(P1 != -1 and P2 != -1 and Psub != -1):
            P = (P1 + P2)/2
            if(P < 50):
                if(Psub >= P1 and Psub < P2):
                    P = (Psub + P2)/2
                elif(Psub >= P2 and Psub < P1):
                    P = (Psub + P1)/2
                elif(Psub >= P1 and Psub >= P2):
                    if(P1 <= P2):
                        P = (Psub + P2)/2
                    else:
                        P = (Psub + P1)/2
                else:
                    P = (P1 + P2)/2
            else:
                return P
        elif(P1 != -1 and P2 != -1 and Psub == -1):
            P = (P1 + P2)/2
        elif(P1 != -1 and P2 == -1):
            if(Psub != -1):
                P = (Psub + P1)/2
            else:
                P = P1 / 2
        elif(P2 != -1 and P1 == -1):
            if(Psub != -1):
                P = (Psub + P2)/2
            else:
                P = P2 / 2
        else:
            if(Psub != -1):
                P = Psub / 2
            else:
                P = 0

        EP1 = int(input("Nota do Exercicio de Programaçao 1: "))
        EP2 = int(input("Nota do Exercicio de Programaçao 2: "))
        EP3 = int(input("Nota do Exercicio de Programaçao 3: "))

        if (EP1 != -1 and EP2 != -1 and EP3 != -1):
            EP = (4*EP1 + 5*EP2 + 11*EP3)/20
        elif (EP1 == -1):
            if(EP2 != -1 and EP3 != -1):
                EP = (5*EP2 + 11*EP3)/20
            elif(EP2 == -1 and EP3 != -1):
                EP = (11*EP3)/20
            elif(EP2 != -1 and EP3 == -1):
                EP = (5*EP2)/20
            else:
                EP = 0
        elif (EP2 == -1):
            if(EP1 != -1 and EP3 != -1):
                EP = (4*EP1 + 11*EP3)/20
            elif(EP1 == -1 and EP3 != -1):
                EP = (11*EP3)/20
            elif(EP1 != -1 and EP3 == -1):
                EP = (4*EP1)/20
            else:
                EP = 0
        elif (EP3 == -1):
            if(EP2 != -1 and EP1 != -1):
                EP = (5*EP2 + 4*EP1)/20
            elif(EP2 == -1 and EP1 != -1):
                EP = (4*EP1)/20
            elif(EP2 != -1 and EP1 == -1):
                EP = (5*EP2)/20
            else:
                EP = 0
        else:
            EP = 0

        Pcerto = (P - int(P)) * 10
        if (Pcerto >= 5):
            Pcorri = int(P) + 1
        else:
            Pcorri = int(P)
        
        EPcerto = (EP - int(EP)) * 10
        if(EPcerto >= 5):
            EPcorri = int(EP) + 1
        else:
            EPcorri = int(EP)

        if(Frequencia >= 70):
            print("Media das Provas: ", Pcorri)
            print("Media das Notas dos Exercicios de Programaçao: ", EPcorri)

            if(Pcorri >= 50 and EPcorri >= 50):
                MF = (3*Pcorri + EPcorri)/4
                MFcerto = (MF - int(MF)) * 10
                if(MFcerto >= 5):
                    MFcorri = int(MF) + 1
                else:
                    MFcorri = int(MF)
                print("Media Final: ", MFcorri)
                print("Voce esta Aprovado !")
                Aprovado = Aprovado + 1
            else:
                if(Pcorri >= EPcorri):
                    MF = EPcorri
                    if(30 <= EPcorri and EPcorri < 50):
                        print("Media final: ", MF)
                        Prec = int(input("Nota da Prova de Recuperaçao: "))
                        MF = (MF + Prec)/2
                        MFcerto = (MF - int(MF)) * 10
                        if(MFcerto >= 5):
                            MFcorri = int(MF) + 1
                        else:
                            MFcorri = int(MF)
                        print("Media Final da Recuperaçao: ", MFcorri)
                        if (MFcorri >= 50):
                            print("Voce esta Aprovado !")
                            Aprovado = Aprovado + 1
                        else:
                            print("Voce foi Reprovado por Nota ! S2")
                    else:
                        print("Voce foi Reprovado por Nota ! S2")
                else:
                    MF = Pcorri
                    if (30 <= Pcorri and Pcorri < 50):
                        print("Media final: ", MF)
                        Prec = int(input("Nota da Prova de Recuperaçao: "))
                        MF = (MF + Prec)/2
                        MFcerto = (MF - int(MF)) * 10
                        if(MFcerto >= 5):
                            MFcorri = int(MF) + 1
                        else:
                            MFcorri = int(MF)
                        print("Media Final da Recuperaçao: ", MFcorri)
                        if (MFcorri >= 50):
                            print("Voce esta Aprovado !")
                            Aprovado = Aprovado + 1
                        else:
                            print("Voce foi Reprovado por Nota ! S2")
                    else:
                        print("Media Final: ", MF)
                        print("Voce foi Reprovado por Nota ! S2")
        else:
            print("Media das Provas: ", Pcorri)
            print("Media das Notas dos Exercicios de Programaçao: ", EPcorri)
            if(Pcorri >= 50 and EPcorri >= 50):
                MF = (3*Pcorri + EPcorri)/4
                MFcerto = (MF - int(MF)) * 10
                if(MFcerto >= 5):
                    MFcorri = int(MF) + 1
                else:
                    MFcorri = int(MF)
                print("Media Final: ", MFcorri)
                print("Voce foi Reprovado por Falta !")
            else:
                if(Pcorri >= EPcorri):
                    MF = EPcorri
                    if(30 <= EPcorri and EPcorri < 50):
                        print("Media Final: ", MF)
                        Prec = int(input("Nota da Prova de Recuperaçao: "))
                        MF = (MF + Prec)/2
                        MFcerto = (MF - int(MF)) * 10
                        if(MFcerto >= 5):
                            MFcorri = int(MF) + 1
                        else:
                            MFcorri = int(MF)
                        print("Media Final da Recuperaçao: ", MFcorri)
                        if (MFcorri >= 50):
                            print("Voce foi Reprovado por Falta !")
                        else:
                            print("Voce foi Reprovado por Nota e Falta ! S2")
                    else:
                        print("Media Final: ", MF)
                        print("Voce foi Reprovado por Nota e Falta ! S2")
                else:
                    MF = Pcorri
                    if(30 <= Pcorri and Pcorri < 50):
                        print("Media Final: ", MF)
                        Prec = int(input("Nota da Prova de Recuperaçao: "))
                        MF = (MF + Prec)/2
                        MFcerto = (MF - int(MF)) * 10
                        if(MFcerto >= 5):
                            MFcorri = int(MF) + 1
                        else:
                            MFcorri = int(MF)
                        print("Media Final da Recuperaçao: ", MFcorri)
                        if (MFcorri >= 50):
                            print("Voce foi Reprovado por Falta !")
                        else:
                            print("Voce foi Reprovado por Nota e Falta ! S2")
                    else:
                        print("Media Final: ", MF)
                        print("Voce foi Reprovado por Nota e Falta ! S2")
        print("**********************************************************")
        Aluno = Aluno + 1
        
        
    print("Total de Alunos Aprovaos: ", Aprovado)
    print("Total de Alunos Reprovados: ", n - Aprovado)
main()









                
            
            

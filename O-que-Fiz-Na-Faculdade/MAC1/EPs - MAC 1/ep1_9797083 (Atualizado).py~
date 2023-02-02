def main():
    n = int(input("Numero de Alunos da Turma: "))
    Aluno = 1
    Aprovado = 0
    
    while (Aluno <= n):
        print("Aluno: ", Aluno)
        P1 = int(input("Nota da Prova 1: "))
        P2 = int(input("Nota da Prova 2: "))
#Na estrutura abaixo coloquei uma condiçao, em caso de o professor colocar alguma nota que nao esteja dentro do intervalo de [0,100] e -1,
#para que o programa pergunte novamente as notas (**)
        if((-1 <= P1 and P1 <= 100) and (-1 <= P2 and P2 <= 100)):
            if (P1 != -1 and P2 != -1):
                P = (P1 + P2)//2
                Psub = -1
                print("Nota da Prova Substitutiva: ", Psub)
            elif ( P1 != -1 and P2 == -1):
                Psub = int(input("Nota da Prova Substitutiva: "))
                if (-1 <= Psub and Psub <= 100):
                    P = (Psub + max(P1,P2))//2
                else:
                    Psub = int(input("Errar e humano - Nota da Prova Substitutiva: "))
                    P = (Psub + max(P1,P2))//2
            elif ( P1 == -1 and P2 != -1):
                Psub = int(input("Nota da Prova Substitutiva: "))
                if (-1 <= Psub and Psub <= 100):
                    P = (Psub + max(P1,P2))//2
                else:
                    Psub = int(input("Errar e humano - Nota da Prova Substitutiva: "))
                    P = (Psub + max(P1,P2))//2
            else:
                Psub = int(input("Nota da Prova Substitutiva: "))
                if (-1 <= Psub and Psub <= 100):
                    P = Psub//2
                else:
                    Psub = int(input("Errar e humano - Nota da Prova Substitutiva: "))
                    P = Psub//2
        else:
            P1 = int(input("Errar e humano - Nota da Prova 1: "))
            P2 = int(input("Errar e humano - Nota da Prova 2: "))
            if((-1 <= P1 and P1 <= 100) and (-1 <= P2 and P2 <= 100)):
                if (P1 != -1 and P2 != -1):
                    P = (P1 + P2)//2
                    Psub = -1
                    print("Nota da Prova Substitutiva: ", Psub)
                elif ( P1 != -1 and P2 == -1):
                    Psub = int(input("Nota da Prova Substitutiva: "))
                    if (-1 <= Psub and Psub <= 100):
                        P = (Psub + max(P1,P2))//2
                    else:
                        Psub = int(input("Errar e humano - Nota da Prova Substitutiva: "))
                        P = (Psub + max(P1,P2))//2
                elif ( P1 == -1 and P2 != -1):
                    Psub = int(input("Nota da Prova Substitutiva: "))
                    if (-1 <= Psub and Psub <= 100):
                        P = (Psub + max(P1,P2))//2
                    else:
                        Psub = int(input("Errar e humano - Nota da Prova Substitutiva: "))
                        P = (Psub + max(P1,P2))//2
                else:
                    Psub = int(input("Nota da Prova Substitutiva: "))
                    if (-1 <= Psub and Psub <= 100):
                        P = Psub//2
                    else:
                        Psub = int(input("Errar e humano - Nota da Prova Substitutiva: "))
                        P = Psub//2
                    
        EP1 = int(input("Nota do Exercicio de Programaçao 1: "))
        EP2 = int(input("Nota do Exercicio de Programaçao 2: "))
        EP3 = int(input("Nota do Exercicio de Programaçao 3: "))
#Analogo ao caso (**)
        if((-1 <= EP1 and EP1 <= 100) and (-1 <= EP2 and EP2 <= 100) and (-1 <= EP3 and EP3 <= 100)):
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
        else:
            EP1 = int(input("Errar e humano - Nota do Exercicio de Programaçao 1: "))
            EP2 = int(input("Errar e humano - Nota do Exercicio de Programaçao 2: "))
            EP3 = int(input("Errar e humano - Nota do Exercicio de Programaçao 3: "))
            if((-1 <= EP1 and EP1 <= 100) and (-1 <= EP2 and EP2 <= 100) and (-1 <= EP3 and EP3 <= 100)):
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
#Analogo ao caso (**)
        if (0 <= Frequencia and Frequencia <= 100):
            if (Frequencia >= 70):
                if(P >= 50 and EP >= 50):
                    MF = (3*P + EP)//4
                    print("Media das Provas: ", P)
                    print("Media das Notas dos Exercicios de Programaçao: ", EP)
                    print("Media Final: ", MF)
                    print("Voce esta Aprovado !")
                    Aprovado = Aprovado + 1
                else:
                    MF = min(P,EP)
                    print("Media das Provas: ", P)
                    print("Media das Notas dos Exercicios de Programaçao: ", EP)
                    if(MF >= 50):
                        print("Media Final: ", MF)
                        print("Voce esta Aprovado !")
                        Aprovado = Aprovado + 1
                    elif(30 <= MF and MF < 50):
                        Prec = int(input("Nota da Prova de Recuperaçao: "))
                        if (0 <= Prec and Prec <= 100):
                            MF = (MF + Prec)//2
                            print("Media Final: ", MF)
                            if (MF >= 50):
                                print("Voce esta Aprovado !")
                                Aprovado = Aprovado + 1
                            else:
                                print("Voce foi Reprovado por Nota ! S2")
                        else:
                            Prec = int(input("Errar e humano - Nota da Prova de Recuperaçao: "))
                            if (0 <= Prec and Prec <= 100):
                                MF = (MF + Prec)//2
                                print("Media Final: ", MF)
                                if (MF >= 50):
                                    print("Voce esta Aprovado !")
                                    Aprovado = Aprovado + 1
                                else:
                                    print("Voce foi Reprovado por Nota ! S2")
                    else:
                        print("Media Final: ", MF)
                        print("Voce foi Reprovado por Nota ! S2")
            elif (Frequencia < 70):
                if(P >= 50 and EP >= 50):
                    MF = (3*P + EP)//4
                    print("Media das Provas: ", P)
                    print("Media das Notas dos Exercicios de Programaçao: ", EP)
                    print("Media Final: ", MF)
                    print("Voce foi Reprovado por Falta !")
                elif(P < 50 or EP < 50):
                    if(P < 50 and EP >= 50):
                        MF = min(P,EP)
                        print("Media das Provas: ", P)
                        print("Media das Notas dos Exercicios de Programaçao: ", EP)
                        print("Media Final: ", MF)
                        if(MF >= 50):
                            print("Voce foi Reprovado por Falta !")
                        else:
                            print("Voce foi Reprovado por Falta e Nota !")
                    elif(P >= 50 and EP < 50):
                        MF = min(P,EP)
                        print("Media das Provas: ", P)
                        print("Media das Notas dos Exercicios de Programaçao: ", EP)
                        print("Media Final: ", MF)
                        if(MF >= 50):
                            print("Voce foi Reprovado por Falta !")
                        else:
                            print("Voce foi Reprovado por Falta e Nota !")
                    else:
                        print("Voce foi Reprovado por Nota e Falta !")
        else:
            Frequencia = int(input("Errar e humano - Frequencia do Aluno: "))
            if (0 <= Frequencia and Frequencia <= 100):
                if (Frequencia >= 70):
                    if(P >= 50 and EP >= 50):
                        MF = (3*P + EP)//4
                        print("Media das Provas: ", P)
                        print("Media das Notas dos Exercicios de Programaçao: ", EP)
                        print("Media Final: ", MF)
                        print("Voce esta Aprovado !")
                        Aprovado = Aprovado + 1
                    else:
                        MF = min(P,EP)
                        print("Media das Provas: ", P)
                        print("Media das Notas dos Exercicios de Programaçao: ", EP)
                        if(MF >= 50):
                            print("Media Final: ", MF)
                            print("Voce esta Aprovado !")
                            Aprovado = Aprovado + 1
                        elif(30 <= MF and MF < 50):
                            Prec = int(input("Nota da Prova de Recuperaçao: "))
                            if (0 <= Prec and Prec <= 100):
                                MF = (MF + Prec)//2
                                print("Media Final: ", MF)
                                if (MF >= 50):
                                    print("Voce esta Aprovado !")
                                    Aprovado = Aprovado + 1
                                else:
                                    print("Voce foi Reprovado por Nota ! S2")
                            else:
                                Prec = int(input("Errar e humano - Nota da Prova de Recuperaçao: "))
                                if (0 <= Prec and Prec <= 100):
                                    MF = (MF + Prec)//2
                                    print("Media Final: ", MF)
                                    if (MF >= 50):
                                        print("Voce esta Aprovado !")
                                        Aprovado = Aprovado + 1
                                    else:
                                        print("Voce foi Reprovado por Nota ! S2")    
                        else:
                            print("Media Final: ", MF)
                            print("Voce foi Reprovado por Nota ! S2")
                elif (Frequencia < 70):
                    if(P >= 50 and EP >= 50):
                        MF = (3*P + EP)//4
                        print("Media das Provas: ", P)
                        print("Media das Notas dos Exercicios de Programaçao: ", EP)
                        print("Media Final: ", MF)
                        print("Voce foi Reprovado por Falta !")
                    elif(P < 50 or EP < 50):
                        if(P < 50 and EP >= 50):
                            MF = min(P,EP)
                            print("Media das Provas: ", P)
                            print("Media das Notas dos Exercicios de Programaçao: ", EP)
                            print("Media Final: ", MF)
                            if(MF >= 50):
                                print("Voce foi Reprovado por Falta !")
                            else:
                                print("Voce foi Reprovado por Falta e Nota !")
                        elif(P >= 50 and EP < 50):
                            MF = min(P,EP)
                            print("Media das Provas: ", P)
                            print("Media das Notas dos Exercicios de Programaçao: ", EP)
                            print("Media Final: ", MF)
                            if(MF >= 50):
                                print("Voce foi Reprovado por Falta !")
                            else:
                                print("Voce foi Reprovado por Falta e Nota !")
                        else:
                            print("Voce foi Reprovado por Nota e Falta !")
                    
        Aluno = Aluno + 1      
    print("Total de Alunos Aprovaos: ", Aprovado)
    print("Total de Alunos Reprovados: ", n - Aprovado)
          
main()
        
        
                    
                    
                
           
                    
                    
                    
                    
                    
                
            
        
        
            

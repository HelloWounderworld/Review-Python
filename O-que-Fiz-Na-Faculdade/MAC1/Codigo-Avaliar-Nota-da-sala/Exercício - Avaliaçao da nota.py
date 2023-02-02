#Escreva um programa em Python que pergunte quatro notas de um aluno, e depois imprima a média, 
#e se ele foi aprovado (média >= 5), reprovado (media < 3) ou em recuperação (5 > media >= 3).
while( True ):
    N_1 = float(input("Entre com o valor de N1:"))
    N_2 = float(input("Entre com o valor de N2:"))
    N_3 = float(input("Entre com o valor de N3:"))
    N_4 = float(input("Entre com o valor de N4:"))

    Media = (N_1+N_2+N_3+N_4)/4

    if ( Media >= 5 ):
        print("Se deu bem !\nSua nota e:", Media)

    elif ( 5 > Media >= 3 ):
        print("Sobreviveu cuzao, boa sorte!\nSua nota e:", Media)

    else:
        print("Se fudeu !\nSua nota e:", Media)
    


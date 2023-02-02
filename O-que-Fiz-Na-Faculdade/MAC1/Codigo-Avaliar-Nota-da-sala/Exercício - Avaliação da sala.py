def main():
    p1=float(input("Entre com a nota p1:")) #eu poderia ter feito "p1_str=input("Entre com a nota p1")
    p2=float(input("Entre com a nota p2:"))
    EP1=float(input("Entre com a nota EP1:"))
    EP2=float(input("Entre com a nota EP2:"))
    EP3=float(input("Entre com a nota EP3:"))
    MP=(p1+p2)/2
    MEP=(4*EP1+5*EP2+11*EP3)/20
    if MP>=5 and MEP>=5:
        MF=(3*MP+MEP)/4
    else:
        if MP < MEP:
            MF=MP
        else:
            MF=MEP
    if MF>=5:
        print("APROVADO")
    else:
        print("Reprovado ou em recuperaçao")
main()

#def main():
    #x=float(input("Entre com o valor de x:")
    #print("O valor de sqrt(",x,")=",math.sqrt(x))


#Escrever um programa que representa uma experessao fatorial ( Defino n!=n*(n-1)!) e 1!=1)

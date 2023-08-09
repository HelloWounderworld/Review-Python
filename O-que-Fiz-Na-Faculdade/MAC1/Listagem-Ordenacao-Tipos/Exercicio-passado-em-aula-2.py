#a-) Dado uma lista x com n numeros reais, e um certo indice k, escreva na funçao em python que determina o indice do menor elemento x[k],x[k+1],...,x[n-1]
#b-) Uso obrigatoriamente a funçao anterior para colocar uma lista em ordem crescente
# x = [10,5,1,6,7,2]
def menor(x,k):
    im = k
    for i in range(k+1,len(x)):
        if (x[i] < x[k]):
            im = i
    return im

def crescente(x):
    y = x[:]
    for i in range(len(y)-1):
        indice = menor(y,i)
        aux = y[i]
        y[i] = y[indice]
        y[indice] = aux
    return y

def main():
    x = [10,5,1,6,7,2]
    ordena = crescente(x)
    print(ordena)
main()

#Simula isso no papel


            
    

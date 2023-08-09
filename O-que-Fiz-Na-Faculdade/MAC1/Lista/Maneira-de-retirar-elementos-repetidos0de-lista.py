def pertence(item,lista):# forma alternativa        #def pertence(item,lista):
    for x in lista: #for i in range(len(lista))       #return item in lista
        if (x == item): #if lista[i] == item:
            return True #return True

    return False

def remove_duplicatas(lista):
    nova = []
    for x in lista:
        if not pertence(x,nova):
            nova.append(x)
    return nova

def main():
    x = [1,2,2,-3,4,-3]
    y = remove_duplicatas(x)
    print(y)
main()

    

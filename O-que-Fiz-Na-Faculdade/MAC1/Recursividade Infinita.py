#def RecursivoInfinito():
    #RecursivoInfinito()
def oddnumber(x):
    y = x%2
    if y != 0:
        print(x)
        oddnumber(x+1)
    else:
        oddnumber(x+1)

    

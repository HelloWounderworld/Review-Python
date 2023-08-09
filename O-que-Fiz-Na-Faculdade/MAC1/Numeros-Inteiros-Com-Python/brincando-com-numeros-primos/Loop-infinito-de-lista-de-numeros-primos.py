def fatorial(n):
    y = n - 1
    prod = 1
    
    while y > 0 :
        prod = prod * y
        y = y - 1
    return prod
def main():
    p = int(input("Digite o número: "))
    while p>0:
        z = fatorial(p)
        w = z+1
        if w%p == 0 :
            print("Numero primo: ", x)
            p = p+1
        else:
            p = p+1
main()
        
    

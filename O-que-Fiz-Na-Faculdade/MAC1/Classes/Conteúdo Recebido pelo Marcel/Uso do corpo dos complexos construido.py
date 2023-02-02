from Complexo import complexo
def main():
    a = Complexo(-2,3)
    b = Complexo(2,-3)
    print(a+b)
    print(a == b)
    print(a.real)
    print(a.imaginario)
    a.real = 5
    a.imaginario = 10
    print(a)
    x = Complexo(-2,3)
    print(x.real + 5)
    
main()

from complexo import Complexo

def main():
    z1 = Complexo()   # __init__()
    print("z1 =", z1)
    z2 = Complexo(3)  #
    print("z2 =", z2)
    z3 = Complexo(0.5, 2)
    print("z3 =", z3)
    z = z2 + z3 # __add__(), __mul__
    print("z =", z)    # __str__()


#-----------------------------------------------------------
if __name__ == "__main__":
    main()

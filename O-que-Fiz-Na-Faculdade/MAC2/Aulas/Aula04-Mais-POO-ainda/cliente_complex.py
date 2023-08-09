def main():
    z1 = complex()   # __init__()
    print("z1 =", z1)
    z2 = complex(3)  #
    print("z2 =", z2)
    z3 = complex(0.5, 2)
    print("z3 =", z3)
    z = z2 + z3 # __add__(), __mul__
    print("z =", z)    # __str__()


#-----------------------------------------------------------
if __name__ == "__main__":
    main()

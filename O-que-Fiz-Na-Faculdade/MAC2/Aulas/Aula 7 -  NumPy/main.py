from array2d import Array2D

def main():

    a = Array2D( (2,3), -1)
    print(a)
    print("type(a)=", type(a))
    print("a.shape=",a.shape)
    print("a.size=", a.size)
    print("a.ndim=", a.ndim)
    print("a.dtype=", a.dtype)
    b = Array2D( (2,3), 4)
    c = a+b
    print(c)
    d = a*2
    print(d)

if __name__ == "__main__":
    main()
    

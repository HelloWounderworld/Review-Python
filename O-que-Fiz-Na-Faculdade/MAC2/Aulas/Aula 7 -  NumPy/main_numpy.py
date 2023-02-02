import numpy as np

def main():

    a = np.full( (2,3), -1)
    print(a)
    print("type a=",  type(a))
    print("a.shape=", a.shape)
    print("a.size=",  a.size)
    print("a.ndim=",  a.ndim)
    print("a.dtype=", a.dtype)
    b = np.full( (2,3), 4)
    c = a+b
    print(c)
    d = a*2
    print(d)

if __name__ == "__main__":
    main()
    

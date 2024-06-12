class A:
    def m(self):
        print("m de A")

class B(A):
    def m(self):
        print("m de B")

class C(A):
    def m(self):
        print("m de C")

class D(B, C):
    pass

d = D()
d.m()

print(D.mro())
# Saída: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
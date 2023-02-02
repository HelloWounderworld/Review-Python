class complexo:
    '''(complexo,float,float) -> None
    '''
    def __init__(self,preal=0,pimag=0):
        self.preal = preal
        self.pimag = pimag

    def __str__(self):
        return str(self.preal)+"+"+str(self.pimag)+"i"

    def preal(self):
        return self.preal

    def pimag(self):
        return self.pimag
    
    def __add__(self,other):
        if (self.preal + other.preal != 0) and (self.pimag+other.pimag !=0):
            return complexo(self.preal + other.preal,self.pimag+other.pimag)
        else:
            if (self.preal + other.preal != 0) and (self.pimag+other.pimag ==0):
                return complexo(self.preal+other.preal)
            else:
                return complexo(0,self.pimag+other.pimag)

def main():
    z1 = complexo()
    z2 = complexo(3)
    z3 = complexo(0.5,2)
    z = z1+z2+z3
    print(z)
main()
    

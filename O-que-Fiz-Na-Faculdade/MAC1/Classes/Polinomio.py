class polinomio:

    def __init__(self,coefs = []):
        self.coefs = coefs

    def __str__(self):
        '''(polinomio) - > str
        '''
        s = str()
        g = len(self.coefs)
        if g == -1:
            s += '0'
        for i in range(g):
            if i == 0:
                s +=  '%.2f x**%d' %(self.coefs[i], i)
            else:
                s = s + '+'+'%.2f x**%d' %(self.coefs[i], i)
        return s

    def grau(self):
        '''(polinomio) ->
        '''
        return len(self.coefs) - 1

    

    def derive(self):
        '''(polinomio) - > polinomio
        '''
        g = self.grau()
        if g <= 0:
            return polinomio([])
        x = []
        for i in range(len(self.coefs)):
            x.append(self.coefs[i]*i)
        del(x[0])
        return polinomio(x)

def main():
    p = polinomio([5,1,2,0,3])
    print("Polinomio:{} \nGrau:{}". format(p,p.grau()))
    dp = p.derive()
    print(dp)
    valores = [0,1,2,0.5]
    for i in valores:
        y = p(i)
        dy = dp(x)
        print(y,dy)
main()

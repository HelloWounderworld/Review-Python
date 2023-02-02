class Point2D:
    def __init__(self,pos = []):
        self.pos  = pos
    
    def __str__(self):
        if len(self.pos) == 0:
            self.pos = [0,0]
            return str(tuple(self.pos))
        return str(tuple(self.pos))
    
    def media(self):
        soma  = 0
        total = 0
        for i in self.pos:
            total = total + i
            soma = soma + 1
        average = total/soma
        return average
    
    def __add__(self,other):
        x = []
        for i in range(len(self.pos)):
            x.append(self.pos[i]+other.pos[i])
        soma = Point2D(x)
        return soma
    
def main():
    pos = [1, -1]
    p0 = Point2D(pos)
    pos[0] = 2
    print("p0.pos =", p0.pos)
    print("p0 =", p0)
    p1 = Point2D()
    print("p1 =", p1)
    p2 = Point2D([3, 2])
    print("p2 =", p2)
    print("p2.media() =", p2.media())
    p3 = p1 + p2
    print("p3 =", p3)
main()

'''
Questão 1. (Pilhas)
Suponha que realizamos uma sequência mesclada* com as operações push() e pop() 
em uma pilha. 
As operações push() inseriram na pilha os inteiros de 0 até 6, nessa ordem. 
Após cada operação pop() o número removido da pilha foi impresso. 
Circule as letras dos itens que correspodem a possíveis permutações (ordens) em
que os números foram impressos.

     0  1  2  3  4  5  6
     2  4  6  5  3  0  1
     2  5  6  3  4  1  0
     2  1  4  3  5  6  0
     4  3  5  1  6  2  0
     1  0  4  6  5  3  2

Solução: (a), (d) e (f)

Questão 2. (Classes e objetos)
Considere a função a seguir onde Point2D representa um ponto no plano.
Escreva a classe Point2D para que a função main() produza a saída a seguir:

p0.pos = [1, -1]
p0 = (1,-1)
p1 = (0,0)
p2 = (3,2)
p2.media() = 2.5
p3 = (3,2)

class Point2D:
    def __init__(self, pos=[0,0]):
        self.pos = pos[:]

    def __str__(self):
        return "(%s,%s)"%(self.pos[0], self.pos[1])

    def __add__(self, other):
        x = self.pos[0]+other.pos[0]
        y = self.pos[1]+other.pos[1]
        return Point2D([x, y])

    def media(self):
        return (self.pos[0]+self.pos[1])/2
'''


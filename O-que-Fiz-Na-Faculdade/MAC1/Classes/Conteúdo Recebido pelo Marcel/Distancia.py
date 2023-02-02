class point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x)**2+(self.y)**2)**0.5

p = point(3,4)
print(p.distanceFromOrigin())

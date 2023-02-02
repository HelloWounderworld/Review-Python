def findCenter(box):
    p = Ponto()
    p.x = box.corner.x + box.width/2.0
    p.y = box.corner.y + box.heigth/2.0
    return p

def mostrarPonto(p):
    return print('('+str(p.x)+','+str(p.y)+')')

def mesmoPonto(p1,p2):
    return (p1.x == p2.x) and (p1.y == p2.y)
    
class Ponto:
    pass

class Rectangle:
    pass

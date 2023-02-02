import turtle

CAMINHO = 'C'
TENTOU  = '.'
PAREDE  = '+'
BECO    = '-'

class Labirinto:
    
    def __init__(self, nome_arquivo):
        '''(Labirinto, str) -> None

        Cria a representação de um labirinto dado através
        de um arquivo.

        ATENÇÃO: O formato de entrada do arquivo é bem 
            restrito. Espera-se que a lista lab criada seja retangular.
            Qualquer caractere a mais ou a menos em uma linha pode
            fazer o programa explodir.
        '''
        self.lab = []
        lab_arq = open(nome_arquivo,'r')
        no_lin = 0
        no_col = 0
        for linha in lab_arq:
            linha_lab = []
            col = 0
            for ch in linha[:-1]:
                linha_lab.append(ch)
                if ch == 'I':
                    self.lin_ini = no_lin
                    self.col_ini = col
                col = col + 1
            no_lin += 1
            self.lab.append(linha_lab)
            no_col = max(no_col, col)
        lab_arq.close()
        
        self.no_lin = no_lin
        self.no_col = no_col
        self.xTranslate = -no_col/2
        self.yTranslate =  no_lin/2
        self.t = turtle.Turtle(shape='turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(no_col-1)/2-.5,-(no_lin-1)/2-.5,(no_col-1)/2+.5,(no_lin-1)/2+.5)
        
    #--------------------------------------------------------------
    def desenhe_lab(self):
        t  = self.t
        wn = self.wn
        t.speed(10)
        wn.tracer(0)
        # print(self.no_lin, self.no_col)
        for y in range(self.no_lin):
            for x in range(self.no_col):
                if self.lab[y][x] == PAREDE:
                    self.drawCenteredBox(x+self.xTranslate,-y+self.yTranslate,'tan')
                    t.color('black','blue')
        t.color('black')
        t.fillcolor('blue')
        self.moveTurtle(self.col_ini, self.lin_ini)
        wn.update()
        wn.tracer(1)
        
    #---------------------------------------------------------------                
    def drawCenteredBox(self, x, y, color):
        wn = self.wn
        t  = self.t
        wn.tracer(0)
        t.up()
        t.goto(x-.5,y-.5)
        t.color('black',color)
        t.setheading(90)
        t.down()
        t.begin_fill()
        for i in range(4):
            t.forward(1)
            t.right(90)
        t.end_fill()
        # wn.update()
        # wn.tracer(1)

    #----------------------------------------------------------------        
    def moveTurtle(self, x, y):
        t = self.t
        t.up()
        t.setheading(t.towards(x+self.xTranslate,-y+self.yTranslate))
        t.goto(x+self.xTranslate,-y+self.yTranslate)

    #----------------------------------------------------------------    
    def dropBreadcrumb(self,color):
        self.t.dot(20, color)

    #----------------------------------------------------------------    
    def atualize_posicao(self, lin, col, val=None):
        if val:
            self.lab[lin][col] = val
            self.moveTurtle(col, lin)

        if val ==   CAMINHO:
            color = 'green'
        elif val == PAREDE:
            color = 'red'
        elif val == TENTOU:
            color = 'black'
        elif val == BECO:
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)

    #-----------------------------------------------------                 
    def encontrou_saida(self, lin, col):
         return (lin == 0 or
                 lin == self.no_lin-1 or
                 col == 0 or
                 col == self.no_col-1 )

    #----------------------------------------------------- 
    def __getitem__(self, ind):
         return self.lab[ind]
         

    #----------------------------------------------------------    
    def exitonclick(self):
        '''(Console) -> None

        Recebe uma referência `self` e a um objeto Console e
        fecha a janela assim que seja feito um click sobre ela.
        '''
        print("\nClick na janela da animação para fechá-la.")
        self.wn.exitonclick()
     

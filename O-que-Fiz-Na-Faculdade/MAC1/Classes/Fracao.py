def mdc(n,m):
    '''Sempre que eu quiser usar alguma outra funcao sem que esteja na forma da estrutura das definicoes que compoe o class, devo colocar
    fora de class e para cima dela para que ao compilar o programa reconheça qual e a funcao que este sendo usado dentro do class, ou
    pode-se colocar tbm a funcao dentro do class, desde que esteja antes das outrass definicoes de class que vc pretente aplicar a funcao
    '''
    while n%m != 0:
        n3 = m
        m = n%m
        n = n3
    if m < 0:
        return (-1)*m
    else:
        return m

def divisao(self):
    num = self.den
    den = self.num
    return Fraction(num,den)

class Fraction:
    
    '''class e uma ferramenta muito util para poder criar uma estrutura de representacao de obejtos. No caso, os exemplos seriam, estrutura axiomatica
    dos corpos dos complexos, reais, Zp, com p primo, estruta de alguma algebra, grupos, espaços vetorias. Alem desses, poderiam criar tbm uma classe
    de equivalencia no geral, estrutura de conta bancaria. Ou seja, toda uma maneira de representar um obejto da maneira como a pessoa queira basta usar
    a class para poder definir a estrutura. Alem disso, dentro de class podemos, a apartir dos elementos atribuidos no class, criar uma colecao de varias
    formas de representacao dos objetos com diversas estruturas, onde o class estaria guardando dentro dele, e com os comandos da funcao no compilador,
    podemos chama-los na estrutura que a pessoa preferir. Cada funcao colocado, como definimos-las, muitas vezes para uma unica operacao, podemos pensar
    , as vezes, como grupo, caso esteja fazendo uma construcao axiomatica de alguma algebra, corpo, etc...
    '''
    def __init__(self,num = 0,den = 1):
        
        if den < 0:
            self.num = (-1)*num//mdc(num,den)
            self.den = (-1)*den//mdc(num,den)
        else:            
            self.num = num//mdc(num,den)
            self.den = den//mdc(num,den)
        
    '''Este e um dos metodos construtores de um certo obejto que sera representado da maneira como a pessoa prefere
    no caso aqui e onde definimos a estrutura para a representacao de tais obejtos.
    Esse construtor e como se fosse uma entrada que recebe os elementos necessarios para,
    em seguida por vias de outras funcoes, construir a estrutura com
    esses obejtos temporariamente mantidos da maneira como a pessoa preferir ?????
    '''
    '''def show(self):
        print(self.num,"/", self.den)'''
    def __str__(self):
        '''essa e uma definicao dentre outros existentes no python que tem por funcao transformar obejtos em uma string. Sem essa funcao, nao poderei
        mostrar os obejtos estruturados explicitamente no compilador, ou seja, no lugar iria aparecer algo do tipo <__main__.Fraction object at algum numero>'''
        if self.den == 1 or self.num == 0:
            return str(self.num)
        else:
            return str(self.num)+'/'+str(self.den)
    '''maneiras para retornar o que esta definido no __str__: print(Fraction(,)), Fraction(,)__str__() no lugar de Fraction poderia ser alguma variavel
    que carrega como objeto a classe Fraction, str(Fraction(,)), nesse e a mesma analogia'''
    
    def __add__(self,other):
        num = self.num*other.den + self.den*other.num
        den = self.den*other.den
        novonum = num//mdc(num,den)
        novoden = den//mdc(num,den)
        '''Nessa definicao sere para definir uma operacao que o sujeito queira. Podemos relacionar essa ideia de quando definimos
        uma operacao binaria em uma algebra, neste caso a soma. Assim, como a definicao __add__ tem por funcao incluir um oberando self e nesse operando,
        incluir um outro operando nessa mesma classe. Podemos associar com a ideia de soma de classes de equivalencia, quando se constroe o corpo dos racionais
        e, o tipo de operacao que definimos nessa classe'''

        return Fraction(novonum,novoden)

    def __eq__(self,other):
        '''uma funcao booleana propria da class'''
        primeiro = self.num*other.den
        segundo = self.den*other.num
        return primeiro == segundo

    def __mul__(self,other):
        novonum = self.num*other.num
        novoden = self.den*other.den
        return Fraction(novonum,novoden)
    
        
    

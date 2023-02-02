from stack import Stack

# constantes
PROMPT = "expr >>> "
QUIT   = "fim"
ABRE   = "("
FECHA  = ")"
ADD    = "+"
SUB    = "-"
MUL    = "*"
DIV    = "/"
OPERADORES = "+-*/"
DIGITOS = "0123456789."
OPER = {'+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y}

def main():
    '''
    Calcula o valor de uma expressão númerica
    posfixa que contém apenas os operadores 
    binários +, -, * e /. 

    Pré-condição: o programa supõe que os operadores
      e operandos estão separados por pelo menos um
      espaço.
    '''
    print("Tranforma infixa para posfixa")
    print("(Tecle ENTER para encerrar programa.)")

    expressao = input(PROMPT)
    while expressao != '':
        posfixa = infixa_para_posfixa(expressao)
        print("posfixa:", end=" ")
        for item in posfixa:
            print(item, end=" ")
        print()    
        expressao = input(PROMPT)

              
#-------------------------------------------------------        
def valor_expressao(posfixa):
    ''' (list) -> float

    Recebe um lista de tokens representando um expressão 
    numérica em notação posfixa e retorna o valor da 
    expressao.

    Pre-condiçao: a funçao supõe que a expressao está
         correta.
    '''
    pilha = Stack()
    for item in posfixa:
        if item in OPERADORES:
            valor_2 = pilha.pop()
            valor_1 = pilha.pop()           
            valor = OPER[item](valor_1, valor_2)
        else:
            # é um numero
            valor = float(item)
        pilha.push(valor)
        
    return pilha.pop() 
        
#-------------------------------------------------------
def infixa_para_posfixa(infixa):
    '''(str) -> list

    Recebe um string infixa com uma expressão numérica
    em notação infixa e cria e retorna uma lista com 
    com os tokens da expressão representando a correspondente
    expressão em notação posfixa.

    Pré-condição: a função supões que os itens da expressão 
    estão separado por pelo menos um espaço.
    '''
    posfixa = []
    pilha = Stack()
    valor = ''
    for car in infixa:
        #------------------------------------    
        if car not in DIGITOS and valor != '':
            posfixa.append(valor)
            valor = ''

        #------------------------------------                
        if car in DIGITOS:
            valor += car
            
        #------------------------------------    
        elif car == ABRE:
            pilha.push(ABRE)

        #------------------------------------        
        elif car == FECHA:
            item_topo = pilha.pop()
            while item_topo != ABRE:
                posfixa.append(item_topo)
                item_topo = pilha.pop()
                
        #------------------------------------
        elif car in [ADD,SUB]:
            while not pilha.isEmpty() and \
                pilha.peek() in OPERADORES:
                item_topo = pilha.pop()
                posfixa.append(item_topo)
            pilha.push(car)

        #------------------------------------
        elif car in [MUL,DIV]:
            while not pilha.isEmpty() and \
                  pilha.peek() in [MUL,DIV]:
                item_topo = pilha.pop()
                posfixa.append(item_topo)
            pilha.push(car)

    if valor != '': posfixa.append(valor)
    
    while not pilha.isEmpty():
        item_topo = pilha.pop()
        posfixa.append(item_topo)
    
    return posfixa


#------------------------------------------------
def pause():
    input("Tecle ENTRE para continuar. ")
    
#----------------------------
if __name__ == "__main__":
    main()

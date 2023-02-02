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

MOSTRE_INFIXA = False
MOSTRE_VALOR  = False
MOSTRE_SEPARA = False

def main():
    '''
    Calcula o valor de uma expressão númerica
    posfixa que contém apenas os operadores 
    binários +, -, * e /. 

    Pré-condição: o programa supõe que os operadores
      e operandos estão separados por pelo menos um
      espaço.
    '''
    print("Calculadora de expressões numéricas")
    print("Deve haver um espaço entre os itens")
    print("(Tecle ENTER para encerrar o programa.)")
    
    expressao = input(PROMPT)
    while expressao != QUIT:
        posfixa = infixa_para_posfixa(expressao)
        try:
            valor = valor_expressao(posfixa)
            print("%g" %valor)
        except:
            print("Erro na expressão")
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
    if MOSTRE_VALOR:
        print("-----")
        print("valor_expressao: posfixa = ", posfixa)
        pause()
        
    pilha = Stack()
    for item in posfixa:
              
        if MOSTRE_VALOR:
            print("item = '%s'" %item, "pilha =", pilha)
            pause()
            
        if item in OPERADORES:
            valor_2 = pilha.pop()
            valor_1 = pilha.pop()           
            if item == ADD:
                valor = valor_1 + valor_2
            elif item == SUB:
                valor = valor_1 - valor_2
            elif item == MUL:
                valor = valor_1 * valor_2
            elif item == DIV:
                valor = valor_1 / valor_2
        else:
            # é um numero
            valor = float(item)
              
        pilha.push(valor)
        
    if MOSTRE_VALOR:
        print("pilha =", pilha)
        pause()
        
    resultado = pilha.pop()
    return resultado    
        
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
    tokens = infixa.split()

    if MOSTRE_INFIXA:
        print("-----")
        print("infixa_para_posfixa: \n",
              "   posfixa = '%s'\n" % infixa,
              "   tokens  =", tokens)                   
        pause()
        
    pilha = Stack()     
    for item in tokens:
        if MOSTRE_INFIXA:
            print("item = '%s'" %item)
            print("  pilha   = ", pilha)
            print("  posfixa = ", posfixa)
            pause()
            
        #------------------------------------    
        if item == ABRE:
            pilha.push(ABRE)

        #------------------------------------        
        elif item == FECHA:
            item_topo = pilha.pop()
            while item_topo != ABRE:
                posfixa.append(item_topo)
                item_topo = pilha.pop()
                
        #------------------------------------
        elif item in [ADD,SUB]:
            while not pilha.isEmpty() and \
                pilha.peek() in OPERADORES:
                item_topo = pilha.pop()
                posfixa.append(item_topo)
            pilha.push(item)

        #------------------------------------
        elif item in [MUL,DIV]:
            while not pilha.isEmpty() and \
                  pilha.peek() in [MUL,DIV]:
                item_topo = pilha.pop()
                posfixa.append(item_topo)
            pilha.push(item)

        #-----------------------------------    
        else: # encontramos um número
           posfixa.append(item)

    while not pilha.isEmpty():
        if MOSTRE_INFIXA:
            print("  pilha   = ", pilha)
            print("  posfixa = ", posfixa)
            pause()
        item_topo = pilha.pop()
        posfixa.append(item_topo)
           
    return posfixa



#-----------------------------------------------------------        
def separa(texto, sep = ' '):
    ''' (string, chr) -> list

     Recebe um string texto e um caractere separador sep e
     retorna uma lista contendo as ´palavras´ do texto usando
     o caractere sep como delimitador:
     Por exemplo para:
     
         texto = "Como e bom estudar MAC2166!"
         sep   = " "
         
     a função retorna
     
        ['Como', 'e', 'bom', 'estudar', 'MAC2166']

     A função ´corta´ o texto nos separadores.
    '''
    lista = []
    palavra = ''
    for car in texto:
        if car == sep:
            if palavra != '': #para quem não gosta de palavra vazia
                lista.append(palavra)
            palavra = ''
        else:
            palavra += car

        if MOSTRE_SEPARA:
            print("palavra = '%s'" %(palavra))
            print("lista =", lista)
            pause()
            
    # coloca a última palavra na lista
    if palavra != '':
       lista.append(palavra)
    
    return lista 

#------------------------------------------------
def pause():
    input("Tecle ENTRE para continuar. ")
    
#----------------------------
main()

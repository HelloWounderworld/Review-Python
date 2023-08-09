from stack import Stack

PROMPT = "expr >>> "
QUIT = ""
ADD  = "+"
SUB  = "-"
MUL  = "*"
DIV  = "/"
MOSTRE = False

def main():
    '''
    Calcula o valor de uma expressão númerica
    posfixa que contém apenas os operadores 
    binários +, -, * e /. 

    Pré-condição: o programa supões que os operadores
      e operandos estão separados por pelo menos um
      espaço.
    '''
    print("Calculadora de expressões numéricas posfixas")
    print("Deve haver um espaço entre os operadores e operandos")
    print("(Tecle ENTER para encerrar o programa.)")
    
    expressao = input(PROMPT).strip()
    while expressao != QUIT:
        posfixa = expressao.split()
        if MOSTRE:
            print("expressao = '%s'\n" %expressao,\
                  "posfixa = ", posfixa, sep="")
            pause()
        try:
            valor = valor_expressao(posfixa)
            if valor != None: print("%s" %valor)
        except:
            print("Erro na expressão")
        
        expressao = input(PROMPT).strip()

#-------------------------------------------------------        
def valor_expressao(posfixa):
    ''' (list) -> int|float|None

    Recebe um lista com os itens representando uma expressão 
    numérica em notação posfixa e calcula e retorna o valor 
    da expressao.

    Pré-condiçao: a funçao supõe que a expressao está
         correta e os operadores e operandos estao separados
         por pelo menos um espaço.
    '''
    pilha = Stack()
    for item in posfixa:
        if MOSTRE:
            print("  item = '%s'" %item, " pilha =", pilha, sep = "")
            pause()
        if item in [ADD,SUB,MUL,DIV]:
            if len(pilha) < 2:
                print("Erro: faltam operandos")
                return None
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
            if "." in item: valor = float(item)
            else: valor = int(item)

        pilha.push(valor)
        
    if MOSTRE:
        print("pilha =", pilha)
        pause()
        
    resultado = pilha.pop()
    if not pilha.isEmpty():
        print("Erro: faltam operadores")
        return None
    return resultado    

def pause():
    input("Tecle ENTER para continuar")
    
#----------------------------
if __name__ == "__main__":
    main()

# Stack.empilhe(), Stack.desempilhe, Stack.topo()
from stack import Stack

PROMPT = ">>> "
ABRE_PARENTESES  = "("
FECHA_PARENTESES = ")"
ABRE_CHAVES      = "{"
FECHA_CHAVES     = "}"
ABRE_COLCHETES   = "["
FECHA_COLCHETES  = "]"
QUIT = 'q'

def main():
    '''
    Recebe uma sequência formada apenas por parênteses e
    colchetes e verifica se é bem formada.
    '''
    print("Verificador de sequencias bem formadas.")

    sequencia = input(PROMPT)
    while sequencia != QUIT:
        if bem_formada(sequencia):
            print("bem-formada: sim")
        else:
            print("bem_formada: não")
        sequencia = input(PROMPT)

#-------------------------------------------------------        
def bem_formada(sequencia):
    ''' (str) -> bool

    Recebe um string contendo uma sequencia de parênteses,
    chaves e colchetes e retorna TRUE se a sequência é bem 
    formada e false em caso contrário.
    '''
    stack = Stack()
    for item in sequencia:
        if item in [ABRE_PARENTESES,ABRE_COLCHETES,ABRE_CHAVES]:
            stack.push(item)
        elif item in [FECHA_PARENTESES,FECHA_COLCHETES,FECHA_CHAVES]:
            if stack.isEmpty():
                return False
            # verifique se o topo da stack tem o abre certo
            item_topo = stack.pop()
            if   item == FECHA_PARENTESES and item_topo != ABRE_PARENTESES:
                return False
            elif item == FECHA_COLCHETES  and item_topo != ABRE_COLCHETES:
                return False
            elif item == FECHA_CHAVES     and item_topo != ABRE_CHAVES:
                return False
            
    if not stack.isEmpty():
        return False

    # passou pelos testes
    return True

#--------------------------------------------
main()

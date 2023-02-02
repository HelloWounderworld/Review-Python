# Stack.push(), Stack.pop(), Stack.pop()
from stack import Stack

PROMPT = ">>> "
ABRES  = "([{"
FECHAS = ")]}"
DICIO  = {')' : '(', ']' : '[', '}' : '{'}
QUIT = ''

def main():
    '''
    Recebe uma sequência formada apenas por parênteses e
    colchetes e verifica se é bem formada.
    '''
    print("Verificador de sequencias bem formadas.")
    print("[Tecle ENTER para encerrar o programa.]")    
    sequencia = input(PROMPT).strip()
    while sequencia != QUIT:
        if bem_formada(sequencia):
            print("bem-formada: sim")
        else:
            print("bem_formada: não")
        sequencia = input(PROMPT).strip()

#-------------------------------------------------------        
def bem_formada(sequencia):
    ''' (str) -> bool

    Recebe um string contendo uma sequencia de parênteses,
    chaves e colchetes e retorna TRUE se a sequência é bem 
    formada e false em caso contrário.
    '''
    pilha = Stack()
    for item in sequencia:
        if item in ABRES:
            pilha.push(item)
        elif item in FECHAS:
            if pilha.isEmpty():
                return False
            # verifique se o topo da pilha tem o abre certo
            item_topo = pilha.pop()
            if   item_topo != DICIO[item]:
                return False
            
    if not pilha.isEmpty():
        return False

    # passou pelos testes
    return True

#--------------------------------------------
if __name__ == "__main__":
    main()

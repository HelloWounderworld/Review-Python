#
# Implementação da função bem_formada
# usando append() e pop() de lista 
# 

TESTE = False
PROMPT = "exp >>> "
ABRE_PARENTESES  = "("
FECHA_PARENTESES = ")"
ABRE_CHAVES      = "{"
FECHA_CHAVES     = "}"
ABRE_COLCHETES   = "["
FECHA_COLCHETES  = "]"
ABRE  = "([{"
FECHA = ")]}"
QUIT = ''

def main():
    '''
    Resolve um problema levemente mais geral.
    
    Recebe uma sequência de strings e para cada string verifica se a substring
    formada apenas pelos seus parênteses, colchetes e chaves é bem formada.
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

    Recebe um string e verifica se a substring formada apenas por parênteses,
    chaves e colchetes da string é bem-formada.
    Retorna True se a sequência é bem formada e False em caso contrário.
    '''
    pilha = []

    for item in sequencia:
        if item in ABRE: 
            pilha.append(item)
        elif item in FECHA: 
            if pilha == []: # pilha vazia -- erro frequente 
                return False
            # verifique se o topo da pilha tem o abre certo
            item_topo = pilha.pop()
            if ABRE.index(item_topo) != FECHA.index(item):
                return False
            
    if len(pilha) > 0: # pilha não vazia -- erro frequente
        return False

    # passou pelos testes
    return True


#--------------------------------------------
if __name__ == "__main__":
    main()      

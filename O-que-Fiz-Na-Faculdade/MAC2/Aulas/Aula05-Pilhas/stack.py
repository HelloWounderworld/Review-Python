class Stack:
    #-----------------------------------------------------
    def __init__(self):
        '''(Pilha) -> None

        Usado pelo construtor da classe.

        Monta um objeto da classe Pilha.
        '''
        self.itens = []

    #-----------------------------------------------------        
    def __str__(self):
        '''(Pilha) -> str

        Recebe uma Pilha referenciada por `self` e constroi e 
        retorna o string exibido por print() para imprimir uma 
        pilha. Esse também é o string retornado por str().
        '''
        return str(self.itens)

    #-----------------------------------------------------
    def __len__(self):
        '''(Pilha) -> int

        Recebe uma Pilha referenciada por self e retorna
        o número de itens na pilha.

        Usado pelo Python quando escrevemos len(Pilha).
        '''
        return len(self.itens)

    #-----------------------------------------------------    
    def isEmpty(self):
        '''(Pilha) -> bool

        Recebe uma Pilha referenciada por self e retorna 
        True se ela está vazia e False em caso contrário.
        '''
        return self.itens == []

    #-----------------------------------------------------    
    def push(self, item):
        '''(Pilha, objeto) -> None

        Recebe uma Pilha referenciada por self e um objeto 
        item e coloca item no topo da pilha.
        ''' 
        self.itens.append(item)

    #-----------------------------------------------------        
    def pop(self):
        '''(Pilha) -> objeto

        Recebe uma Pilha referenciada por self e desempilha 
        e retorna o objeto no topo da pilha.
        '''
        return self.itens.pop()

    #-----------------------------------------------------    
    def peek(self):
        '''(Pilha) -> objeto 

        Recebe uma Pilha referenciada por self e retorna
        o objeto no topo da pilha. O objeto não é removido 
        da pilha.
        '''
        return self.itens[-1]


class Stack:
    #-----------------------------------------------------
    def __init__(self):
        '''(Stack) -> None

        Usado pelo construtor da classe.

        Monta um objeto da classe Stack.
        '''
        self.itens = []

    #-----------------------------------------------------        
    def __str__(self):
        '''(Stack) -> str

        Recebe uma Stack referenciada por `self` e constroi e 
        retorna o string exibido por print() para imprimir uma 
        pilha. Esse também é o string retornado por str().
        '''
        return str(self.itens)

    #-----------------------------------------------------
    def __len__(self):
        '''(Stack) -> int

        Recebe uma Stack referenciada por self e retorna
        o número de itens na pilha.

        Usado pelo Python quando escrevemos len(Stack).
        '''
        return len(self.itens)

    #-----------------------------------------------------    
    def isEmpty(self):
        '''(Stack) -> bool

        Recebe uma Stack referenciada por self e retorna 
        True se ela está vazia e False em caso contrário.
        '''
        return self.itens == []

    #-----------------------------------------------------    
    def push(self, item):
        '''(Stack, objeto) -> None

        Recebe uma Stack referenciada por self e um objeto 
        item e coloca item no topo da pilha.
        ''' 
        self.itens.append(item)

    #-----------------------------------------------------        
    def pop(self):
        '''(Stack) -> objeto

        Recebe uma Stack referenciada por self e desempilha 
        e retorna o objeto no topo da pilha.
        '''
        return self.itens.pop()

    #-----------------------------------------------------    
    def peek(self):
        '''(Stack) -> objeto 

        Recebe uma Stack referenciada por self e retorna
        o objeto no topo da pilha. O objeto não é removido 
        da pilha.
        '''
        return self.itens[-1]

    def __iter__(self):
        '''(Stack) -> Stack
        
        Recebe um Stack referenciado por self e inicializa o 
        iterador. Usado pelo Python quando escrevenos 
        "for item in Stack". Retorna self.
        '''
        self.i = 0
        return self

    def __next__(self):
        '''(Stack) -> object

        Recebe um Stack referenciado por self e responsável por fornecer
        o próximo item da pilha quando escrevemos
        "for item in Stack". Retorna o item ou levanta a excessão
        StopIteration.
        '''
        if self.i < len(self):
            x = self.itens[self.i]
            self.i += 1
            return x
        raise StopIteration

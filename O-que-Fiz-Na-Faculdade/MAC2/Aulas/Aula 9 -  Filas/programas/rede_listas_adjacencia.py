class Rede:
    #---------------------------------------------   
    def __init__(self, n):
        '''(Rede, int) -> None

        Recebe um inteiro positivo n e retorna uma Rede
        com n cidades e sem estradas.

        As cidades são números entre 0 e n-1.

        self.adj[i] é a lista das cidades adjacentes a i.
        '''
        adj = []
        for i in range(n):
            adj.append([])
        self.adj = adj
        
    #----------------------------------------------     
    def __str__(self):
        '''(Rede) -> str

        Recebe uma Rede referênciada por self e cria
        e retorna um string que representa a rede.
        '''
        s   = "Listas de adjacências:\n"
        adj = self.adj
        n   = len(adj)
        for i in range(n):
            s += "%d:" %i + str(adj[i]) + "\n"
        return s    

    #---------------------------------------------   
    def insira_estrada(self, i, j):
        '''(Rede, int, int) -> None

        Recebe um rede referênciada por self e um par 
        de inteiros representando cidades e insere
        na rede a estrada de i a j.
        '''
        self.adj[i].append(j)

    #---------------------------------------------           
    def existe_estrada(self, i, j):
        '''(Rede, int, int) -> bool

        Recebe uma rede referênciada por self e dois
        inteiros i e j representando duas cidades e retorna
        True se existe uma estrada de i a j e False em caso 
        contrário.
        '''
        return j in self.adj[i]

    #---------------------------------------------       
    def __len__(self):
        '''(Rede) -> int

        Recebe uma referência self e retorna o número de
        cidades na rede.
        '''
        return len(self.adj)
        

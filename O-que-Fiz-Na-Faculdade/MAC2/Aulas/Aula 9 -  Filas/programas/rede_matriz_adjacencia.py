class Rede:
    #---------------------------------------------   
    def __init__(self, n):
        '''(Rede, int) -> None

        Chamada pelo construtor.
        Recebe um inteiro positivo n e retorna uma Rede
        com n cidades e sem estradas.

        As cidades são números entre 0 e n-1.

        self.adj[i][j] == 1     existe estrada de i a j
        self.adj[i][j] == 0 não existe estrada de i a j  
        '''
        self.adj = []
        for i in range(n):
            linha = n * [0]
            self.adj.append(linha)

    #----------------------------------------------     
    def __str__(self):
        '''(Rede) -> str

        Recebe uma Rede referênciada por self e cria
        e retorna um string que representa a rede.
        '''
        s = "Matriz de adjacência:\n"
        adj = self.adj
        n   = len(adj)
        for i in range(n):
            for j in range(n):
                s += str(adj[i][j]) + " "
            s += "\n"
        return s    

    #---------------------------------------------   
    def insira_estrada(self, i, j):
        '''(Rede, int, int) -> None

        Recebe um rede referênciada por self e um par 
        de inteiros i e j representando cidades e insere
        na rede a estrada de i a j.
        '''
        self.adj[i][j] = 1

    #---------------------------------------------           
    def existe_estrada(self, i, j):
        '''(Rede, int, int) -> bool

        Recebe uma rede referênciada por self e dois
        inteiros i e j representando duas cidades e retorna
        True se existe uma estrada de i a j e False em caso 
        contrário.
        '''
        return self.adj[i][j] == 1

    #---------------------------------------------       
    def __len__(self):
        '''(Rede) -> int

        Recebe uma referência self e retorna o número de
        cidades na rede.
        '''
        return len(self.adj)
        

import random            
        
class Cliente:
    
    def __init__(self,nome):
        self.nome = nome
        self.classificacao = {}
        self.lista = []
    
    def put_classificacao(self,filmes):
        for i in range(len(filmes)):
            self.classificacao[i] = filmes[i]
    
    def __str__(self):
        x = self.nome+'\n'
        for i in range(len(self.classificacao)):
            x = x + '%d: %s\n' %(i,self.classificacao[i])
        return x
    
    def get_nome(self):
        return self.nome
    
    def get_classificacao(self):
        for i in range(len(self.classificacao)):
            self.lista.append(self.classificacao[i])
        return self.lista
    
    def distancia(self,other):
        if self.lista == other.lista:
            return 0
        else:
            lista_modelo = {}
            lista_compara = []
            ordem = 0
            for i in range(len(self.lista)):
                if self.lista[i] in other.lista:
                    lista_modelo[self.lista[i]] = ordem
                    ordem += 1
            for j in range(len(other.lista)):
                if other.lista[j] in lista_modelo:
                    lista_compara.append(lista_modelo[other.lista[j]])
            if len(lista_modelo) == 1 or len(lista_modelo) == 2:
                return 0
            else:
                transposicao = 0
                print("Estado inicial da lista_compara")
                print(lista_compara)
                print()
                for i in range(0,len(lista_compara)):
                    for j in range(0,len(lista_compara)-1):
                        if lista_compara[j] > lista_compara[j+1]:
                            x = lista_compara[j+1]
                            lista_compara[j+1] = lista_compara[j]
                            lista_compara[j] = x
                            transposicao += 1
                            print("estado que esta a lista")
                            print(lista_compara)
                            print()
                return transposicao
    
#####################################################################
# CONSTANTES
# cada caractere representa o nome de um filme para testes
FILMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

#------------------------------------------------------------
def main(args=None):
    ''' (None) -> None
        Essa função main está aqui para testar a classe Cliente.
        Você pode alterá-la e incluir os seus próprios testes.
        '''
    # para podermos reproduzir os testes
    random.seed(0) # para outros testes, troco valor

    # lst de filmes
    lst_filmes = args
    if lst_filmes == None: lst_filmes = FILMES
    n_filmes     = len(lst_filmes)

    print("Cliente(): iniciando teste...")
    lst_clientes = []
    lst_clientes.append(Cliente("T'Challa"))
    lst_clientes.append(Cliente('Nakia'))
    lst_clientes.append(Cliente('Natasha Romanoff'))
    print("Cliente() não explodiu... sorriso")
    
    print("put_classificacao(): iniciando teste...")
    lst_clientes[0].put_classificacao(lst_filmes[:5]) 
    random.shuffle(lst_filmes)
    lst_clientes[1].put_classificacao(lst_filmes[:10])
    random.shuffle(lst_filmes) 
    lst_clientes[2].put_classificacao(lst_filmes[:7])
    print("put_classificao() não explodiu... sorriso")

    
    print("__str__(): iniciando teste:")
    for cliente in lst_clientes:
        print(cliente)
    print("__str__(): não explodiu... sorriso")
    
    print("get_nome() e get_classificacao(): iniciando teste")
    for cliente in lst_clientes:
        print("%s: %s"%(cliente.get_nome(), cliente.get_classificacao())) 
    print("get_nome() e get_classificacao() não explodiu sorriso\n")
        
    print("distancia(): iniciando teste...")
    for cliente0 in lst_clientes:
        for cliente1 in lst_clientes:
            print("distancia(%s,%s)= %s"%(cliente0.get_nome(),
                                          cliente1.get_nome(),
                                          cliente0.distancia(cliente1)))
    print("distancia(): não explodiu... sorriso")
main()

'''
 Cliente(): iniciando teste...
    Cliente() não explodiu... :-)
    put_classificacao(): iniciando teste...
    put_classificao() não explodiu... :-)
    __str__(): iniciando teste:
    T'Challa
    0: A
    1: B
    2: C
    3: D
    4: E

    Nakia
    0: B
    1: J
    2: I
    3: F
    4: K
    5: C
    6: D
    7: H
    8: E
    9: A

    Natasha Romanoff
    0: C
    1: B
    2: F
    3: H
    4: D
    5: G
    6: A

    __str__(): não explodiu... sorriso

    get_nome() e get_classificacao(): iniciando teste
    T'Challa: ['A', 'B', 'C', 'D', 'E']
    Nakia: ['B', 'J', 'I', 'F', 'K', 'C', 'D', 'H', 'E', 'A']
    Natasha Romanoff: ['C', 'B', 'F', 'H', 'D', 'G', 'A']
    get_nome() e get_classificacao() não explodiu :-)

    distancia(): iniciando teste...
    distancia(T'Challa,T'Challa)= 0
    distancia(T'Challa,Nakia)= 4
    distancia(T'Challa,Natasha Romanoff)= 2
    distancia(Nakia,T'Challa)= 4
    distancia(Nakia,Nakia)= 0
    distancia(Nakia,Natasha Romanoff)= 3
    distancia(Natasha Romanoff,T'Challa)= 2
    distancia(Natasha Romanoff,Nakia)= 3
    distancia(Natasha Romanoff,Natasha Romanoff)= 0
'''



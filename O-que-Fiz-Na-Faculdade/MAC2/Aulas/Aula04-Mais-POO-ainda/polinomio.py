class Polinomio:
    #----------------------------------------------------------------
    def __init__(self, coef = []):
        '''(Polinomio, list) -> None

        Construtor: recebe uma referência/apelido para um objeto
           `self` a ser construído e uma referência/apelido
           `coef` para os coeficientes de um polinômio e cria
           e retorna um Polinomio.

        Decisões de projeto:

            * valor de self.coef[i] é o coeficiente do termo x**i;
            * polinômio nulo é representado pela lista []; 
            * coeficiente do termo dominante de um polinômio não nulo 
               é diferente de zero; e, portanto
            * len(self.coef)-1 é o grau do polinômio e o grau do polinômio 
                nulo é -1.
    
        Método mágico/especial: usado pelo Python quando
            escrevemos Polinomio() para cria um Polinomio.
            Não tem return.
        '''
        # perigo, coef é um apelido para a lista
        # determine o grau do polinômio
        grau = len(coef)-1
        while grau > -1 and coef[grau] == 0:
            grau -= 1
        # crie um clone
        coef_clone = []
        i = 0
        while i < grau+1:
            coef_clone.append(coef[i])
            i += 1
        # atualize o atributo coef
        self.coef = coef_clone

    #----------------------------------------------------------------    
    def __str__(self):
        '''(self) -> str

        Recebe uma referência `self` para um Polinomio e cria
        e retorna um string que representa o polinômio.

        Método mágico/especial: usado pelo Python quando usamos
            print() em um Polinomio. Também é usado pelo Python
            quando usamos str().

        '''
        s = ''
        coef = self.coef
        grau = self.grau() # len(coef)-1
        if grau == -1:
            s += '0'
        else:
            # encontre primeiro coeficiente não nulo
            i = 0
            while coef[i] == 0:
                i += 1
            # aqui coef[i] != 0
            s += str(coef[i]) 
            if i > 0:
                s += "*x**%d" %i
            i += 1
            while i < grau+1:
                valor = coef[i]
                if   valor > 0:
                    s += " + " + str(valor) + "*x**%d" %i 
                elif valor < 0:
                    s += " - " + str(-valor) + "*x**%d" %i 
                i += 1
        return s

    #----------------------------------------------------------------            
    def __call__(self, x):
        '''(Polinomio, número) -> número

        Recebe uma referência/apelido `self` a um Polinomio e
            um número x. 
            Calcula e retorna o valor do polinômio em x.

        Método mágico/especial: usado pelo Python quando chamamos um 
             Polinomio com um argumento: p(x).
        '''
        valor = 0
        coef = self.coef
        grau = self.grau() # len(coef)-1
        i = 0
        xi = 1
        while i < grau+1:
            valor += coef[i] * xi
            xi *= x
            i += 1
        return valor    

    #----------------------------------------------------------------
    def __add__(self, other):
        '''(Polinomio, Polinomio) -> Polinomio

        Recebe referências/apelidos  `self` e `other` para Polinomios
        e cria e retorna um Polinomio que é sua soma.

        Método mágico/especial: usado pelo Python quando escrevemos 
             Polinomio + Polinomio.

        A solução do problema proposto não usa esse método. 
        '''
        # apelidos
        coef1 = self.coef
        grau1 = self.grau() # len(coef1)-1
        coef2 = other.coef
        grau2 = other.grau() # len(coef2)-1

        # calcule os coeficientes da soma dos polinômios
        coef_soma = []
        i = 0
        while i < grau1+1 or i < grau2+1:
            valor1 = 0
            valor2 = 0
            if i < grau1+1: valor1 = coef1[i]
            if i < grau2+1: valor2 = coef2[i]
            valor = valor1 + valor2
            coef_soma.append(valor)
            i += 1

        soma = Polinomio(coef_soma)
        return soma
        
    #----------------------------------------------------------------                    
    def grau(self):
        '''(Polinomio) -> int

        Recebe uma referência/apelido `self` para um Polinomio 
        e retorna o seu grau.
        '''
        return len(self.coef) - 1

    #----------------------------------------------------------------                
    def derive(self):
        '''(Polinomio) -> Polinomio

        Recebe uma referência/apelido 'self' para um Polinomio
        e retorna um Polinomio que representa a sua derivada.
        '''
        # apelidos
        coef    = self.coef
        grau    = self.grau() # len(self.coef)-1
        coef_dp = []
        i = 1
        while i < grau+1:
            # calcule o coeficiente de x**(i-1) da derivada
            valor = i*coef[i]
            coef_dp.append(valor) 
            i += 1
        # crie um polinomio    
        dp = Polinomio(coef_dp)
        return dp


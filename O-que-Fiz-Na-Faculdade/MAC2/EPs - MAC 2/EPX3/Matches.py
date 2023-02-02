class Matches:
    
    def __init__(self,s):
        self.s = s
    
    def matches(self,t):
        lista = []
        for i in range(0,len(self.s)-len(t)+1):
            if self.s[i:i+len(t)] == t:
                lista.append(i)
        return lista

def main():
    buscador1 = Matches("abracadabra")
    buscador2 = Matches("banana")
    buscador3 = Matches("yabbadabbadoo")
    print(buscador1)
    print()
    print(buscador2)
    print()
    print(buscador3)
    print()
    print('Teste mathces()')
    print()
    print(buscador1.matches("abra"))
    print()
    print(buscador1.matches("ra"))
    print()
    print(buscador1.matches("a"))
    print()
    print(buscador1.matches(" a"))
    print()
    print(buscador2.matches("ana"))
    print()
    print(buscador3.matches("ab"))
    print()
    print(buscador3.matches("ba"))
    print()
    print(buscador3.matches("abba"))
    print()
    print(buscador3.matches("yabbadabbadoo"))
    print()
    print(buscador3.matches("yabbadabbadoox"))
    print()
    print(buscador3.matches("ad"))
main()

'''
    >>> buscador1 = Matches("abracadabra")
    >>> buscador2 = Matches("banana")
    >>> buscador3 = Matches("yabbadabbadoo")
    >>> buscador1.matches("abra")
    [0, 7]
    >>> buscador1.matches("ra")
    [2, 9]
    >>> buscador1.matches("ra ")
    []
    >>> buscador1.matches("a")
    [0, 3, 5, 7, 10]
    >>> buscador1.matches(" a")
    []
    >>> buscador2.matches("ana")
    [1, 3]
    >>> buscador3.matches("ab")
    [1, 6]
    >>> buscador3.matches("ba")
    [3, 8]
    >>> buscador3.matches("abba")
    [1, 6]
    >>> buscador3.matches("yabbadabbadoo")
    [0]
    >>> buscador3.matches("yabbadabbadoox")
    []
    >>> buscador3.matches("ad")
    [4, 9]
    >>> 
'''

#Julgando se é ou não palíndromo
while (True):
    def palindromo(n):
        x = n
        m = 0
        while x > 0:
            dig = x % 10
            m = m * 10 + dig
            x = x // 10
        if m == n:
            return True # Onde tem o if e o else, ao em vez de colocar toda a estrutura, vc poderia colocar no lugar de tudo isso o "return m == n"
        else:
            return False
    def main():
        n = int(input("Entre com o valor de n:"))
        if palindromo(n):
            print("{} e um palindromo". format(palindromo(n)))
        else:
            print("{} nao e um palindromo". format(palindromo(n)))
    main() #Onde esta escrito main poderia colocar o que quiser e, isso vai deixar de executar o def main. Mas nao vai deixar de executar o que esta definido.

#Operador booleanos: "True", "False". Expressões lógicas: "and", "or", "not". (Em C ou C++: and = && , or = || , not = !)

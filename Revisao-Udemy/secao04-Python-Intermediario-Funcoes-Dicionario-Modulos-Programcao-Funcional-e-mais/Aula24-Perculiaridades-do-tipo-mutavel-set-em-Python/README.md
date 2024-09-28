# Aula 24 - Peculiaridades do tipo mutável set em Python:
Vamos ver mais algumas peculiaridades do tipo mutável set em Python.

No caso, os set's:

- Não aceitam valores mutáveis;

- Seus valores serão sempre únicos;

- não tem índexes;

- não garantem ordem;

- são iteráveis (for, in, not in)

Além de serem eficientes de removerem valores duplicados, por serem conjuntos em sua própria definição. Como podemos ver no exemplo abaixo

    s3 = {1, 1, 1, 1, 2, 3, 3, 3, 3, 3}
    print(s3)

Note que, no exemplo acima, temos o número "1" e "3" repetidos. Enttretanto, ao darmos o print desse conjunto, vemos que é exibido somente 1, 2 e 3.

Podemos converter listas e tuplas em um conjunto tbm da seguinte forma

    l1 = [1, 1, 1, 1, 2, 3, 3, 3, 3, 3]
    t1 = (1, 1, 1, 1, 2, 3, 3, 3, 3, 3)

    s4 = set(l1)
    s5 = set(t1)

    print(s4)
    print(s5)

E de conjunto, podemos converte em lista e tuplas tbm, como segue

    l1 = [1, 1, 1, 1, 2, 3, 3, 3, 3, 3]
    t1 = (1, 1, 1, 1, 2, 3, 3, 3, 3, 3)

    s4 = set(l1)
    s5 = set(t1)

    print(s4)
    print(s5)

    l2 = list(s4)
    t2 = tuple(s5)
    
    print(l2)
    print(t2)

Bom, isso é um método bem eficiente para vc conseguir remover valores repetidos de uma lista do que usar outros recursos de iteração.

Agora, para reforçar de não pudermos colocar algum valor mutável dentro do set, vale ver o seguinte exemplo

    s6 = {1,2,3,[123]}

Se vc compilar o código acima, será retornando um erro dizendo que não podemos colocar uma lista dentro de um conjunto, o mesmo vale para dicionário. Entretanto, podemos colocar uma tupla, pois a tupla é um valor imutável.

    s7 = {1,2,3,(123,)}

Agora, podemos colocar um conjunto dentro de um conjunto? Dica: Axioma do Zermelo Freankel kkkkkkk

Bom, outra vantagem de usar o set para realizar alguma iteração, seria pela sua eficiência que é um pouco acima do que das listas, dicionários e tuplas.

Além disso, podemos usar as linguagens de conferência de pertencimento sobre o set como é feito em conjunto, o "in" e "not in".

    s7 = {1,2,3,(123,)}
    print(3 in s7)
    print(4 in s7)
    print(5 not in s7)
def letras(n):
    '''note que, ao expressarmos uma string, por exemplo, "abacaixi", podemos identificar cada algarismo
usando a mesma noção de uma lista, ou seja, no caso, a possibilidade desse uso faz com que para cada
algarismo que aparece na palavra "abacaixi", podemos definir uma classe de numeros inteiros que represente a posicao
de cada algarismo presente na mesma palavra, mas lembrando que o sentido da classe que esta sendo atribuido aqui
seria levar em consideracao os numero que excedem a ordem de uma lista mas que pode ser equilavente a um numero
representante na qual a funcao dentro do colchetes "[]" reconhece, ou seja, por exemplo, se -1 colocado no [] a string
reconhece e supondo que essa string tenha 5 letras, ao colocar -6 no colchetes ele nao reconhecera, mas podemos transformar
de alguma maneira em -1, pois em Z5 esse e o mesmo que -1. Alem disso, note que, por mais que tenha algarismos repetidos, por se tratar
da sua manipulacao ser parecida de uma lista, entao cada algarismo, representara como tipagens diferentes'''
    '''A unica coisa que diferece uma string de uma list, seria que a primeira e imutavel, ou seja, em uma lista
caso a pessoa queira trocar ou substituir um certo algarismo por outro o comando "list[indice]="string"" sera
bem reconhecido. Ja numa stringo isso nao ocorre e, ao tentar processa-lo o python informara um erro. Logo,
uma maneira de mudar algum algarismo da string, podemos usar um processo de concatenaçao e fatias de strings'''
    comprimento = len(n)
    x = []
    for i in range(comprimento):
        print(n[i], end="\t")
        x.append(n[i])
    return x

# Aula 23 - if, elif e else: entendendo o fluxo do interpretador em condicionais
Vamos entender mais ainda sobre blocos.

Lembra quando foi dito sobre a identação?

Pois bem, no caso, como podemos ver 

    condicao = True

    if condicao:
        print('Este é o codigo do if')
        
    print('Fora do if')

Vemos que quando rodamos o código acima, o print('Fora do if'), será exibido, pois ele está no mesmo nível de alinhamento com a condicional if em que foi utilizado.

    condicao = True

    if condicao:
        print('Este é o codigo do if')
    else:
        print('Este é o codigo do else')
    if 10 == 10:
        print('Outro if')
        
    print('Fora do if')

Aqui estamos deixando claro que se quisermos usar o else ou elif, necessariamente precisa da existência do if e mesmo criando um bloco com as condicionais, nada impede de criar um outro if depois delas tbm.

Existe casos em que mesmo que entre na condição vc não pensou em algum código nela ainda. No caso, vc poderia usar o pass

    condicao = False

    if condicao:
        print('Este é o codigo do if')
    elif 3 == 3:
        pass
    else:
        print('Este é o codigo do else')
    if 10 == 10:
        print('Outro if')
        
    print('Fora do if')

Basicamente, o bloco de condicionais, a forma como ela funciona, é o mesmo que a do JavaScript. Em um único bloco, vc poderia ter muita, mas muita, condicionais para ser avaliado. Mas bastou que uma delas seja satisfeita, então irá sair do bloco inteiro em seguida.

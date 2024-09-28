# Aula 07 - Retorno de valores das funções (return):
O retorno das funções, sempre que executada, ela retorna um determinado valor. Por padrão, as funções executadas retornam o "None", como podemos ver abaixo

    variavel = print("Leonardo")
    print(variavel)

No caso, a função "print" foi criado, pelo desenvolvedores python, para que ele, sempre que chamado, exibisse a msg que foi colocado dentro dela, não importa se foi tentado atribuir ela dentro de uma variável. O mesmo vale quando definimos uma função personalizado usando "def"

    def soma(x,y):
        print(x+y)

    variavel = soma(1,2)
    print(variavel)

Mas, agora, suponhamos que tal valor exibido pelo "x+y" queremos que tal valor seja atribuído para à variável "random". No caso, para isso, teremos que utilizar o "return" como segue

    def soma(x,y):
        return x+y

    random = soma(1,2)
    print(random)

Ou seja, a sintaxe "return", como o nome disse, ele retorna algum valor. E isso só pode ser executado dentro da função e que é uma sintaxe que serve para parar a execução de uma função. Ou seja, podemos criar uma função, donde combinado com condicionais, exista um conjunto de return. Quando acionado o return dentro de uma função, mesmo havendo outros códigos posteriores, ela não será mais executada. A função para exatamente nela.
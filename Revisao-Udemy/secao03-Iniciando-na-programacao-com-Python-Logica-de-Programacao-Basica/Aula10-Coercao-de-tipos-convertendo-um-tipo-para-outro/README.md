# Aula 10 - Coerção de tipos (convertendo um tipo para outro):
Vamos ver o que é conversão de tipos e coerção.

No caso, type convertion, typecasting, coercion é o ato de converter um tipo em outro tipos imutáveis e primitivos: str, int, float, bool

Em python, com a estrutura de programação com tipagem dinâmica forte, ele permite que vc define algum valor sem necessidade de declarar o mesmo, como foi visto antes. O mesmo vale para operações, donde vc consegue realizar operações aritméticas sem a necessidade de declar o ato. No caso, em especial, o operador "+" ele tem uma estrutura de polimorfismo aqui, ou seja, ela está definida tanto para operações aritméticas com números quanto para operações de concatenação e tais ações, tbm, vc não precisaria declarar

    print(1 + 1)
    print('a' + 'b')

Obs: Diferentemente de JavaScript, no python se vc fizar a operação do tipo 

    print('a' + 1)

Ele não será válido, pois no JavaScript essa operação ele interpreta que valor number seria uma string para concatenar com a outra string. Em python, isso gera um erro

    Traceback (most recent call last):
    File "/home/leonardo/Documentos/estudos/Review-Python/Revisao-Udemy/secao03-Iniciando-na-programacao-com-Python-Logica-de-Programacao-Basica/Aula10-Coercao-de-tipos-convertendo-um-tipo-para-outro/aula10.py", line 8, in <module>
        print('a' + 1)
    TypeError: can only concatenate str (not "int") to str

Ou seja, isso é tipicamente característica de uma linguagem de programação de tipagem dinâmica forte, diferentemente de JavaScript, que é de tipagem dinâmica fraca.

No caso, a forma como eu interpreto isso é que Python ele é como se fosse um cara muito rígido com as definições matemáticas sem abuso de notações, equanto que o JavaScript, ele não é tão rígido, ao ponto de permitir algumas operações com abuso de notação.

Existem funções em Python que ele converte um tipo de dado para outro quando isso é permissível, visto que o Python é uma linguagem dinâmica de tipagem forte.

    print('1', type('1'))
    print(int('1'), type(int('1')))

No caso, acima vemos que estamos convertendo uma string, mas com caractere 1 que é um número, para um inteiro. Visto que a classe type está verificando o seu tipo e, como prova disso, no terminal podemos ver que o primeiro print ele retorna um tipo string e o segundo um tipo int, de inteiro. Porém, note que, isso só foi possível visto que o dado primitivo que está como string ele era permissível de ser alterado para um número inteiro, pois o seguinte caso não seria possível realizar o mesmo processo que fizemos acima

    print('a', type('a'))
    print(int('a'), type(int('a')))

Um outro detalhe importante que precisamos saber seria quando realizamos as operações entre dois números, sendo um int e outro um float

    print(1.0 + 1)

O que vc acha que o python iria retornar nesse caso? 

A resposta é que quando vc realiza alguma operação matemática com int e um float, será devolvido um float, isso faz sentido, visto que os floats são números que permitem a existência de números flutuantes.

O mesmo uso que fizemos acima para a função int, vale para o float.

Algumas coisas, podemos converter para um booleano tbm.

Uma curiosidade seria o seguinte

    print(bool(''))
    print(bool(' '))

    print(bool({}))
    print(bool({ 'Estado': 'SP'}))

    print(bool([]))
    print(bool([1]))

No código acima, estamos usando a função bool para uma string vazia e um bool para uma string com um espaço, da mesma forma para outros dois objetos, um bool para objeto vazio e outro que conste algum elemento. O que vc acha que será devolvido?

Outra função que temos de conversão é o str, ou seja, ela converte em uma string

    print(str(11) + 'b')
    print(str({}))
    print(str([]))
    print(str(True))
    print(str(False))

Podemos ver acima que a função str consegue converter um monte valores em uma string, bastaria ver o que está sendo retornado pelo terminal.

# Aula 07 - Tipo str (string) - Introdução aos tipos de dados:
Vamos introduzir aos tipos de dados.

Vamos primeiro entender o que é a linguagem de programação Python.

Assim como o JavaScript, Python ela é uma linguagem de programação de tipagem dinâmica. O que difere com o JavaScript, é que, enquanto o Python essa tipagem dinâmica é forte, o JavaScript ela é de uma tipagem dinâmica fraca.

Obs: Ser uma linguagem de programacao de tipagem fraca ou forte, para entender, voce pode imaginar dois individuo, um que fala a sua lingua nativa de forma coloquial, mas que seja o suficiente para entender muito bem e, o outro individuo, usando a sua lingua nativa de forma bem rigorosa e formal. Ou seja, o primeiro e a tipagem fraca e, o segundo, e o de tipagem forte. Ou se for para dar de exemplo de dois matematico enquanto um faz o abuso de notacao, mas que nao tem problema, e o outro e extremamente formal, rigoso e preciso com as notacoes e que nao perdoa nenhum abuso de notacao.

    https://www.treinaweb.com.br/blog/quais-as-diferencas-entre-tipagens-estatica-ou-dinamica-e-forte-ou-fraca

    https://pt.stackoverflow.com/questions/21508/qual-a-diferen%C3%A7a-entre-uma-linguagem-de-programa%C3%A7%C3%A3o-est%C3%A1tica-e-din%C3%A2mica

    https://medium.com/@alissoncs_/diferen%C3%A7as-entre-tipagens-est%C3%A1tica-din%C3%A2mica-fraca-e-forte-755e08d82caa

O que significa que uma linguagem de programação ser de tipagem dinâmica, significa que a linguagem em si já sabe que tipo de linguagem de programação está sendo passada para ela. No caso do Python, quando colocamos 

    print(1234)

O conteúdo de dentro, 1234, da função print, o python já conhece. O que difere, por exemplo, da linguagem de programação de tipagem estática, pois nela, sempre que vc colcoar algum valor, vc precisa declarar se ela é um number, string, boolean, etc...

Agora, nessa aula, objetivo é falar sobre strings. 

No caso, o que são strings?

Strings são textos que estão dentro de aspas, pode ser simples ou dupla, tanto faz.

    # Strings - Textos que vão dentro de aspas, pode ser simples ou duplas
    print('Hello WounderWordl!')
    print("Hello WounderWordl!")

A mesma lógica de aspas que eu estudei em JavaScript, aqui funciona tbm

    # Strings - Textos que vão dentro de aspas, pode ser simples ou duplas
    print('Hello WounderWordl!')
    print("Hello WounderWordl!")
    print("Hello 'WounderWordl!'")
    print('Hello "WounderWordl!"')
    print("Hello \"WounderWordl!\"")
    print('Hello \'WounderWordl!\'')

Quando rodamos o código acima, no terminal não conseguimos ver se foi usado o escape, \, ou não. Mas existe uma forma de vc conseguir exibir isso no terminal tbm

    print(r"Hello \"WounderWordl!\"")
    print(r'Hello \'WounderWordl!\'')

No caso, segundo o criador do python, esse "r" que usamos para poder exibir os escapes ele é usado muito para expressões regulares.

Uma outra coisa que precisa-se saber bem seria sobre quando vc cria uma documentação usando """ """ ou ''' ''', os DocStrings. Eles são strings tbm.

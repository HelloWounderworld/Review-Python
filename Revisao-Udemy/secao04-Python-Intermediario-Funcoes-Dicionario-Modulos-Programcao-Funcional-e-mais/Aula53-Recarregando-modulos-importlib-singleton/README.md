# Aula 53 - Recarregando módulos, importlib e singleton:
Vamos aprender a recarregar os módulos aqui.

Vamos criar uma pasta "code-class-53" e dentro dela iremos criar dois arquivos "aula53.py" e "aula53_m.py". Daí, vamos realizar a importação do módulo, aula53_m.py, como fizemos nas últimas duas aulas anteriores para o módulo principal, aula53.py.

Por começo, no módulo, aula53_m.py, colocamos

    print(123)

Até agora nada de novo. Em seguida, vamos colocar no módulo, aula53_m.py, a seguinte variável

    variavel = 'Leonardo'

Agora, no módulo, aula53.py, vamos tentar realizar o seguinte

    import aula53_m

    print(aula53_m.variavel)

    for i in range(10):
        import aula53_m

    print('Fim')

Note que, o print que está dentro do módulo, aula53_m.py, não está sendo exibido nas dez interações do for. O for, por exemplo, ela está sim iterando, bastaria dar um print no índice "i" que está percorrendo de 0 à 9.

Isso porque a importação de módulos elas são um tipo singleton. O que é isso?

Basicamente, o singleton é algo que a existência dela seja única naquele programa. Em outras palavras, quando importamos algum módulo, essa importação fica guardado na memória do processador de modo que vc não precisa importar novamente sempre que for necessário realizar o uso dela. Isso entra dentro do padrão de eficiência para economizar espaço na memória.

Entretanto, existem cenários em que vc precisa recarregar alguns módulos já importados. Não é algo muito comum, porém, em raras ocasiões é necessário realizar o recarregamento do módulo. Para isso, usamos um outro módulo para possibilitar esse recarregamento que seria o importlib. No caso, no arquivo, aula53.py, importamos o módulo

    import importlib

    import aula53_m

    print(aula53_m.variavel)

    for i in range(10):
        importlib.reload(aula53_m)

    print('Fim')

No caso, a cada chamada desse reload dentro do módulo importlib, iremos recarregar o módulo aula53_m.py.

Bom, qual a necessidade disso? Para entendermos isso, vamos ativar no terminal o modo iterativo em Python. Ou seja, pelo terminal, vai até a pasta code-class-53, e nela joga o seguinte comando

    python -i aula53.py

Vamos ver que nela irá o arquivo e ficará no modo interactive Python. Feito isso, no módulo, aula53_m.py, realizamos a seguinte alteração

    variavel = 'Leonardo 1'

Daí, no modo interactive Python ainda ativo, em ">>>" jogamos o seguinte comando

    aula53_m.variavel

Será exibido o antigo valor

    Leonardo

E não o atual.

Para isso que serve o reload do método importlib, pois ela irá recarregar o módulo, aula53_m.py, de modo que vc irá conseguir verificar a alteração feita nela. Joga de novo, no '>>>', o comando

    importlib.reload(aula53_m)

Em seguida, acessamos a variável de novo, '>>> aula53_m.py'. Verá que a alteração feita no módulo, aula53_m.py, agora está sendo considerado.

Para sair do modo interactive Python, basta colocar o comando 'quit()'.

Bom, precisa fazer tudo isso só para recarregar o módulo? Não!

No caso, a cada mudança que eu realizar no módulo, aula53_m.py, se eu recompilar novamente o módulo, aula53.py, seja ela pelo terminal ou diretamente no arquivo ou numa aplicação, refresh page, conseguimos considerar as alterações que ocorreram no outro módulo.

Bom, a moral da história é que vc tem que entender que os módulos Pythons são recarregados uma única vez, o que define a natureza de coisas que são chamados singletons em programação!

Link para leitura:

    https://refactoring.guru/pt-br/design-patterns/singleton/python/example
    https://docs.python.org/3/library/importlib.html
    https://realpython.com/lessons/reloading-module/
    https://stackoverflow.com/questions/18500283/how-do-you-reload-a-module-in-python-version-3-3-2

# Aula 51 - Modularização - Entendendo os seus próprios módulos e sys.path no Python:
Vamos abordar sobre a modularização do código. Ou seja, vamos criar um módulo próprio personalizado, independente dos módulos que já existem na linguagem Python.

Basicamente, a modiularização é uma forma de organizar cada classe ou código em um arquivo, em vez de colocar todos os códigos em um único arquivo. Em outras palavras, seria o seguinte. Em qualquer sistema conseguimos realizar um esboço topológico da arquitetura desse sistema. Ou seja, vc consegue esboçar a arquitetura do sistema de forma simples e que bastaria entender o esboço simples para entender a funcionalidade do sistema inteiro. Só que esse esboço simples ela poderia estar em duas formas, uma inteiramente em um único arquivo, donde, dentro dela, esteja separado de forma didática ou não cada funcionalidade, o que é considerado de muita má prática, ou que cada funcionalidade esteja feita em cada arquivos e simplesmente a funcionalidade do sistema inteiro esteja sendo feito com base das relações entre tais arquivos.

Portanto, a ideia da modularização seria a segunda alternativa. Em outras palavras, vc organiza melhor as funcionalidades em cada arquivo de forma que fique mais fácil de compreender como o sistema inteiro funciona e que isso ajuda na manutenção e desenvolvimento da mesma.

Agora, vamos para a aplicação do coceito teórico acima. No Python, em qualquer caso, sempre, o primeiro módulo que é executado é o "__main__", podemos verificar isso chamando a classe "__name__" para identificar qual módulo está em funcionamento

    print('Este modulo, dentro do aula51.py, se chama ', __name__)

No caso, que tenha em mente que sempre o primeiro módulo que é executado pelo Python é o "__main__".

Agora, vamos tentar importar um outro módulo que é criado por vc ou parte dela. Uma coisa que sempre precisamos tomar cuidado seria no nome do módulo que vc queira colocar, pois isso correria o risco de colcarmos o nome de um módulo já existente no Python, o que ocorreria o problema de sobrescrição.

Vamos começar por uma importação simples onde o arquivo se encontra no mesmo nível do arquivo da aula51.py. No caso, criamos um arquivo "aula_51.py" e nela colocamos o seguinte

    print('Este modulo, dentro do aula_51.py, se chama ', __name__)

No caso, nos nomes dos módulos não podemos colocar espaços ou caracteres especiais como acentos, etc... Sempre elas precisam estar juntas com underscore em letras minúsculas.

Agora, voltando para o arquivo aula51.py, ao executarmos esse módulo, vamos ver que, será exibido o print dentro do arquivo aula51.py, primeiro, e, em seguida, a do arquivo aula_51.py. E o que o "__name__" vai exibir nos dois casos será diferente.

Além disso, vale ressaltar que o Python, no processo de importação de módulo, ela não é possível realizar busca dos arquivos externos a não ser que vc não especifique direito as paths para chegar até no arquivo desejado. Para isso, podemos ver isso usando o método path que tem dentro do módulo sys. Vamos importar no arquivo aula51.py o módulo sys e darmos o print no método dela

    import sys

    import aula_51

    print('Este modulo, dentro do aula51.py, se chama ', __name__)
    print(sys.path)
    print(*sys.path, sep='\n') # para melhorar a visualizacao

Note que, o "sys.path" ela mostra o caminho que foi feito para ser executado o "__name__" .

Da mesma forma, dentro do sys.path podemos incluir, por append(), uma path externa donde nessa path, na pasta final que estará sendo indicado, vc estará dizendo que existe um módulo Python que pode ser importado. Vc poderá testar na sua máquina como seguinte

    try:
        import sys
        sys.path.append('/Users/ltakashi/Documents/') # path que tenho dentro da minha maquina
    except ModuleNotFoundError:
        ...

    import helloWounderWorld

    import aula_51

    print('Este modulo, dentro do aula51.py, se chama ', __name__)
    print(*sys.path, sep='\n')

No caso, no sys.path acima eu adicionei uma path e dentro da pasta final dessa path criei um arquivo "helloWounderWorld.py" e dentro dela coloquei

    print('Hello WounderWorld!!!')

Indicando qual módulo python existente dentro da pasta "Documents" estou querendo importar.

Bom, não é comum realizarmos uma manipulação do tipo para trabalharmos. O comum é termos um arquivo python e ao redor dela, em níveis mais baixo dela ocorrer as alterações necessárias para conseguirmos trabalhar.

Link para leitura

    https://www.geeksforgeeks.org/sys-path-in-python/
    https://acervolima.com/sys-path-em-python/

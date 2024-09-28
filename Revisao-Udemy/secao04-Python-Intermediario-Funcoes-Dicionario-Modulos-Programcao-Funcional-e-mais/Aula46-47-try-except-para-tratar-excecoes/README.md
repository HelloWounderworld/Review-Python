# Aula 46 e 47 - (Parte 1 e 2) try e except para tratar exceções:
Bom, essa parte, a lógica é muito similar ao try/catch que se ensina na linguagem JavaScript.

Ela serve para conseguir tratarmos uma exceção.

Assim, temo como sintaxe disso os seguinte try, except, else e finally. No caso, a combinação é válida da seguinte forma try/except, try/finally, mas não tem try/else. Então em que momento se usa o else? Vamos abordar isso ao longo do curso.

    try:
        ...
    except:
        ...

ou

    try:
        ...
    finally:
        ...

Bom, como uma boa prática, é recomendável que nunca deixe de acontecer algum erro silencioso. Na forma, como está acima para except

    try:
        ...
    except:
        ...

Vc está criando, propositalmente, um erro silencioso. Claro, a forma acima só foi para mostrar as combinações possíveis, mas que fique bem claro que na prática não se deve colocar algum erro silecioso, no geral.

Agora, vamos ver o seguinte exemplo 

    a = 18
    b = 0
    c = a / b

Bom, ao definirmos a variável acima, se tentarmos executar o código, teremos um erro, pois não está definido matematicamente, dentro do conjunto que estamos trabalhando, a divisão por zero. Logo, ao tentarmos rodar o código acima, não será possível pois isso irá induzir à um erro.

Agora, vamos utilizar do cenário acima para conseguirmos explorar sobre o uso de try/exception. No caso, obviamente, em cenários usuais, tais divisões acima, estariam sendo utilizados de forma dinâmica, onde o cliente que irá colocar algum valor para conseguirmos tratar. No caso, pensando nisso, vamos colocar o seguinte

    a = 18
    b = 0

    try:
        c = a / b
    except:
        print('Deu ruim!')

    print('CONTINUAR')

Ao rodarmos o código acima, as duas mensagens 'Deu ruim' e 'CONTINUAR' serão exibidos pois, como podemos ler literalmente, foi feito uma tentativa de divisão, mas isso não deu certo, então acabou entrando na exceção e dentro da exceção foi feito o que foi definido, print, então saímos do código e seguimos para o print('CONTINUAR').

Bom, como podemos ver, a funcionalidade é igualzinho ao try/catch do JavaScript para tratamento de exceções ou impedimento de que a aplicação não pare no meio do processo. Advinha, então, o que o finally faz? kkkkkkk Bom, bastaria dar uma lembrada, para quem estudou JavaScript, mas vamos abordar isso ao longo da aula.

Voltando para o try/except, a forma como foi codado acima, mesmo que sirva para entender como é o tipo de uso, a forma acima ainda assim, está dentro dos conjuntos de más práticas, pois a msg que utilizei acima "Deu ruim" torna ainda o erro silecioso. Mesmo que eu tenha colocado alguma msg do tipo 'Não se pode dividir por zero', ainda sim, continuará sendo uma má prática, pois qualquer tipo de outro erro que acontecer, a msg exibida será o aviso de não dividir por zero. Ou seja, o erro continua sendo silecioso, como segue

    try:
        a = 18
        b = 0
        print('Linha 1')
        c = a / b
        print('Linha 2')
    except:
        print('Dividiu por zero.')

    print('CONTINUA')

No caso, o formato acima deixa ainda mais nítido em que momento o código dentro do try para e vai para o except, o print('Linha 2') não será exibido.

Agora, falseando um outro tipo de erro, seria colocando o seguinte

    try:
        a = 18
        # b = 0
        print('Linha 1')
        c = a / b
        print('Linha 2')
    except:
        print('Dividiu por zero.')

    print('CONTINUA')

Agora, nesse cenário, como a variável b está comentado, cairá em um outro tipo de erro. Bastaria rodar só o código

    a = 18
    # b = 0
    c = a / b

para conseguirmos ver que tipo de erro será exibido.

Ou seja, se tivessemos um try/except da forma como estamos acima, mesmo exibindo a msg 'Dividiu por zero.' dificilmente iremos saber que tipo de erro, realmente, está ocorrendo para ter acontecido algo do tipo acima.

No caso, em resumo, sempre precisamos ter em mente que é necessário exibir direito que tipo de erro está sendo tratado na exception. Como?

Bom, basicamente, temos várias formas. Primeiro, de forma clássica, vamos mostrar o jeito mais arcaico, que é definindo o tipo de erro uma por uma. Ao rodarmos o código 

    a = 18
    b = 0
    c = a / b

pelo terminal, será exibido o tipo de erro. Em Python, as exceções são classes, então o tipo de erro que é exibido pelo terminal, no caso acima, "ZeroDivisionError" é uma classe, então uma das formas de tratarmos o excetp seria literalmente chamar esse tipo de classe nela como segue

    try:
        a = 18
        b = 0
        print('Linha 1')
        c = a / b
        print('Linha 2')
    except ZeroDivisionError:
        print('Dividiu por zero.')

    print('CONTINUA')

Obs: Todas as nomenclaturas de uma classe é escrito em Pascal Case. Ou seja, sempre que inicia algum nome ela começa, primeiro, com letra maiúscula.

Note que, com o código acima, iremos conseguir tratar o erro caso ocorra alguma divisão por zero. Além disso, se ocorrer algum outro erro, esse erro será exibido pelo terminal, claro parando toda a aplicação, que é o que queremos evitar a priori, pensando no cenário em que tiver algum usuário utilizando a aplicação, como no caso abaixo

    try:
        a = 18
        # b = 0
        print('Linha 1')
        c = a / b
        print('Linha 2')
    except ZeroDivisionError:
        print('Dividiu por zero.')

    print('CONTINUA')

Ou seja, o tipo de erro já não é mais a divisão por zero. Então, não irá cair dentro da except e isso irá parar de rodar o código, sem exibir 'CONTINUA'. Daí, o que precisaria ser feito? Claro, criar uma outra except colocando nela o erro que foi capturado

    try:
        a = 18
        b = 0
        print('Linha 1')
        c = a / b
        print('Linha 2')
    except ZeroDivisionError:
        print('Dividiu por zero.')
    except NameError:
        print('Alguma variável não está definido')

    print('CONTINUA')

Aí vem a seguinte pergunta. Devo sempre ficar caçando uma por uma os possíveis erros para gradualmente tornar o sistema muito mais completo?

A resposta para isso é, depende. Pois existem cenários em que a contagem dos tipos de erros é evidente e existem cenários que não. Ok, mas e se acontecer o segundo cenário? Para esse caso, existe uma forma de tratar o erro, mas que eu não gosto muito, que seria chamando a classe de erro mais superior de todas que é Exception

    try:
        a = 18
        b = 0
        print('Linha 1')
        c = a / b
        print('Linha 2')
    except ZeroDivisionError:
        print('Dividiu por zero.')
    except NameError:
        print('Alguma variável não está definido')
    except Exception:
        print('Erro desconhecido')

    print('CONTINUA')

Eu, particularmente, detesto esse tipo de classe, pois, querendo ou não, torna, de certa forma, silencioso o tipo de erro. Pois, a classe Exception, ela é a classe de nível mais acima de todas as outras classes de erros existente. Serve para conseguir tratar qualquer tipo de erro, mas, muitas vezes, não deixando claro a natureza desse erro.

Bom, a moral da história, é que o try/except, dentro do except, não podemos dinamizar de forma que quando venha algum erro desconhecido, seja possível que o sistema trate ela de forma eficiente. Ou seja, esse exception existe mais para conseguir facilitar que o usuário continue utilizando a aplicação, enquanto que, em paralelo, o desenvolvedor consiga realizar o reparo ou investigação do problema para conseguir incluir, possivelmente, mais uma except e nela definir algum tratamento mais eficiente, depois que toma o devido conhecido do erro, que antes era desconhecido.

Bom, vamos explorar os seguintes erros tbm

    try:
        a = 18
        b = 0
        print(b[0])
        print('Linha 1'[1000000])
        c = a / b
        print('Linha 2')
    except ZeroDivisionError:
        print('Dividiu por zero.')
    except NameError:
        print('Alguma variável não está definido')
    except Exception:
        print('Erro desconhecido')

    print('CONTINUA')

Acima, temos dois tipos de erros. A primeiroa é de tipagem, pois a variável "b" é imuável e estamos tentando acessar algum índice dentro dela comoc se fosse lista e a outra é um erro de tipagem, no print('Linha 1'), pois estamos tentando acessar o índice que não existe dentro dessa string. Bom, se rodarmos cada um dos códigos de forma isolado, vamos ter os seguinte erros TypeError e IndexError.

No caso, bastaria colocar mais dois except, como uma boa prática. Mas desta vez, vamos colocar duas de uma vez, que não é uma boa prática, mas de forma proposital, para conseguirmos mostrar uma coisa interessante

    try:
        a = 18
        b = 0
        print(b[0])
        print('Linha 1'[1000000])
        c = a / b
        print('Linha 2')
    except ZeroDivisionError:
        print('Dividiu por zero.')
    except NameError:
        print('Alguma variável não está definido')
    except (TypeError, IndexError):
        print('TypeError + IndexError')
    except Exception:
        print('Erro desconhecido')

    print('CONTINUA')

Note que, no except (TypeError, IndexError):, não sabemos que tipo de erro está acontecendo, mas sabemos que é certeza uma das duas. Para isso, existe uma froma de conseguirmos exibir isso que seria usando o alias "as" das seguinte forma

    try:
        a = 18
        b = 0
        print(b[0])
        print('Linha 1'[1000000])
        c = a / b
        print('Linha 2')
    except ZeroDivisionError:
        print('Dividiu por zero.')
    except NameError:
        print('Alguma variável não está definido')
    except (TypeError, IndexError) as error:
        print('TypeError + IndexError')
        print('Mensagem:', error)
        print('Nome do erro:', error.__class__.__name__)
    except Exception:
        print('Erro desconhecido')

    print('CONTINUA')

No caso, a forma acima, irá exibir que tipo de erro ocorreu na mensagem e qual foi o nome do erro, que seria o nome da classe. Tornando assim, mais evidente o tipo de erro que aconteceu. O mesmo podemos realizar para except que tem somente uma classe de erro, como seguinte

    try:
        a = 18
        b = 0
        print(b[0])
        print('Linha 1'[1000000])
        c = a / b
        print('Linha 2')
    except ZeroDivisionError as e:
        print('Dividiu por zero.')
        print('Mensagem:', e)
        print('Nome do erro:', e.__class__.__name__)
    except NameError:
        print('Alguma variável não está definido')
    except (TypeError, IndexError) as error:
        print('TypeError + IndexError')
        print('Mensagem:', error)
        print('Nome do erro:', error.__class__.__name__)
    except Exception:
        print('Erro desconhecido')

    print('CONTINUA')

Tornando assim, mais evidente o tipo de erro.

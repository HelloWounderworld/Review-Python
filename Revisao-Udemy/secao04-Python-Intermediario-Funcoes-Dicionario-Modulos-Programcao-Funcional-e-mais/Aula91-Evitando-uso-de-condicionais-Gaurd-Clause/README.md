# Aula 91 - Evitando uso de condicionais + Guard Clause:
Conforme o exercício feito anteriormente, vamos melhorar a qualidade do código.

Não signigica que não podemos usar as condicionais "if/elif/else". Porém, para tornar o código da pessoa mais robusta, no sentido de melhor performance e que não engloba possibilidades desnecessárias ou, até mesmo, interrupções indesejadas, seria um diferencial o estudante compreender muito bem os momentos convenientes de se usar as condicionais ou outras formas, que são tipos de condicionais, porém, mais convenientes ao cenário.

Vamos levar em consideração o código da aula antecessora, donde, dentro do loop, while, foi feito o seguinte

    while (True):
        print('Comandos: listar, desfazer e refazer')
        entrada = input('Digite uma tarefa ou comando: ')
        
        if entrada == 'listar':
            listar(lista)
            continue

        elif entrada == 'desfazer':
            desfazer(lista, listaRefaz)
            listar(lista)
            continue

        elif entrada == 'refazer':
            refazer(listaRefaz, lista)
            listar(lista)
            continue

        elif entrada == 'clear':
            # aqui serve para dar o comando "clear" para limpar o terminal
            os.system('clear')
            continue

        else:
            adicionar(entrada, lista)
            listar(lista)
            continue

Bom, primeiro, vamos explicar o por quê, que o uso da condicional no cenário acima, não está tão conveniente. Motivo disso, está no fato de que existem condicionais que não precisa ser considerado ou até mesmo, iria causar alguma interrupção.

O conceito que o estudante poderia consultar para melhorar a condição de de estudos dele é "Guard" em ciências da computação. É um conceito que ajuda a pessoa a conseguir refinar os melhores momentos em que seria conveniente o uso das condicionais e a sua forma de uso.

No caso, aplicando o conceito de guard no código acima, seria melhor realizarmos o seguinte

    def listar(lista):
        print()
        if not lista:
            print('Não há nada a ser listado!')
            return

        print('Tarefas:')
        for tarefa in lista:
            print(f'{tarefa}')
        print()

    def desfazer(lista, listaRefaz):
        print()
        if not lista:
            print('Não há nada a ser desfeito!')
            return

        listaRefaz.append(lista.pop())
        print()
        listar(lista)

    def refazer(listaRefaz, lista):
        print()
        if not listaRefaz:
            print('ListaRefaz vazio')
            return

        lista.append(listaRefaz.pop())
        print()
        listar(lista)

    def adicionar(argumento, lista):
        print()
        argumento = argumento.strip()
        if not argumento:
            print('Você precisa digitar algo!')
            return
        lista.append(argumento)
        print()
        listar(lista)

    guardando_sigla = {'listar': 0, 'desfazer': 1, 'refazer': 2, 'clear': 3}
    # print(tuple(guardando_sigla.keys())[0])
    # print(tuple(guardando_sigla.keys())[1])
    # print(tuple(guardando_sigla.keys())[2])
    # print(tuple(guardando_sigla.keys())[3])

    lista = []
    listaRefaz = []

    # Motivo de ter usado o continue:
    # É mais para garantir que nada depois dela será executado!
    while (True):
        print('Comandos: listar, desfazer e refazer')
        entrada = input('Digite uma tarefa ou comando: ')

        comandos = {
            'listar': lambda: listar(entrada),
            'desfazer': lambda: desfazer(lista, listaRefaz),
            'refazer': lambda: refazer(listaRefaz, lista),
            'clear': lambda: os.system('clear'),
            'adicionar': lambda: adicionar(entrada, lista)
        }

        comando = comandos.get(entrada) if comandos.get(entrada) is not None else \
            comandos['adicionar']
        comando()
        
        #if entrada == 'listar':
        #    listar(lista)
        #    continue

        #elif entrada == 'desfazer':
        #    desfazer(lista, listaRefaz)
        #    listar(lista)
        #    continue

        #elif entrada == 'refazer':
        #    refazer(listaRefaz, lista)
        #    listar(lista)
        #    continue

        #elif entrada == 'clear':
        #    # aqui serve para dar o comando "clear" para limpar o terminal
        #    os.system('clear')
        #    continue

        #else:
        #    adicionar(entrada, lista)
        #    listar(lista)
        #    continue

Bom, confesso que esse conceito ficou um pouco boiado na minha cabeça. Logo, será necessário que eu faça uma revisão. Dar uma leitura do que foi abordado até agora para deixar firme.

Seguir link para a compreensão:

    https://en.wikipedia.org/wiki/Guard_(computer_science)

    https://medium.com/lemon-code/guard-clauses-3bc0cd96a2d3

    https://www.codementor.io/@clintwinter/use-guard-clauses-for-cleaner-code-1rrsczgwxp

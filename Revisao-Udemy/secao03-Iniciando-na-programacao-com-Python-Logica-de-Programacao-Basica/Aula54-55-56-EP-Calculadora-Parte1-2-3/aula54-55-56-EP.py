""" Calculadora com while """
while True:
    numeros_validos = None
    numero1 = input('Digite um primeiro número: ')

    try:
        numero1 = float(numero1)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Favor colocar os números válidos')
        continue

    numero2 = input('Digite outro segundo número: ')

    try:
        numero2 = float(numero2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Favor colocar os números válidos')
        continue

    operador = input('Digite o operador (+-/*): ')

    operadores_usados = '+-/*'
    
    if operador not in operadores_usados:
        print('Digite um operador válido!')
        continue

    if len(operador) > 1:
        print('Digite apenas um tipo de operador')
        continue
    
    print('Realizando a sua conta. Confira o resultado abaixo:')
    
    if operador == '+':
        print(f'{numero1}+{numero2}=', numero1+numero2)
    elif operador == '-':
        print(f'{numero1}-{numero2}=', numero1-numero2)
    elif operador == '/':
        print(f'{numero1}/{numero2}=', numero1/numero2)
    elif operador == '*':
        print(f'{numero1}*{numero2}=', numero1*numero2)
    else:
        print('Caixa de pandora')
        
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
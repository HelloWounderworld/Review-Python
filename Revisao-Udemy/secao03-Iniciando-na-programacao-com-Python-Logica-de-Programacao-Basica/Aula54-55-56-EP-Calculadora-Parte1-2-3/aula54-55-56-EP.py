""" Calculadora com while """
while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    
    numeros_validos = None
    
    # print(type(operador))
    
    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
        numeros_validos = True
    # Exception as error é uma alternativa
    # except Exception as error:
    #     print(error)
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Favor colocar os números válidos')
        continue

    operadores_usados = '+-/*'
    
    if operador not in operadores_usados:
        print('Digite um operador válido!')
        continue
    if len(operador) > 1:
        print('Digite apenas um tipo de operador')
        continue
    
    print('Realizando a sua conta. Confira o resultado abaixo')
    
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
    # print(sair)

    if sair is True:
        break
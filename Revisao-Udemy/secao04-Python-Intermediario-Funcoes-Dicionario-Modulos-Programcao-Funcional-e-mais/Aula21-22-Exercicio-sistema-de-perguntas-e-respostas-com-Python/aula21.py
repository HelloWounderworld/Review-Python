# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opcoes': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
count = 0
while count < len(perguntas):
    reserva = count
    count += 1
    print(perguntas[reserva]['Pergunta'])
    print()
    print('Opções:')
    print()
    for j in range(0,len(perguntas[reserva]['Opcoes'])):
        print(f'{j+1})',perguntas[reserva]['Opcoes'][j])
    print()

    l = input('Escolha uma das opções: ')
    print()
    digito = None

    if l.isdigit():
        digito = int(l)

    if digito is not None:
        if digito > 0 and digito <= len(perguntas):
            if perguntas[reserva]['Resposta'] == perguntas[reserva]['Opcoes'][digito-1]:
                acertos += 1
                print('Acertou')
                print()
            else:
                print('Errou')
                print()
        else:
            print('Por favor, escolher entre as opções de 1 à 4.')
            print()
            count -= 1
    else:
        print('Por favor, digitar um número inteiro!')
        print()
        count -= 1

print()
print(f'Você acertou {acertos} dentro de {len(perguntas)} perguntas.')

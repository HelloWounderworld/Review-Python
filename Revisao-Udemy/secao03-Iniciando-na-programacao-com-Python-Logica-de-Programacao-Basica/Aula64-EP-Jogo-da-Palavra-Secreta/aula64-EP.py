"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
secret_word = 'Leonardo Takashi Teramatsu'
exibe_palavra = ''
numero_tentativas = 0
deseja_continuar = ''

for i in secret_word:
    if i == ' ':
        exibe_palavra += i
    else:
        exibe_palavra += '*'

while True:
    
    letra = input('Digite uma letra: ')
    numero_tentativas += 1
    
    if len(letra) > 1 or letra == ' ' or letra == '':
        print('Por favor, digite apenas uma letra diferente de espaço e vazio!')
        continue

    if letra.lower() in secret_word.lower():
        for i in range(len(secret_word)):
            if secret_word[i].lower() == letra.lower():
                troca = f'{exibe_palavra[:i]}{secret_word[i]}{exibe_palavra[i+1:]}'
                exibe_palavra = troca
            
    print(f'Letra formatada: {exibe_palavra}')
    
    if secret_word == exibe_palavra:
        print('Parabéns! Vc completou a palavra secreta!')
        print(f'A palavra era {secret_word}!')
        print(f'Depois de {numero_tentativas}x tentativas!')
        while True:
            deseja_continuar = input('Deseja continuar? [s]im ou [n]ão: ')
            if deseja_continuar == 's':
                secret_word = input('Redefinindo a palavra secreta: ')
                exibe_palavra = ''
                numero_tentativas = 0
                for i in secret_word:
                    if i == ' ':
                        exibe_palavra += i
                    else:
                        exibe_palavra += '*'
                break
            elif deseja_continuar == 'n':
                print('Até a próxima!')
                break
            else:
                print('Por favor, selecionar apenas \'s\' ou \'n\'.')
                continue
    if deseja_continuar == 'n':
        break

def find(n,ch):
    x = []
    for letra in n:
        if letra == ch:
            x.append(letra)
    return print("Essa frase possui {} o caractere '{}'". format(len(x),ch))

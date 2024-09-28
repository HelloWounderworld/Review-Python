# Aula 32 - Interpolação de string com % em Python:
Vamos ver sobre a interpolação de string com % em Python.

Basicamente, a interpolação é o mesmo que realizamos com o format antes, só que por via de uma sintaxe diferente

    """
    Interpolação básica de strings
    s - strings
    d e i - int
    f - float
    x e X - Hexadecimal (ABCDEF0123456789)
    """
    nome = 'Leonardo'
    preco = 1000.95897643
    # em % expressando a variável, se tiver somente uma variável
    # não precisa colocar () para especificar cada uma
    variavel1 = 'Meu nome é %s' %nome
    # variavel = '%s, o preco total foi R$ %f' %(nome, preco)
    variavel = '%s, o preco total foi R$ %.2f' %(nome, preco)
    print(variavel)
    print(variavel1)

No caso, é uma outra forma de conseguirmos colocar os valores das variáveis dentro de uma string.

O Hexadecimal é o mesmo uso

    print('O hexadecialm de %d é %x' %(15,15))
    print('O hexadecialm de %d é %04x' %(15,15))
    print('O hexadecialm de %d é %04x' %(1500,1500))
    print('O hexadecialm de %d é %08x' %(1500,1500))

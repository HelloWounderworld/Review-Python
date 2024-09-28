# Aula 40 - id - A identidade do valor que está na memória:
No caso, sempre que criamos alguma variável e queremos verificar se tal variável está guardada na memória, podemos ver isso vasculhando um identificador único, id.

Toda variável e valores tem esse identificador único, donde pode ser expresso usando a função id()

    v1 = 'a'
    print(id(v1))
    print(id(1))

Daí, note que, se colocarmos duas variáveis com mesmos valores o identificadores serão os mesmos, pois estão apontando para o mesmo valor

    v1 = 'a'
    v2 = 'a'
    print(id(v1))
    print(id(v2))
    print(id(1))

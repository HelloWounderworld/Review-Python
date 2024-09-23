# Aula 07 - Mantendo estados dentro da classe:
Bom, uma das caracteristicas muito legal de uma programacao orientada a objetos, seria que as suas instancias poderiam carregar os seus estados.

No caso, como podemos ver no exemplo

    class Camera:
        def __init__(self, nome, filmando=False):
            self.nome = nome
            self.filmando = filmando

        def filmar(self):
            print(f'{self.nome} esta filmando...')
            self.filmando = True

    c1 = Camera('Canon')
    c2 = Camera('Sony')

    c1.filmar()
    print(c1.filmando)
    print(c2.filmando)

Como podemos ver abaixo, no print(C1.filmando) e print(C2.filmando), podemos ver que e devolvido True e False, respectivamente. Ou seja, isso significa que o estado da instancia, filmando, foi guardado, depois que foi acionado o metodo, filmar, que muda o valor desse atributo de False para True e ela mantem mesmo depois disso.

Bom, podemos melhorar mais ainda a qualidade desse metodo para conseguirmos verificar se a camera ja esta no estado de gravacao

    class Camera:
        def __init__(self, nome, filmando=False):
            self.nome = nome
            self.filmando = filmando

        def filmar(self):
            if self.filmando:
                print(f'{self.nome} ja esta filmando...')
                return

            print(f'{self.nome} esta filmando...')
            self.filmando = True

    c1 = Camera('Canon')
    c2 = Camera('Sony')

    c1.filmar()
    print(c1.filmando)
    print(c2.filmando)

Bom, como podemos ver, acima, testando ela, fica mais nitido ainda a caracteristica de que o estado de uma instancia estar sendo mantido.

Agora, vamos acrscentar mais um metodo, fotografar. Nela, podemos aproveitar algumas condicoes que foi criado no metodo, filmar

    class Camera:
        def __init__(self, nome, filmando=False):
            self.nome = nome
            self.filmando = filmando

        def filmar(self):
            if self.filmando:
                print(f'{self.nome} ja esta filmando...')
                return

            print(f'{self.nome} esta filmando...')
            self.filmando = True

        def fotografar(self):
            if self.filmando:
                print(f'{self.nome} nao pode fotografar filmando...')
                return
            
            print(f'{self.nome} esta fotografando...')
            self.filmando = True
            
    c1 = Camera('Canon')
    c2 = Camera('Sony')

    c1.filmar()
    c1.filmar()
    c1.fotografar()
    print(c1.filmando)
    print(c2.filmando)

Bom, claro, depois de feito o metodo acima, falta criar um outro metodo que desative o modo de filmagem, entao vamos precisar criar o seguinte metodo

    class Camera:
        def __init__(self, nome, filmando=False):
            self.nome = nome
            self.filmando = filmando

        def filmar(self):
            if self.filmando:
                print(f'{self.nome} ja esta filmando...')
                return

            print(f'{self.nome} esta filmando...')
            self.filmando = True

        def parar_filmar(self):
            if not self.filmando:
                print(f'{self.nome} nao esta filmando...')
                return

            print(f'{self.nome} esta parando de filmar...')
            self.filmando = False

        def fotografar(self):
            if self.filmando:
                print(f'{self.nome} nao pode fotografar filmando...')
                return
            
            print(f'{self.nome} esta fotografando...')
            self.filmando = True
            
    c1 = Camera('Canon')
    c2 = Camera('Sony')

    c1.filmar()
    c1.filmar()
    c1.fotografar()
    c1.parar_filmar()
    c1.fotografar()
    # print(c1.filmando)
    # print(c2.filmando)

Bom, como podemos ver, conseguimos criar a funcionalidade basica de uma camera atraves de uma classe.
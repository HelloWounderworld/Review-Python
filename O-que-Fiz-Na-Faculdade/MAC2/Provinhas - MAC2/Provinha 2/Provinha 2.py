class Estudante:
    def __init__(self,nome,nusp):
        self.nome = nome #Isso cria um atributo nome, pois utilizei o self - linha 1
        self.nusp = nusp #Isso cria um atributo nusp, pois utilizei o self - linha 2

class Relogio1:
    def __init__(self, horario):
        self.horario = horario
        horario = '07h 30m'
    def mostre(self):
        #horario = '07h 30m'
        print(self.horario)

class Relogio2:
    def __init__(self, horario):
        self.horario = horario
    def mostre(self):
        print(horario) 
        
class Relogio3:
    def __init__(self, horario):
        self.horario = horario
    def mostre(self):
        print(self.horario)

def main():
    print("In [1]: relogio1 = Relogio1('06h 30m')\nIn [2]: relogio1.mostre()")
    relogio1 = Relogio1('06h 30m')
    print("Resposta")
    relogio1.mostre()
    print("Note que, na classe Relogio1 dentro do metodo 'mostre'\nesta definido uma variavel 'horario = 07h 30m', onde ao realizar a chamada\ndesse metodo o atributo chamado no print nao e afetado, ou seja, como o atributo esta sendo guardado no init\nmesmo que eu defina uma variavel onde tenha em comum o nome daquilo que\nfoi atribuido, e colocando um outro valor nessa variavel, o atributo nao e afetado\nO mesmo vale para caso seja feito o mesmo no init")
    print()
    print("In [3]: horario = '03h 45m'\nIn [4]: relogio2 = Relogio2('09h 30m')\nIn [5]: relogio2.mostre()")
    #horario = '03h 45m'
    #relogio2 = Relogio2('09h 30m')
    #print(relogio2.mostre())
    print("Vai dar bezu")
    print("Aqui deu erro, pois na class Relogio2 no metodo mostre\no que esta sendo chamado no print nao e um atributo que esta guardado no \ninit,e sim, e uma variavel nao definida, no caso o 'horario'\nque apareceu nesse metodo nao carrega nenhum atributo ou algum valor")
    print()
    print("In [6]: sp_hor = Relogio3('16h 30m')\nIn [7]: ms_hor = sp_hor|\nIn [8]: ms_hor.horario = '15h 30m'\nIn [9]: sp_hor.mostre()")
    sp_hor = Relogio3('16h 30m')
    ms_hor = sp_hor
    ms_hor.horario = '15h 30m'
    print("Resposta: ")
    sp_hor.mostre()
    print("Aqui a situacao e mais interessante ainda\npois esta sendo feita uma copia raza de uma variavel que carrega o objeto criado pela classe Relogio3\ndonde a copia raza, que tbm carrega o mesmo objeto, esta chamando exatamente o atributo 'self.horario', onde este guarda o valor instanciado pelo 'sp_hor',\ndentro da classe init por fora, usando o comando '.horario' no objeto no caso no 'ms_hor'\nmas como este e uma copia raza, entao caso eu chamar o metodo 'mostre()' para a variavel sp_hor, essa tera a sua instancia mudada exatamente para o valor que foi atribuido para 'ms_hor.horario'")
    print()
    print("In [10]: type(ms_hor)\nOut[10]: Relogio3 ")
    print(type(ms_hor))
main()
    

'''
Questão 1. Qual método é executado quando fazemos f = Fracao(4,3)?

Resposta: __init__()

Questão 2. Qual método da classe de um objeto obj é executado quando fazemos print(obj)?

Resposta: __str__() 

Questão 3. A classe Estudante a seguir tem os atributos (de estado) nome e nusp.

Qual é o comando na linha 1?

Resposta: self.nome = nome

Qual é o comando na linha 2?

Resposta: self.nusp = nusp 

Questão 4. Suponha que o Python tenha lido todas as classes a seguir (teclamos F5 no spyder). 

A seguir está uma transcrição de uma seção do Python Shell. Complete as três primeiras lacunas com o valor exibido pelo método mostre() e a última com o resultado da expressão. Como sempre, se ocorrer um erro, escreva apenas ERRO.

In [1]: relogio1 = Relogio1('06h 30m')

In [2]: relogio1.mostre()

Resposta: 06h 30m

In [3]: horario = '03h 45m'

In [4]: relogio2 = Relogio2('09h 30m')

In [5]: relogio2.mostre()

Resposta: ERRO

In [6]: sp_hor = Relogio3('16h 30m')

In [7]: ms_hor = sp_hor|

In [8]: ms_hor.horario = '15h 30m'

In [9]: sp_hor.mostre()

Resposta: 15h 30m

In [10]: type(ms_hor)

Out[10]: Relogio3 
'''

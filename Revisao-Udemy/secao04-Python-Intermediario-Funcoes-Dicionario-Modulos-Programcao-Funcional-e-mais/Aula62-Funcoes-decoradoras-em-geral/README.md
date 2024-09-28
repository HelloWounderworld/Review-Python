# Aula 62 - Funções decoradoras em geral:
Vamos aprender sobre funções decoradoras e decoradores.

Basicamente, funções decoradoras/decoradores, como o nome já disse, são funções que decora outras coisas. No caso, sempre que vc estiver utilizando essa função decoradora, vc estará recebendo essa coisa e decorando essa coisa e mudando o valor dela, ou não, ou nem retornando nada.

    Decorar = Adicionar / Remover/ Restringir / Alterar

Vamos começar com um exemplo básico

    def inverte_string(string):
        return string[::-1]

    invertida = inverte_string('Leonardo')
    print(invertida)

Lembre-se, em programação, uma boa prática fundamental no processo de compilação e eficiência está no quesito de obedecer a regra "Princípio de Responsabilidade Única (Single Responsability Principle - SRP)". Em outras palavras, se um determinado objeto está fazendo mais do que o necessário, então está errado. Você precisa dividir esse objeto de modo que separe cada finalidade para cada lugar, de forma organizada.

No caso, esse conceito um pouco avançado, como quero colocar isso aqui no exemplo que demos acima. No caso, suponhamos que no lugar de uma string colocamos uma numeração

    def inverte_string(string):
        return string[::-1]

    invertida = inverte_string(123)
    print(invertida)

Com certeza, isso iria resultar em um erro. Masl, então, como iremos tratar? Seguindo a definição do SRP, teríamos que criar mais uma função que trate, especificamente, esse problema, como seguinte

    def criar_funcao(func):
        def interno(*args, **kwargs):
            print('Vou te decorar!')
            for arg in args:
                is_string(arg)
            resultado = func(*args, **kwargs)
            print('Ok, agora você foi decorado!')
            return resultado
        return interno
    
    def inverte_string(string):
        return string[::-1]

    def is_string(param):
        if not isinstance(param, str):
            raise TypeError('param deve ser uma string')

    inverte_string_checando_parametro = criar_funcao(inverte_string)
    invertida = inverte_string_checando_parametro(123)
    print(invertida)

E é aqui, o momento que entra em jogo a prática da função decoradora. No caso, estamos decorando uma função via "criar_funcao".

O estudante poderia muito bem pensar o seguinte "Ué? Não bastava colocar um if dentro da função inverte_string? Qual é a finalidade de ter que usar uma função decoradora?"

Bom, a resposta para essa pergunta está que ela serviu, antes do passo de executar definitivamente a função, se todos os critérios estão satisfeitos, o que difere de realizar a tal conferencia dentro da execução da função. A vantagem disso, está em otimizar o processo sem a necessidade de ter que compilar uma função, visto que algumas hipóteses não está sendo satisfeitas.

Link para leitura:

    https://www.hashtagtreinamentos.com/decorators-no-python?gad=1&gclid=CjwKCAjwg4SpBhAKEiwAdyLwvAFakfQTcdMgNmUSBm-C9p2qBeA-S3SJLyGWaLH2Cv6wCXME1rBUWRoCV9EQAvD_BwE
    
    https://pt.stackoverflow.com/questions/23628/como-funcionam-decoradores-em-python

    https://www.datacamp.com/tutorial/decorators-python

    https://www.geeksforgeeks.org/decorators-in-python/

Link para leitura - SRP:

    https://www.freecodecamp.org/news/solid-principles-single-responsibility-principle-explained/#:~:text=The%20Single%20Responsibility%20Principle%20(SRP,only%20one%20reason%20to%20change%22.&text=The%20class%20above%20violates%20the%20single%20responsibility%20principle.

    https://en.wikipedia.org/wiki/Single-responsibility_principle

    https://www.devmedia.com.br/arquitetura-o-principio-da-responsabilidade-unica/18700#:~:text=O%20Mandamento%20do%20princ%C3%ADpio%20da,ela%20n%C3%A3o%20segue%20este%20princ%C3%ADpio.

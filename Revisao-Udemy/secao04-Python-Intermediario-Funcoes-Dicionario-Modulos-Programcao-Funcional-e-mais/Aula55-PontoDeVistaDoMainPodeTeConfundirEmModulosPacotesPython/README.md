# Aula 55 - O ponto de vista do __main__ pode te confundir em módulos e pacotes Python:
Bom, nas últimas 4 aulas, vire e mexe estávamos insistindo de que sempre, mas sempre, o primeiro arquivo que é executado é o __main__, que é o arquivo que estará no nível mais alto e o primeiro que será sempre executado. Basta criarmos um arquivo aula55.py, que será o nosso arquivo main, e então colocarmos nela

    print(__name__)

Agora, vamos criar uma pasta "aula55_p" e dentro dela criamos dois arquivos "modulo.py" e "modulo_b.py".

Mas, primeiro, para entendermos melhor sobre o ponto de vista de "__main__". Ao analisarmos o sys.path do main sempre ela é mostrado de onde ela está sendo chamado. Mas existe uma outra forma de analisarmos isso tbm, que é usando o Python path. Basta jogar no terminal no diretório em que está o arquivo aula55.py, o comando

    python --help

Nela vc procura pelo nome "PYTHONPATH" e estará explicando o que estará sendo usando para identificar a path. Estará escrito "sys.path".

Bom, um cenário usual dentro de um pacote, aula55_p, é que dentro dela tenha mais e mais módulos. É muito difícil ver um pacote com apenas um único módulo. No caso, no módulo, modulo_b.py, vamos definir uma função

    def fala_oi():
        print('Hello WounderWorld!')

E esse módulo, poderia ser chamado por um outro módulo, modulo.py. Bastaria importar da forma usual

    from modulo_b import fala_oi

Agora, ao chegarmos no arquivo main, aula55.py, se tentarmos importar o módulo, modulo.py, vamos ter o seguinte

    from aula55_p.modulo import fala_oi

    print(__name__)

Você verá que teremos a opção de importar o "fala_oi" que é a função definida no módulo, modulo_b.py.

Por hora, vamos definir uma função simples dentro do módulo, modulo.py

    def soma_do_modulo(x, y):
        return x + y

Vamos tentar importar essa função acima junto com o, from modulo_b import fala_oi, no arquivo main, aula55.py

    from aula55_p import soma_do_modulo

    print(__name__)

E dessa forma tentamos compilar o arquivo. Você verá que o mesmo erro irá acontecer de quando tentamos compilar na forma, from aula55_p.modulo import fala_oi

    ModuloNotFoundError: No module named 'modulo_b'

O motivo desse erro acontecer, seria por conta de que, quando tentamos importar pela forma, from aula55_p,modulo import soma_do_modulo, do ponto de vista do arquivo main, aula55.py, visto que o módulo, modulo.py, está importando um outro modulo do mesmo nível dele, o main tentará importar o outro módulo que está sendo importando pelo módulo que o main está importando. Ou seja, se dentro dos módulos existentes dentro desse pacote, existir algum modulo que importa um outro modulo do mesmo nível, mas do ponto de vista desse módulo que esteja dentro do pacote, ao tentarmos importar esse módulo dentro desse pacote do ponto de vista do main, o mesmo irá tentar importar até o módulo que está sendo importado pelo módulo que o main está importando.

Portanto, para evitar que tais erros aconteça, sempre que formos importar algo de um modulo para outro temos que considerar do ponto de vista do main, neste caso a aula55.py. Assim, no módulo, modulo.py, vamos ter que realizar a seguinte alteração

    from modulo_b import fala_oi -> 
    
Assim, ao compilarmos o main, aula55.py, aquele erro não irá ser mais exibido e conseguimos carregar todos os módulos.

Temos a opção de conseguirmos, no modulo.py, simplesmente colocar apenas o ponto, em vez do nome da pasta inteira

    from .modulo_b import fala_oi

Porém, para possibilitar isso, precisamos realizar uma alteração no setting.json do Python da seguinte forma

    "[python]": {
    "editor.defaultFormatter": "ms-python.python",
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "editor.insertSpaces": false,
    "editor.formatOnSave": true
    // "editor.codeActionsOnSave": {
    //   "source.fixAll": true,

Entretanto, por hora, vamos deixar do jeito que está para melhor conseguirmos entender o conceito.

Link para leitura

    https://docs.python.org/pt-br/3/library/__main__.html
    https://docs.python.org/3/reference/import.html

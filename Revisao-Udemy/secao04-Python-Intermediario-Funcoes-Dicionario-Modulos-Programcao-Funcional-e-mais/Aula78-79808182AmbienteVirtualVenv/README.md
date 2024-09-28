# Aula 78 e 79 - O que são ambientes virtuais? (venv) Como criar o seu ambiente virtual com venv:
Foi lançado recentemente (eu tô vendo essa aula em 06/11/2023, então não sei especificamente o quanto foi recente) um módulo no Python chamado venv que é própriamente para criar o ambiente virtual em Python. Claro, segundo o professor, Luiz Otávio Miranda, diz que na área de tecnologia frequentemente quando vem novidades na linguagem está atrelado aos novos módulos ou bibliotecas, porém, precisa ter um cuidado nisso, pois existem módulos ou bibliotecas que não dão continuidade ao ponto de tornarem obsoletos no meio do processo. Então, é recomendável que ao longo do processo de atualização do que vem de novidade na tecnologia em seus estudos, quando está sendo lançado um novo módulo ou biblioteca, que o estudante seja cauteloso em verificar se ela é promissora ou não deixando no ar por hora antes mesmo de implementar ela de forma oficial em seus projetos importantes.

Agora, o venv, segundo o professor, Luiz Otávio Miranda, é um módulo novo do Python que chegou para ficar pois ela será usada para criar ambientes virtuais que é usado até em frameworks do Python chamado Django para a pessoa conseguir trabalhar com frontEnd usando a linguagem Python como base.

Vantagens do venv, ela é que nem Docker. No caso, se por acaso vc estiver trabalhando num projeto que vc já trabalhou anos atrás e o cliente pedir para melhorar ela ou corrigir uns bugs, as versões dos pacotes que vc havía usado vc não irá precisar baixar na sua máquina toda tornando ela desnecessariamente pesado. Mas, sim, sem a necessidade de instalar as versões dos pacotes antigos na sua máquina, vc poderá criar um ambiente virtual e dentro dela instalar as versões antigas dos pacotes que serão necessário e nela rodar o projeto antigo para realizar as devidas melhorias nela.

O ambiente virtual venv, para o sistemas operacionais Linux e MacOS, são as mesmas. Porém, para o Windows, ela tem suas peculiaridades para possibilitar nos seus funcionamentos.

A máquina que eu uso, o OS dela, é Linux Ubuntu. Caso o estudante esteja utilizando o Windows, recomendamentos seguir a seguinte documentação:

    https://docs.python.org/pt-br/dev/library/venv.html

    https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html

Agora, para quem for usuário de Linux ou MacOS, como no meu caso, vamos seguir com o seguinte script para conseguirmos criar o ambiente virtual.

Primeiro, vamos executar o seguinte comando para verificarmos a versão do Python

    python -V ou python3 - V

Depois que fizermos isso, realizamos o seguinte

    python -m venv (nome do ambiente) ou python3 -m venv (nome do ambiente)

Nesse curso, no caso, foi colocado o "nome do ambiente" como "ambiente" sem os parênteses.

Assim, conseguimos ver que foi criado uma pasta chamado "ambiente".

Para procurarmos o executável, onde está o ambiente virtual que pode ser execudado, usamos o seguinte comando. Funciona apenas no PowerShell.

    gcm python ou gcm python -Syntax

No caso de Linux ou MacOs é

    which python ou which python3

No meu caso, foi retornado

    /usr/bin/python3

Se colocarmos

    /usr/bin/python3 -V

Será o mesmo que

    python3 -V

Bom, essa aula só foi para conseguirmos criar o ambiente virtual.

Qualquer coisa, recomendamos que o aluno pegue a leitura do README.md da pasta raiz desse repositório e realize as devidas instalações necessárias para, depois, voltar nesse curso.

Seguir link para leitura e aplicação:

    https://docs.python.org/3/library/venv.html

    https://docs.python.org/pt-br/3/library/venv.html

    https://csguide.cs.princeton.edu/software/virtualenv#:~:text=A%20Python%20virtual%20environment%20(venv,installed%20in%20the%20specific%20venv.

# Aula 80 - Ativando e desativando o meu ambiente virtual venv:
Vamos aprender a ativar e desativar o ambiente virtual que criamos na aula anterior.

No caso, o tipo de path que será colocado, depende de cada pessoa da forma como está seguindo esse curso e onde está guardando a pasta do ambiente virtual. Logo, identificado a path necessária, onde está o ambiente, bastaria colocar a seguinte path (Novamente, estou fazendo pelo Linux. No Windows, isso muda.)

    . ambiente/bin/activate ou source ambiente/bin/activate

Para desativar o ambiente virtual, será o seguinte comando

    deactivate

Detalhe!! Essa parte do curso de saber configurar o ambiente virtual é de extrema importância. Logo, recomendamos que o aluno dê um gás nesse curso de forma que não deixe nenhuma dúvida à respeito. E, se necessário, refaça todas as configurações do ambiente, passo a passo, de novo, para se certificar que está sabendo como fazer tudo.

Irei atualizar a versão do meu Ubuntu de 20.04 para 22.04! (19/11/2023)

Foi feito a devida atualização, então vamos prosseguir com o curso.

# Aula 81 - pip - instalando pacotes e bibliotecas:
Vamos aprender a instalar e desinstalar os pacotes dentro do ambiente virtual venv. No caso, usaremos o "pip" para realizar isso. O "pip" é a versão "npm" que é usado muito para linguagem JavaScript nos seus respectivos frameworks para possibilitar nas instalações de pacotes. Ou seja, o "pip" é um instalador de pacotes python. Um exemplo, o django, ele não vem junto com o Python. Caso vc quiser aprender sobre Django, teremos que instalar a parte tal pacote.

Na pasta, ambiente, criado pelo venv na última aula, vamos realizar tais procedimentos.

Com o ambiente virtual, ambiente, ativo, vamos instalar um pacote como experimento. Colocamos o seguinte comando

    pip install pymysql

Vc verá que que esse "pymysql" será instalado ao olharmos na pasta "site-packages" que é onde fica guardado os pacotes dentro do ambiente virtual. Feito isso, no "main.py", podemos importar esse pacote

    import pymysql

Podemos ver que o programa não estranha a importação desse pacote, visto que temos ela instalado.

Não vamos usar esse pacote, ela só foi um exemplo para tal finalidade.

Uma outra forma de instalarmos algum pacote seria colocando "python -m" antes do comando que colocamos acima para o "pip"

    python -m pip install pymysql

e é até recomendável realizar essa forma de instalação.

O motivo disso, seria que, até o instalador "pip" ela passa por um processo de atualização, assim como ocorre para o "npm". Logo, existem casos em que, usando somente o "pip" não conseguimos realizar a instalação ou até mesmo no aumento da versão de algum pacote, por conta do próprio instalador "pip" estar esatualizado na sua versão. Por isso que é recomendável que usemos "python -m" antes do "pip".

Caso vc queira atualizar a versão do "pip" realizamos o seguinte

    pip install pip --upgrade ou python -m pip install pip --upgrade

Agora, como desinstalamos usando o "pip"? Bom, não tem muito segredo, usando do pacote "pymysql" de exemplo, colocamos o seguinte

    pip uninstall pymysql

Isso irá realizar a desinstalação do pacote "pymysql". No meio do processo de desinstalação, será perguntado se quer mesmo desinstalar tal pacote e vc pode colocar como "Y" (yes). Porém se vc quiser pular tal etapa, podemos acrescentar, no último comando acima, o seguinte

    pip uninstall pymysql -y

donde "-y" indica "yes".

Depois que vc desinstala o "pymysql" no arquivo "main.py", podemos ver que o "import pymysql" exibirá um erro de não reconhecimento da existência desse pacote. Qualquer coisa, basta executar para ficar claro que o tal "import pymysql" não está reconhecendo a existência do pacote. Daí, instala novamente o mesmo pacote e execute novamente o mesmo arquivo.

Caso vc queira analisar, via terminal no ambiente virtual ativo, o pacotes que estão instalados, bastar da o comando

    pip freeze

Ela irá mostrar os pacotes instalados com os respectivos versões de cada pacote.

Claro, da mesma forma que conseguimos realizar pelo "npm", podemos usar o "pip" para instalar algum pacote com a sua respectiva versão.

Caso vc queira consultar quais tipos de versões um determinado pacote possui bastaria colocar o seguinte

    pip index version "nome do pacote" (pymysql)

No caso, acima, iremos conseguir consultar todas as versões disponíveis de "pymysql" ao colocarmos esse nome do pacote no lugar do "nome do pacote".

Dentro dessa lista de versões, por exemplo, existe a versão 0.3, podemos tentar instalar o pacote "pymysql" com a versão "0.3" como seguinte, claro, depois que vc desinstala o pacote atual

    pip install pymysql==0.3

No meu caso deu erro de "metada", vamos tentar uma outra, a penúltima versão, por exemplo, "1.0.1"

    pip install pymysql==1.0.1

Bom, no meu caso, ela instalou. Ao darmos o "pip freeze" será exibido o pacote "pymysql" com a versão que foi escolhida para ser instalado. Daí, se quisermos atualizar a versão do pacote "pymysql" podemos colocar o seguinte

    pip install pymysql --upgrade

Daí, novamente, damos o "pip freeze" e conseguimos ver que foi atualizado para a versão mais recente.

Bom, até agora, além de instalação, pedimos várias vezes em utilizar o comando "pip freeze". Isso tem sim um motivo. É com esse "pip freeze" que iremos criar um arquivo chamado "requirements.txt", que é como se fosse o "package.json" que temos nos framework do JavaScript e que, em seguida, sempre que baixamos algum projeto JavaScript nas nossas máquinas, para possibilitar em rodar o projeto nas nossas máquinas, precisamos colocar o comando "npm i" ou "npm install" que esse comando irá ler o "package.json" para instalar os pacotes nececessários para possibilitar em rodar o projeto. O "requirements.txt" não muda nada. Em algum projeto na linguagem python, tendo esse arquivo, iremos usar o instalador "pip" para conseguirmos baixar e instalar os pacotes necessários para que possibilite que o mesmo projeto rode na máquina de outra pessoa.

Obs: inclusive é recomendável que a pessoa coloque no gitignore a pasta do ambiente virtual criada. Já tive problema de subir o "ambiente" e tentar baixar em uma outra máquina dando "git clone" e não baixar tudo por conta de algumas falhas nas dependências.

Seguir o link para saber mais sobre pip:

    https://pypi.org/

# Aula 82 - Criando e usando um requirements.txt:
Como dito na última aula, vamos falar sobre esse arquivo "requirements.txt". Ela serve como uma espécie de script do que seria preciso para que uma outra pessoa consiga rodar o seu projeto python em alguma outra máquina. Em vez de enviarmos a pasta "ambiente" criado pelo "venv" inteirinho, usando esse arquivo txt e tendo em mãos o conhecimento dos instaladores "pip" será possível, de forma mais leve, que a pessoa consiga subir o seu projeto no repositório git ou até mesmo enviar para a outra máquina.

Bom, a ideia é que esse arquivo "requirements.txt" sejá criado depois que vc fizer tudo o que vc precisa no seu projeto, instalando um monte de pacotes. Claro que vc não irá mandar a pasta "ambiente" inteiro para a pessoa ou subir para o seu repositório, pois seria muito pesado. No lugar disso, vc irá mandar para a pessoa esse arquivo "requeriments.txt" com os códigos que vc criou para, quando a pessoa baixar na máquina dela esses dois elementos, bastaria usar o instalador "pip" para conseguir configurar o mesmo ambiente do seu projeto para ele conseguir rodar na máquina dele.

O comando para conseguirmos criar o tal arquivo txt é

    pip freeze > requirements.txt

Note que, isso gerou um arquivo txt com o nome de requirements.

Como teste, apaga a pasta "ambiente" que foi criado pelo "venv". Daí, no ambiente global, se colocarmos o comando "pip freeze" veremos que o tal comando não estará sendo reconhecido. Ou se tiver o instalador configurado na sua máquina, esse instalador estará correspondendo para o ambiente global, então não seria nem um pouco recomendável vc instalar os pacotes que estiver mostrando dentro do requeriments.txt, pois isso poderá zuar os outros projetos seu. É por isso que temos o ambiente virtual, pois é dentro dela que iremos instalar os pacotes necessário de forma independente sem que afete outros projetos.

Logo, antes de acionarmos a instalação dos pacotes que estiver dentro do arquivo "requeriments.txt", primeiro, como uma boa prática, vamos criar um ambiente virtual

    python3 -m venv venv (coloque o nome que vc quiser do ambiente)

Em seguida, ativamos esse ambiente virtual

    source venv/bin/activate
    
Logo, finalmente, iremos instalar os pacotes que estiverem indicados dentro do requirements.txt com o seguinte comando

    pip install -r requeriments.txt

Assim, se dermos, agora, o "pip freeze", novamente, vemos que o que estiver dentro do requeriments.txt (errei no inglês requirements rsrs) estará instalado.

# Review-Python
Esse repositório será uma revisão minha da linguagem python que aprendi na faculdade, durante o meu curso de Matemática Pura. Irei usar um curso da Udemy, Curso de Python 3 do Básico Ao Avançado (com projetos reais), para revisão de conceitos.

Conforme o meu progresso na revisão, irei reviver os meus códigos que eu criei no passado, no intuito de exercer as minhas skills sobre essa linguagem de programação.

## Referência:
Usarei as seguintes referências:

- Curso Udemy, Curso de Python 3 do Básico Ao Avançado (com projetos reais), Luiz Otávio Miranda.

- Lógica de Programação: A construção de algoritmos e estruturas de dados, ANDRÉ WIZ VILLAR FORBELLONE e HENRI FREDERICO EBERSPACHER.

- Problem Solving with Algorithms and Data Structures using Python - Second Edition, Bradley N. Miller e David L. Ranum.

- Fluent Python - Luciano Ramalho. 

Tais referências, em livros, citados acima serão lidos, em paralelo, conforme o conceito revisado pelo curso da Udemy na expectativa de me aprofundar mais ainda no conceito.

Outras referências complementares que irei lendo por fora, independente de qual linguagem de programação que eu esteja estudando, mas que são bons serem citados para o desencargo de consciência:

- Introduction to Algorithms, Fouths Edition. Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein

- The Self-Taught Computer Scientist - The beginner’s guide to
data structures algorithms, Cory Althoff.

- Clean Code, A Handbook of Agile Software Craftsmanship, Robert C. Martin.


## Recursos para revisar a linguagem de programação Python:
Utilizei o editor de código VSCode (Visual Studio Code), da Microsoft, e usei a linguagem Git, para o controle de versionamento ao meu repositório GitHub.

A versão do python que foi usado para essa revisão é o python3. Precisaria instalar ela pelo terminal, visto que o meu sistema operacional é Linux Ubuntu versão 20.04, caso não tenha sido instalado ainda, https://www.itsupportwale.com/blog/how-to-upgrade-to-python-3-10-on-ubuntu-18-04-and-20-04-lts/. Mas vamos tbm precisar de mais alguns pacotes python para ser instalado:

    sudo apt-get install python3.11-dev python3.11-full

Além disso, vamos precisar instalar um conjuto de pacotes que não são python:

    sudo apt-get install curl build-essential gcc make default-libmysqlclient-dev libssh-dev

Agora, para testar se conseguimos ativar o python em um ambiente virtual:

    - Criar um diretório "teste" e entrar nesse diretório pelo terminal

    - Rodar o comando python3 -m venv (algum nome que vc queira)

    - "source (nome colocado)/bin/activate" ou ". (nome colocado)/bin/activate".

    - Agora, ao digitarmos dentro desse ambiente virtual "python --version" irá mostrar a mesma versão do python em que vc está trabalhando.

    - Para mais detalhes podemos digitar "which python".

Visto que o ambiente virtual, teste, está funcionando, então sempre que fizermos alguma instalação dentro desse ambiente virtual, a tal instalação, será guardado de forma particular para esse ambiente virtual. Para conferir isso bastaria entrar na sua pasta/ambiente virtual -> lib -> python(sua versao) -> site-packages, dentro desse diretório que virá qualquer instalação que vc fizer dentro desse ambiente virtual. Experimente:

    - pip install pymysql

    - caso não reconhça o comando pip, precisaria dar um upgrade para permitir o tal comando, "python -m pip install pip --upgrade".

Para desativar o ambiente virtual seria:

    - deactivate

Uma outra coisa que podemos testar, ativando novamente o nosso ambiente virtual, entrando no diretório teste criado, e, fora do diretório teste-inicial, criar um arquivo main.py e dentro desse arquivo, na primeira linha, apenas colocar print(1+1). Assim, acessado o ambiente virtual ativo, jogamos o comando "python main.py". Se retornar um 2, significa que deu certo.

No caso, agora, vc aprendeu em como configurar um ambiente virtual em que iremos trabalhar. Podemos desativar o ambiente virtual e excluir o diretório teste.

No VSCode vamos instalar as seguintes extensões:

- Python - Essa extensão vai te permitir rodar o arquivo python clicando no play do VSCode, visto que vc está dentro do ambiente virtual do python, em vez de ficar toda hora jogando no terminal o comando "python (nome do arquivo).py" dentro do ambiente virtual.

- Code Runner - Uma outra extensão que permite fazer o mesmo que a extensão acima, mas para várias linguagens.

Além disso, no próprio VSCode tem um desenho de uma engrenagem donde vc pode encontrar a opção Settings e, clicando nela, será encaminhado para um arquivo Settings e bastaria clicar, ao lado do play do VSCode, em um desenho de um arquivo que será produzido um arquivo settings.json. Visto que será executado dentro do ambiente virtual.

    {
        "window.zoomLevel": 2,
        "workbench.startupEditor": "none",
        "explorer.compactFolders": false,
        "workbench.iconTheme": "material-icon-theme",
        "editor.fontSize": 18,
        "workbench.colorTheme": "OM Theme (Default Dracula Italic)",
        "code-runner.executorMap": {
            "python": "clear ; python -u",
        },
        "code-runner.runInTerminal": true,
        "code-runner.ignoreSelection": true
    }

Nela, vc poderia configurar o formato como está no json acima.
 
Temos, também, essa configuração.

    {
        "window.zoomLevel": 0,
        "workbench.startupEditor": "none",
        "explorer.compactFolders": false,
        "workbench.iconTheme": "material-icon-theme",
        "editor.fontSize": 12,
        "workbench.colorTheme": "OM Theme (Default Dracula Italic)",
        "code-runner.executorMap": {
            "python": "clear ; python3 -u",
        },
        "code-runner.runInTerminal": true,
        "code-runner.ignoreSelection": true,
        "python.defaultInterpreterPath": "python"
    }

Caso, vc queira executar fora do ambiente virtual.

Agora, temos o tema (opcional) e os ícones, donde vc pode escolher a extensão:

    - Omni Dracula VSCode Theme

    - Material Icon Theme

Agora, temos tudo o que precisamos para começarmos a revisar.

### Aviso:
Se caso o python3.11 não for a versão em que está instalado na sua máquina, sempre que vc terminar de trabalhar com a versão desejada, volte para a versão padrão da sua máquina com o comando:

sudo update-alternatives --config python3

Se não, vc poderá ter problemas de atualizações na sua máquina ou nem mesmo o comando padrão para abrir o terminal não rode.

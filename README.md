# Review-Python
Esse repositório será uma revisão minha da linguagem python que aprendi na faculdade, durante o meu curso de Matemática Pura. Irei usar um curso da Udemy, Curso de Python 3 do Básico Ao Avançado (com projetos reais), para revisão de conceitos.

Conforme o meu progresso na revisão, irei reviver os meus códigos que eu criei no passado, no intuito de exercer as minhas skills sobre essa linguagem de programação.

### Obs:
Lembrando que esse repositório, somente, está voltado para a revisão conceitual da linguagem de programação Python. Logo, frameworks relacionados, como Django, o seu estudo teório, será realizado em outro repositório.

Assim, como projetos usando a linguagem Python ou os seus respectivos frameworks, irei criar repositórios independentes, porém irei mencionar na forma de lista com um breve resumo nos repositórios de estudos teóricos/conceitos.

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

Estarei passando os comandos para conseguirmos configurar o ambiente que precisamos para seguirmos com o curso de programação Python. No caso, o sistema operacional que estou utilizando é Linux Ubuntu 22.04 LTS e nela irei realizar as devidas configurações.

- Abrindo o terminal na pasta raiz colocamos o seguinte comando

        sudo apt-get update -y
        sudo apt-get upgrade -y
        sudo apt-get install git curl build-essential gcc make default-libmysqlclient-dev libssh-dev

- Agora, vamos instalar os pacotes necessários para o Python:

        python3 --version

    O meu caso apareceu "Python 3.10.12". Visto isso seguimos com o seguinte comando

        sudo apt install python3.10-dev python3.10-full

    Em seguida vamos ver se o python está sendo executado pelo bash

        echo $SHELL

    Se aparecer "/bin/bash" é uma evidência de que o python está, sim, sendo executado pelo bash.

    Agora, vamos entrar na área de trabalho

        cd Área\ de\ Trabalho/
        
    Nela vamos criar uma pasta

        mkdir projeto

    Vamos testar um ambiente virtual do Python dentro dessa pasta projetos. Entrando nela "cd projeto" digitamos

        python3 -m venv ambiente

    Ao darmos "ls" no comando, vamos ver que será exibido a pasta com o nome "ambiente". Dentro dessa pasta temos vários executáveis para conseguirmos rodar o projeto python localmente. Vamos ativar o ambiente virtual, você pode optar por um dos dois comandos, estando em projetos

        source ambiente/bin/activate ou . ambiente/bin/activate

    Daí, na minha apareceu o seguinte "(ambiente) leonardo@leonardo-Dell-G15-5520:~/Área de Trabalho/projeto$". Ou seja, é evidência de que o ambiente está ativo. Assim, dentro desse ambiente virtual, não vamos precisar mais digitar "python3" mas sim "python", como teste rode o seguinte comando

        python --version ou python -V

    Para verificar qual python está sendo usado podemos realizar o seguinte

        which python

    O meu apareceu o seguinte "/home/leonardo/Área de Trabalho/projeto/ambiente/bin/python".

    Agora, se quisermos instalar algum pacote, donde todos os pacotes são guardados dentro da pasta "site-packages" que vc consegue acessar pela path "ambiente/lib/python3.10/site-packages", acessa via aplicação mesmo e, não, pelo terminal. Vamos instalar um pacote dentro dela

        pip install pymysql

    Vamos ver que esse novo pacote irá aparecer dentro dessa pasta.

    Caso o terminal te informe que o "pip" está desatualizado, joga o comando

        python -m pip install pip --upgrade

    Agora, para desativar o ambiente virtual do Python o comando é 

        deactivate

- Agora, falta baixar a IDE chamado "VSCode" na sua máquina.

Instalado o VSCode, vamos abrir o projeto via essa IDE.

Uma outra coisa que podemos testar, ativando novamente o nosso ambiente virtual, entrando no diretório teste criado, e, fora do diretório ambiente, criar um arquivo main.py e dentro desse arquivo, na primeira linha, apenas colocar print(1+1). Assim, acessado o ambiente virtual ativo, jogamos o comando "python main.py". Se retornar um 2, significa que deu certo.

No caso, agora, vc aprendeu em como configurar um ambiente virtual em que iremos trabalhar. Podemos desativar o ambiente virtual e excluir o diretório projeto.

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

# Instalando o Pyenv:
Essa seção já é uma seção mais complexa e que pode mudar a configuração da sua máquina. Logo, ela é opcional. Para caso o estudante não quiser se arriscar, só com as configurações acima que fizemos, pode ser continuado o curso sem problema nenhum.

Se for possível, recomendamos que o estudante crie uma máquina virtual com Linux Ubuntu 22.04 e realize tais instalações por lá, para não correr o risco de danificar a configuração da sua máquina e ter que chegar no ponto de formatar ela.

    #!/bin/bash

Executar comandos a seguir para atualizar os pacotes

    sudo apt update -y
    sudo apt upgrade -y

Só o Python

    sudo apt install python3.11-full python3.11-dev -y

Instalar pacotes a seguir

    sudo apt install git curl build-essential dkms perl wget -y
    sudo apt install gcc make default-libmysqlclient-dev libssl-dev -y
    sudo apt install -y zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm \
    libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
    Pyenv
    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    Seguir instruções do Pyenv

## Abaixo tudo é opcional:
Instalar e configurar ZSH

    sudo apt install zsh -y
    chsh -s /bin/zsh
    zsh

Instalar Oh-my-zsh!

    https://ohmyz.sh/

    sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

Instalar Spaceship Prompt

    https://github.com/spaceship-prompt/spaceship-prompt

    git clone https://github.com/spaceship-prompt/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt" --depth=1
    ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"

Mudar ~/.zshrc

    vi ~/.zshrc

Alterar a linha para esta forma -> ZSH_THEME="spaceship"

Instalar Zsh Autosuggestions

    https://github.com/zsh-users/zsh-autosuggestions
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

Instalar Zsh Syntax Highlighting

    https://github.com/zsh-users/zsh-syntax-highlighting
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

Mudar plugins

    plugins=(git zsh-autosuggestions zsh-syntax-highlighting)

Font optional

    (https://github.com/pdf/ubuntu-mono-powerline-ttf)

    mkdir -p ~/.fonts
    git clone https://github.com/pdf/ubuntu-mono-powerline-ttf.git ~/.fonts/ubuntu-mono-powerline-ttf
    fc-cache -vf

Para finalizar

    REBOOT seu sistema!

### obs:
Se caso o python3.11 não for a versão em que está instalado na sua máquina, sempre que vc terminar de trabalhar com a versão desejada, volte para a versão padrão da sua máquina com o comando:

sudo update-alternatives --config python3

Se não, vc poderá ter problemas de atualizações na sua máquina ou nem mesmo o comando padrão para abrir o terminal não rode.

# Projetos que consegui criar:

## Nome do Projeto e as tecnologias usadas nela suas versões e o que precisa para rodar na máquina da pessoa:

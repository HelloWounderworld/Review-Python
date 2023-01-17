# Review-Python
Esse repositório será uma revisão minha da linguagem python que aprendi na faculdade, durante o meu curso de Matemática Pura. Irei usar um curso da Udemy, Curso de Python 3 do Básico Ao Avançado (com projetos reais), para revisão de conceitos.

Conforme o meu progresso na revisão, irei reviver os meus códigos que eu criei no passado, no intuito de exercer as minhas skills sobre essa linguagem de programação.

### Recursos para revisar a linguagem de programação Python:
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

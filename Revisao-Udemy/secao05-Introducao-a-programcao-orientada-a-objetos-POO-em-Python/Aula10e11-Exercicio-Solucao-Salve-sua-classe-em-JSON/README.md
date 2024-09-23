# Aula 10 e 11 - Exercício e Solução - Salve sua classe em JSON + if __name__ == '__main__':
Na aula 87 da secao 04, foi ensinado o conceito de salvar e recuperar os dados em JSON.

Recomendo o estudante revisar o conceito e aplicar nessa aula.

Em Python, a variável especial __name__ é usada para determinar se um script está sendo executado como o programa principal ou está sendo importado como um módulo em outro script. O valor de __name__ é definido automaticamente pelo Python da seguinte forma:

- Se o script está sendo executado diretamente pelo Python (ou seja, não está sendo importado), __name__ é definido como '__main__'.

- Se o script está sendo importado de outro script, __name__ é definido como o nome do módulo sob o qual ele está sendo executado.

## Utilidades de __name__ == '__main__':
- 1. Controle de Execução: Permite que um script tenha partes que sejam executadas apenas quando o script é executado diretamente, e não quando é importado como um módulo. Isso é útil para testes ou quando o script também pode ser usado como um módulo.

- 2. Testes e Debugging: Facilita a escrita de código de teste no mesmo arquivo que o código principal, permitindo que os testes sejam executados apenas quando o arquivo é executado diretamente.

- 3. Organização do Código: Ajuda a manter o código limpo e organizado, separando a funcionalidade do módulo da lógica de execução.

Exemplo de Uso:

    def func():
        print("Função sendo executada")

    if __name__ == '__main__':
        print("Executando como o programa principal")
        func()

Usar __name__ == '__main__' é uma prática comum em Python para facilitar a reutilização de código e a escrita de scripts que são tanto executáveis quanto importáveis como módulos, sem alterar seu comportamento quando são importados.

## Cenarios para comparar:
Vamos considerar um cenário onde temos dois arquivos Python: main.py e module.py. O arquivo module.py contém uma função que queremos usar tanto diretamente quanto importada em outro script. Usaremos __name__ para controlar como o código é executado dependendo de como o script é chamado.

No arquivo, moduleAula1011.py

    def print_message():
        print("Esta função foi chamada de module.py")

    if __name__ == '__main__':
        print("module.py está sendo executado diretamente")
        print_message()
    else:
        print("module.py foi importado")

No arquivo, mainAula1011.py

    import module

    def main():
        print("Esta é a função main de main.py")
        module.print_message()

    if __name__ == '__main__':
        main()

### Cenário 1: Executando module.py diretamente
Quando você executa module.py diretamente usando python module.py, a saída será:

    module.py está sendo executado diretamente
    Esta função foi chamada de module.py

Neste caso, __name__ em module.py é '__main__', então o bloco de código dentro do if __name__ == '__main__': é executado.

### Cenário 2: Importando module.py de main.py
Quando você executa main.py diretamente usando python main.py, a saída será:

    module.py foi importado
    Esta é a função main de main.py
    Esta função foi chamada de module.py

Aqui, module.py é importado, então __name__ em module.py não é '__main__', mas sim 'module'. Isso significa que o bloco if __name__ == '__main__': em module.py não é executado, mas a função print_message() ainda é acessível e usada em main.py.

### Conclusão
Este exemplo mostra claramente como __name__ ajuda a controlar o comportamento do script dependendo de ele ser o ponto de entrada principal ou ser importado como um módulo. Isso permite que o mesmo arquivo funcione tanto como um script independente quanto como um módulo reutilizável em outros scripts, sem interferir na lógica de outros programas que o importam.

# Aula 12 - Curiosidades sobre convenções de nomes:
Como você viu na aula anterior, usamos certas convenções para nomes de variáveis, funções, classes e assim por diante. Essas convenções tem um nome que podemos usar para nos referir ao modo como estamos nomeando determinados objetos em nosso programa: PascalCase, camelCase e snake_case.

PascalCase - significa que todas as palavras iniciam com letra maiúscula e nada é usado para separá-las, como em: MinhaClasse, Classe, MeuObjeto, MeuProgramaMuitoLegal. Essa á a convenção utilizada para classes em Python;

camelCase - a única diferença de camelCase para PascalCase é a primeira letra. Em camelCase a primeira letra sempre será minúscula e o restante das palavras deverá iniciar com letra maiúscula. Como em: minhaFuncao, funcaoDeSoma, etc... Essa conversão não é usada em Python (apesar de eu confundir as duas e às vezes acabar chamando camelCase de PascalCase ou vice-versa, mas agora você sabe a diferença);

snake_case - este é o padrão usado em Python para definir qualquer coisa que não for uma classe. Todas as letras serão minúsculas e separadas por um underline, como em: minha_variavel, funcao_legal, soma.

Os padrões usados em Python são: snake_case para qualquer coisa e PascalCase para classes.
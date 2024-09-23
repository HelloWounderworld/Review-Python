# Aula 14 - @staticmethod (métodos estáticos) são inúteis em Python =):
O decorador @staticmethod em Python é usado para definir um método dentro de uma classe que não opera sobre uma instância da classe nem modifica o estado da classe. Esse método não recebe o primeiro parâmetro automático self (referência à instância) ou cls (referência à classe), que são comuns em métodos de instância e métodos de classe, respectivamente.

## Utilidades do @staticmethod:
- 1. Organização de Código: Permite agrupar funções que têm relevância lógica com uma classe, mas que não precisam acessar ou modificar dados da instância ou da classe.

- 2. Reuso de Código: Facilita a reutilização de métodos, pois eles podem ser chamados tanto a partir da classe quanto de suas instâncias, sem a necessidade de criar um objeto.

- 3. Desacoplamento: Como os métodos estáticos não dependem do estado de uma instância ou da classe, eles promovem um menor acoplamento entre o comportamento do método e os dados da classe/instância.

Obs: Desacoplamento em programação é o processo de projetar sistemas de modo que os componentes individuais sejam o mais independentes possível uns dos outros. Isso significa que mudanças em um componente têm impacto mínimo ou nenhum sobre outros componentes. O desacoplamento facilita a manutenção, o teste, a atualização e a reutilização do código, tornando o sistema mais flexível e robusto. Ele é alcançado através de práticas como o uso de interfaces, injeção de dependências, e padrões de design que promovem a separação de preocupações. Lei de Demeter (Clean Code).

## Exemplo de Uso de @staticmethod:

    class Matematica:
        @staticmethod
        def somar(x, y):
            return x + y

    # Chamando o método estático
    resultado = Matematica.somar(5, 3)
    print(resultado)  # Saída: 8

Neste exemplo, somar é um método estático que realiza uma operação de soma. Ele pode ser chamado diretamente através da classe sem a necessidade de criar uma instância.

## Considerações:
- Quando Usar: Use @staticmethod quando precisar de uma função que não modifica nem acessa variáveis da classe ou instâncias, mas que logicamente pertence à classe.

- Limitações: Métodos estáticos não podem acessar ou modificar o estado da classe ou das instâncias, o que pode ser uma limitação se tal acesso for necessário.

Em resumo, @staticmethod é útil para funções utilitárias ou auxiliares que se relacionam com a classe, mas que operam de forma independente de qualquer estado específico da classe ou de suas instâncias.

## Razões pelas quais @staticmethod pode ser visto como menos útil:
- 1. Sem Acesso ao Estado: Métodos estáticos não podem acessar ou modificar o estado da classe ou das instâncias. Se a funcionalidade requer acesso a esses dados, @staticmethod não seria apropriado.

- 2. Desacoplamento Excessivo: Embora o desacoplamento seja geralmente uma vantagem, em alguns casos, pode-se argumentar que um método estático é tão desacoplado que poderia simplesmente ser uma função fora da classe, não havendo necessidade de estar dentro da classe.

- 3. Alternativas Disponíveis: Em muitos casos, @classmethod pode ser mais apropriado se você precisar de acesso ao estado da classe. @classmethod permite acessar e modificar o estado da classe, o que pode ser mais útil para métodos que devem operar com esses dados.

- 4. Coesão: A coesão refere-se a quão bem os componentes de um módulo (ou classe) estão relacionados. Métodos estáticos, ao não operarem sobre o estado da classe, podem levar a uma coesão mais baixa, pois eles não estão trabalhando diretamente com os dados ou comportamentos que definem a classe.

## Exemplo de onde o uso de @staticmethod torna a melhor escolha para o seu uso:
Um exemplo prático onde @staticmethod é a melhor escolha envolve uma classe que realiza cálculos ou operações que são logicamente relacionadas à classe, mas que não necessitam acessar ou modificar o estado da classe ou de suas instâncias. Um exemplo comum pode ser uma classe que lida com operações matemáticas.

Suponha que você tenha uma classe que fornece utilitários matemáticos, como calcular a área de diferentes formas geométricas. Estas são operações puras que não dependem de nenhum estado específico da classe ou de suas instâncias.

    class Matematica:
        @staticmethod
        def area_circulo(raio):
            return 3.14159 * raio * raio

        @staticmethod
        def area_retangulo(largura, altura):
            return largura * altura

    # Uso dos métodos estáticos
    print("Área do Círculo:", Matematica.area_circulo(5))
    print("Área do Retângulo:", Matematica.area_retangulo(4, 5))

Quando você está construindo uma base axiomática matemática ou qualquer tipo de funcionalidade que envolva cálculos ou operações puras que não dependem do estado de uma instância ou da classe em si, o uso de @staticmethod é frequentemente a melhor escolha. Isso se deve a várias razões:

- 1. Independência de Estado: Métodos estáticos não acessam ou modificam o estado da instância ou da classe, o que é ideal para funções matemáticas que dependem apenas dos argumentos fornecidos e seguem princípios axiomáticos ou teoremas.

- 2. Reutilização e Acesso Fácil: Você pode chamar um método estático diretamente na classe sem precisar criar uma instância. Isso é muito prático para funções matemáticas que você deseja acessar frequentemente de diferentes partes do seu programa.

- 3. Organização Lógica: Agrupar funções matemáticas relacionadas dentro de uma classe usando @staticmethod ajuda a manter o código organizado e logicamente estruturado. Isso facilita a manutenção e o entendimento do código, especialmente em contextos onde múltiplas operações matemáticas estão sendo utilizadas.

- 4. Coesão: Manter operações matemáticas como métodos estáticos em uma classe relevante (como uma classe Matematica ou Calculadora) mantém o código coeso e focado, com todas as operações relacionadas agrupadas em um único local.

Exemplo bem esdruxulo e informal de uma classe que define os axiomas dos numeros reais

    class NumerosReais:
        @staticmethod
        def adicionar(x, y):
            return x + y

        @staticmethod
        def subtrair(x, y):
            return x - y

        @staticmethod
        def multiplicar(x, y):
            return x * y

        @staticmethod
        def dividir(x, y):
            if y == 0:
                raise ValueError("Não é possível dividir por zero.")
            return x / y

    # Uso dos métodos estáticos
    print("Adição:", NumerosReais.adicionar(5, 3))
    print("Subtração:", NumerosReais.subtrair(5, 3))
    print("Multiplicação:", NumerosReais.multiplicar(5, 3))
    print("Divisão:", NumerosReais.dividir(5, 3))

Bom, em resumo, os melhores momentos em que se utiliza @staticmethod, seriam em situacoes em que voce esteja definindo, postulando ou axiomatixando algo como uma linha de partida independente. Ao lembrar de definicoes matematicas, axiomas, postulados fisicos, etc... Algo dessas naturezas, percebemos que elas nao dependem de nenhum outro conceito e a partir delas que se iniciam toda a construcao.
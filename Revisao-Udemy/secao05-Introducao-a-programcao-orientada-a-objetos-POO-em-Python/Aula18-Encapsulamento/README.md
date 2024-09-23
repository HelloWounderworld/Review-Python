# Aula 18 - Encapsulamento (modificadores de acesso: public, _protected, __private):
Antes de abordarmos os tres modificadores de acesso, vamos entender o conceito de Encapsulamento em programacao orientada a objetos.

## Encapsulamento:
Encapsulamento é um dos princípios fundamentais da programação orientada a objetos (POO). Ele se refere à prática de ocultar os detalhes internos ou a implementação de uma classe e expor apenas o que é necessário para o mundo externo através de uma interface bem definida. Isso ajuda a proteger os dados internos da classe contra acessos indevidos e modificações não autorizadas, além de permitir uma maneira controlada de interagir com os objetos.

### Funcionalidades do Encapsulamento:
- 1. Ocultação de Dados: Encapsulamento permite que os detalhes internos de implementação de uma classe sejam ocultados. Isso inclui atributos e métodos que não são necessários para os usuários da classe. Apenas uma interface necessária é exposta, o que simplifica o uso da classe.

- 2. Controle de Acesso: Através do encapsulamento, você pode controlar quem pode acessar os dados da classe e como eles podem ser modificados. Isso é feito através de métodos acessores (getters) e modificadores (setters), e pelo uso de níveis de acesso como public, protected e private.

- 3. Redução de Acoplamento: Encapsulamento ajuda a reduzir o acoplamento entre as classes, o que significa que mudanças em uma classe não afetam significativamente outras partes do programa. Isso torna o sistema mais modular e fácil de modificar ou estender.

- 4. Manutenção e Evolução: Com o encapsulamento, é mais fácil gerenciar e evoluir o código, pois as mudanças em uma classe podem ser feitas com um impacto mínimo sobre as outras classes que a utilizam. Isso é especialmente útil em sistemas grandes e complexos.

### Exemplo em Python:

    class ContaBancaria:
        def __init__(self, titular, saldo_inicial=0):
            self.titular = titular
            self.__saldo = saldo_inicial  # Atributo privado

        def depositar(self, valor):
            if valor > 0:
                self.__saldo += valor
                print(f"Depósito de {valor} realizado com sucesso.")
            else:
                print("Valor do depósito deve ser positivo.")

        def sacar(self, valor):
            if valor > 0 and valor <= self.__saldo:
                self.__saldo -= valor
                print(f"Saque de {valor} realizado com sucesso.")
            else:
                print("Saque inválido.")

        def get_saldo(self):
            return self.__saldo

- O atributo __saldo é privado, o que significa que ele não pode ser acessado diretamente fora da classe ContaBancaria.

- Métodos públicos depositar, sacar e get_saldo são fornecidos para permitir operações controladas sobre o saldo.

Encapsulamento, portanto, não só protege os dados dentro de uma classe, mas também define claramente como a classe deve ser usada, contribuindo para um design de software mais robusto e manutenível.

## Modificadores de Acesso em Python - Importante: PYTHON NAO TEM MODIFICADORES DE ACESSO! E TUDO CONVENCAO!!

Em Python, os conceitos de public, protected e private são usados para controlar o acesso aos atributos e métodos de uma classe, ajudando a implementar o encapsulamento. No entanto, diferentemente de outras linguagens como Java ou C++, Python não possui keywords específicas para definir explicitamente o nível de acesso. Em vez disso, ele usa convenções de nomenclatura para indicar como um atributo ou método deve ser tratado em termos de visibilidade e acessibilidade.

### Public
Public: Atributos e métodos públicos podem ser acessados de qualquer lugar, dentro ou fora da classe. Em Python, todos os membros de uma classe são públicos por padrão.

    class Carro:
        def __init__(self, marca):
            self.marca = marca  # Atributo público

        def dirigir(self):
            print("Carro está sendo dirigido")

### Protected
Protected: Atributos e métodos protegidos são destinados a ser usados por subclasses, indicando que devem ser acessados apenas dentro da própria classe e por instâncias de subclasses. Em Python, isso é indicado por um único sublinhado (_) antes do nome do membro.

      class Carro:
        def __init__(self, marca):
            self._marca = marca  # Atributo protegido

        def _dirigir_privado(self):
            print("Método protegido, uso interno ou em subclasses")

### Private
Private: Atributos e métodos privados não devem ser acessados fora da classe. Eles são usados para evitar que o código externo interfira diretamente com as variáveis internas. Em Python, isso é indicado por dois sublinhados (__) antes do nome do membro.

    class Carro:
        def __init__(self, marca):
            self.__marca = marca  # Atributo privado

        def __dirigir_privado(self):
            print("Método privado, acesso restrito à própria classe")

## Considerações
Em Python, o encapsulamento é mais uma convenção do que uma imposição estrita. Por exemplo, membros privados (com __) são apenas renomeados internamente com um nome da classe prefixado (ex: _Carro__marca), mas ainda podem ser acessados diretamente se realmente necessário, embora isso seja considerado uma má prática.

A ideia é que "somos todos adultos aqui", e os programadores são responsáveis por usar os membros da classe de maneira apropriada, respeitando as convenções de encapsulamento.

Essas convenções ajudam a manter o código mais organizado, seguro e fácil de manter, permitindo que os desenvolvedores saibam quais propriedades e métodos devem ou não ser acessados diretamente.

Seguir link para leitura PEP8:

    https://peps.python.org/pep-0008/#descriptive-naming-styles
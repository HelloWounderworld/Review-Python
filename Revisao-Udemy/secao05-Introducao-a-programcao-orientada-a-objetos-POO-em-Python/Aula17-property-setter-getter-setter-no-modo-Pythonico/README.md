# Aula 17 - @property + @setter - getter e setter no modo Pythônico:
O decorador @setter em Python é usado em conjunto com o decorador @property para criar um "setter" que permite definir o valor de um atributo com controle adicional. Essencialmente, ele permite encapsular a lógica de atribuição de valores a um atributo, adicionando validações ou operações adicionais durante esse processo.

Aqui esta um exemplo basico de como @setter e usado

    class Pessoa:
        def __init__(self, nome):
            self._nome = nome

        @property
        def nome(self):
            return self._nome

        @nome.setter
        def nome(self, valor):
            if not isinstance(valor, str):
                raise ValueError("O nome deve ser uma string")
            self._nome = valor

No exemplo acima:

- @property é usado para definir um método getter para o atributo nome.

- @nome.setter define o método setter correspondente que permite modificar o valor do atributo _nome. Antes de atribuir o valor, ele verifica se o valor é uma string. Se não for, ele levanta uma exceção ValueError.

Essa abordagem de usar @property com @setter é útil para:

- Validação de dados: Garantir que os dados estejam corretos antes de serem atribuídos a um atributo.

- Encapsulamento: Esconder a representação interna enquanto expõe uma interface para passar e receber valores, permitindo mudanças na implementação interna sem afetar os usuários da classe.

- Controle adicional: Executar código adicional durante a atribuição de valores, como limpeza de dados ou transformação.
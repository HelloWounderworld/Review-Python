# Aula 30, 31 e 32 - (Parte 2, 3 e 4) Log, LogFileMixin, LogPrintMixin e a união de tudo até aqui:

## Log, LogFileMixin, e LogPrintMixin em Python
Em Python, mixins podem ser usados para adicionar funcionalidades de log a classes de maneira modular. LogFileMixin e LogPrintMixin são dois exemplos de mixins que podem ser usados para adicionar capacidades de log a uma classe, seja escrevendo em um arquivo ou imprimindo na saída padrão, respectivamente.

### LogFileMixin
Este mixin adiciona a capacidade de logar mensagens em um arquivo. Ele pode ser usado para manter um registro de eventos ou dados que ocorrem durante a execução do programa.

    class LogFileMixin:
        def __init__(self, filename):
            self.log_file = open(filename, 'a')

        def log(self, message):
            self.log_file.write(message + '\n')
            self.log_file.flush()

        def close_log(self):
            self.log_file.close()

### LogPrintMixin
Este mixin fornece uma funcionalidade simples de log que imprime mensagens na saída padrão. É útil para depuração ou quando você quer informações rápidas sobre o que está acontecendo.

    class LogPrintMixin:
        def log(self, message):
            print(message)

### Combinação dos Mixins
Você pode combinar esses mixins em uma única classe para obter ambas as funcionalidades de log. Isso ilustra a flexibilidade dos mixins e como eles podem ser combinados para criar classes com funcionalidades ricas.

    class Application(LogFileMixin, LogPrintMixin):
        def __init__(self, filename):
            LogFileMixin.__init__(self, filename)

        def log(self, message):
            LogFileMixin.log(self, message)
            LogPrintMixin.log(self, message)

        def run(self):
            self.log("Aplicação está rodando.")
            # Simula algum processamento
            self.log("Aplicação está finalizando.")

        def close(self):
            self.close_log()

### Exemplo de Uso
Aqui está como você pode usar a classe Application para logar mensagens tanto em um arquivo quanto na saída padrão.

    app = Application("app.log")
    app.run()
    app.close()

### Explicação Detalhada
- LogFileMixin: Inicializa um arquivo de log e define um método log que escreve mensagens nesse arquivo. Também possui um método close_log para fechar o arquivo adequadamente.

- LogPrintMixin: Define um método log que simplesmente imprime a mensagem na saída padrão.

- Application: Combina ambos os mixins. No construtor, inicializa o LogFileMixin. O método log é sobrescrito para chamar log de ambos os mixins, garantindo que as mensagens sejam logadas tanto no arquivo quanto na saída padrão. O método run simula a execução da aplicação, logando mensagens no início e no fim. O método close garante que o arquivo de log seja fechado corretamente ao final da execução.

### Conclusão
Este exemplo ilustra como mixins podem ser usados para adicionar funcionalidades de maneira modular e flexível em Python. Mixins como LogFileMixin e LogPrintMixin permitem que você adicione capacidades de log a qualquer classe de maneira simples e reutilizável, promovendo a separação de preocupações e melhorando a manutenibilidade do código.
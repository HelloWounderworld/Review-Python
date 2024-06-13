# Abstração
# Herança - é um
class Log:
    # Nao pode ser instanciado diretamente.
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def __init__(self, filename):
        self.log_file = open(filename, 'a')

    def log(self, message):
        self.log_file.write(f'{message}  ({self.__class__.__name__})' + '\n')
        self.log_file.flush()

    def close_log(self):
        self.log_file.close()

    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    # l1 = LogFileMixin('qualquer')
    # l1._log('qualquer coisa')
    # print()
    l2 = LogPrintMixin()
    l2.log_error('qualquer coisa')
    l2.log_success('Que legal')
    print()
    l3 = LogFileMixin("c:\\Users\\leona\\Documents\\study-programming\\Review-Python\\Revisao-Udemy\\secao05-Introducao-a-programcao-orientada-a-objetos-POO-em-Python\\Aula30-Parte2-Log-LogFileMixin-LogPrintMixin-uniao-de-tudo-ate-aqui\\log_functionality\\log.txt")
    l3.log('qualquer coisa')
    l3.close_log()

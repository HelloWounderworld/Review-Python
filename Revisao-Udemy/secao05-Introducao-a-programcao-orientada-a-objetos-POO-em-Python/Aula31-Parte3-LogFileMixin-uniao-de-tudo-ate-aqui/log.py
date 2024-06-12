# Abstração
# Herança - é um
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'
print(LOG_FILE)


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_fomatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_fomatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_fomatada)
            arquivo.write('\n')

class LogPrintMixin(Log):
    if __name__ == '__main__':
        lp = LogPrintMixin()
        lp.log_error('qualquer coisa')
        lp.log_success('Que legal')
        lf = LogFileMixin()
        lf.log_error('qualquer coisa')
        lf.log_success('Que legal')

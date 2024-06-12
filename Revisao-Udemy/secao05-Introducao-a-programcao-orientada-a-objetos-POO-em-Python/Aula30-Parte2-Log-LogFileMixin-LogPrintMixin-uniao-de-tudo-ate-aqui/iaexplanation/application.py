from logfilemixin import LogFileMixin
from logprintmixin import LogPrintMixin

class Application(LogFileMixin, LogPrintMixin):
    def __init__(self, filename):
        LogFileMixin.__init__(self, filename)

    def log(self, message):
        LogFileMixin.log(self, message)
        LogPrintMixin.log(self, message)

    def run(self):
        self.log("Aplicacao esta rodando.")
        # Simula algum processamento
        self.log("Aplicacao esta finalizando.")

    def close(self):
        self.close_log()

app = Application("c:\\Users\\leona\\Documents\\study-programming\\Review-Python\\Revisao-Udemy\\secao05-Introducao-a-programcao-orientada-a-objetos-POO-em-Python\\Aula30-Parte2-Log-LogFileMixin-LogPrintMixin-uniao-de-tudo-ate-aqui\\iaexplanation\\log.txt")
app.run()
app.close()

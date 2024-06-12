class LogFileMixin:
    def __init__(self, filename):
        self.log_file = open(filename, 'a')

    def log(self, message):
        self.log_file.write(message + '\n')
        self.log_file.flush()

    def close_log(self):
        self.log_file.close()
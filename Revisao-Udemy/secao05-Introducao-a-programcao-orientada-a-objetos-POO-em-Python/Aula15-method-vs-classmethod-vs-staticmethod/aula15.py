class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_authentication(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def soma(x, y):
        return x + y
    
    @staticmethod
    def log(msg):
        # verifica se esta logado
        print('LOG', msg)

def connection_log(msg):
    print('LOG', msg)

c1 = Connection()
print(c1.user)
c1.set_user('leonardo')
print(c1.user)

print()

print(c1.password)
c1.set_password('123HelloWounderworld!')
print(c1.password)

print()

c2 = Connection.create_with_authentication('leonardo', '123456')
print(c2.user)
print(c2.password)

print()

print(Connection.soma(1, 2))

print()

print(Connection.log('Essa e a mensagem de log'))

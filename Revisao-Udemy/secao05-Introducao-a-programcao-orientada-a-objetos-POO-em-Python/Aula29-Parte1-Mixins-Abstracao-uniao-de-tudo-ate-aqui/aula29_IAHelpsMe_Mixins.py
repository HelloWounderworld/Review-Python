class LoggerMixin:
    def log(self, message):
        print(f"Log: {message}")

class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class Person(LoggerMixin, JSONMixin):
    def __init__(self, name):
        self.name = name

# Uso dos mixins
p = Person("Alice")
p.log("Starting program")
print(p.to_json())  # Saída: {"name": "Alice"}
# Aula 37 - Criando Exceptions em Python Orientado a Objetos (Exceções):
Em Python, você pode criar exceções personalizadas definindo uma nova classe que herda de uma classe de exceção existente, geralmente Exception ou uma de suas subclasses. Isso permite que você crie exceções específicas para os erros que podem ocorrer em seu código, facilitando a identificação e o tratamento desses erros.

## Passos para Criar uma Exceção Personalizada
### 1. Definir uma Nova Classe de Exceção:
- A classe deve herdar de Exception ou de uma de suas subclasses, como ValueError, TypeError, etc., dependendo do tipo de erro que você deseja representar.

- Você pode adicionar um método de inicialização 1 para personalizar a inicialização da exceção, permitindo que você passe mensagens de erro ou outros atributos relevantes.

### 2. Implementar o Método __init__ (opcional):
- Você pode sobrescrever o método __init__ para aceitar parâmetros adicionais e passá-los para a classe base Exception.

- Isso é útil para adicionar mensagens de erro personalizadas ou para armazenar dados adicionais na exceção.

### 3. Levantar a Exceção com raise:
Use a palavra-chave raise para lançar a exceção quando uma condição de erro específica for encontrada em seu código.

## Exemplo de Código
Aqui está um exemplo de como você pode definir e usar uma exceção personalizada em Python:

    class MyCustomError(Exception):
        def __init__(self, message, code):
            super().__init__(message)  # Chama o construtor da classe base com a mensagem
            self.code = code  # Um código de erro adicional

    # Em algum lugar do seu código, você pode levantar essa exceção:
    def do_something(param):
        if param < 0:
            raise MyCustomError("O parâmetro não pode ser negativo", code=400)

    try:
        do_something(-1)
    except MyCustomError as e:
        print(f"Erro capturado: {e}, Código: {e.code}")

- Classe MyCustomError: Define uma nova exceção que inclui uma mensagem de erro e um código de erro. A mensagem é passada para a classe base Exception, enquanto o código de erro é armazenado como um atributo da classe.

- Função do_something: Verifica se o parâmetro é negativo e, nesse caso, levanta a MyCustomError com uma mensagem e um código de erro.

- Bloco try-except: Captura a MyCustomError e imprime a mensagem e o código de erro.

## Boas Práticas
- Nomeie Exceções de Forma Clara: O nome da exceção deve refletir o tipo de erro que ela representa, facilitando a compreensão do código.

- Documente Exceções Personalizadas: Se você está criando uma biblioteca ou um módulo, documente as exceções personalizadas para que outros desenvolvedores saibam como capturá-las e tratá-las corretamente.

- Use Exceções Apropriadas: Herde de Exception ou de uma subclasse mais específica, dependendo do contexto do erro.

## Conclusao
Criar exceções personalizadas é uma prática poderosa em Python que ajuda a tornar o código mais robusto, legível e fácil de manter.
# Aula 22 - Introdução aos blocos de código + if / elif / else (condicionais):
Vamos ver sobre bloco de código começando com as condicionais if, elif e else.

No caso, bloco em python, por hora, vc poderia entender como uma espécie de instrução para uma determinada ação. Ou seja, ela é uma lista de sequências de passos que será executado avaliando um determinado valor de entrada.

Geralmente, a criação de tal instrução em outras linguagens orientada à objetos, como JavaScript, são feitas usando-se uma chave "{}". Já o Python, ele não precisa de chave.

   entrada = input('Você quer "entrar" ou "sair"? ')

    if entrada == 'entrar':
        print('Você entrou no sistema')
    elif entrada == 'sair':
        print('Você saiu do sistema')
    else:
        print('Você não digitou nem entrar e nem sair.')

    print('Fora dos blocos')

Note que, o bloco como está acima, vc digitando algo e, consequentemente, mesmo devolvendo algo, note que, as linhas de código fora do bloco posteriores continuam em funcionamento?

Bom, aqui a analogia é a mesma que no JavaScript, donde vc poderia usar o return caso vc queira que naquele escopo, seja finalizada até alí.

Bom, vimos que a ideia principal de montar um bloco em python é que ele seja feita via identação. Ou seja, quando vc cria uma instrução, tudo o que vem depois dele que esteja espaçado por um tab estará sendo executado dentro dele.

## Try/Except (try/catch do Python) e o uso do if/elif/else: Section 03 Class 37
In programming, both try/catch blocks and conditionals (such as if statements) are used to control the flow of a program, but they serve different purposes and are used in different situations. Here’s an explanation of when to use each:

### Try/Catch Blocks
Purpose: try/catch blocks are primarily used for handling exceptions—situations where an error occurs during the execution of a program that disrupts the normal flow of instructions.

When to Use:

- Handling Exceptions: When you anticipate that an operation may fail and you want to handle the failure gracefully without crashing the program. This is especially useful for unpredictable runtime errors such as file I/O operations, network requests, or parsing data.

- Improving Reliability: When you need to ensure that your program can recover from errors, log them, or perform clean-up operations (like closing a file or releasing resources).

- Separating Error-Handling Logic: When you want to separate error-handling logic from regular code to improve readability and maintainability.

Example of Try/Except Blocks:

    try:
        with open('nonexistentfile.txt', 'r') as file:
            for _ in range(3):
                print(file.readline())
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except IOError as e:
        print(f"I/O error: {e}")

### Conditional Statements
Purpose: Conditionals (like if/else statements) are used to execute different code branches based on boolean conditions. They are primarily used for controlling the flow of a program based on known conditions at compile time or runtime.

When to Use:

- Decision Making: When you need to execute different blocks of code based on specific conditions. For example, checking user input, performing different actions based on a variable’s value, or setting default values.

- Validating Preconditions: When you want to ensure that certain conditions are met before proceeding with a block of code. For example, ensuring that a variable is not null or that a number is within a specific range.

- Executing Mutually Exclusive Code Blocks: When you have multiple conditions and you want to execute only the block of code associated with the first true condition.

Example of Conditional Statements:

    number = 10

    if number > 0:
        print("Number is positive.")
    elif number < 0:
        print("Number is negative.")
    else:
        print("Number is zero.")

### Combining Try/Catch and Conditional Statements
In practice, you often use both try/catch blocks and conditionals together to handle both expected conditions and unexpected exceptions.

Example:

    import os

    def read_file(file_path):
        if not os.path.exists(file_path):
            print("File does not exist.")
            return

        try:
            with open(file_path, 'r') as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError as e:
            print(f"File not found exception: {e}")
        except IOError as e:
            print(f"I/O exception: {e}")

    # Example usage
    read_file('nonexistentfile.txt')

### Summary
- Use try/catch: For handling exceptions that are unpredictable and might occur during runtime, such as file operations, network requests, or operations that depend on external systems.

- Use conditionals (if/else): For controlling the flow of your program based on known conditions and making decisions based on variable states or predefined logic.

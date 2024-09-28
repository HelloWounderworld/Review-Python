# Aula 23 - Introdução ao tipo set em Python (conjuntos):
Vamos aprender sobre set aqui. Bom, basicamente, o set aqui a lógica dela é literalmente eoria dos conjuntos que aprendemos em ensino médio. O leitor poderá pegar qualquer livro sobre teoria de conjuntos. Eu, particularmente, recomendo dois livros em ambas nos seus primeiros capítulos:

- Curso de Analise Vol.1 - Elon Lages Lima 

- Curso de analise real - Cassio Neri e Marcos Cabral

Lembrando que, ambos os livros, o leitor não precisa ler ela inteirinho para entender a seção de conjuntos. Bastaria entender teoria a teoria de conjuntos logo na primeira seção.

Para quem quiser um livro muito mais punk aprendendo desde os primórdios de Fundamentos da Teoria de Conjuntos, recomendamos o livro

- Set Theory, The third Milennium Edition, Revised and Expanded - Thomas Jech

Lembrando, esse último livro é beeeem mais trabalhoso de se ler e de resolver os exercícios.

Pois bem, vamos abordar sobre "set" e o seu uso. Bom, basicamente, para criar um set começamos assim

    s1 = set()

Bom, o set, ele parece um dicionário, mas não tem chave e valor. Eu acho mais fácil de entender de forma inversa. Entender primeiro o set em seguida entender dicionário e, por fim, listas e tuplas, pois querendo ou não, na matemática, tudo se resume em conjuntos e relações, quando a pessoa começa a estudar desde o axioma de Zermelo Fraenkel and Choice. Pois assim, o leitor conseguirá perceber que dicionários, listas e tuplas, estão todas elas apoiadas sobre conceitos de conjuntos e funções, como uma forma de consequência.

Bom, como em conjuntos, o set, ele não tem uma ordem. Logo, podemos colocar um iterável dentro do set como segue, e veremos que ela não necessariamente exibe em ordem alfabética

    s1 = set('Leonardo')
    print(s1, type(s1))

Ou seja, já vimos que se colocarmos uma string dentro do set, ela irá iterar o nome "Leonardo". Mas, então, como podemos colocar o elemento "Leonardo" detro desse conjunto sem iterar as letras desse nome? Bastaria realizar o seguinte

    s2 = {'Leonardo'}
    print(s2, type(s2))

Ou seja, usando as chaves "{}".
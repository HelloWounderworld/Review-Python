# Aula 58 - while - Qual letra apareceu mais vezes na frase? (Iterando strings com while):
Essa aula é opcional considerar ela como uma aula ou como um exercício.

Irei considerar ela como um exercício. Daí, a tarefa é o seguinte.

Criar um código que itera uma string e conte dentro dela, a letra que mais apareceu e exiba ela com a quantidade total de aparição da mesma

    print(
        'A letra que apareceu mais vezes foi '
        f'"{letra_apareceu_mais_vezes}" que apareceu '
        f'{qtd_apareceu_mais_vezes}x'
    )

Bom, lembrando que a minha resolução eu utilizei while dentro de while. Mas podemos evitar de usar isso usando um método da string chamado .count() como é feito na solução do professor que substitui o while dentro do meu while que eu criei.

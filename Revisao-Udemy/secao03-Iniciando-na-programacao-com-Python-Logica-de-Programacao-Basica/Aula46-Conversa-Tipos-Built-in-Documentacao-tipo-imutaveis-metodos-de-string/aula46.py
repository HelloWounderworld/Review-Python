"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'leonardo takashi teramatsu'
# string[3] = 'ABC' # Isso ira retornar um erro
# outra_variavel = string
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)
# Exige que um dado string tenha obrigatoriamente, pelo menos, x caracteres
# Se não tiver preenchido esses x caracteres, o restante ele preenche com zeros pela esquerda
print(string.zfill(30))
print(string.capitalize())
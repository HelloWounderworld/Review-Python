# \r\n -> CRLF (Quebras de linhas que o VSCode já tem - esse aqui é válido para windows 11)
# \n -> LF (Para UX)
print(12, 34, sep='-')
print(12, 34, sep='')
print(56, 78, sep="*")

print(12, 34, sep='-', end='\r\n')
print(12, 34, sep='', end='\n')
print(56, 78, sep="*", end='\n')

print(12, 34, sep='-', end='##')
print(56, 78, sep="*", end='\n')
def relatorio(salarios):
    estudantes = salarios.keys()
    estudantes.sort()
    for estudante in estudantes:
        print("%-20s %12.02f" % (estudante,salarios[estudante]))

# verifique o erro.

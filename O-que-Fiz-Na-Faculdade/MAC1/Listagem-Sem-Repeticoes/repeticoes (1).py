###
### Dada uma sequencia de n valores reais, imprimi-los eliminando as repeticoes
###

def main():

	valor_str = ""
	sequencia = []

	while valor_str != "fim":
		valor_str = input("Entre com um valor ou 'fim' para terminar: ")
		if valor_str != "fim":
			sequencia.append(float(valor_str))

	## versao 1) usando operador in
	nova_sequencia = []
	for valor in sequencia:
		if valor not in nova_sequencia:
			nova_sequencia.append(valor)

	print("Sequencia sem repeticoes:", nova_sequencia)

	## versao 2) sem o operador <in> no if, usando for, sem usar break
	for x in sequencia:
		contido = False
		for y in nova_sequencia:
			if x == y:
				contido = True
		if not contido:
			nova_sequencia.append(x)

	print("Sequencia sem repeticoes:", nova_sequencia)

	## versao 3) sem o operador <in> no if, usando for, e usando break
	for x in sequencia:
		for y in nova_sequencia:
			if x == y:
				break
		if x != y:
			nova_sequencia.append(x)

	print("Sequencia sem repeticoes:", nova_sequencia)
				
	## versao 4) usar <in> em nenhum lugar, so usando whiles
	i = 0
	while i < len(sequencia):
		j = 0
		while j < len(nova_sequencia):
			if sequencia[i] == nova_sequencia[j]:
				break
			j += 1
		if j == len(nova_sequencia):
			nova_sequencia.append(x)
		i += 1

	print("Sequencia sem repeticoes:", nova_sequencia)

main()






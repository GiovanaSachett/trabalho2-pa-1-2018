from binHeap import *


def column(matrix, i):
    return [row[i] for row in matrix]

    
def corte(S, complementar, arestas):
	c = list()
	for i in arestas:
		if (i[0] in S and i[1] in complementar) or (i[1] in S and i[0] in complementar): # tem que checar os dois porque como eu fiz soh o triangulo inferior da matriz ele nao repete
			c.append(i)
	return c


def atualiza_corte(corte_antigo, vertice_inserido, arestas, S, complementar):
	remover = list()
	
	corte_novo = corte_antigo[:] #copia o corte antigo pro novo
	# remove todas as arestas que continham o vertice que foi adicionado (sao arestas que tao com dois elementos do conjunto S, porque antes o vertice inserido era do complementar)
	for i in corte_antigo: 
		if i[0] == vertice_inserido or i[1] == vertice_inserido:
			remover.append(i)
	for i in remover:
		corte_novo.remove(i)
		
	# adiciona as novas arestas que sao as que tem o que foiinserido e outro do complementar
	#vou fazer essas duas linhas fora daqui porque isso eh do algoritmo e nao bem atualizar o corte
	# S.append(vertice_inserido)
	# complementar.remove(vertice_inserido)
	for i in arestas: # adiciona as que entraram no corte (sao as que ligam o inserido ao complementar de S)
		if (i[0] == vertice_inserido and i[1] in complementar) or (i[1] == vertice_inserido and i[0] in complementar):
			corte_novo.append(i)
	
	return corte_novo
	
		
def prim(vertices, arestas):
	# como funciona o prim:
	# escolhe um vertice inicial (pode ser aeatorio) para o conjunto S
	# escolhe a aresta com menor peso do corte de S e passa o vertice que ela liga pra S
	# faz isso ate que o complementar de S esteja vazio
	
	mst = list()
	
	#adiciona um vertice ao conjunto S
	complementar = vertices[:]
	S = list()
	S.append(complementar.pop()) 
	
	bh = BinHeap()
	while complementar: # enquanto tiver elementos no conjunto complementar
		print("aaaaaaaa")
		break
	
	# print(bh.delMin())

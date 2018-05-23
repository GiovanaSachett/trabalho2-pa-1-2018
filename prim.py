from binHeap import *


def column(matrix, i):
    return [row[i] for row in matrix]

    
def corte(S, complementar, arestas):
	c = list()
	for i in arestas:
		if (i[0] in S and i[1] in complementar) or (i[1] in S and i[0] in complementar): # tem que checar os dois porque como eu fiz soh o triangulo inferior da matriz ele nao repete
			c.append(i)
	return c


def atualiza_corte(corte, v_inserido, arestas, complementar):
	
	for i in arestas: # adiciona as que entraram no corte (sao as que ligam o inserido ao complementar de S)
		if (i[0] == v_inserido and i[1] in complementar) or (i[1] == v_inserido and i[0] in complementar):
			corte.insert(i)


def prim(vertices, arestas, k):
	# como funciona o prim:
	# escolhe um vertice inicial (pode ser aeatorio) para o conjunto S
	# escolhe a aresta com menor peso do corte de S e passa o vertice que ela liga pra S
	# faz isso ate que o complementar de S esteja vazio
	
	mst = list()
	
	#adiciona um vertice ao conjunto S
	complementar = vertices[:]
	S = list()
	S.append(complementar.pop())
	
	# nesse heap binario eu soh vou colocar aresta que pelo menos um os vertices ta em S
	# assim, eu sempre vou verificar se os dois nao tao em S
	# mas eu nao preciso me preocupar com remover uma aresta com dois elementos
	# no complementar que seriam valido em uma iteracao seguinte
	 
	bh = BinHeap()
	bh.buildHeap(corte(S, complementar, arestas))
	
	while complementar: # enquanto tiver elementos no conjunto complementar
		a = bh.delMin()
		#se realmente for do corte 
		if a[1] in S and a[0] in complementar:
			mst.append(a)
			S.append(a[0])
			complementar.remove(a[0])
			atualiza_corte(bh, a[0], arestas, complementar)

		elif a[0] in S and a[1] in complementar:
			mst.append(a)
			S.append(a[1])
			complementar.remove(a[1])
			atualiza_corte(bh, a[1], arestas, complementar)
	
	mst = sorted(mst, key = lambda x : x[2])
	
	for i in range(k):
		mst.pop()
	
	#print(mst)
	
	return mst

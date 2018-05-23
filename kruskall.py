from unionFind import *

def kruskall(vertices, arestas, k):
	#arestas = arestas[0:10]
	
	conjuntos = UnionFind()
	conjuntos.buildSets(vertices)
	
	arestas = sorted(arestas, key = lambda x : x[2])
	mst = list()
	
	while conjuntos.nSets > k: # ate que tenha soh um conjunto
		a = arestas.pop(0)
		
		if not conjuntos.findUF(a[0]) == conjuntos.findUF(a[1]): #quero vertices que nao estejam no mesmo conjunto
			#print("antes da union", conjuntos.findUF(a[0]), conjuntos.findUF(a[1]), conjuntos.nSets)
			
			conjuntos.unionUF(a[0], a[1])
			#print("depois da union", conjuntos.findUF(a[0]), conjuntos.findUF(a[1]), conjuntos.nSets)
			
			mst.append(a)
	#print(conjuntos.setsDict)
	return mst

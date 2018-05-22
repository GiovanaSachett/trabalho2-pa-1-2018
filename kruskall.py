from unionFind import *

def kruskall(vertices, arestas):
	#arestas = arestas[0:10]
	
	conjuntos = UnionFind()
	conjuntos.buildSets(vertices)
	
	arestas = sorted(arestas, key = lambda x : x[2])
	mst = list()
	
	while conjuntos.nSets > 1: # ate que tenha soh um conjunto
		a = arestas.pop(0)
		
		if not conjuntos.findUF(a[0]) == conjuntos.findUF(a[1]): #quero vertices que nao estejam no mesmo conjunto
			conjuntos.unionUF(a[0], a[1])
			mst.append(a)
			
	return mst

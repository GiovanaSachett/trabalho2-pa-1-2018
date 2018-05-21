from binHeap import *
from math import sqrt
from prim import *

def dist_euclidiana(x1, y1, x2, y2):
	return( sqrt( (x1-x2)**2 + (y1 - y2)**2))

def main():
	data = open("data.txt", 'r')
	classes = open("classes.txt", 'r')
	
	vertices = list() #nome, coord x, coord y, classe
	for line in data:
		vertices.append([float(i) for i in line.split("\t")])
	for i in range(len(vertices)):
		vertices[i].insert(0, i)
		vertices[i].append(int(classes.readline()))
		
	data.close()
	classes.close()
	#print(vertices)

	#criando as arestas
	arestas_dict = dict()
	arestas = list() # inicio, fim, peso
	for i in range(len(vertices)):
		for j in range(i):
			#if i!=j:
			#arestas_dict[dist_euclidiana(vertices[i][1], vertices[i][2], vertices[j][1], vertices[j][2])] = (i, j) # tem que ver como isso se comporta pra valores iguais 
																													# (eu acho que vai soh sobreescrever o valor)
			arestas.append([i, j, dist_euclidiana(vertices[i][1], vertices[i][2], vertices[j][1], vertices[j][2])])
	
	vertices_indices = range(len(vertices))
	bh = BinHeap()
	bh.buildHeap(arestas[0:10])
	print(sorted(arestas[0:10], key=lambda x: x[2]))
	#print(bh.heapList)
	print(bh.delMin())
	print(bh.delMin())
	print(bh.delMin())
	print(bh.delMin())
	print(bh.delMin())
	print(bh.delMin())
	print(bh.delMin())
	print(bh.delMin())
	print(bh.delMin())
	print(bh.delMin())
	#prim(vertices_indices, arestas)

if __name__ == '__main__':
    main()

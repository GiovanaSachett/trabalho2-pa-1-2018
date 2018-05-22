import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from binHeap import *
from prim import *
from kruskall import *

def dist_euclidiana(x1, y1, x2, y2):
	return( sqrt( (x1-x2)**2 + (y1 - y2)**2))

def column(matrix, i):
	return [row[i] for row in matrix]


def main():
	data = open("data.txt", 'r')
	classes = open("classes.txt", 'r')
	
	vertices = list() #nome, coord x, coord y, classe
	for line in data:
		vertices.append([float(i) for i in line.split("\t")])
	for i in range(len(vertices)):
		vertices[i].insert(0, i)
		vertices[i].append(int(classes.readline()))
	
	# plt.scatter(column(vertices, 1), column(vertices, 2))
	# plt.show()
	
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
	
	#print(bh.heapList)
	mst = kruskall(vertices_indices, arestas)

	arvore = set()
	for a in mst:
		arvore.add(a[0])
		arvore.add(a[1])
		plt.plot([vertices[a[0]][1], vertices[a[0]][2]], 
			[vertices[a[1]][1], vertices[a[1]][2]])
	plt.show()

if __name__ == '__main__':
	main()

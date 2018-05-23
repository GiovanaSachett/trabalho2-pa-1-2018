class UnionFind:
	def __init__(self):
		self.setsDict = dict()
		self.nSets = 0

	def unionUF(self,i,j):
		self.nSets -= 1
		self.setsDict[self.findUF(i)] = self.setsDict[j]

	def findUF(self,i):
		if self.setsDict[i] == i:
			return i
		return self.findUF(self.setsDict[i])

	def buildSets(self,elementos):
		for i in elementos:
			self.setsDict[i] = i
		self.nSets = len(elementos)

class SparseArray(object):
		def __init__(self, items=0):
			self.L = [0]*items

		def __setitem__(self, j, e):
			self.L[j] = e

		def __getitem__(self, j):
			return self.L[j]

		def __str__(self):
			return str(self.L)

sa=SparseArray(5)

sa[0]=(14,"some")
sa[1]=(27,"more")
sa[2]=(68,"values")
sa[3]=(79,"are")
sa[4]=(118,"here")

print("Sparse Array Content: \n",sa)
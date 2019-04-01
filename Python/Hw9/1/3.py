import collections

class DefCounter(collections.Counter):
	miss = 0
	obj = None
	def __init__(self,string,**kwargs):
		self.miss = kwargs.get("missing")
		self.obj = collections.Counter(string)

	def __str__(self):
		return collections.Counter.__str__(self.obj)

A = DefCounter("QWEqweQWEqweQWE",missing = -10)
print(A)
print(A["Z"])
A["P"]+=5
print(A)

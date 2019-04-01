import collections
class DefCounter(collections.Counter):
	d = {}
	miss = 0
	def __init__(self,string,**kwargs):
		#print(type(kwargs))
		#print(kwargs)
		self.d = {}
		self.miss = kwargs.get("missing")
		#print(self.miss)
		size = len(string)
		i = 0
		while i < size:
			if string[i] in self.d.keys():
				count = self.d.get(string[i])
				count += 1
				self.d.update({string[i]:count})
				count = 0
			else:
				self.d.setdefault(string[i],1)
			i += 1
		#print(self.d)

	def __iadd__(self,other):
		print("!!!")

	def __getitem__(self, item):
		#print(item)
		if item in self.d:
			return self.d.get(item)
		else:
			self.d.setdefault(item,self.miss)
			print("***", self.d.get(item))
			return self.d.get(item)

	def __str__(self):
		return(f"DefCounter({self.d})")
		

A = DefCounter("QWEqweQWEqweQWE", missing=-10)
#print(A)
#print(A["Z"])
A["P"]+=5
print(A)

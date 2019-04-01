class vector:
	b = []
	c = ""
	res = []
	def __init__(self,a):
		self.b = []
		for i in a:
			self.b.append(i)

	def __str__(self):
		self.c = ""
		d = ":"
		for i in self.b:
			self.c += str(i)
			self.c += d
		self.c = self.c[:len(self.c)-1]
		return self.c

	def __add__(self, other):
		self.res = []
		count = 0
		if isinstance(other, vector):
			while count < len(self.b):
				#print(count)
				self.res.append(self.b[count]+other.b[count])
				count+=1
			return vector(self.res)
		else:
			while count < len(self.b):
				self.res.append(self.b[count]+other[count])
				count+=1
			return vector(self.res)

	def __radd__(self, other):
		self.res = []
		count = 0
		if isinstance(other, vector):
			while count < len(self.b):
				#print(count)
				self.res.append(self.b[count]+other.b[count])
				count+=1
			return vector(self.res)
		else:
			while count < len(self.b):
				self.res.append(self.b[count]+other[count])
				count+=1
			return vector(self.res)

#a, b = vector([2,1,2,1,2,1,2,1]), vector(range(8))
#print(a)
#print(b)
#print(a+b)
#print(b+range(8))
#print(range(8)+b)

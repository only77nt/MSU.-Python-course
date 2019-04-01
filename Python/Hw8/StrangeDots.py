class Dots():
	res = 0
	start = 0
	end = 0
	def __init__(self,a,b):
		self.res = b-a
		self.start = a
		self.end = b
		#print(self.res)

	def __getitem__(self, item):
		if isinstance(item, slice):
			a = item.start
			b = item.stop
			c = item.step
			count = self.start
			#print(a,b,c)
			if (c == None):
				step = self.res/(b-1)
				count = self.start + a * step
				return count
			elif (a==None) and (b!=None) and (c!=None):
				a = 0
				l = []
				step = self.res/(c-1)
				while a!=b:
					count = self.start + a * step 
					l.append(count)
					a += 1
				return l
			elif (a==None) and (b==None) and (c!=None):
				a = 0
				b = c
				l = []
				step = self.res/(c-1)
				while a!=b:
					count = self.start + a * step 
					l.append(count)
					a += 1
				return l	
			elif (a!=None) and (b==None) and (c!=None):
				b = c	
				l = []
				step = self.res/(c-1)
				while a!=b:
					count = self.start + a * step 
					l.append(count)
					a += 1
				return l					
			elif (a!=None) and (b!=None) and (c!=None):
				l = []
				step = self.res/(c-1)
				while a!=b:
					count = self.start + a * step 
					l.append(count)
					a += 1
				return l
		else:
			l = []
			a = item
			step = self.res/(a-1)
			count = self.start
			b = 1
			while count <= self.end:
				l.append(count)
				count = self.start + b * step
				b += 1
			return l

a = Dots(0,40)
print(*a[5])
print(a[0:5])
print(a[2:5])
print(a[4:5])
print(a[7:5])
print(a[-7:5])
print(*a[1:3:5])
print(*a[:3:5])
print(*a[2::5])
print(*a[::5])
print(*a[-2:6:5])





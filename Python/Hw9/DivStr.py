class DivStr(str):
	res = []
	word = ""
	def __mod__(self,n):
		self.word = ""
		size = len(self)
		how = size//n
		#print(size)
		#print(how)
		now = size - how*n
		#print(now)
		i = how * n
		while i!=size:
			self.word += self[i]
			i += 1
		return self.word

	def __floordiv__(self,n):
		self.word = ""
		self.res = []
		size = len(self)
		how = size//n
		j = 0
		while how!=0:
			i = 0			
			self.word = ""
			while i<n:
				self.word += self[j*n+i]
				i += 1
			self.res.append(self.word)
			j += 1
			how -= 1
		return self.res
	

#a = DivStr("XcDfQWEasdERTdfgRTY")
#print(*a//4)
#print(a%4)


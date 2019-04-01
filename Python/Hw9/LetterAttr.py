class LetterAttr(str):
	name = ""
	def __setattr__(self,name,val):
		res = ""
		#print(self.name)
		#print(val)
		#print(list(name))
		for i in val:
			if i in list(name):
				res += i
		#print(res)
		return str.__setattr__(self,name,res)

	def __getattr__(self,name):
		return name

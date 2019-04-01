def toint(f):
	def newf(*argp):
		count = 0
		a = []
		for i in argp:
			if type(i) == type(3.5):
				a.append(int(argp[count]))
			else:
				a.append(argp[count])
			count += 1
		b = tuple(a)
		res = f(*b)
		if type(res) == type(3.5):
			return int(res)
		else:
			return res
	return newf

@toint
def fun(a,b,c):
	return a+b+c

print(fun(1.5,2.5,3.5))

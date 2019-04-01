def getlex(lst,i):
	return lst[i]

def expr(lst,i):
	e = add(lst,i)
	if curlex == '+':
		getlex(lst,i)
		e+=add(lst,i)
	else:
		getlex(lst,i)
		e-=add(lst,i)
	return e

def add(lst,i):
	a = expo()
	if curlex == '*':
		getlex()
		a*=expo()
	else:
		getlex()
		a/=expo()
	return a

def expo(lst,i):
	int a=mult()
	if curlex ==

sentinel = '' # ends when this string is seen
for line in iter(input, sentinel):
	L = list(line)
	print(L)
	i = 0
	result = expr(L,i)
	

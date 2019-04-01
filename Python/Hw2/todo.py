def Nod (a,b):
	if (a!=0 and b!=0):
		if a > b:
			a = a % b
			return Nod(a,b)
		else:
			b = b % a
			return Nod(a,b)
	return (a+b)

def Check(c,d,Nd):
	if Nd==1:
		return c,d
	else:
		c = c//Nd
		d = d//Nd
		Nd = Nod(c,d)
		return Check(c,d,Nd)

a,b = eval(input())
unit = a//b
a = a%b
a,b = Check(a,b,Nod(a,b))
if unit!=0:
	if a!=0:
		print(unit," ",a,"/",b, sep = '')
	else:
		print(unit)
else:
	if a!=0:
		print(a,"/",b, sep = '')

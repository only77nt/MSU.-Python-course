a = input()
a = a.split()
b = []
for i in a:
	if i=='-' or i=='+' or i=='*':
		b.append(i)
	if i.isdigit():
		b.append(i)
	elif i[1:].isdigit() and (i[0]=='-' or i[0]=='+' or i[0]=='*'):
		b.append(i)
#print(b)
res = 0
c = []

while len(b)!=0:
	op = b.pop(0)
	#print(op)
	#print(c)
	if op=='+' or op=='-' or op=='*':
		x1 = c.pop(0)
		x2 = c.pop(0)
		if op == '+':
			res=x1+x2
		elif op == '-':
			res=x2-x1
		elif op == '*':
			res=x1*x2
		c.insert(0,res)
	else:
		if op[0] == '-':
			op=int(op[1:])*(-1)
		else:
			op=int(op)
		c.insert(0,op)
op = c.pop(0)
print(op)


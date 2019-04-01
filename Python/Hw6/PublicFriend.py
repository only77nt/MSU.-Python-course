a = 1
b = 1
m = set()
d = {}
count = set()
res = []

while True:
	a, b = eval(input())
	if (a == 0 and b == 0):
		break
	if a not in m:
		m.add(a)
	if b not in m:
		m.add(b)
	if a in d.keys():
		count = d.get(a)
		count.add(b)
		d.update({a:count})
	else:
		d.setdefault(a,{a,b})	
	if b in d.keys():
		count = d.get(b)
		count.add(a)
		d.update({b:count})
	else:
		d.setdefault(b,{a,b})
	
#print(m)
#print(d)
len1 = len(m)
for i in d.items():
	if len1 == len(i[1]):
		res.append((i[0]))

#print(res)
res.sort()
#print(res)
for i in res:
	print(i, end = ' ')


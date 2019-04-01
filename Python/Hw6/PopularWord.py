sentinel = '' # ends when this string is seen
count = 0
flag = False
max1 = 0
maxstr = ""
a = {}
for line in iter(input, sentinel):
	for s in line.split():
		if s in a:
			count = a.get(s)
			count += 1
			a.update({s:count})
			count = 0
		else:
			a.setdefault(s,1)
#print(a)
for s in a.items():
	if s[1]>max1:
		max1 = s[1]
		maxstr = s[0]
c = 0
for s in a.values():
	if s == max1:
		c += 1
		if c > 1:
			break
if c > 1:
	print("---")
else:
	print(maxstr)


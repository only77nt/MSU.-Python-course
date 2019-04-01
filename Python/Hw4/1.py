l = eval(input())

s = l.copy()
size = len(l)-1
pos = size-1
res = []
sep = True
res.append(size)

while (pos+l[pos] != size) and (pos!=-1):
	l[pos] = 0
	pos -= 1
if pos==-1:
	sep = False
	l[0] = 0

while pos!=-1 and sep:
	print(l[pos])
	if pos+l[pos] in res:
		print("! ",pos)
		res.append(pos)
		pos -= 1
	else:
		l[pos] = 0
		pos -= 1

print(res)
print(l)

if l[0]!=0:
	print("YES")
else:
	print("NO")

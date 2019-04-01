a = input()
b = input()

ind = 0
indstr = -1
size = len(b)
task = False
pos = True

for s in a.split():
	if not task:
		j = 0
		s += ' '
		for i in s:
			indstr += 1
			if j == size:
				task = True
				indstr += 1
				break
			elif b[j] == '@':
				j += 1
			elif b[j] == i:
				if pos:
					ind = indstr
					pos = False
				j += 1
			else:
				j = 0
				ind = indstr
				pos = True

#print(task)
#print(indstr)
if len(b)>len(a):
	print(-1)
else:
	print(ind)


		

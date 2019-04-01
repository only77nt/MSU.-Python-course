a = input()
b = input()

ind = 0
indstr = 0
size = len(b)
size1 = len(a)
task = False
pos = True
j = 0

for i in a:
	#print(i)
	if not task:
		indstr += 1
		if j == size-1:
			task = True
			break
		elif b[j] == '@':
			j += 1
		elif b[j] == i:
			j += 1
		else:
			j = 0
			ind = indstr

#print(task)
#print(indstr)
if len(b)>len(a) or not task:
	print(-1)
else:
	print(ind)


		

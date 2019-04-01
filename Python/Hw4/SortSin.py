import math

l = eval(input())
i = 0
for elem in l:
	l[i] = math.sin(elem), elem
	i += 1
l = sorted(l)
i = 0
for elem in l:
	l[i] = elem[1]
	i += 1
print(l)

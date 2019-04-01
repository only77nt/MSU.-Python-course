l = eval(input())

size = len(l)-1
pos = size - 1
ind = size
sep = True

while pos!=-1:
	if ind <= pos+l[pos] < len(l):
		ind = pos
		pos -= 1
	else:
		pos -= 1

if ind == 0:
	print("YES")
else:
	print("NO")

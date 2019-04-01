def Check(pos):
	res = False

	while True:
		if (pos+1)==len(l):
			return True
		elif(pos<0):
			return False
		elif (pos+1)>len(l):
			return False
		elif l[pos]==0:
			return Check(pos-1)
		else:
			var = l[pos]
			l[pos] = 0
			return (Check(pos+var) or (Check(pos-1) if l[pos-1]!=1 else False))


l = eval(input())

pos = 0
res = Check(pos)

if res:
	print("YES")
else:
	print("NO")


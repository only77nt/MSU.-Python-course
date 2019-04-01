def Check(x,y,r):
	a,b = eval(input())
	if (a == 0) and (b == 0):
		print("YES")
		return
	else:
		point=(a-x)**2+(b-y)**2
		if point > r**2:
			print("NO")
			return
		else:
			Check(x,y,r)
			return

x,y,r = eval(input())
Check(x,y,r)

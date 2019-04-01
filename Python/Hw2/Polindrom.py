def Step(a):
	if a==0:
		return 0
	else:
		return Step(a//10)+1

def First(a):
	if (a//10 == 0):
		return a
	else:
		return First(a//10)
		

def Check(a):
	if 0<=a<=9:
		print("YES")
		return
	b = a%10
	c = First(a)
	d=10**(Step(a)-2)
	if (b == c):
		Check((a//10)%d)
		return
	else:
		print("NO")
		return

a = eval(input())
Check(a)

	

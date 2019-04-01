def f(n):
	if n==1:
		return 2
	elif n==2:
		return 4
	elif n==3:
		return 7
	else:
		return f(n-1)+f(n-2)+f(n-3)

n = eval(input())
res = f(n)
print(res)



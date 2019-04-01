def gen(n):
	for i in range(n):
		yield i

n = eval(input())
g = gen(n)
i = 0
while i!=7:
	i = next(g)
	print(i)

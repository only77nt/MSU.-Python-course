n = eval(input())
n1 = 2
n2 = 4
n3 = 7
if n == 1:
	print(n1)
elif n == 2:
	print(n2)
elif n == 3:
	print(n3)
else:
	for i in range(3,n):
		n1,n2,n3 = n2,n3,n1+n2+n3
	print(n3)

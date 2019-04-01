a = eval(input())
sep = True
while sep:
	for i in range(2,a//2+1):
		if a%i==0:
			sep = True
			break
		sep = False
	if sep:
		a -= 1

print(a)

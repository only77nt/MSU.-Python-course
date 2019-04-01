from math import sqrt
a = eval(input())
sep = True
while sep:
	for i in range(2,(int(sqrt(a))+1)):
		if a%i==0:
			sep = True
			break
		sep = False
	if sep:
		a -= 1

print(a)

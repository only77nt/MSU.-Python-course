def moar(a,b,n):
	sum1 = 0
	sum2 = 0
	for i in a:
		if i%n==0:
			sum1 += 1
	for i in b:
		if i%n==0:
			sum2 += 1
	if sum1>sum2:
		return True
	else:
		return False


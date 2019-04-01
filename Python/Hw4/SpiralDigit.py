import pprint

n,m = eval(input())

digit = 0
i = 0
j = 0
l = [[0]*n for y in range(m)]

imax = m-1
jmax = n-1
imin = 1
jmin = 0
sz = n*m

while (digit < sz):
	j=jmin
	while j<=jmax: #Слева-направо
		l[imin-1][j] = digit%10
		digit += 1
		j += 1
	i = imin
	if(digit >= sz):
		break
	while i<=imax: #Сверху-вниз
		l[i][jmax] = digit%10
		digit += 1
		i += 1
	jmax -= 1
	j = jmax
	if(digit >= sz):
		break
	while j>=jmin: #Справа-налево
		l[imax][j] = digit%10
		digit += 1
		j -= 1
	imax-=1
	i = imax
	if(digit >= sz):
		break
	while i>=imin: #Снизу-вверх
		l[i][jmin] = digit%10
		digit += 1
		i -= 1
	imin += 1
	jmin += 1
	if(digit >= sz):
		break

#pprint.pprint(l)
for i in range(m):
	for j in range(n):
		print(l[i][j],end=' ')
	print()
	
	





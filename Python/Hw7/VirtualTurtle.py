def turtle(coord,d):
	a = []
	a.append(coord[0])
	a.append(coord[1])
	x = yield a[0],a[1]
	while 1:
		if x == 'f':
			if d == 0:
				a[0]+=1
				x = yield a[0],a[1]
			elif d == 1:
				a[1]+=1
				x = yield a[0],a[1]
			elif d == 2:
				a[0]-=1
				x = yield a[0],a[1]
			elif d == 3:
				a[1]-=1
				x = yield a[0],a[1]
		elif x == 'l':
			d = (d+1)%4	
			x = yield a[0],a[1]	
		elif x == 'r':
			d = (d-1)%4
			x = yield a[0],a[1]

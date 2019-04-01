def squares(*args):
	w = args[0]
	h = args[1]
	args = args[2:]
	l = [['.']*w for y in range(h)]
	for i in args:
		x = i[0]
		y = i[1]
		s = i[2]
		c = i[3]

		for i in range(y,y+s):
			for j in range(x, x+s):
				l[i][j] = c

	for i in range(h):
		for j in range(w):
			print(l[i][j],end = '')
		print()

#squares(20,23,(1,1,5,'@'), (2,3,1,'!'), (4,5,11,'#'), (8,11,9,'/'))

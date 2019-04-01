sentinel = '' # ends when this string is seen
i = 0
for line in iter(input, sentinel):
	a = [int(s) for s in line.split() if (s.isdigit() or (s[0] == '-') and (s[1:].isdigit()))]
	if i == 0 and a:
		max1 = a[0]
		i += 1
	else:
		for r in a:
			if r > max1:
				max1 = r
print(max1)

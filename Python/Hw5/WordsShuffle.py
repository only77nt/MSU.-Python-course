a = input()
b = input()

a2 = len(a)
b2 = len(b)

a = a.lower()
b = b.lower()

a = a.split()
b = b.split()

a1 = []
b1 = []

for i in a:
	if not i.isalpha():
		if i[:len(i)-1].isalpha():
			a1.append(i[:len(i)-1])
			a1.append(i[len(i)-1])
	else:
		a1.append(i)

for i in b:
	if not i.isalpha():
		if i[:len(i)-1].isalpha():
			b1.append(i[:len(i)-1])
			b1.append(i[len(i)-1])
	else:
		b1.append(i)

#print(a1)
#print(b1)

for i in a1:
	if i in b1: 
		b1.remove(i)
	else:
		break

#print(count)

if not b1 and (a2 == b2):
	print(True)
else:
	print(False)

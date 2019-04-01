import sys

a = input()
b = input()

a2 = len(a)
b2 = len(b)

if a2!=b2:
	print(False)
	sys.exit(0)

a = a.lower()
b = b.lower()

a = a.split()
b = b.split()

a1 = []

for i in a:
	if not i.isalpha():
			a1.append(i[:len(i)-1])
			a1.append(i[len(i)-1])
	else:
		a1.append(i)

for i in b:
	if not i.isalpha():
		if i[:len(i)-1] in a1:
			a1.remove(i[:len(i)-1])
		else:
			break
		if i[len(i)-1] in a1:
			a1.remove(i[len(i)-1])
		else:
			break
	else:
		if i in a1:
			a1.remove(i)
		else:
			break

if not a1 and (a2 == b2):
	print(True)
else:
	print(False)

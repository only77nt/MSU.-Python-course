a = input()
b = input()

a2 = len(a)
b2 = len(b)

a = a.lower()
b = b.lower()

a = a.split()
b = b.split()

a1 = []

flag = True

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
			if i[:len(i)-1] in a1:
				pass
			else:
				flag = False
				break
			if i[len(i)-1] in a1:
				pass
			else:
				flag = False
				break
	else:
		if i in a1:
			pass
		else:
			flag = False
			break

if flag and (a2 == b2):
	print(True)
else:
	print(False)

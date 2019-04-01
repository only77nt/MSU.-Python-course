j = 0
curlex = ""

def expr(lst):
	global j
	global curlex
	e = add(lst)
	if curlex == '+':
		j += 1
		curlex = lst[j]
		e+=add(lst)
	else:
		j += 1
		curlex = lst[j]
		e-=add(lst)
	return e

def add(lst):
	global j
	global curlex
	a = mult(lst)
	if curlex == '*':
		j += 1
		curlex = lst[j]
		a*=mult(lst)
	else:
		j += 1
		curlex = lst[j]
		a/=mult(lst)
	return a

def mult(lst):
	global j
	global curlex
	#print(j)
	print(curlex)
	if curlex in "0123456789":
		m = int(curlex)
	elif curlex == '(':
		j += 1
		curlex = lst[j]
		m = expr(lst)
	elif curlex == ')':
		print("Скобки ОК!")
	else:
		print("Ошибка!")
	j += 1
	curlex = lst[j]
	return m

sentinel = '' # ends when this string is seen
#Ввод до enter`а
for line in iter(input, sentinel):
	lst = []
	left = []
	right = []
	lex = ""
	L = list(line)
	#print(L)
	for i in L:
		if i in '=+-*/()':
			if lex != "":
				lst.append(lex)
			lex = ""
			lst.append(i)
		else:
			lex += i
	lst.append(lex)
	lex = ""
	#print(lst)
#Находим двойные знаки
	i = 0
	while i<len(lst):
		if lst[i] == '=':
			if lst[i] == lst[i+1]:
				lst.insert(i,"==")
				lst.pop(i+1)
		if lst[i] == '/':
			if lst[i] == lst[i+1]:
				lst.insert(i,"//")
				lst.pop(i+1)
		i += 1
	print(lst)
#Находим знак равенства
	if '=' in lst:
		flag = True
		for i in lst:
			if i != '=' and flag:
				left.append(i)
			elif i == '=':
				flag = False
			else:
				right.append(i)
		print("left = ",left)
		print("right = ",right)
#Начинаем вычисления
	if left == []:
		res = 0
		if lst.count('(')!=lst.count(')'):
			print("Скобки!")
		else:
			curlex = lst[j]
			#print(curlex)
			res = expr(lst)
		print(res)
	else:
		print("Есть = !")

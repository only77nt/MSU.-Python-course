sentinel = ''
s = dict()
word = ""
key = ""
for line in iter(input, sentinel):
	#print(line)
	if line[0]=='#':
		pass
	elif line[0] in "0123456789" and '=' in line:
		for i in line:
			if i == '=':
				break
			word += i
		print(f"invalid identifier '{word}'")
		word = ""
	elif '=' in line and "==" not in line:
		#print("!!!")
		flag = True
		for i in line:
			if i == '=':
				flag = False
				continue
			if flag:				
				word += i
			else:
				key += i
		#print("word: ", word)
		#print("key: ", key)
		s.update({word:eval(key,s)})
		#print(s)
		word = ""
		key = ""
	elif "==" in line:
		print("invalid assignment 'd==100'")
	else:
		try:
			a = eval(line,s)
			print(a)
		except Exception as E:
			print(E)

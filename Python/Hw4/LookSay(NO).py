def LookSay(n):
	p = "1"
	seq = [1]
	while (n > 1):
		q = ''
		idx = 0 # Счётчик
		l = len(p) # Длина текущего слова, для получения нового
		while idx < l:
			start = idx
			idx = idx + 1
			while idx < l and p[idx] == p[start]: # Считаем кол-во одинаковых цифр до первой не одинаковой
				idx = idx + 1
			q = q + str(idx-start) + p[start] # В последовательность заносим: (то, что было) + (столько) + (чего)
		n, p = n - 1, q # Переходим к след. числу последовательности и меняем p
		seq.append(int(p))
	return seq

a = eval(input())
max1 = a[0]
max2 = a[0]
for i in a:
	if i>max1:
		max1=i
for j in a:
	if max2==max1:
		if j<max1:
			max2=j
	if max2<j<max1:
		max2=j

if max1==max2:
	print("NO")
else:
	print(max2)

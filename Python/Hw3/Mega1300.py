from math import sqrt
n = eval(input())
lst=[]
for i in range(2, n+1):
    for j in lst:
        if j > int((sqrt(i)) + 1):
            lst.append(i)
            break
        if (i % j == 0):
            break
    else:
        lst.append(i)
print(lst.pop())

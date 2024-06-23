num = [2,3,5,4,8]
num[2] = 3
num.append(9)
num.sort(reverse=False)
num.insert(0,3)
num.pop()
print(num)

a = [1,2,3,4,5]
b = a.copy()
b.pop()
print(a,b)
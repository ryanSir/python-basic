t = ('python', 'hello', 'world')
# 根据索引访问元组
print(t[0])

# 元组切片操作
t2 = t[0:3:2]
print(t2)

# 元组的遍历
for item in t:
    print(item)

for i in range(len(t)):
    print(i, t[i], sep="-->")

for index, item in enumerate(t):
    print(index, '---->', item)

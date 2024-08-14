list = ['hello', 'world', 'a', 'b']

# 使用遍历循环for遍历列表
for item in list:
    print(item)

print("------")

# 使用for循环，range()函数，len()函数，根据索引进行遍历
for i in range(0, len(list)):
    print(i, '-->' + list[i])

print("------")

# 第三种遍历方式，使用 enumearte 函数
for index, item in enumerate(list):
    print(index, item)  # index 是序号，不是索引

for index, item in enumerate(list, start=1):  # 手动修序号的起始值
    print(index, item)

for index, item in enumerate(list, 1):  # 手动修序号的起始值，可以沈略start
    print(index, item)

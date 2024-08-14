# 创建字典
d = {10: 'cat', 20: 'dog', 30: 'pet', 20: 'zoo'}
print(d)  # 当value值相同时，后一个会覆盖前一个

# zip函数
list1 = [10, 20, 30, 40]
list2 = ['cat', 'dog', 'pet', 'zoo', 'car']
obj = zip(list1, list2)
print(obj)  # <zip object at 0x104aa7ec0>
# print(list(obj))  # 会转成元组 [(10, 'cat'), (20, 'dog'), (30, 'pet'), (40, 'zoo')]

print(dict(obj))  # {10: 'cat', 20: 'dog', 30: 'pet', 40: 'zoo'}

# 使用参数创建字典
d = dict(cat=10, dog=20)
print(d)

t = (10, 20, 30)
print({t: 'dog'})  # 元组也可以作为键

# list = [10, 20, 30]
# print({list: 'cat'})  # list 不可以作为键

print(max(d))
print(min(d))
print(len(d))

del d
print(d)
